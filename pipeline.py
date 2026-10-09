"""Collection pipeline: discover -> scrape -> (optionally) delta upload -> run summary.

Scope of one run is the *selected collection*: the first `limit` usable,
published articles of one locale, newest-updated first, always including the
required article IDs within that total. A limited run does not synchronize the
whole help center and never deletes documents of articles it did not select.

Upload results per selected article are mutually exclusive:
  added    newly indexed (no document was tracked for the article)
  updated  tracked document replaced (changed content) or repaired (missing/failed)
  skipped  unchanged content, tracked document confirmed STATE_ACTIVE
  failed   scrape or upload/confirmation failed; retried on the next run
"""

from __future__ import annotations

import logging
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable

import requests

import scraper
import uploader

log = logging.getLogger(__name__)

DEFAULT_LOCALE = "en-us"
# The working YouTube article is always part of the collection.
REQUIRED_ARTICLE_IDS = ("360051014713",)
MAX_REJECTIONS_REPORTED = 50


@dataclass
class ArticleOutcome:
    article_id: str
    title: str = ""
    canonical_url: str = ""
    updated_at: str | None = None
    source: str = ""
    required: bool = False
    markdown_path: str | None = None
    content_sha256: str | None = None
    delta: str | None = None          # vs manifest: new | changed | unchanged
    scrape_status: str = "pending"    # scraped | failed
    upload: str | None = None         # added | updated | skipped | failed (run only)
    document_name: str | None = None
    replaced_document: str | None = None
    error: str | None = None


@dataclass
class Collection:
    locale: str
    limit: int
    outcomes: list[ArticleOutcome] = field(default_factory=list)
    rejected: list[dict] = field(default_factory=list)
    stats: dict = field(default_factory=dict)
    discovery_error: str | None = None

    @property
    def scraped(self) -> list[ArticleOutcome]:
        return [o for o in self.outcomes if o.scrape_status == "scraped"]


# ---------------------------------------------------------------- file index

def file_index_path(paths: uploader.StatePaths) -> Path:
    return paths.manifest_file.parent / "article-files.json"


def load_file_index(paths: uploader.StatePaths) -> dict[str, str]:
    """article_id -> Markdown filename. Records scrape output only, never upload status."""
    return dict((uploader.read_json(file_index_path(paths), {}) or {}).get("files") or {})


def save_file_index(paths: uploader.StatePaths, files: dict[str, str]) -> None:
    uploader.write_json_atomic(file_index_path(paths), {"version": 1, "files": dict(sorted(files.items())),
                                                        "updated_at": uploader.utc_now()})


def choose_filename(article: scraper.Article, file_index: dict[str, str], manifest: dict,
                    used: dict[str, str], articles_dir: Path) -> str:
    """Stable, Windows-safe filename; reuses state, resolves slug collisions by article ID."""
    article_id = article.ref.article_id
    candidates = [file_index.get(article_id)]
    tracked_path = (manifest.get("articles", {}).get(article_id) or {}).get("markdown_path")
    if tracked_path:
        candidates.append(Path(tracked_path).name)
    candidates.append(scraper.safe_filename(article))
    name = next(c for c in candidates if c and scraper.is_safe_filename(c))

    def taken(n: str) -> bool:
        owner = used.get(n)
        if owner and owner != article_id:
            return True
        on_disk = articles_dir / n
        if on_disk.is_file():
            disk_id = scraper.file_article_id(on_disk)
            return bool(disk_id) and disk_id != article_id
        return False

    if taken(name):
        name = f"{name[:-3]}-{article_id}.md"
    return name


# ---------------------------------------------------------------- scraping

def _delta(manifest: dict, article_id: str, sha: str) -> str:
    entry = manifest.get("articles", {}).get(article_id) or {}
    if not entry.get("content_sha256") and not entry.get("pending"):
        return "new"
    if entry.get("content_sha256") == sha and entry.get("upload_status") == "active":
        return "unchanged"
    return "changed"


def collect_articles(session: requests.Session, base_url: str, limit: int, articles_dir: Path,
                     paths: uploader.StatePaths, locale: str = DEFAULT_LOCALE,
                     required_ids: tuple[str, ...] = REQUIRED_ARTICLE_IDS,
                     progress: Callable[[str], None] = print) -> Collection:
    """Discover and save the selected collection as Markdown. Never calls Gemini."""
    if limit < 1:
        raise ValueError("limit must be >= 1")
    required = [r for r in dict.fromkeys(required_ids)][:limit]
    other_quota = limit - len(required)
    col = Collection(locale=locale, limit=limit)
    manifest = uploader.load_manifest(paths)
    file_index = load_file_index(paths)
    used = {name: aid for aid, name in file_index.items()}
    by_id: dict[str, ArticleOutcome] = {}
    others = 0

    def save(article: scraper.Article, outcome: ArticleOutcome) -> None:
        markdown = scraper.render_markdown(article)  # ScrapeError if the body converts to nothing
        name = choose_filename(article, file_index, manifest, used, articles_dir)
        path = articles_dir / name
        written = scraper.write_if_changed(path, markdown)
        sha = uploader.sha256_bytes(markdown.encode("utf-8"))
        used[name] = article.ref.article_id
        file_index[article.ref.article_id] = name
        outcome.title, outcome.canonical_url = article.title, article.ref.url
        outcome.updated_at, outcome.source = article.updated_at, article.source
        outcome.markdown_path = uploader._relative(path, paths.project_root)
        outcome.content_sha256, outcome.delta = sha, _delta(manifest, article.ref.article_id, sha)
        outcome.scrape_status = "scraped"
        progress(f"  [{len(col.outcomes) + 1:>3}/{limit}] scraped {article.ref.article_id} "
                 f"({outcome.delta}{'' if written else ', file unchanged'}) {name}")

    def reject(article_id: str, reason: str) -> None:
        col.stats["rejected_candidates"] = col.stats.get("rejected_candidates", 0) + 1
        if len(col.rejected) < MAX_REJECTIONS_REPORTED:
            col.rejected.append({"article_id": article_id, "reason": reason})
        log.info("Skipping candidate %s: %s", article_id, reason)

    def done() -> bool:
        return others >= other_quota and all(r in by_id for r in required)

    try:
        for item in scraper.iter_listed_articles(session, base_url, locale, stats=col.stats):
            article_id = str(item["id"])
            is_required = article_id in required
            if not is_required and others >= other_quota:
                continue  # quota full; keep paging only to reach a required article
            article, ref, reason = scraper.article_from_listing(item, locale)
            if article is None and reason == "empty body" and ref is not None:
                try:
                    article = scraper.fetch_from_page(session, ref)  # existing HTML fallback
                except scraper.ScrapeError as exc:
                    reason = f"empty API body; HTML fallback failed ({exc})"
            outcome = ArticleOutcome(article_id=article_id, required=is_required)
            if article is not None:
                try:
                    save(article, outcome)
                except (scraper.ScrapeError, OSError) as exc:
                    reason = f"{type(exc).__name__}: {exc}"
            if outcome.scrape_status != "scraped":
                if not is_required:
                    reject(article_id, reason or "unusable")
                    continue
                outcome.scrape_status, outcome.error = "failed", reason or "unusable"
                progress(f"  [{len(col.outcomes) + 1:>3}/{limit}] FAILED required {article_id}: {outcome.error}")
            by_id[article_id] = outcome
            col.outcomes.append(outcome)
            others += 0 if is_required else 1
            if done():
                break
    except scraper.ScrapeError as exc:
        col.discovery_error = str(exc)
        log.error("Article discovery stopped: %s", exc)

    # A required article not reached through the listing is fetched directly.
    for article_id in required:
        if article_id in by_id:
            continue
        outcome = ArticleOutcome(article_id=article_id, required=True)
        tracked_url = (manifest.get("articles", {}).get(article_id) or {}).get("canonical_url")
        url = tracked_url or f"{base_url.rstrip('/')}/hc/{locale}/articles/{article_id}"
        try:
            save(scraper.fetch_article(url, session=session), outcome)
        except (scraper.ScrapeError, OSError) as exc:
            outcome.scrape_status, outcome.error = "failed", f"{type(exc).__name__}: {exc}"
            progress(f"  [{len(col.outcomes) + 1:>3}/{limit}] FAILED required {article_id}: {outcome.error}")
        by_id[article_id] = outcome
        col.outcomes.append(outcome)

    save_file_index(paths, file_index)
    return col


# ---------------------------------------------------------------- upload

def upload_collection(client, col: Collection, configured_store: str, paths: uploader.StatePaths,
                      timeout_seconds: int, sanitize: Callable[[Exception], str],
                      progress: Callable[[str], None] = print, sleep=time.sleep) -> str | None:
    """Sequential delta upload of scraped articles. Returns the store name (None if unresolved)."""
    try:
        store_name = uploader.get_or_create_store(client, configured_store, paths)
    except Exception as exc:  # noqa: BLE001 - recorded per article, sanitized
        message = f"store unavailable: {sanitize(exc)}"
        for o in col.outcomes:
            if o.scrape_status == "scraped":
                o.upload, o.error = "failed", message
        log.error("Upload phase aborted: %s", message)
        return None

    targets = col.scraped
    for i, o in enumerate(targets, 1):
        try:
            result = uploader.upload_one(client, paths.project_root / o.markdown_path, configured_store, paths,
                                         timeout_seconds=timeout_seconds, sleep=sleep, store_name=store_name)
        except uploader.PendingTimeoutError as exc:
            o.upload, o.error = "failed", f"still indexing; resumed on next run ({sanitize(exc)})"
        except Exception as exc:  # noqa: BLE001 - one article failing must not stop the others
            o.upload, o.error = "failed", sanitize(exc)
        else:
            o.upload, o.document_name, o.replaced_document = result.action, result.document_name, result.replaced_document
        progress(f"  [{i:>3}/{len(targets)}] {o.upload:<7} {o.article_id} {o.title[:60]}"
                 + (f" -- {o.error}" if o.error else ""))
    return store_name


# ---------------------------------------------------------------- summary

def summarize(col: Collection, *, command: str, base_url: str, started_at: str, started_monotonic: float,
              uploaded: bool, store_name: str | None = None, paths: uploader.StatePaths | None = None) -> dict:
    outcomes = col.outcomes
    scraped = len(col.scraped)
    counts = {"limit": col.limit, "selected": len(outcomes), "scraped": scraped}
    if uploaded:
        for key in ("added", "updated", "skipped"):
            counts[key] = sum(o.upload == key for o in outcomes)
        counts["failed"] = sum(o.scrape_status == "failed" or o.upload in (None, "failed") for o in outcomes)
        counts["selected_documents_confirmed_active"] = counts["added"] + counts["updated"] + counts["skipped"]
        ok = counts["selected_documents_confirmed_active"] == col.limit and counts["failed"] == 0
    else:
        counts["failed"] = len(outcomes) - scraped
        for key in ("new", "changed", "unchanged"):
            counts[f"delta_{key}"] = sum(o.delta == key for o in outcomes)
        ok = scraped == col.limit and counts["failed"] == 0
    ok = ok and not col.discovery_error
    counts["rejected_candidates"] = col.stats.get("rejected_candidates", 0)
    counts["duplicate_ids_ignored"] = col.stats.get("duplicate_ids_ignored", 0)
    counts["list_pages_fetched"] = col.stats.get("list_pages_fetched", 0)

    summary = {
        "command": command,
        "status": "success" if ok else "failed",
        "started_at": started_at,
        "finished_at": uploader.utc_now(),
        "elapsed_seconds": round(time.monotonic() - started_monotonic, 1),
        "scope": {
            "source": scraper.list_articles_url(base_url, col.locale),
            "locale": col.locale,
            "order": "updated_at desc",
            "limit": col.limit,
            "required_article_ids": list(REQUIRED_ARTICLE_IDS),
            "note": "Limited run over the selected collection only; not a full help-center sync. "
                    "Documents of unselected articles are left untouched.",
        },
        "counts": counts,
        "discovery_error": col.discovery_error,
        "articles": [asdict(o) for o in outcomes],
        "rejected_candidates": col.rejected,
    }
    if uploaded:
        cfg = uploader.chunking_config()["white_space_config"]
        tracked_active = 0
        if paths is not None:
            tracked_active = sum(1 for e in uploader.load_manifest(paths)["articles"].values()
                                 if e.get("upload_status") == "active" and e.get("store_name") == store_name)
        summary["store_name"] = store_name
        summary["indexing"] = {
            "chunking": {"strategy": "white_space", **cfg},
            "indexed_files_confirmed_active_this_run": counts["selected_documents_confirmed_active"],
            "tracked_active_documents_in_manifest": tracked_active,
            "provider_chunk_count": None,
            "provider_chunk_count_reason": "Gemini File Search does not expose a per-document or "
                                           "per-store chunk count; no estimate is reported.",
        }
    if not ok and counts["selected"] < col.limit:
        summary["insufficient_articles"] = f"only {counts['selected']} of {col.limit} usable articles were selected"
    return summary


def write_summary(summary: dict, logs_dir: Path, *, last_name: str, success_name: str | None) -> None:
    """Always write the latest summary; the 'last successful' file only on success."""
    uploader.write_json_atomic(logs_dir / last_name, summary)
    if success_name and summary["status"] == "success":
        uploader.write_json_atomic(logs_dir / success_name, summary)


def print_summary(summary: dict, out: Callable[[str], None] = print) -> None:
    c = summary["counts"]
    out("")
    out(f"Summary ({summary['command']}, status={summary['status']}):")
    keys = ["selected", "scraped", "added", "updated", "skipped", "failed", "selected_documents_confirmed_active"] \
        if "added" in c else ["selected", "scraped", "failed", "delta_new", "delta_changed", "delta_unchanged"]
    for key in keys:
        out(f"  {key}: {c[key]}")
    out(f"  elapsed_seconds: {summary['elapsed_seconds']}")
    if "indexing" in summary:
        ch = summary["indexing"]["chunking"]
        out(f"  chunking (configured): white_space max_tokens_per_chunk={ch['max_tokens_per_chunk']}, "
            f"max_overlap_tokens={ch['max_overlap_tokens']}")
        out(f"  indexed files confirmed active (this collection): "
            f"{summary['indexing']['indexed_files_confirmed_active_this_run']}; "
            f"tracked active in manifest: {summary['indexing']['tracked_active_documents_in_manifest']}")
        out("  provider_chunk_count: unavailable (not exposed by the API)")
    if summary.get("insufficient_articles"):
        out(f"  insufficient: {summary['insufficient_articles']}")
    if summary.get("discovery_error"):
        out(f"  discovery error: {summary['discovery_error']}")
