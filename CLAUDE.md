# CLAUDE.md

## Assignment context

Take-home assignment. Future GitHub repo name: `paper-lantern`. Full scope:

1. Scrape at least 30 public articles from `support.optisigns.com`.
2. Convert each to clean Markdown.
3. Upload them programmatically to a Gemini File Search Store.
4. Run the pipeline daily in Docker.

This repo currently covers steps 1-3 for a limited collection (default 30 articles).

## Gemini approach

- SDK: `google-genai` (the current `from google import genai` package, not
  the deprecated `google-generativeai`).
- Client is always constructed with an explicit `api_key=` argument — never
  rely on the SDK's implicit environment-variable auto-detection, so the
  resolved key (including the `API_KEY` fallback) is always what gets used.
- Lightweight connectivity check: `client.models.list()` — does not generate
  content or touch File Search.
- File Search workflow (for the future uploader milestone):
  `client.file_search_stores.create(...)`, then either
  `client.file_search_stores.upload_to_file_search_store(...)` (direct) or
  `client.files.upload(...)` + `client.file_search_stores.import_file(...)`
  (import from Files API).
- Default model: `gemini-3.8-flash` (per current quickstart docs).

## Secret handling rules

- `.env` is never created, opened, printed, or overwritten by tooling. The
  user manages it manually; `.env.sample` is the tracked template.
- Config reads `GEMINI_API_KEY` with `API_KEY` as a fallback (the assignment's
  Docker invocation uses `API_KEY`).
- All paths resolve relative to the project root (`Path(__file__).parent` in
  `config.py`), not the current working directory.
- No code path logs, prints, or includes the raw API key in exception text;
  `--check-api` redacts the key from any error message before printing.

## Single-article milestone (current)

- `scraper.py`: `scrape-one` (Zendesk API `/api/v2/help_center/<locale>/articles/<id>.json`,
  fallback `.article-body` on the page). Writes provenance header
  (`Article URL:`, `Article ID:`, `Updated at:`) that `upload-one` parses.
- `uploader.py`: persistent store (`state/gemini-store.json`), manifest
  (`state/ingestion-manifest.json`), skip/resume/replace logic, chunking 500/50.
- `query.py`: Interactions API (`client.interactions.create`, tool
  `{"type": "file_search", ...}`); verified sources come only from
  `file_citation` annotations mapped via the manifest.
- Prompt: `prompts/optibot.txt` (verbatim, loaded per query).
- Tests: `python -m unittest discover -s tests` (stdlib, offline, fake clients).
- `ask`: single retry policy in `query.ask_with_retry` (max 2 attempts); SDK Interactions retries disabled on the query client via `sdk_configuration.retry_config` (google-genai 2.28.0 internals). Timeout: `GEMINI_QUERY_TIMEOUT_SECONDS` (s), passed as per-call `timeout=` (s) and `HttpOptions.timeout` (ms).
- Live Gemini upload/ask are run manually by the user, never automatically by tooling.

## Collection milestone (current)

- `pipeline.py`: `collect_articles` (list endpoint `/api/v2/help_center/en-us/articles.json`,
  cursor pagination `page[size]=100` + `sort_by=updated_at&sort_order=desc`, verified live;
  dedupe by ID; YouTube `360051014713` always inside the limit), `upload_collection`
  (sequential `uploader.upload_one` with a pre-resolved store), `summarize`/`write_summary`.
- CLI: `scrape --limit N` (no Gemini), `run --limit N`; no command = `run` with `SUPPORT_ARTICLE_LIMIT`.
- Result classes are mutually exclusive: added / updated / skipped / failed (`UploadResult.action`).
- `state/article-files.json` keeps stable filenames; manifest is still the only upload record.
- Logs: `logs/last-run.json`, `logs/last-successful-run.json` (success only), `logs/last-scrape.json`.
- The help center rate-limits anonymous API calls (429 + Retry-After); the retry session honours it.

## Docker milestone (current)

- `Dockerfile`: `python:3.14-slim`, `ENTRYPOINT ["python", "main.py"]`, `CMD ["run"]`; image `paper-lantern:local`.
- `.dockerignore` excludes `.env*` (except `.env.sample`), `.venv`, `.git`, caches, `data/`, `state/`, `logs/`, `tests/`.
- State persists only via bind mounts `data/`, `state/`, `logs/` -> `/app/...`; manifest paths are relative POSIX.
- `.env.sample` must stay Docker `--env-file` compatible (literal `KEY=value`, no quotes/interpolation).

## Hosted daily run (current)

- `.github/workflows/daily-sync.yml`: cron `17 1 * * *` + `workflow_dispatch`, concurrency `daily-sync`,
  `API_KEY` secret, `GEMINI_MODEL=gemini-3.5-flash-lite`; details in `docs/hosted-sync.md`.
- State persists on branch `pipeline-state` via `scripts/state_sync.py` (stdlib; restore / save / bootstrap),
  git plumbing with a temp index, explicit allowlist, non-force push, no PAT.
- Restore must fail before Gemini is called if state is missing/invalid; save runs even after pipeline failure.
- `scripts/job_summary.py` renders the job summary from `logs/last-run.json`.
- Bootstrap/push of `pipeline-state` is done manually by the user.
