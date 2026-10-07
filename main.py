"""CLI entry point for the OptiSigns support-article pipeline.

Commands:
  run         discover + scrape + delta upload of the selected collection (default
              when no command is given; size from SUPPORT_ARTICLE_LIMIT)
  scrape      discover + scrape the selected collection only (no Gemini calls)
  scrape-one  fetch one Help Center article and save it as Markdown
  upload-one  upload one Markdown file into the persistent File Search store
  ask         query the store via the Interactions API with verified citations

The setup checks --check-config and --check-api are unchanged.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

from config import (
    ARTICLES_DIR,
    LOGS_DIR,
    OPTIBOT_PROMPT_PATH,
    PROJECT_ROOT,
    STATE_DIR,
    ConfigError,
    describe_non_secret,
    ensure_runtime_dirs,
    load_config,
)

API_TIMEOUT_SECONDS = 15
UPLOAD_HTTP_TIMEOUT_SECONDS = 120

log = logging.getLogger("paper_lantern")
PROGRESS_LOGGER = "paper_lantern.progress"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description=(
            "OptiSigns support-article scraper and Gemini File Search uploader. "
            "Use --check-config or --check-api to validate setup, or one of the "
            "commands below. With no command, runs the collection pipeline once "
            "(same as `run`, limit from SUPPORT_ARTICLE_LIMIT)."
        ),
    )
    parser.add_argument(
        "--check-config",
        action="store_true",
        help="Validate configuration (.env values) without calling any API, then exit.",
    )
    parser.add_argument(
        "--check-api",
        action="store_true",
        help=(
            "Verify Gemini API authentication and connectivity with a lightweight "
            "metadata request (lists available models). Does not generate text, "
            "create stores, upload files, or scrape articles."
        ),
    )

    sub = parser.add_subparsers(dest="command", metavar="COMMAND")

    limit_help = ("Size of this run's selected collection: the newest-updated usable en-us articles, "
                  "always including the YouTube article (default: SUPPORT_ARTICLE_LIMIT, 30). "
                  "Not a full help-center sync.")
    p_run = sub.add_parser("run", help="Discover, scrape and delta-upload the selected collection once, then exit.")
    p_run.add_argument("--limit", type=positive_int, default=None, help=limit_help)
    p_run.add_argument("--timeout", type=int, default=300, help="Max seconds to wait for indexing per article (default 300).")
    p_col = sub.add_parser("scrape", help="Discover and scrape the selected collection to Markdown (no Gemini calls).")
    p_col.add_argument("--limit", type=positive_int, default=None, help=limit_help)

    p_scrape = sub.add_parser("scrape-one", help="Scrape one Help Center article to Markdown (no API key needed).")
    p_scrape.add_argument("--article-url", required=True, help="Full Help Center article URL.")

    p_upload = sub.add_parser("upload-one", help="Upload one Markdown file to the persistent File Search store.")
    p_upload.add_argument("--file", required=True, help="Markdown path (relative to the project root or absolute).")
    p_upload.add_argument("--timeout", type=int, default=300, help="Max seconds to wait for indexing (default 300).")

    p_ask = sub.add_parser("ask", help="Ask OptiBot a question answered only from the File Search store.")
    p_ask.add_argument("--question", required=True)
    p_ask.add_argument("--output-prefix", required=True,
                       help="Output path prefix; writes <prefix>.json and <prefix>.md (relative to project root).")
    p_ask.add_argument("--require-citations", action="store_true",
                       help="Exit nonzero unless every returned citation maps to a tracked article URL.")
    return parser


def positive_int(value: str) -> int:
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"expected a positive integer, got {value!r}") from None
    if number < 1:
        raise argparse.ArgumentTypeError(f"expected a positive integer, got {value!r}")
    return number


def setup_logging() -> None:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    console = logging.StreamHandler(sys.stderr)
    console.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    console.addFilter(lambda record: record.name != PROGRESS_LOGGER)  # progress is already printed
    file_handler = logging.FileHandler(LOGS_DIR / "pipeline.log", encoding="utf-8")
    file_handler.setFormatter(fmt)
    root.addHandler(console)
    root.addHandler(file_handler)
    # Third-party HTTP loggers stay quiet: they could echo request details.
    for name in ("httpx", "httpcore", "urllib3", "google_genai", "google.genai"):
        logging.getLogger(name).setLevel(logging.WARNING)


def resolve_project_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else PROJECT_ROOT / path


def redacted(exc: Exception, secret: str | None) -> str:
    message = str(exc)
    if secret:
        message = message.replace(secret, "[REDACTED]")
    return f"{type(exc).__name__}: {message}"


def make_client(api_key: str, timeout_seconds: int):
    from google import genai
    from google.genai import types

    return genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(timeout=timeout_seconds * 1000),
    )


def cmd_check_config() -> int:
    try:
        config = load_config(require_api_key=False, require_file_search_store=False)
    except ConfigError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 1

    if not config.has_api_key:
        print("Configuration error: GEMINI_API_KEY (or API_KEY fallback) is missing or a placeholder.", file=sys.stderr)
        print("Copy .env.sample to .env and set a real key, then re-run --check-config.", file=sys.stderr)
        settings = describe_non_secret(config)
        for key, value in settings.items():
            print(f"  {key}: {value}")
        return 1

    print("Configuration OK (GEMINI_FILE_SEARCH_STORE may be empty; state/gemini-store.json is used then).")
    settings = describe_non_secret(config)
    for key, value in settings.items():
        print(f"  {key}: {value}")
    return 0


def cmd_check_api() -> int:
    try:
        config = load_config(require_api_key=True, require_file_search_store=False)
    except ConfigError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 1

    try:
        from google import genai  # noqa: F401
    except ImportError as exc:
        print(f"Gemini SDK is not installed correctly: {exc}", file=sys.stderr)
        return 1

    try:
        client = make_client(config.gemini_api_key, API_TIMEOUT_SECONDS)
        models = list(client.models.list())
    except Exception as exc:  # noqa: BLE001 - surface a redacted summary, not raw secrets
        print(f"Gemini API check failed: {redacted(exc, config.gemini_api_key)}", file=sys.stderr)
        return 1

    print(f"Gemini API check OK — authenticated, {len(models)} model(s) visible.")
    print(f"  model configured for use: {config.gemini_model}")
    return 0


def cmd_scrape_one(article_url: str) -> int:
    import scraper

    try:
        path, article = scraper.scrape_one(article_url, ARTICLES_DIR)
    except scraper.ScrapeError as exc:
        log.error("Scrape failed: %s", exc)
        return 1
    log.info("Scraped article %s via %s -> %s", article.ref.article_id, article.source,
             path.relative_to(PROJECT_ROOT).as_posix())
    print(f"Saved: {path.relative_to(PROJECT_ROOT).as_posix()}")
    print(f"  title: {article.title}")
    print(f"  source: {article.source}")
    print(f"  updated_at: {article.updated_at or '(not provided)'}")
    return 0


def cmd_upload_one(file_arg: str, timeout_seconds: int) -> int:
    import uploader

    try:
        config = load_config(require_api_key=True)
    except ConfigError as exc:
        log.error("Configuration error: %s", exc)
        return 1

    paths = uploader.StatePaths.under(PROJECT_ROOT, STATE_DIR)
    try:
        client = make_client(config.gemini_api_key, UPLOAD_HTTP_TIMEOUT_SECONDS)
        result = uploader.upload_one(client, resolve_project_path(file_arg), config.gemini_file_search_store,
                                     paths, timeout_seconds=timeout_seconds)
    except uploader.PendingTimeoutError as exc:
        log.error("%s", redacted(exc, config.gemini_api_key))
        print("Upload NOT confirmed yet (still indexing). Re-run the same command to resume.", file=sys.stderr)
        return 2
    except Exception as exc:  # noqa: BLE001 - redacted summary
        log.error("Upload failed: %s", redacted(exc, config.gemini_api_key))
        return 1

    cfg = uploader.chunking_config()["white_space_config"]
    log.info("Upload summary: uploaded=%d skipped=%d store=%s document=%s",
             result.uploaded, result.skipped, result.store_name, result.document_name)
    print(f"Result: {result.status}")
    print(f"  files uploaded: {result.uploaded}")
    print(f"  files skipped (unchanged, active): {result.skipped}")
    print(f"  store: {result.store_name}")
    print(f"  document: {result.document_name} (STATE_ACTIVE confirmed)")
    if result.replaced_document:
        print(f"  replaced previous document: {result.replaced_document}")
    for note in result.notes:
        print(f"  note: {note}")
    print(f"  chunking (configured): white_space max_tokens_per_chunk={cfg['max_tokens_per_chunk']}, "
          f"max_overlap_tokens={cfg['max_overlap_tokens']}")
    print("  provider chunk count: unavailable (the File Search Document API does not expose it)")
    print(f"  manifest: {paths.manifest_file.relative_to(PROJECT_ROOT).as_posix()}")
    return 0


def cmd_ask(question: str, output_prefix: str, require_citations: bool) -> int:
    import query
    import uploader

    try:
        config = load_config(require_api_key=True)
    except ConfigError as exc:
        log.error("Configuration error: %s", exc)
        return 1

    paths = uploader.StatePaths.under(PROJECT_ROOT, STATE_DIR)
    try:
        store_name, origin = uploader.resolve_store_name(config.gemini_file_search_store, paths)
    except uploader.StoreConflictError as exc:
        log.error("%s", exc)
        return 1
    if not store_name:
        log.error("No File Search store configured or saved. Run upload-one first.")
        return 1

    manifest = uploader.load_manifest(paths)
    system_instruction = query.load_system_instruction(OPTIBOT_PROMPT_PATH)

    from google import genai

    timeout_seconds = config.gemini_query_timeout_seconds
    log.info("ask: google-genai %s, model=%s, timeout=%.1fs per attempt, max attempts=%d (SDK retries disabled)",
             genai.__version__, config.gemini_model, timeout_seconds, query.MAX_QUERY_ATTEMPTS)
    try:
        client = query.make_query_client(config.gemini_api_key, timeout_seconds)
        interaction, attempts = query.ask_with_retry(
            client, model=config.gemini_model, question=question,
            system_instruction=system_instruction, store_name=store_name, timeout_seconds=timeout_seconds)
    except query.QueryFailedError as exc:
        log.error("Gemini query failed after %d attempt(s): %s. No answer artifact written.",
                  exc.attempts, query.error_label(exc.last_error))
        if query.is_transient(exc.last_error):
            print("The model is likely overloaded or slow. Retry later, or raise GEMINI_QUERY_TIMEOUT_SECONDS.",
                  file=sys.stderr)
        else:
            print(f"Details: {redacted(exc.last_error, config.gemini_api_key)}", file=sys.stderr)
        return 1
    except Exception as exc:  # noqa: BLE001 - redacted summary
        log.error("Gemini query failed: %s", redacted(exc, config.gemini_api_key))
        return 1

    answer, annotations = query.extract_answer(interaction)
    verification = query.verify_citations(annotations, manifest)
    record = query.build_record(question=question, model=config.gemini_model, store_name=store_name,
                                interaction=interaction, answer=answer, annotations=annotations,
                                verification=verification, require_citations=require_citations)
    record["query"] = {"attempts": attempts, "max_attempts": query.MAX_QUERY_ATTEMPTS,
                       "timeout_seconds": timeout_seconds}
    record = query.redact(record, config.gemini_api_key)
    json_path, md_path = query.save_outputs(record, resolve_project_path(output_prefix))

    status = record["interaction_status"]
    print("Answer:")
    print(answer or "(empty answer)")
    print()
    print(query.format_sources(verification.verified_urls))
    print()
    print(f"Saved: {json_path.relative_to(PROJECT_ROOT).as_posix()}, {md_path.relative_to(PROJECT_ROOT).as_posix()}"
          if json_path.is_relative_to(PROJECT_ROOT) else f"Saved: {json_path}, {md_path}")
    log.info("ask: status=%s file_citations=%d verified_urls=%d unmapped=%d",
             status, verification.file_citation_count, len(verification.verified_urls), len(verification.unmapped))

    if status not in (None, "completed"):
        log.error("Interaction status is %s, not completed.", json.dumps(status))
        return 1
    if require_citations and not verification.passed:
        log.error("Citation verification FAILED: %s", verification.failure_reason())
        return 3
    return 0


def cmd_collection(limit: int | None, upload: bool, timeout_seconds: int = 300) -> int:
    """`scrape` (upload=False) or `run` (upload=True) over the selected collection."""
    import time

    import pipeline
    import scraper
    import uploader

    try:
        config = load_config(require_api_key=upload)
    except ConfigError as exc:
        log.error("Configuration error: %s", exc)
        return 1
    limit = limit or config.support_article_limit
    command = "run" if upload else "scrape"
    started_at, started = uploader.utc_now(), time.monotonic()
    paths = uploader.StatePaths.under(PROJECT_ROOT, STATE_DIR)

    def sanitize(exc: Exception) -> str:
        return redacted(exc, config.gemini_api_key)

    def progress(line: str) -> None:
        print(line, flush=True)
        logging.getLogger(PROGRESS_LOGGER).info(line.strip())

    client = None
    if upload:
        try:  # resolve the store before scraping so a conflict fails fast, without API calls
            uploader.resolve_store_name(config.gemini_file_search_store, paths)
            client = make_client(config.gemini_api_key, UPLOAD_HTTP_TIMEOUT_SECONDS)
        except Exception as exc:  # noqa: BLE001 - redacted summary
            log.error("Cannot start run: %s", sanitize(exc))
            return 1

    log.info("%s: limit=%d locale=%s order=updated_at desc source=%s", command, limit, pipeline.DEFAULT_LOCALE,
             scraper.list_articles_url(config.support_base_url, pipeline.DEFAULT_LOCALE))
    print(f"Discovering and scraping {limit} article(s) (newest updated first)...", flush=True)
    col = pipeline.collect_articles(scraper.build_session(), config.support_base_url, limit, ARTICLES_DIR,
                                    paths, progress=progress)
    store_name = None
    if upload:
        cfg = uploader.chunking_config()["white_space_config"]
        log.info("run: uploading sequentially, chunking white_space max_tokens_per_chunk=%d max_overlap_tokens=%d",
                 cfg["max_tokens_per_chunk"], cfg["max_overlap_tokens"])
        print(f"Delta upload of {len(col.scraped)} scraped article(s)...", flush=True)
        store_name = pipeline.upload_collection(client, col, config.gemini_file_search_store, paths,
                                                timeout_seconds, sanitize, progress=progress)

    summary = pipeline.summarize(col, command=command, base_url=config.support_base_url, started_at=started_at,
                                 started_monotonic=started, uploaded=upload, store_name=store_name, paths=paths)
    if upload:
        pipeline.write_summary(summary, LOGS_DIR, last_name="last-run.json", success_name="last-successful-run.json")
    else:
        pipeline.write_summary(summary, LOGS_DIR, last_name="last-scrape.json", success_name=None)
    pipeline.print_summary(summary)
    log.info("%s finished: status=%s counts=%s", command, summary["status"], json.dumps(summary["counts"]))
    print(f"  summary: logs/{'last-run.json' if upload else 'last-scrape.json'}")
    return 0 if summary["status"] == "success" else 1


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="replace")  # never crash printing non-ASCII answers
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.check_config:
        return cmd_check_config()
    if args.check_api:
        return cmd_check_api()
    ensure_runtime_dirs()
    setup_logging()
    if not args.command:
        return cmd_collection(None, upload=True)
    if args.command == "run":
        return cmd_collection(args.limit, upload=True, timeout_seconds=args.timeout)
    if args.command == "scrape":
        return cmd_collection(args.limit, upload=False)
    if args.command == "scrape-one":
        return cmd_scrape_one(args.article_url)
    if args.command == "upload-one":
        return cmd_upload_one(args.file, args.timeout)
    if args.command == "ask":
        return cmd_ask(args.question, args.output_prefix, args.require_citations)
    parser.error(f"unknown command {args.command!r}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
