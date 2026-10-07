# Hosted daily sync (GitHub Actions)

`.github/workflows/daily-sync.yml` runs `paper-lantern:local run --limit 30` in
Docker every day at **01:17 UTC (08:17 Vietnam time)** and on manual dispatch.
It never runs on push or pull request.

## How a run works

1. **Restore**: fetch the `pipeline-state` branch and restore its files with
   `scripts/state_sync.py restore`. If the branch is missing, or the store,
   manifest or any Markdown file the manifest references is missing or
   invalid, the job fails here, **before Gemini is called**. Nothing runs on
   empty state.
2. **Run**: build the Dockerfile and run the pipeline with `API_KEY` from the
   repository secret and `GEMINI_MODEL=gemini-3.5-flash-lite`. Timeout and
   retry settings keep their defaults. The store comes from
   `state/gemini-store.json`. The step has a 45-minute limit inside the job's
   60-minute limit.
3. **Persist**: this step runs even when the pipeline fails, so finished
   articles are kept. `scripts/state_sync.py save` builds a commit containing
   **only** the allowlist below and pushes it **without force** on top of the
   fetched tip. It refuses invalid or incomplete state, and refuses any file
   that contains the API key. If the push is rejected, the branch keeps its
   previous commit.
4. **Logs**: `logs/` is uploaded as artifact `pipeline-logs-<run id>-<attempt>`
   (kept 14 days), even on failure. The job summary shows each step's
   result, the counts and the artifact link.
5. **Status**: if the pipeline failed, the job fails with the pipeline's own
   exit code after state is saved. A persistence failure also fails the job
   and is flagged in the summary.

**`pipeline-state` allowlist** (nothing else is ever committed there):
`state/gemini-store.json`, `state/ingestion-manifest.json`,
`state/article-files.json`, `logs/last-run.json`,
`logs/last-successful-run.json`, `data/articles/<slug>.md`.
These contain the store name and public article text, never credentials. If
the repository is public, this branch is public too.

## One-time setup (PowerShell)

Placeholders are written as `<...>`:

| Placeholder | Where to get it |
| --- | --- |
| `<your Gemini API key>` | The key already in your local `.env`, or Google AI Studio → *Get API key*. It **must belong to the same Google Cloud project** as the store in `state/gemini-store.json`, because File Search stores are project-scoped. |
| `<run-id>` | The Actions run URL (`.../actions/runs/<run-id>`), or `gh run list --workflow daily-sync.yml` |

### 1. Publish the workflow on the default branch

Schedules and the *Run workflow* button only work for workflows on the default
branch (`main`). Commit the application, `scripts/`, `tests/`, `docs/` and
`.github/workflows/daily-sync.yml`, then push to `main`. `data/`, `state/`,
`logs/` and `.env` are gitignored and must stay out of `main`.

```powershell
cd D:\home-test-os
git status            # review: no .env, data/, state/ or logs/ files listed
git add -A
git commit -m "Add daily GitHub Actions sync"
git push origin main
```

### 2. Repository settings

On GitHub, open the repository's **Settings**:

- **Secrets and variables → Actions → New repository secret**: Name `API_KEY`,
  Secret `<your Gemini API key>`. With the GitHub CLI you can run
  `gh secret set API_KEY`, which prompts for the value without echoing it.
- **Actions → General → Actions permissions**: allow actions. If you restrict
  them, allow at least the GitHub-authored `actions/checkout` and
  `actions/upload-artifact`.
- **Actions → General → Workflow permissions**: the default (read) is fine.
  The workflow grants itself `contents: write`. No personal access token is
  needed.
- **Branches / Rules**: don't protect `pipeline-state`, or let GitHub Actions
  push to it.
- Public repositories: GitHub disables schedules after 60 days without
  repository activity. Re-enable them from the Actions tab if that happens.

### 3. Seed `pipeline-state` from local state (before the first run)

This reuses the store and the 30 indexed documents. Seed from the state of the
last successful live run, and don't run the local pipeline between seeding and
the first hosted run.

```powershell
cd D:\home-test-os
git fetch origin
git ls-remote --heads origin pipeline-state     # must print nothing
.\.venv\Scripts\python.exe scripts\state_sync.py bootstrap
git ls-tree -r --name-only pipeline-state       # review: only allowlisted paths
git push origin pipeline-state                  # plain push: fails if the branch already exists
```

`bootstrap` validates the state first: the store, a non-empty manifest, and
every Markdown file the manifest references. It creates the local branch
without switching branches or touching the working tree, and it never pushes.
To redo it before pushing, run `git branch -D pipeline-state` (local only).

After seeding, **`pipeline-state` is the source of truth**. Before running the
pipeline locally again, restore from it so the local state matches what the
hosted job will see:

```powershell
git fetch origin pipeline-state
.\.venv\Scripts\python.exe scripts\state_sync.py restore --ref FETCH_HEAD
```

### 4. Run manually twice and check for duplicates

GitHub → **Actions → Daily sync → Run workflow** (branch `main`). Wait until
it finishes, then run it again. With the GitHub CLI:
`gh workflow run daily-sync.yml --ref main`, then `gh run watch`.

Check the job summary of both runs:

- **Restore state** and **Persist state** succeed, and the pipeline exits `0`.
- `selected 30`, `failed 0`, `selected_documents_confirmed_active 30`.
- Run 1 should show `added 0`. Articles edited upstream since seeding show up
  as `updated`, which replaces their document rather than adding one.
- Run 2 must show `added 0`, `updated 0` and `skipped 30`. That confirms the
  second run reused the state the first run saved and uploaded nothing.

To check what was persisted:

```powershell
git fetch origin pipeline-state
git log --oneline -3 FETCH_HEAD
git show FETCH_HEAD:logs/last-run.json | Select-String '"(added|updated|skipped|failed)"'
```

### 5. Logs and artifacts

- **Actions → Daily sync → (run)**: the **Summary** tab has the job summary.
  The *Artifacts* section at the bottom lists `pipeline-logs-<run-id>-<attempt>`,
  which contains `pipeline.log`, `last-run.json` and `last-successful-run.json`.
- Step logs: click the `sync` job. Look at *Restore state*, *Run pipeline* and
  *Persist state*.
- With the GitHub CLI: `gh run view <run-id> --log-failed` and
  `gh run download <run-id>`.
