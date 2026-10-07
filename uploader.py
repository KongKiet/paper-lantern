"""Uploads converted Markdown articles to a Gemini File Search Store.

State lives under state/:

- gemini-store.json          the persistent File Search store resource name
- ingestion-manifest.json    per-article upload record (no secrets)

Upload flow for one file:
  1. Resolve the store (configured > saved > create-once-and-persist).
  2. If a pending operation was recorded for this article, resume polling it.
  3. If the tracked document has the same SHA-256 and is ACTIVE, skip.
  4. Otherwise upload, record the operation as pending immediately, poll with
     a bounded timeout, confirm the new document is ACTIVE, and only then
     delete the previously tracked document for this same article.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from scraper import parse_markdown_metadata

log = logging.getLogger(__name__)

STORE_DISPLAY_NAME = "paper-lantern-optisigns"
MARKDOWN_MIME_TYPE = "text/markdown"

# White-space chunking. 500 tokens keeps one help-article section (a heading
# plus its steps/list) in a chunk; 50 tokens (10%) of overlap preserves
# context across chunk boundaries without duplicating much text.
MAX_TOKENS_PER_CHUNK = 500
MAX_OVERLAP_TOKENS = 50

DEFAULT_TIMEOUT_SECONDS = 300
POLL_INTERVAL_SECONDS = 5

STATE_ACTIVE = "STATE_ACTIVE"
STATE_PENDING = "STATE_PENDING"
STATE_FAILED = "STATE_FAILED"


class UploadError(RuntimeError):
    """Upload could not be completed or confirmed."""


class StoreConflictError(UploadError):
    """Configured and saved store identities disagree."""


class PendingTimeoutError(UploadError):
    """Indexing did not finish within the timeout; the operation is kept for resume."""


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def chunking_config() -> dict:
    return {
        "white_space_config": {
            "max_tokens_per_chunk": MAX_TOKENS_PER_CHUNK,
            "max_overlap_tokens": MAX_OVERLAP_TOKENS,
        }
    }


# ---------------------------------------------------------------- state files

def read_json(path: Path, default):
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def write_json_atomic(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    os.replace(tmp, path)


@dataclass
class StatePaths:
    project_root: Path
    store_file: Path
    manifest_file: Path

    @classmethod
    def under(cls, project_root: Path, state_dir: Path) -> "StatePaths":
        return cls(
            project_root=project_root,
            store_file=state_dir / "gemini-store.json",
            manifest_file=state_dir / "ingestion-manifest.json",
        )


def load_manifest(paths: StatePaths) -> dict:
    manifest = read_json(paths.manifest_file, {})
    manifest.setdefault("version", 1)
    manifest.setdefault("articles", {})
    return manifest


def save_manifest(paths: StatePaths, manifest: dict) -> None:
    manifest["updated_at"] = utc_now()
    write_json_atomic(paths.manifest_file, manifest)


# ---------------------------------------------------------------- store

def _is_not_found(exc: Exception) -> bool:
    return getattr(exc, "code", None) == 404


def resolve_store_name(configured: str, paths: StatePaths) -> tuple[str | None, str]:
    """Return (store_name or None, origin) without any API call.

    Raises StoreConflictError when both sources are set and disagree.
    """
    saved = (read_json(paths.store_file, {}) or {}).get("store_name") or ""
    configured = (configured or "").strip()
    if configured and saved and configured != saved:
        raise StoreConflictError(
            f"GEMINI_FILE_SEARCH_STORE={configured!r} conflicts with the saved store {saved!r} "
            f"in {paths.store_file.name}. Refusing to continue. Either clear GEMINI_FILE_SEARCH_STORE "
            f"or update/remove {paths.store_file} deliberately."
        )
    if configured:
        return configured, "configured"
    if saved:
        return saved, "saved"
    return None, "none"


def get_or_create_store(client, configured: str, paths: StatePaths) -> str:
    store_name, origin = resolve_store_name(configured, paths)
    if store_name:
        try:
            store = client.file_search_stores.get(name=store_name)
        except Exception as exc:
            if _is_not_found(exc):
                raise UploadError(
                    f"File Search store {store_name!r} ({origin}) was not found. "
                    "Not creating a replacement automatically; fix the configuration or remove the saved state."
                ) from exc
            raise
        if origin == "configured" and not paths.store_file.exists():
            write_json_atomic(paths.store_file, {"store_name": store.name, "origin": "configured", "recorded_at": utc_now()})
        log.info("Using File Search store %s (%s).", store.name, origin)
        return store.name

    store = client.file_search_stores.create(config={"display_name": STORE_DISPLAY_NAME})
    if not store.name:
        raise UploadError("Store creation returned no resource name.")
    write_json_atomic(paths.store_file, {
        "store_name": store.name,
        "display_name": STORE_DISPLAY_NAME,
        "origin": "created",
        "created_at": utc_now(),
    })
    log.info("Created File Search store %s and saved it to %s.", store.name, paths.store_file)
    return store.name


# ---------------------------------------------------------------- polling

def _state_str(state) -> str:
    return getattr(state, "value", None) or str(state or "")


def get_document_state(client, document_name: str) -> str | None:
    """Return the document state string, or None if the document no longer exists."""
    try:
        doc = client.file_search_stores.documents.get(name=document_name)
    except Exception as exc:
        if _is_not_found(exc):
            return None
        raise
    return _state_str(doc.state)


def wait_for_operation(client, operation, deadline: float, sleep=time.sleep):
    while not operation.done:
        if time.monotonic() >= deadline:
            raise PendingTimeoutError(
                f"Indexing operation {operation.name} still running at timeout; it is recorded and will be resumed on rerun."
            )
        sleep(POLL_INTERVAL_SECONDS)
        operation = client.operations.get(operation)
    if operation.error:
        raise UploadError(f"Indexing operation {operation.name} failed: {operation.error}")
    return operation


def wait_for_active(client, document_name: str, deadline: float, sleep=time.sleep) -> None:
    while True:
        state = get_document_state(client, document_name)
        if state == STATE_ACTIVE:
            return
        if state is None:
            raise UploadError(f"Document {document_name} not found after indexing.")
        if state == STATE_FAILED:
            raise UploadError(f"Document {document_name} is in STATE_FAILED.")
        if time.monotonic() >= deadline:
            raise PendingTimeoutError(f"Document {document_name} still {state} at timeout.")
        sleep(POLL_INTERVAL_SECONDS)


def _operation_from_name(name: str):
    from google.genai import types

    return types.UploadToFileSearchStoreOperation(name=name)


def _document_name_from_operation(operation) -> str | None:
    response = getattr(operation, "response", None)
    return getattr(response, "document_name", None) if response is not None else None


# ---------------------------------------------------------------- upload

@dataclass
class UploadResult:
    status: str                      # "uploaded" | "skipped"
    article_id: str
    document_name: str
    store_name: str
    uploaded: int = 0
    skipped: int = 0
    replaced_document: str | None = None
    previously_tracked: bool = False  # a document was tracked for this article before this call
    notes: list[str] = field(default_factory=list)

    @property
    def action(self) -> str:
        """Mutually exclusive classification: added | updated | skipped."""
        if self.status == "skipped":
            return "skipped"
        return "updated" if self.previously_tracked else "added"


def _relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def _delete_tracked_document(client, store_name: str, document_name: str) -> bool:
    if not document_name.startswith(f"{store_name}/documents/"):
        log.warning("Not deleting %s: it is not in store %s.", document_name, store_name)
        return False
    try:
        client.file_search_stores.documents.delete(name=document_name, config={"force": True})
        return True
    except Exception as exc:
        if _is_not_found(exc):
            return True
        log.warning("Could not delete superseded document %s (%s); recorded for later cleanup.", document_name, type(exc).__name__)
        return False


def _finalize(client, paths: StatePaths, manifest: dict, entry: dict, store_name: str,
              document_name: str, sha: str, result: UploadResult) -> None:
    """Promote a confirmed ACTIVE document to tracked; then remove the superseded one."""
    previous = entry.get("document_name")
    entry.update({
        "store_name": store_name,
        "document_name": document_name,
        "content_sha256": sha,
        "upload_status": "active",
        "confirmed_at": utc_now(),
    })
    entry.pop("pending", None)
    entry.pop("last_error", None)
    save_manifest(paths, manifest)

    if previous and previous != document_name:
        if _delete_tracked_document(client, store_name, previous):
            result.replaced_document = previous
        else:
            entry.setdefault("stale_document_names", []).append(previous)
            save_manifest(paths, manifest)


def upload_one(client, file_path: Path, configured_store: str, paths: StatePaths,
               timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS, sleep=time.sleep,
               store_name: str | None = None) -> UploadResult:
    """Upload one file; `store_name` (already resolved by the caller) skips store lookup."""
    file_path = Path(file_path)
    if not file_path.is_absolute():
        file_path = paths.project_root / file_path
    if not file_path.is_file():
        raise UploadError(f"Markdown file not found: {file_path}")

    data = file_path.read_bytes()
    sha = sha256_bytes(data)
    meta = parse_markdown_metadata(data.decode("utf-8"))
    article_id = meta.get("Article ID")
    canonical_url = meta.get("Article URL")
    if not article_id or not canonical_url:
        raise UploadError(f"{file_path.name} lacks 'Article ID:'/'Article URL:' provenance lines; run scrape-one first.")

    store_name = store_name or get_or_create_store(client, configured_store, paths)
    manifest = load_manifest(paths)
    entry = manifest["articles"].setdefault(article_id, {})
    entry.update({
        "article_id": article_id,
        "canonical_url": canonical_url,
        "title": meta.get("Title"),
        "markdown_path": _relative(file_path, paths.project_root),
        "display_name": file_path.name,
    })

    # A tracked document in a different store is not ours to replace or delete here.
    if entry.get("store_name") and entry["store_name"] != store_name:
        log.warning("Manifest tracks this article in store %s; uploading fresh to %s (old store untouched).",
                    entry["store_name"], store_name)
        for key in ("document_name", "content_sha256", "upload_status", "pending"):
            entry.pop(key, None)

    deadline = time.monotonic() + timeout_seconds
    result = UploadResult(status="", article_id=article_id, document_name="", store_name=store_name,
                          previously_tracked=bool(entry.get("document_name")))

    # 1. Resume a recorded pending operation.
    pending = entry.get("pending")
    if pending and pending.get("operation_name"):
        log.info("Resuming pending indexing operation %s.", pending["operation_name"])
        try:
            op = wait_for_operation(client, client.operations.get(_operation_from_name(pending["operation_name"])), deadline, sleep)
            doc_name = _document_name_from_operation(op)
            if not doc_name:
                raise UploadError("Resumed operation completed without a document_name; cannot confirm identity.")
            wait_for_active(client, doc_name, deadline, sleep)
        except PendingTimeoutError:
            save_manifest(paths, manifest)
            raise
        except Exception as exc:
            entry.pop("pending", None)
            entry["last_error"] = f"{type(exc).__name__}: resumed operation failed"
            save_manifest(paths, manifest)
            raise
        _finalize(client, paths, manifest, entry, store_name, doc_name, pending["content_sha256"], result)
        result.notes.append(f"resumed pending operation {pending['operation_name']}")
        if pending["content_sha256"] == sha:
            result.status, result.uploaded, result.document_name = "uploaded", 1, doc_name
            return result

    # 2. Skip unchanged content whose tracked document is confirmed ACTIVE.
    tracked = entry.get("document_name")
    if tracked and entry.get("content_sha256") == sha:
        state = get_document_state(client, tracked)
        if state == STATE_ACTIVE:
            entry["upload_status"] = "active"
            entry["last_verified_at"] = utc_now()
            save_manifest(paths, manifest)
            result.status, result.skipped, result.document_name = "skipped", 1, tracked
            return result
        if state == STATE_PENDING:
            wait_for_active(client, tracked, deadline, sleep)
            _finalize(client, paths, manifest, entry, store_name, tracked, sha, result)
            result.status, result.skipped, result.document_name = "skipped", 1, tracked
            result.notes.append("tracked document was pending; waited until active")
            return result
        log.info("Tracked document %s is %s; re-uploading.", tracked, state or "missing")
        if state is None:
            entry.pop("document_name", None)

    # 3. Upload (new or changed content).
    operation = client.file_search_stores.upload_to_file_search_store(
        file_search_store_name=store_name,
        file=str(file_path),
        config={
            "mime_type": MARKDOWN_MIME_TYPE,
            "display_name": file_path.name,
            "custom_metadata": [
                {"key": "article_id", "string_value": article_id},
                {"key": "content_sha256", "string_value": sha},
            ],
            "chunking_config": chunking_config(),
        },
    )
    entry["pending"] = {"operation_name": operation.name, "content_sha256": sha, "started_at": utc_now()}
    entry["upload_status"] = "pending"
    save_manifest(paths, manifest)

    try:
        operation = wait_for_operation(client, operation, deadline, sleep)
        doc_name = _document_name_from_operation(operation)
        if not doc_name:
            raise UploadError("Upload operation completed without a document_name; cannot confirm identity.")
        wait_for_active(client, doc_name, deadline, sleep)
    except PendingTimeoutError:
        raise
    except Exception as exc:
        entry.pop("pending", None)
        entry["upload_status"] = "failed" if not entry.get("document_name") else "active"
        entry["last_error"] = f"{type(exc).__name__}: upload not confirmed"
        save_manifest(paths, manifest)
        raise

    _finalize(client, paths, manifest, entry, store_name, doc_name, sha, result)
    result.status, result.uploaded, result.document_name = "uploaded", 1, doc_name
    return result
