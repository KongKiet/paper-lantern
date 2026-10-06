"""Scrapes OptiSigns support articles and converts them to clean Markdown.

Not yet implemented — this is a placeholder interface for the setup milestone.
"""

from __future__ import annotations

from pathlib import Path


def discover_article_urls(base_url: str, minimum_count: int = 30) -> list[str]:
    """Discover public article URLs under the support site.

    Intended to crawl section/category pages to collect at least
    `minimum_count` article URLs from `base_url`.
    """
    raise NotImplementedError(
        "scraper.discover_article_urls is not implemented yet. "
        "This setup milestone only establishes the project skeleton."
    )


def fetch_article(url: str) -> str:
    """Fetch the raw HTML of a single article page."""
    raise NotImplementedError(
        f"scraper.fetch_article is not implemented yet (requested url={url!r})."
    )


def convert_to_markdown(html: str) -> str:
    """Convert article HTML into clean Markdown suitable for File Search upload."""
    raise NotImplementedError("scraper.convert_to_markdown is not implemented yet.")


def save_article_markdown(slug: str, markdown: str, articles_dir: Path) -> Path:
    """Persist converted Markdown to `articles_dir/{slug}.md`."""
    raise NotImplementedError(
        f"scraper.save_article_markdown is not implemented yet (slug={slug!r})."
    )
