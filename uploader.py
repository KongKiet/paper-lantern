"""Uploads converted Markdown articles to a Gemini File Search Store.

Not yet implemented — this is a placeholder interface for the setup milestone.
"""

from __future__ import annotations

from pathlib import Path


def get_or_create_file_search_store(client, display_name: str) -> str:
    """Return an existing File Search Store name, creating one if needed.

    Intended to use client.file_search_stores.create(...) /
    client.file_search_stores.list(...) per the current Gemini File Search API.
    """
    raise NotImplementedError(
        "uploader.get_or_create_file_search_store is not implemented yet "
        f"(display_name={display_name!r})."
    )


def upload_markdown_file(client, file_search_store_name: str, markdown_path: Path) -> str:
    """Upload a single Markdown file into the given File Search Store."""
    raise NotImplementedError(
        "uploader.upload_markdown_file is not implemented yet "
        f"(file_search_store_name={file_search_store_name!r}, path={markdown_path!r})."
    )


def sync_articles_dir(client, file_search_store_name: str, articles_dir: Path) -> int:
    """Upload all new/changed Markdown files in `articles_dir`, returning the count uploaded."""
    raise NotImplementedError(
        "uploader.sync_articles_dir is not implemented yet "
        f"(file_search_store_name={file_search_store_name!r}, articles_dir={articles_dir!r})."
    )
