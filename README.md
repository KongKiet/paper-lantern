# paper-lantern

Scrapes public support articles from `support.optisigns.com`, converts them to
clean Markdown, uploads them to a Gemini File Search store, and answers
questions with verified citations.

**Current milestone: a 30-article collection** with a one-shot
scrape-and-upload pipeline and delta detection, runnable locally, in Docker,
or daily on GitHub Actions.

## Setup (Windows PowerShell)

```powershell
py -m venv .venv                       # skip if .venv exists
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.sample .env; notepad .env   # set GEMINI_API_KEY
.\.venv\Scripts\python.exe main.py --check-config
.\.venv\Scripts\python.exe main.py --check-api
```

| Variable | Purpose |
| --- | --- |
| `GEMINI_API_KEY` | Gemini key (fallback `API_KEY`); passed explicitly to `genai.Client` |
| `GEMINI_MODEL` | Generation model (default `gemini-3.8-flash`) |
| `GEMINI_FILE_SEARCH_STORE` | Optional `fileSearchStores/...` name; otherwise `state/gemini-store.json` is used |
| `GEMINI_QUERY_TIMEOUT_SECONDS` | Per-attempt timeout for `ask`, in seconds (default `120`, must be > 0) |
| `SUPPORT_ARTICLE_LIMIT` | Collection size when `main.py` runs with no command (default `30`) |

## Commands

```powershell
# Collection: discover + scrape only (no Gemini calls)
.\.venv\Scripts\python.exe main.py scrape --limit 30
# Collection: discover + scrape + delta upload, once, then exit (no command = run with SUPPORT_ARTICLE_LIMIT)
.\.venv\Scripts\python.exe main.py run --limit 30
.\.venv\Scripts\python.exe main.py

# 1. Scrape one article (no API key needed): Zendesk Help Center API, HTML page (.article-body) as fallback
.\.venv\Scripts\python.exe main.py scrape-one --article-url "https://support.optisigns.com/hc/en-us/articles/360051014713-How-to-Use-YouTube-with-OptiSigns"

# 2. Upload to File Search (waits until the document is STATE_ACTIVE)
.\.venv\Scripts\python.exe main.py upload-one --file "data/articles/how-to-use-youtube-with-optisigns.md"

# 3. Ask (Interactions API, File Search is the only tool)
.\.venv\Scripts\python.exe main.py ask --question "How do I add a YouTube video?" --require-citations --output-prefix "logs/youtube-smoke-test"

# Offline tests
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## Docker (Windows PowerShell)

```powershell
docker build -t paper-lantern:local .
docker run --rm paper-lantern:local --help

# One collection run (default command is `run`), reusing local state
docker run --rm --env-file .env `
  -v D:\home-test-os\data:/app/data `
  -v D:\home-test-os\state:/app/state `
  -v D:\home-test-os\logs:/app/logs `
  paper-lantern:local

# Any CLI arguments go after the image name
docker run --rm --env-file .env -v D:\home-test-os\data:/app/data `
  -v D:\home-test-os\state:/app/state -v D:\home-test-os\logs:/app/logs `
  paper-lantern:local run --limit 30
```

- **Image**: `python:3.14-slim`, `ENTRYPOINT ["python", "main.py"]`, `CMD ["run"]`.
  `.env`, `.venv/`, `.git/`, caches and `data/`, `state/`, `logs/` are excluded
  by `.dockerignore`, so no key, manifest or store identity is baked in.
- **API key**: `GEMINI_API_KEY` wins; `API_KEY` is used when it is unset or
  empty, e.g. `docker run --rm -e API_KEY=<key> ... paper-lantern:local`.
- **Persistence**: the three bind mounts keep Markdown, `state/gemini-store.json`,
  `state/ingestion-manifest.json` and logs between runs. Manifest paths are
  relative POSIX (`data/articles/<name>.md`), so a container reuses the store
  and manifest created on Windows and skips unchanged articles. Without the
  mounts, every run starts with empty state and creates a new store.
- **`--env-file` syntax**: Docker reads each line literally as `KEY=value`.
  Don't put quotes around values, use `${VAR}` interpolation, or add inline
  comments. Docker would pass them through as part of the value.
  `.env.sample` follows this format.

## Hosted daily sync (GitHub Actions)

`.github/workflows/daily-sync.yml` runs `paper-lantern:local run --limit 30`
daily at 01:17 UTC (08:17 Vietnam time) and on manual dispatch. It uses the
`API_KEY` repository secret and `GEMINI_MODEL=gemini-3.5-flash-lite`. State
(store, manifest, articles, run summaries) persists on the `pipeline-state`
branch through `scripts/state_sync.py`. Only an explicit file allowlist is
committed there, never with force. Logs are uploaded as an artifact on every
run. Setup, seeding and verification are in
[docs/hosted-sync.md](docs/hosted-sync.md).

Exit codes: `0` ok, `1` error (for `scrape`/`run`: any failed article or fewer
usable articles than `--limit`), `2` upload still indexing (rerun to resume),
`3` `--require-citations` verification failed.

## Collection scope (`scrape` / `run`)

`--limit N` selects **this run's collection**: the first N usable, published
en-us articles from `/api/v2/help_center/en-us/articles.json`, sorted
`updated_at desc`. Pagination follows `meta.has_more` / `links.next` (cursor,
100 per page), and duplicate IDs are ignored. The YouTube article
(`360051014713`) is always included **within** N. Drafts, other locales and
empty bodies are skipped; an empty API body falls back to the HTML page.
Discovery continues until N articles are usable. A limited run does **not**
synchronize the whole help center, and documents of unselected articles are
never deleted.

Per article, `run` saves the Markdown and then uploads it sequentially through
`upload-one`'s logic. Each article gets exactly one result:

- **added**: new
- **updated**: changed content replaced, or a missing/failed document repaired
- **skipped**: same SHA-256 and the tracked document is confirmed active
- **failed**: kept retryable for the next run

Files are only rewritten when their content changes, and the hash covers only
the article content and its `updated_at`, never a fetch time.

## State reuse

- **Store**: `GEMINI_FILE_SEARCH_STORE` if set, else `state/gemini-store.json`.
  If neither exists, one store is created and saved immediately. If both are
  set and differ, the command stops and reports the conflict.
- **Manifest** `state/ingestion-manifest.json`: article ID, canonical URL,
  Markdown path, SHA-256, store, document name, upload status. No secrets.
- **Filenames** `state/article-files.json`: article ID → filename (scrape output
  only, never upload status). Names are Windows-safe slugs, existing names are
  reused, and a slug collision gets `-<article_id>`.
- **Reruns**: same SHA-256 + document confirmed `STATE_ACTIVE` → skipped. A
  recorded pending operation is resumed, not re-uploaded. Changed content is
  uploaded first; only after the new document is active is the article's
  previously tracked document deleted. Other documents are never touched.

## Chunking

White-space chunking, `max_tokens_per_chunk=500`, `max_overlap_tokens=50`.
A 500-token chunk holds one help-article section (heading + its steps) so a
retrieved chunk is self-contained; 10% overlap keeps sentences that straddle a
boundary retrievable without much duplication. The API does not report a
per-document chunk count, so the CLI prints it as "unavailable" and
`provider_chunk_count` is `null` in run summaries. The summary reports the
configured chunking and the number of indexed files confirmed active instead.

## Citations

Sources are taken **only** from `file_citation` annotations Gemini returns,
mapped to canonical URLs via the manifest (custom metadata `article_id`,
document name, or an unambiguous file name). A URL that merely appears in the
answer text is never counted. At most 3 `Article URL:` lines are printed.

## Query timeouts and retries

`ask` makes at most **2 network attempts**. It retries once, after about 2-3 s
(with jitter), only on timeouts, connection errors and HTTP 408/429/5xx such as
`503 high demand`. Auth, permission and invalid-request errors (400/401/403/404)
fail immediately. The SDK's own Interactions retries are turned off on the query
client so the two policies never stack. Each attempt logs the SDK version,
model, timeout, attempt number, elapsed time and error type (never the message).
If every attempt fails, the exit code is `1` and no answer file is written. A
retried success still has to pass citation verification.

## Outputs

| Path | Content |
| --- | --- |
| `data/articles/*.md` | Scraped Markdown (H1, `Article URL:` line, updated-at, body) |
| `state/` | Store identity and ingestion manifest |
| `logs/pipeline.log` | Run log (no secrets) |
| `logs/last-run.json` | Latest `run` summary: timestamps, status, scope, counts, per-article results |
| `logs/last-successful-run.json` | Latest **successful** `run` (a failed run never overwrites it) |
| `logs/last-scrape.json` | Latest `scrape` summary |
| `<output-prefix>.json` / `.md` | Answer, raw citation annotations, verified sources |

`.env`, `.venv/`, `data/articles/`, `state/` and `logs/` contents are gitignored.
