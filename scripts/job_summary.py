"""Render a GitHub Actions job summary (Markdown on stdout) for the daily sync.

Inputs come from environment variables so workflow expressions never reach a shell:
  JOB_STARTED_AT    UTC ISO timestamp taken at job start; older run summaries are ignored
  RESTORE_OUTCOME   outcome of the restore step
  PIPELINE_EXIT     exit code of `main.py run` (empty if it did not run)
  SAVE_OUTCOME      outcome of the save step;  SAVE_RESULT: pushed | unchanged | failed
  ARTIFACT_URL      link to the uploaded log artifact;  RUN_URL: link to this run
Stdlib only.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

EXIT_MEANINGS = {"0": "success", "1": "error", "2": "upload still indexing", "124": "timed out"}
COUNT_KEYS = ("selected", "scraped", "added", "updated", "skipped", "failed", "selected_documents_confirmed_active")


def load_fresh_run(path: Path, started_at: str) -> dict | None:
    """Return the run summary only if it was written by this job (ISO UTC strings compare in order)."""
    try:
        run = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    if not isinstance(run, dict) or (started_at and str(run.get("started_at", "")) < started_at):
        return None
    return run


def render(env: dict, run: dict | None) -> str:
    exit_code = env.get("PIPELINE_EXIT", "")
    pipeline = f"exit {exit_code} ({EXIT_MEANINGS.get(exit_code, 'failure')})" if exit_code else "did not run"
    save_outcome = env.get("SAVE_OUTCOME") or "skipped"
    save = save_outcome if save_outcome != "success" else env.get("SAVE_RESULT") or "success"
    lines = [
        "## Daily sync",
        "",
        "| Step | Result |",
        "| --- | --- |",
        f"| Restore state | {env.get('RESTORE_OUTCOME') or 'skipped'} |",
        f"| Pipeline (`run --limit 30`) | {pipeline} |",
        f"| Persist state | {save} |",
        "",
    ]
    if save_outcome == "failure":
        lines += ["> **State was not persisted.** The next run starts from the previous state commit. "
                  "See the *Persist state* step log.", ""]
    if run:
        counts = run.get("counts") or {}
        lines += [f"Run status: **{run.get('status', 'unknown')}**, "
                  f"{run.get('started_at', '?')} to {run.get('finished_at', '?')}", "",
                  "| " + " | ".join(COUNT_KEYS) + " |",
                  "|" + " --- |" * len(COUNT_KEYS),
                  "| " + " | ".join(str(counts.get(k, "")) for k in COUNT_KEYS) + " |", ""]
        failed = [a for a in run.get("articles") or [] if a.get("error") or a.get("upload") == "failed"]
        if failed:
            lines += ["Failed articles:", ""]
            lines += [f"- `{a.get('article_id')}` {a.get('title', '')}: {str(a.get('error') or '')[:200]}"
                      for a in failed[:30]]
            lines.append("")
        if run.get("discovery_error"):
            lines += [f"Discovery error: {str(run['discovery_error'])[:300]}", ""]
    else:
        lines += ["No run summary was written by this job (`logs/last-run.json` missing or stale).", ""]
    links = []
    if env.get("ARTIFACT_URL"):
        links.append(f"[Diagnostic logs artifact]({env['ARTIFACT_URL']})")
    if env.get("RUN_URL"):
        links.append(f"[Run page]({env['RUN_URL']})")
    if links:
        lines.append(" - ".join(links))
    return "\n".join(lines) + "\n"


def main() -> int:
    env = dict(os.environ)
    run = load_fresh_run(Path(env.get("LAST_RUN_PATH", "logs/last-run.json")), env.get("JOB_STARTED_AT", ""))
    sys.stdout.write(render(env, run))
    return 0


if __name__ == "__main__":
    sys.exit(main())
