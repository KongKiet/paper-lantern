# CLAUDE.md

## Assignment context

Take-home assignment. Future GitHub repo name: `paper-lantern`. Full scope:

1. Scrape at least 30 public articles from `support.optisigns.com`.
2. Convert each to clean Markdown.
3. Upload them programmatically to a Gemini File Search Store.
4. Run the pipeline daily in Docker.

This repo currently covers **only** step 0: repository and Python environment
setup. Steps 1-4 are not implemented.

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

## Setup milestone (current)

- `.venv` created with Python 3.14.8.
- Dependencies pinned in `requirements.txt`: google-genai, python-dotenv,
  requests, beautifulsoup4, markdownify (see file for exact versions).
- `config.py`, `main.py`, `scraper.py` (placeholder), `uploader.py`
  (placeholder) in place.
- `main.py --check-config` and `main.py --check-api` implemented and verified
  (`--check-api` not run automatically — requires a real key in `.env`).
- Runtime dirs `data/articles/`, `state/`, `logs/` created with `.gitkeep`,
  gitignored otherwise.

## Next milestone

Implement `scraper.py`: discover article URLs under
`support.optisigns.com`, fetch each page, convert to clean Markdown with
`markdownify`, and save under `data/articles/`. Target: at least 30 articles.
