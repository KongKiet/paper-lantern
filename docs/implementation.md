# Implementation details

Reference for everything the [README](../README.md) only summarizes. Hosted
GitHub Actions setup is in [hosted-sync.md](hosted-sync.md).

## Configuration

`--check-config` validates settings without any API call. `--check-api` lists
models (`client.models.list()`) to confirm the key works; it does not generate
text, create stores, upload or scrape.

| Variable | Purpose |
| --- | --- |
| `GEMINI_API_KEY` | Gemini key (fallback `API_KEY` when unset or empty); passed explicitly to `genai.Client` |
| `GEMINI_MODEL` | Generation model for `ask` (default `gemini-3.8-flash`; see [Models](#models)) |
| `GEMINI_FILE_SEARCH_STORE` | Optional `fileSearchStores/...` name; otherwise `state/gemini-store.json` is used |
| `GEMINI_QUERY_TIMEOUT_SECONDS` | Per-attempt timeout for `ask`, in seconds (default `120`, must be > 0) |
| `SUPPORT_BASE_URL` | Help center base URL (default `https://support.optisigns.com`) |
| `SUPPORT_ARTICLE_LIMIT` | Collection size when `main.py` runs with no command (default `30`) |

### Models

The model differs by context:

| Context | Model | Source |
| --- | --- | --- |
| CLI default | `gemini-3.8-flash` | `config.py` default and `.env.sample` |
| Hosted daily sync | `gemini-3.5-flash-lite` | `GEMINI_MODEL` in `.github/workflows/daily-sync.yml` |
| Recorded CLI `ask` evidence | `gemini-3.5-flash-lite` | `Model:` line in `docs/evidence/youtube.md`, `fire-tv.md`, `out-of-scope.md` |
| AI Studio evidence | `gemini-3.8-flash` | Shown in `docs/evidence/youtube-ai-studio.png` |

`run` and `scrape` only scrape and index documents, so `GEMINI_MODEL` affects
`ask`, not ingestion. The AI Studio app in the screenshot queried the same
File Search store but is not part of this repository.

## Commands

```powershell
# Collection: discover + scrape only (no Gemini calls)
.\.venv\Scripts\python.exe main.py scrape --limit 30
# Collection: discover + scrape + delta upload, once, then exit
.\.venv\Scripts\python.exe main.py run --limit 30
# No command = run with SUPPORT_ARTICLE_LIMIT
.\.venv\Scripts\python.exe main.py
# run also accepts --timeout N: max seconds to wait for indexing per article (default 300)

# Scrape one article (no API key needed): Zendesk Help Center API, HTML page (.article-body) as fallback
.\.venv\Scripts\python.exe main.py scrape-one --article-url "https://support.optisigns.com/hc/en-us/articles/360051014713-How-to-Use-YouTube-with-OptiSigns"

# Upload one file to File Search (waits until the document is STATE_ACTIVE; --timeout default 300)
.\.venv\Scripts\python.exe main.py upload-one --file "data/articles/how-to-use-youtube-with-optisigns.md"

# Ask (Interactions API, File Search is the only tool)
.\.venv\Scripts\python.exe main.py ask --question "How do I add a YouTube video?" --require-citations --output-prefix "logs/youtube-smoke-test"

# Offline tests (stdlib unittest, fake clients, no network)
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Exit codes:

| Code | Meaning |
| --- | --- |
| `0` | OK |
| `1` | Error. For `scrape`/`run`: any failed article (including one still indexing at `--timeout`, which resumes next run) or fewer usable articles than `--limit`. For `ask`: query failed or interaction not `completed`. |
| `2` | `upload-one` only: document still indexing; rerun the same command to resume |
| `3` | `ask --require-citations` only: citation verification failed |

## Docker

Run from the repository root (`${PWD}` is the current directory):

```powershell
docker build -t paper-lantern:local .
docker run --rm paper-lantern:local --help

# One collection run (default command is `run`), reusing local state
docker run --rm --env-file .env `
  -v "${PWD}\data:/app/data" `
  -v "${PWD}\state:/app/state" `
  -v "${PWD}\logs:/app/logs" `
  paper-lantern:local

# Any CLI arguments go after the image name
docker run --rm --env-file .env -v "${PWD}\data:/app/data" `
  -v "${PWD}\state:/app/state" -v "${PWD}\logs:/app/logs" `
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

Configured in `uploader.py`: white-space chunking with
`max_tokens_per_chunk=500` and `max_overlap_tokens=50` (10%).

- **Why 500**: large enough that a typical help-article section (a heading and
  its steps) often fits in one or two chunks, so a retrieved chunk carries
  usable context; small enough that retrieval stays specific to one topic.
  Chunks are cut by token count, not by heading, so a chunk can still start or
  end mid-section, and a long section spans several chunks.
- **Why 50 overlap**: text near a boundary appears in both neighboring chunks,
  so a step split across the boundary is still retrievable with its context.
  The cost is duplication: about 10% of the text is indexed twice, and two
  overlapping chunks can both be retrieved. Larger overlap would add context
  but also more duplicate text and index size.

**Chunk counts are not available.** The File Search API does not expose how
many chunks a document (or a store) was split into, so this project reports no
chunk count and never substitutes an estimate (e.g. tokens / 500) for the
number of chunks actually embedded. What is logged instead:

- `upload-one` prints the configured chunking and `provider chunk count:
  unavailable`.
- `run` writes `indexing` in `logs/last-run.json`:
  - `chunking`: strategy and the two settings above.
  - `indexed_files_confirmed_active_this_run`: selected articles whose
    document was confirmed `STATE_ACTIVE` this run via
    `file_search_stores.documents.get` (documents, not chunks).
  - `tracked_active_documents_in_manifest`: all documents the manifest tracks
    as active in this store (can exceed the run's selection, e.g. 31 vs 30).
  - `provider_chunk_count: null` and `provider_chunk_count_reason`, which
    states that the API does not expose the count.

**Known gap:** the requirement to log the total number of chunks actually
embedded is not fully met. The logs prove which files are active and which
chunking settings were requested, but not the server-side chunk total.
`logs/last-run.json` files and artifacts recorded before
`provider_chunk_count_reason` was added contain `provider_chunk_count: null`
without that field.

The `file_citation` annotations returned by `ask` are the chunks that supported
one answer. Their number (e.g. 8 in `docs/evidence/youtube.md`) is not the
number of chunks indexed for the document.

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
| `data/articles/*.md` | Scraped Markdown: H1 title, `Article URL:`, `Article ID:`, `Locale:`, `Updated at:` header, then the body |
| `state/` | Store identity, ingestion manifest, article filenames |
| `logs/pipeline.log` | Run log (no secrets) |
| `logs/last-run.json` | Latest `run` summary: timestamps, status, scope, counts, per-article results, indexing |
| `logs/last-successful-run.json` | Latest **successful** `run` (a failed run never overwrites it) |
| `logs/last-scrape.json` | Latest `scrape` summary |
| `<output-prefix>.json` / `.md` | Answer, raw citation annotations, verified sources |

`.env`, `.venv/`, `data/articles/`, `state/` and `logs/` contents are gitignored.

## Validation evidence

Recorded results from completed runs, stored in `docs/evidence/`. The GitHub
screenshots show commit `0afce58` on `main`.

| Evidence | What it shows |
| --- | --- |
| [youtube-ai-studio.png](evidence/youtube-ai-studio.png) | AI Studio app, `gemini-3.8-flash`, store `fileSearchStores/paperlanternoptisigns-sqsdd5vpeno6`: answer to "How do I add a YouTube video?" with the YouTube article as cited URL |
| [youtube.md](evidence/youtube.md), [fire-tv.md](evidence/fire-tv.md), [out-of-scope.md](evidence/out-of-scope.md) | CLI `ask` outputs (`gemini-3.5-flash-lite`, same store). YouTube: 8 `file_citation` annotations, all mapped, verification passed. Fire TV: 5, all mapped, passed. Out-of-scope question: refused, 0 citations. JSON versions and CLI screenshots are alongside. |
| [docker-run.png](evidence/docker-run.png) | `run` summary: status `success`, selected 30, added 0, updated 0, skipped 30, failed 0, 30 confirmed active, exit code `0` |
| [github-manual-run.png](evidence/github-manual-run.png) | Daily sync via `workflow_dispatch` (2026-10-07): restore success, `run --limit 30` exit 0, state pushed; added 0, updated 0, skipped 30, failed 0 |
| [github-scheduled-run.png](evidence/github-scheduled-run.png) | Daily sync via `schedule` (pipeline 2026-10-08 07:30 UTC): restore success, exit 0, state pushed; added 1, updated 0, skipped 29, failed 0 |
| [run-links.txt](evidence/run-links.txt) | Links to both GitHub Actions runs (#2 manual, #3 scheduled) |
| [github-manual-artifact.zip](evidence/github-manual-artifact.zip), [github-scheduled-artifact.zip](evidence/github-scheduled-artifact.zip) | Downloaded log artifacts: `pipeline.log`, `last-run.json`, `last-successful-run.json` |
| [offline-tests.txt](evidence/offline-tests.txt) | Offline test run: `Ran 55 tests ... OK` (UTF-16 encoded) |

In the scheduled run, `added 1` is article `33940834613139`, recorded as
`delta: new` in that run's `last-run.json` (scheduled artifact); the other 29
were skipped without upload, and the manifest then tracked 31 active
documents.
