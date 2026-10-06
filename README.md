# paper-lantern

Scrapes public support articles from `support.optisigns.com`, converts them to
clean Markdown, and uploads them to a Gemini File Search Store for retrieval.
Intended to run daily in Docker.

## Current status

**Setup milestone only.** Implemented so far:

- Python environment and pinned dependencies
- Configuration loading/validation (`config.py`)
- CLI skeleton (`main.py`) with `--check-config` and `--check-api`
- Placeholder interfaces for scraping (`scraper.py`) and uploading
  (`uploader.py`) — both raise `NotImplementedError`

Not yet implemented: the scraper, the uploader, the chatbot, Docker
deployment, and the daily scheduler.

## Setup — Windows (PowerShell)

```powershell
cd D:\home-test-os
py -m venv .venv          # skip if .venv already exists
.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.sample .env
notepad .env               # fill in GEMINI_API_KEY (and GEMINI_FILE_SEARCH_STORE later)
.venv\Scripts\python.exe main.py --check-config
.venv\Scripts\python.exe main.py --check-api
```

## Setup — Linux/macOS

```bash
cd /path/to/home-test-os
python3 -m venv .venv      # skip if .venv already exists
.venv/bin/python -m pip install -r requirements.txt
cp .env.sample .env
$EDITOR .env                # fill in GEMINI_API_KEY (and GEMINI_FILE_SEARCH_STORE later)
.venv/bin/python main.py --check-config
.venv/bin/python main.py --check-api
```

## Configuration

Copy `.env.sample` to `.env` and fill in real values. `.env` is gitignored and
is never read, printed, or overwritten by any automated tooling other than
your own edits.

| Variable | Purpose |
| --- | --- |
| `GEMINI_API_KEY` | Gemini API key (fallback: `API_KEY`, for the assignment's Docker invocation) |
| `GEMINI_MODEL` | Model used for generation (default `gemini-3.8-flash`) |
| `GEMINI_FILE_SEARCH_STORE` | Name of the Gemini File Search Store; may be empty until the uploader is implemented |
| `SUPPORT_BASE_URL` | Base URL of the support site to scrape |

## CLI

```
main.py --help            # show available commands
main.py --check-config    # validate .env without calling any API
main.py --check-api       # verify Gemini auth/connectivity (lists models; no generation)
main.py                   # default: reports that the pipeline is not implemented yet
```
