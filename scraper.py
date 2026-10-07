"""Scrapes OptiSigns support articles and converts them to clean Markdown.

`scrape_one` fetches one article (Zendesk Help Center API first, public HTML
page as fallback) and writes Markdown with a provenance header.
`iter_listed_articles` discovers articles through the paginated public list
endpoint (newest-updated first); `pipeline.py` selects and saves a collection.

No Gemini credentials are used or sent here; requests go only to the help
center host taken from the article URL.
"""

from __future__ import annotations

import html
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup, Comment
from markdownify import markdownify
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

log = logging.getLogger(__name__)

HTTP_TIMEOUT = (5, 20)  # (connect, read) seconds
USER_AGENT = "paper-lantern/0.1 (+take-home article scraper)"

_ARTICLE_PATH_RE = re.compile(r"^/hc/(?P<locale>[a-z]{2}(?:-[a-z]{2,4})?)/articles/(?P<id>\d+)(?:-(?P<slug>[^/?#]+))?/?$", re.I)

# Selector verified against the live page: Zendesk Copenhagen-style themes
# wrap the article content in <div class="article-body">.
ARTICLE_BODY_SELECTOR = ".article-body"
ARTICLE_TITLE_SELECTOR = "h1.article-title"

# Page chrome that must never leak into Markdown if it appears inside the body.
_NOISE_SELECTORS = [
    "script", "style", "noscript", "iframe", "form", "nav", "header", "footer",
    "[role=search]", ".search", ".article-votes", ".article-more-questions",
    ".article-relatives", ".article-comments", ".article-subscribe",
    ".article-share", ".breadcrumbs",
]

# Closing boilerplate used across OptiSigns articles ("That's all!" heading
# followed by an "OptiSigns is the leader in digital signage software" plug).
_OUTRO_HEADING_RE = re.compile(r"^that[’']?s all!?$", re.I)
_PROMO_PARAGRAPH_RE = re.compile(r"^OptiSigns is (?:the|a) leader in digital signage", re.I)


class ScrapeError(RuntimeError):
    """Raised when an article cannot be fetched or yields no usable content."""


@dataclass
class ArticleRef:
    url: str          # canonical URL (no query/fragment)
    base: str         # scheme://host
    locale: str
    article_id: str
    slug: str


@dataclass
class Article:
    ref: ArticleRef
    title: str
    body_html: str
    updated_at: str | None
    source: str       # "zendesk-api" or "html-page"


def parse_article_url(url: str) -> ArticleRef:
    parts = urlsplit(url.strip())
    if parts.scheme not in ("http", "https") or not parts.netloc:
        raise ScrapeError(f"Not an absolute http(s) URL: {url!r}")
    match = _ARTICLE_PATH_RE.match(parts.path)
    if not match:
        raise ScrapeError(f"URL is not a Help Center article URL (/hc/<locale>/articles/<id>-<slug>): {url!r}")
    canonical = urlunsplit(("https", parts.netloc, parts.path.rstrip("/"), "", ""))
    return ArticleRef(
        url=canonical,
        base=f"https://{parts.netloc}",
        locale=match["locale"].lower(),
        article_id=match["id"],
        slug=(match["slug"] or "").lower(),
    )


def build_session() -> requests.Session:
    """HTTP session with bounded retries for transient failures only."""
    retry = Retry(
        total=3,
        connect=3,
        read=3,
        status=3,
        backoff_factor=0.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}),
        respect_retry_after_header=True,
        raise_on_status=False,
    )
    session = requests.Session()
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    # Only a UA header; no credentials of any kind are attached.
    session.headers.update({"User-Agent": USER_AGENT})
    return session


def fetch_from_api(session: requests.Session, ref: ArticleRef) -> Article | None:
    """Fetch via the public localized Zendesk endpoint; None if unusable."""
    api_url = f"{ref.base}/api/v2/help_center/{ref.locale}/articles/{ref.article_id}.json"
    try:
        resp = session.get(api_url, timeout=HTTP_TIMEOUT, headers={"Accept": "application/json"})
    except requests.RequestException as exc:
        log.warning("Zendesk API request failed (%s); falling back to HTML page.", type(exc).__name__)
        return None
    if resp.status_code != 200:
        log.warning("Zendesk API returned HTTP %s; falling back to HTML page.", resp.status_code)
        return None
    try:
        data = resp.json().get("article") or {}
    except ValueError:
        log.warning("Zendesk API returned non-JSON; falling back to HTML page.")
        return None
    title = (data.get("title") or data.get("name") or "").strip()
    body = data.get("body") or ""
    if str(data.get("id")) != ref.article_id or not title or not body.strip() or data.get("draft"):
        log.warning("Zendesk API response lacked usable article data; falling back to HTML page.")
        return None
    return Article(
        ref=ref,
        title=title,
        body_html=body,
        updated_at=data.get("updated_at") or data.get("edited_at"),
        source="zendesk-api",
    )


def extract_from_page_html(html: str, ref: ArticleRef) -> Article:
    """Extract only the article body (and title) from a full Help Center page."""
    soup = BeautifulSoup(html, "html.parser")
    body = soup.select_one(ARTICLE_BODY_SELECTOR)
    if body is None or not body.get_text(strip=True):
        raise ScrapeError(f"Selector {ARTICLE_BODY_SELECTOR!r} not found or empty on {ref.url}")
    title_el = soup.select_one(ARTICLE_TITLE_SELECTOR) or soup.find("h1")
    title = title_el.get_text(" ", strip=True) if title_el else ""
    if not title:
        raise ScrapeError(f"Could not find article title on {ref.url}")
    updated_at = None
    time_el = soup.select_one(".article-meta time[datetime], .article-updated time[datetime]")
    if time_el is not None:
        updated_at = time_el.get("datetime")
    return Article(ref=ref, title=title, body_html=body.decode_contents(), updated_at=updated_at, source="html-page")


def fetch_from_page(session: requests.Session, ref: ArticleRef) -> Article:
    try:
        resp = session.get(ref.url, timeout=HTTP_TIMEOUT, headers={"Accept": "text/html"})
    except requests.RequestException as exc:
        raise ScrapeError(f"Fetching article page failed: {type(exc).__name__}") from exc
    if resp.status_code != 200:
        raise ScrapeError(f"Article page returned HTTP {resp.status_code}")
    resp.encoding = resp.encoding or "utf-8"
    return extract_from_page_html(resp.text, ref)


def fetch_article(url: str, session: requests.Session | None = None) -> Article:
    ref = parse_article_url(url)
    session = session or build_session()
    return fetch_from_api(session, ref) or fetch_from_page(session, ref)


# In-page links ("#Name") keep a target: each referenced <a name> / id becomes a
# GitHub-compatible `<a name="Name"></a>`. markdownify drops empty anchors, so
# targets are swapped for an alphanumeric placeholder (nothing it would escape)
# and restored after conversion.
_ANCHOR_TOKEN = "zzplanchor{}zz"
_ANCHOR_TOKEN_RE = re.compile(r"zzplanchor(\d+)zz")
_HEADING_RE = re.compile(r"^h[1-6]$")
_BLOCK_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "div", "section", "table", "blockquote", "ul", "ol"}


def _mark_anchors(soup: BeautifulSoup) -> list[str]:
    """Insert placeholders for fragment targets referenced by in-page links."""
    referenced = {a["href"][1:] for a in soup.find_all("a", href=True)
                  if a["href"].startswith("#") and len(a["href"]) > 1}
    names: list[str] = []
    for el in soup.find_all(True):
        if el.name in ("pre", "code") or el.find_parent(["pre", "code"]):
            continue
        for target in (el.get("name") if el.name == "a" else None, el.get("id")):
            if target not in referenced or target in names:
                continue
            names.append(target)
            token = _ANCHOR_TOKEN.format(len(names) - 1)
            # Zendesk sometimes wraps an anchor in its own empty heading; the
            # placeholder goes before that heading, which is dropped as blank.
            heading = el.find_parent(_HEADING_RE) if el.name == "a" else None
            block = heading if heading and not heading.get_text(strip=True) else el
            if block.name in _BLOCK_TAGS:
                marker = soup.new_tag("p")
                marker.string = token
                block.insert_before(marker)
            elif el.name == "a" and not el.get("href"):
                el.insert_before(token)  # an empty named anchor itself is dropped below
            else:
                el.insert(0, token)
    return names


# Markup the author typed as escaped text (`&lt;iframe ...&gt;...&lt;/iframe&gt;`) is a
# copyable example, not embedded media (real <iframe> tags are noise above).
# markdownify would emit it as live raw HTML, so it becomes a fenced html block.
_LITERAL_MARKUP_RE = re.compile(r"^<([a-z][a-z0-9-]*)\b[^<>]*>.*</\1>$", re.I | re.S)
_LITERAL_MARKUP_INLINE = {"span", "strong", "b", "em", "i", "u", "font"}


def _literal_markup_to_code(soup: BeautifulSoup) -> None:
    for container in soup.find_all(["p", "li", "td", "div"]):
        if container.find_parent(["pre", "code"]):
            continue
        line: list = []
        for node in [*container.children, None]:  # None flushes the last line
            if node is not None and node.name != "br" and node.name not in _BLOCK_TAGS | {"li", "img", "pre"}:
                line.append(node)
                continue
            text = "".join(n.get_text() if n.name else str(n) for n in line).strip()
            # Only plain text and formatting spans: never links, images or code.
            if _LITERAL_MARKUP_RE.match(text) and all(
                    n.name is None or {n.name, *(c.name for c in n.find_all(True))} <= _LITERAL_MARKUP_INLINE
                    for n in line):
                pre = soup.new_tag("pre")
                code = soup.new_tag("code", attrs={"class": "language-html"})
                code.string = text
                pre.append(code)
                line[0].insert_before(pre)
                for n in line:
                    n.extract()
            line = []


def _clean_body(body_html: str) -> tuple[BeautifulSoup, list[str]]:
    soup = BeautifulSoup(body_html, "html.parser")
    for comment in soup.find_all(string=lambda s: isinstance(s, Comment)):
        comment.extract()
    for selector in _NOISE_SELECTORS:
        for el in soup.select(selector):
            el.decompose()

    # Closing promo block: "That's all!" heading + "OptiSigns is the leader..." paragraph.
    for p in soup.find_all("p"):
        if _PROMO_PARAGRAPH_RE.match(p.get_text(" ", strip=True)):
            p.decompose()
    for heading in soup.find_all(re.compile(r"^h[1-6]$")):
        if _OUTRO_HEADING_RE.match(heading.get_text(" ", strip=True)):
            heading.decompose()

    _literal_markup_to_code(soup)
    anchors = _mark_anchors(soup)
    # Empty named anchors (<a name="...">), blank paragraphs and blank headings
    # carry no content; referenced targets were replaced by placeholders above.
    for a in soup.find_all("a"):
        if not a.get("href") and not a.get_text(strip=True) and not a.find("img"):
            a.decompose()
    for p in soup.find_all(["p", _HEADING_RE]):
        if not p.get_text(strip=True) and not p.find("img"):
            p.decompose()

    # The document has exactly one H1 (the title); demote any in the body.
    for h1 in soup.find_all("h1"):
        h1.name = "h2"
    return soup, anchors


def _code_language(el) -> str:
    for node in (el, el.find("code")):
        if node is None:
            continue
        for cls in node.get("class") or []:
            if cls.startswith(("language-", "lang-")):
                lang = cls.split("-", 1)[1]
                return "" if lang == "auto" else lang  # Zendesk editor placeholder, not a language
    return ""


def body_to_markdown(body_html: str) -> str:
    soup, anchors = _clean_body(body_html)
    md = markdownify(
        str(soup),
        heading_style="ATX",
        bullets="-",
        code_language_callback=_code_language,
        strip=["span"],
    )
    md = md.replace(" ", " ")
    md = _ANCHOR_TOKEN_RE.sub(
        lambda m: f'<a name="{html.escape(anchors[int(m.group(1))], quote=True)}"></a>', md)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def render_markdown(article: Article) -> str:
    header = [
        f"# {article.title}",
        "",
        f"Article URL: {article.ref.url}",
        "",
        f"Article ID: {article.ref.article_id}",
        "",
        f"Locale: {article.ref.locale}",
    ]
    if article.updated_at:
        header += ["", f"Updated at: {article.updated_at}"]
    body = body_to_markdown(article.body_html)
    if not body:
        raise ScrapeError("Article body converted to empty Markdown.")
    return "\n".join(header) + "\n\n---\n\n" + body + "\n"


def output_filename(article: Article) -> str:
    slug = article.ref.slug or re.sub(r"[^a-z0-9]+", "-", article.title.lower()).strip("-")
    slug = re.sub(r"[^a-z0-9-]+", "-", slug).strip("-")
    if not slug:
        slug = f"article-{article.ref.article_id}"
    return f"{slug}.md"


def save_article_markdown(filename: str, markdown: str, articles_dir: Path) -> Path:
    articles_dir.mkdir(parents=True, exist_ok=True)
    path = articles_dir / filename
    path.write_text(markdown, encoding="utf-8", newline="\n")
    return path


def scrape_one(url: str, articles_dir: Path, session: requests.Session | None = None) -> tuple[Path, Article]:
    article = fetch_article(url, session=session)
    markdown = render_markdown(article)
    path = save_article_markdown(output_filename(article), markdown, articles_dir)
    return path, article


_META_LINE_RE = re.compile(r"^(Article URL|Article ID|Locale|Updated at): (.+)$", re.M)


def parse_markdown_metadata(markdown: str) -> dict[str, str]:
    """Read the provenance header written by `render_markdown`."""
    header = markdown.split("\n---\n", 1)[0]
    meta = {key: value.strip() for key, value in _META_LINE_RE.findall(header)}
    title = re.search(r"^# (.+)$", header, re.M)
    if title:
        meta["Title"] = title.group(1).strip()
    return meta


# ---------------------------------------------------------------- discovery

# Verified against the live endpoint: cursor pagination (page[size] <= 100)
# combined with sort_by=updated_at&sort_order=desc returns meta.has_more and
# links.next. Offset-style responses (next_page) are followed as a fallback.
LIST_PAGE_SIZE = 100
MAX_LIST_PAGES = 50


def list_articles_url(base_url: str, locale: str) -> str:
    return f"{base_url.rstrip('/')}/api/v2/help_center/{locale}/articles.json"


def _same_host(url: str, base_url: str) -> bool:
    return urlsplit(url).netloc.lower() == urlsplit(base_url).netloc.lower()


def iter_listed_articles(session: requests.Session, base_url: str, locale: str,
                         page_size: int = LIST_PAGE_SIZE, max_pages: int = MAX_LIST_PAGES,
                         stats: dict | None = None):
    """Yield article objects newest-updated first, following API pagination.

    Article IDs are deduplicated across pages; repeats are counted in
    stats["duplicate_ids_ignored"] and never yielded twice.
    """
    stats = stats if stats is not None else {}
    stats.setdefault("list_pages_fetched", 0)
    stats.setdefault("duplicate_ids_ignored", 0)
    url = list_articles_url(base_url, locale)
    params: dict | None = {"sort_by": "updated_at", "sort_order": "desc", "page[size]": page_size}
    seen: set[str] = set()
    for _ in range(max_pages):
        try:
            resp = session.get(url, params=params, timeout=HTTP_TIMEOUT, headers={"Accept": "application/json"})
        except requests.RequestException as exc:
            raise ScrapeError(f"Article list request failed: {type(exc).__name__}") from exc
        if resp.status_code != 200:
            raise ScrapeError(f"Article list returned HTTP {resp.status_code}")
        try:
            data = resp.json()
        except ValueError as exc:
            raise ScrapeError("Article list returned non-JSON") from exc
        stats["list_pages_fetched"] += 1
        for item in data.get("articles") or []:
            article_id = str(item.get("id") or "")
            if not article_id:
                continue
            if article_id in seen:
                stats["duplicate_ids_ignored"] += 1
                continue
            seen.add(article_id)
            yield item
        meta = data.get("meta") or {}
        if "has_more" in meta:
            next_url = (data.get("links") or {}).get("next") if meta.get("has_more") else None
        else:
            next_url = data.get("next_page")
        if not next_url:
            return
        if not _same_host(next_url, base_url):
            raise ScrapeError("Pagination link points to an unexpected host; not following it.")
        url, params = next_url, None
    log.warning("Stopped article discovery after %d pages (safety limit).", max_pages)


def article_from_listing(item: dict, locale: str) -> tuple[Article | None, ArticleRef | None, str | None]:
    """Build an Article from a list-endpoint item: (article, ref, rejection_reason)."""
    article_id = str(item.get("id") or "")
    if item.get("draft"):
        return None, None, "draft"
    if (item.get("locale") or "").lower() != locale:
        return None, None, f"locale {item.get('locale')!r}"
    try:
        ref = parse_article_url(item.get("html_url") or "")
    except ScrapeError:
        return None, None, "no usable html_url"
    if ref.article_id != article_id:
        return None, None, "html_url/id mismatch"
    title = (item.get("title") or item.get("name") or "").strip()
    if not title:
        return None, ref, "empty title"
    body = item.get("body") or ""
    if not body.strip():
        return None, ref, "empty body"
    # Same fields as fetch_from_api, so the rendered Markdown (and its hash) match.
    return Article(ref=ref, title=title, body_html=body,
                   updated_at=item.get("updated_at") or item.get("edited_at"), source="zendesk-api"), ref, None


def discover_article_urls(base_url: str, minimum_count: int = 30, locale: str = "en-us") -> list[str]:
    """Canonical URLs of the first `minimum_count` usable articles, newest-updated first."""
    urls = []
    for item in iter_listed_articles(build_session(), base_url, locale):
        article, _, _ = article_from_listing(item, locale)
        if article:
            urls.append(article.ref.url)
            if len(urls) >= minimum_count:
                break
    return urls


# ---------------------------------------------------------------- filenames

_WINDOWS_RESERVED = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)), *(f"lpt{i}" for i in range(1, 10))}
MAX_SLUG_LENGTH = 80
_SAFE_FILENAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*\.md$")


def safe_filename(article: Article) -> str:
    """Lowercase ASCII slug, length-bounded, never a Windows reserved device name."""
    stem = output_filename(article)[:-3][:MAX_SLUG_LENGTH].strip("-") or f"article-{article.ref.article_id}"
    if stem in _WINDOWS_RESERVED:
        stem = f"{stem}-{article.ref.article_id}"
    return f"{stem}.md"


def is_safe_filename(name: str) -> bool:
    return bool(_SAFE_FILENAME_RE.match(name or "")) and name[:-3] not in _WINDOWS_RESERVED \
        and len(name) <= MAX_SLUG_LENGTH + 20


def file_article_id(path: Path) -> str | None:
    """Article ID recorded in an existing Markdown file's header, if any."""
    try:
        return parse_markdown_metadata(path.read_text(encoding="utf-8")).get("Article ID")
    except (OSError, UnicodeDecodeError):
        return None


def write_if_changed(path: Path, markdown: str) -> bool:
    """Write UTF-8 Markdown only when the content differs; returns True if written."""
    data = markdown.encode("utf-8")
    if path.is_file() and path.read_bytes() == data:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    tmp.replace(path)
    return True
