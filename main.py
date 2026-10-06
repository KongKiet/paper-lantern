"""CLI entry point for the OptiSigns support-article pipeline.

Setup milestone: configuration validation and a lightweight API connectivity
check are implemented. The scrape/convert/upload pipeline is not yet
implemented — see scraper.py and uploader.py.
"""

from __future__ import annotations

import argparse
import sys

from config import ConfigError, describe_non_secret, ensure_runtime_dirs, load_config

API_TIMEOUT_SECONDS = 15


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description=(
            "OptiSigns support-article scraper and Gemini File Search uploader. "
            "Run with no flags to see pipeline status; use --check-config or "
            "--check-api to validate setup before the pipeline is implemented."
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
    return parser


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

    print("Configuration OK (GEMINI_FILE_SEARCH_STORE may be empty at this stage).")
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
        from google import genai
        from google.genai import types
    except ImportError as exc:
        print(f"Gemini SDK is not installed correctly: {exc}", file=sys.stderr)
        return 1

    try:
        client = genai.Client(
            api_key=config.gemini_api_key,
            http_options=types.HttpOptions(timeout=API_TIMEOUT_SECONDS * 1000),
        )
        models = list(client.models.list())
    except Exception as exc:  # noqa: BLE001 - surface a redacted summary, not raw secrets
        message = str(exc).replace(config.gemini_api_key, "[REDACTED]")
        print(f"Gemini API check failed: {type(exc).__name__}: {message}", file=sys.stderr)
        return 1

    print(f"Gemini API check OK — authenticated, {len(models)} model(s) visible.")
    print(f"  model configured for use: {config.gemini_model}")
    return 0


def cmd_default() -> int:
    ensure_runtime_dirs()
    print("OptiSigns support-article pipeline: NOT IMPLEMENTED YET.")
    print("This repository is at the setup milestone only.")
    print("  - scraper.py: placeholder, raises NotImplementedError")
    print("  - uploader.py: placeholder, raises NotImplementedError")
    print()
    print("Use --check-config to validate settings, or --check-api to verify Gemini connectivity.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.check_config:
        return cmd_check_config()
    if args.check_api:
        return cmd_check_api()
    return cmd_default()


if __name__ == "__main__":
    raise SystemExit(main())
