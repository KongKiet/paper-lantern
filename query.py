"""Ask Gemini questions grounded only in the File Search store.

Uses the Interactions API with File Search as the only tool. Sources shown to
the user come exclusively from `file_citation` annotations returned by
Gemini, mapped to canonical URLs through the ingestion manifest; URLs that
merely appear in the answer text are never treated as verified.
"""

from __future__ import annotations

import json
import logging
import random
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

log = logging.getLogger(__name__)

MAX_SOURCES = 3

# Single retry policy for a query, owned by this module. SDK-internal retries
# are disabled on the query client (see make_query_client) so attempts never
# stack: at most MAX_QUERY_ATTEMPTS network requests per question.
MAX_QUERY_ATTEMPTS = 2
RETRY_BASE_DELAY_SECONDS = 2.0
RETRY_JITTER_SECONDS = 1.0
TRANSIENT_STATUS_CODES = frozenset({408, 429, 500, 502, 503, 504})


class CitationError(RuntimeError):
    """Citations were required but missing or unmappable."""


def load_system_instruction(path: Path) -> str:
    text = path.read_text(encoding="utf-8").rstrip()
    if not text:
        raise ValueError(f"System instruction file is empty: {path}")
    return text


def _get(obj, key, default=None):
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _to_plain(obj):
    if obj is None or isinstance(obj, (str, int, float, bool)):
        return obj
    if isinstance(obj, dict):
        return {k: _to_plain(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_to_plain(v) for v in obj]
    if hasattr(obj, "model_dump"):
        return _to_plain(obj.model_dump(mode="json", by_alias=True, exclude_none=True))
    return str(obj)


def redact(obj, secret: str | None):
    if not secret:
        return obj
    if isinstance(obj, str):
        return obj.replace(secret, "[REDACTED]")
    if isinstance(obj, dict):
        return {k: redact(v, secret) for k, v in obj.items()}
    if isinstance(obj, list):
        return [redact(v, secret) for v in obj]
    return obj


def extract_answer(interaction) -> tuple[str, list[dict]]:
    """Return (answer text, annotations) from model_output text blocks.

    Each annotation is a plain dict of exactly what the API returned, plus
    `text_block_index` so start/end indices can be related to their block.
    """
    texts: list[str] = []
    annotations: list[dict] = []
    for step in _get(interaction, "steps") or []:
        if _get(step, "type") != "model_output":
            continue
        for block in _get(step, "content") or []:
            if _get(block, "type") != "text":
                continue
            block_index = len(texts)
            texts.append(_get(block, "text") or "")
            for ann in _get(block, "annotations") or []:
                plain = _to_plain(ann)
                if isinstance(plain, dict):
                    plain = {**plain, "text_block_index": block_index}
                    annotations.append(plain)
    answer = _get(interaction, "output_text") or "".join(texts)
    return answer, annotations


@dataclass
class Verification:
    verified_urls: list[str] = field(default_factory=list)
    mapped: list[dict] = field(default_factory=list)
    unmapped: list[dict] = field(default_factory=list)
    file_citation_count: int = 0

    @property
    def passed(self) -> bool:
        return bool(self.verified_urls) and not self.unmapped

    def failure_reason(self) -> str | None:
        if self.file_citation_count == 0:
            return "Gemini returned no file_citation annotations."
        if self.unmapped:
            return f"{len(self.unmapped)} citation(s) could not be mapped to a tracked article."
        if not self.verified_urls:
            return "No citation mapped to a canonical URL."
        return None


def _map_citation(ann: dict, articles: dict) -> tuple[str | None, str | None]:
    """Map one file_citation to (article_id, matched_by) using the manifest."""
    custom = ann.get("custom_metadata") or {}
    if isinstance(custom, dict):
        aid = custom.get("article_id")
        if isinstance(aid, dict):  # tolerate {"string_value": ...} shapes
            aid = aid.get("string_value")
        if aid is not None and str(aid) in articles:
            return str(aid), "custom_metadata.article_id"

    for key in ("document_uri", "source", "file_name"):
        value = ann.get(key)
        if not isinstance(value, str) or not value:
            continue
        for aid, entry in articles.items():
            doc = entry.get("document_name")
            if doc and (value == doc or value.endswith("/" + doc) or value.rstrip("/").endswith(doc)):
                return aid, f"{key}=document_name"

    file_name = ann.get("file_name")
    if isinstance(file_name, str) and file_name:
        matches = [aid for aid, e in articles.items() if e.get("display_name") == file_name]
        if len(matches) == 1:
            return matches[0], "file_name=display_name"
    return None, None


def verify_citations(annotations: list[dict], manifest: dict) -> Verification:
    """Only provider `file_citation` annotations can produce verified URLs."""
    articles = {
        aid: e for aid, e in (manifest.get("articles") or {}).items()
        if e.get("upload_status") == "active" and e.get("canonical_url")
    }
    result = Verification()
    for ann in annotations:
        if ann.get("type") != "file_citation":
            continue
        result.file_citation_count += 1
        aid, matched_by = _map_citation(ann, articles)
        if aid is None:
            result.unmapped.append(ann)
            continue
        url = articles[aid]["canonical_url"]
        result.mapped.append({"article_id": aid, "canonical_url": url, "matched_by": matched_by})
        if url not in result.verified_urls and len(result.verified_urls) < MAX_SOURCES:
            result.verified_urls.append(url)
    return result


class QueryFailedError(RuntimeError):
    """All query attempts failed; `last_error` is the final exception."""

    def __init__(self, attempts: int, last_error: Exception):
        super().__init__(f"Gemini query failed after {attempts} attempt(s): {error_label(last_error)}")
        self.attempts = attempts
        self.last_error = last_error


def make_query_client(api_key: str, timeout_seconds: float, httpx_client=None):
    """Client dedicated to Interactions queries.

    Units: HttpOptions.timeout is MILLISECONDS (client default); the per-call
    `timeout=` passed in `ask` is SECONDS (google-genai 2.28.0
    `_coerce_timeout_ms`: seconds * 1000). Both come from the same value.

    The SDK's own Interactions retry (default: up to 3 retries on
    408/409/429/5XX) is replaced by a no-retry config on this client only, so
    `ask_with_retry` is the single retry policy.
    """
    from google import genai
    from google.genai import types
    from google.genai._gaos import utils as gaos_utils

    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(timeout=int(timeout_seconds * 1000), httpx_client=httpx_client),
    )
    client.interactions.sdk_configuration.retry_config = gaos_utils.RetryConfig("none", None, False)
    return client


def _timeout_error_types() -> tuple[type, ...]:
    types_: list[type] = []
    try:
        import httpx

        types_.append(httpx.TimeoutException)
    except ImportError:
        pass
    try:  # the exception the Interactions client actually raises on timeout
        from google.genai._gaos.lib.compat_errors import APIConnectionError

        types_.append(APIConnectionError)  # includes APITimeoutError
    except ImportError:
        pass
    return tuple(types_)


def status_code_of(exc: Exception) -> int | None:
    code = getattr(exc, "status_code", None)
    if code is None:
        code = getattr(exc, "code", None)
    return code if isinstance(code, int) else None


def is_transient(exc: Exception) -> bool:
    """Timeouts/connection failures and 408/429/5xx are retryable; 400/401/403/404 etc. are not."""
    if isinstance(exc, _timeout_error_types()):
        return True
    return status_code_of(exc) in TRANSIENT_STATUS_CODES


def error_label(exc: Exception) -> str:
    """Sanitized error description: type name and HTTP status only, never the message."""
    code = status_code_of(exc)
    return f"{type(exc).__name__}" + (f" (HTTP {code})" if code is not None else "")


def ask(client, *, model: str, question: str, system_instruction: str, store_name: str, timeout_seconds: float):
    """One Interactions API call; File Search over our store is the only tool."""
    return client.interactions.create(
        model=model,
        input=question,
        system_instruction=system_instruction,
        tools=[{"type": "file_search", "file_search_store_names": [store_name]}],
        timeout=timeout_seconds,  # seconds (per-call override)
    )


def ask_with_retry(client, *, model: str, question: str, system_instruction: str, store_name: str,
                   timeout_seconds: float, max_attempts: int = MAX_QUERY_ATTEMPTS,
                   sleep=time.sleep, clock=time.monotonic, jitter=random.uniform):
    """Run `ask` under the single bounded retry policy. Returns (interaction, attempts)."""
    for attempt in range(1, max_attempts + 1):
        started = clock()
        log.info("ask attempt %d/%d: model=%s timeout=%.1fs", attempt, max_attempts, model, timeout_seconds)
        try:
            interaction = ask(client, model=model, question=question, system_instruction=system_instruction,
                              store_name=store_name, timeout_seconds=timeout_seconds)
        except Exception as exc:  # noqa: BLE001 - classified below, logged sanitized
            elapsed = clock() - started
            transient = is_transient(exc)
            log.warning("ask attempt %d/%d failed after %.1fs: %s (%s)", attempt, max_attempts, elapsed,
                        error_label(exc), "transient" if transient else "not retryable")
            if not transient or attempt == max_attempts:
                raise QueryFailedError(attempt, exc) from exc
            delay = RETRY_BASE_DELAY_SECONDS * attempt + jitter(0, RETRY_JITTER_SECONDS)
            log.info("retrying in %.1fs", delay)
            sleep(delay)
            continue
        log.info("ask attempt %d/%d succeeded after %.1fs", attempt, max_attempts, clock() - started)
        return interaction, attempt
    raise AssertionError("unreachable")


def build_record(*, question: str, model: str, store_name: str, interaction, answer: str,
                 annotations: list[dict], verification: Verification, require_citations: bool) -> dict:
    return {
        "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "question": question,
        "model": model,
        "file_search_store": store_name,
        "interaction_id": _get(interaction, "id"),
        "interaction_status": _to_plain(_get(interaction, "status")),
        "answer": answer,
        "citations": {
            "raw_annotations": annotations,
            "file_citation_count": verification.file_citation_count,
            "mapped": verification.mapped,
            "unmapped": verification.unmapped,
        },
        "verified_sources": verification.verified_urls,
        "verification": {
            "require_citations": require_citations,
            "passed": verification.passed,
            "reason": verification.failure_reason(),
        },
    }


def format_sources(urls: list[str]) -> str:
    if not urls:
        return "Verified sources: (none - no provider citation metadata mapped to a tracked article)"
    return "Verified sources:\n" + "\n".join(f"Article URL: {u}" for u in urls[:MAX_SOURCES])


def render_markdown_report(record: dict) -> str:
    v = record["verification"]
    lines = [
        "# OptiBot query",
        "",
        f"- Question: {record['question']}",
        f"- Model: {record['model']}",
        f"- File Search store: {record['file_search_store']}",
        f"- Interaction ID: {record['interaction_id']}",
        f"- Citations required: {v['require_citations']}; verification passed: {v['passed']}"
        + (f" ({v['reason']})" if v["reason"] else ""),
        "",
        "## Answer (as returned by Gemini)",
        "",
        record["answer"] or "(empty)",
        "",
        "## Verified sources",
        "",
    ]
    lines += [f"Article URL: {u}" for u in record["verified_sources"]] or ["(none)"]
    lines += [
        "",
        "## Citation evidence",
        "",
        f"file_citation annotations: {record['citations']['file_citation_count']}, "
        f"mapped: {len(record['citations']['mapped'])}, unmapped: {len(record['citations']['unmapped'])}",
        "",
        "```json",
        json.dumps(record["citations"], indent=2, ensure_ascii=False),
        "```",
        "",
    ]
    return "\n".join(lines)


def save_outputs(record: dict, prefix: Path) -> tuple[Path, Path]:
    prefix.parent.mkdir(parents=True, exist_ok=True)
    json_path = prefix.with_name(prefix.name + ".json")
    md_path = prefix.with_name(prefix.name + ".md")
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown_report(record), encoding="utf-8")
    return json_path, md_path
