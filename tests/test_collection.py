"""Offline tests for collection discovery, selection and delta upload.

A scripted fake HTTP session stands in for the Zendesk list endpoint and a
fake Gemini client for File Search; nothing leaves the process.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import time
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config  # noqa: E402
import pipeline  # noqa: E402
import scraper  # noqa: E402
import uploader  # noqa: E402

BASE = "https://support.optisigns.com"
LIST_URL = scraper.list_articles_url(BASE, "en-us")
YT = "360051014713"
STORE = "fileSearchStores/teststore-abc"


def item(article_id, slug=None, *, body="<p>Body text.</p>", draft=False, locale="en-us",
         updated="2026-10-01T00:00:00Z", title=None):
    slug = slug or f"Article-{article_id}"
    return {"id": int(article_id), "title": title or slug.replace("-", " "), "body": body, "draft": draft,
            "locale": locale, "updated_at": updated, "html_url": f"{BASE}/hc/en-us/articles/{article_id}-{slug}"}


class FakeResponse:
    def __init__(self, status, payload=None, text=""):
        self.status_code, self._payload, self.text, self.encoding = status, payload, text, "utf-8"

    def json(self):
        if self._payload is None:
            raise ValueError("not json")
        return self._payload


class FakeSession:
    """Cursor-paginated list endpoint; pages are lists of items."""

    def __init__(self, pages, html_pages=None):
        self.pages, self.html_pages, self.calls = pages, html_pages or {}, []

    def get(self, url, params=None, timeout=None, headers=None):
        self.calls.append((url, params))
        assert timeout is not None, "every request must be bounded"
        if url == LIST_URL or url.startswith(f"{LIST_URL}?") or "page%5Bafter%5D" in url:
            index = 0 if params else int(url.rsplit("=", 1)[1])
            more = index + 1 < len(self.pages)
            nxt = f"{BASE}/api/v2/help_center/en-us/articles?page%5Bafter%5D={index + 1}" if more else None
            return FakeResponse(200, {"articles": self.pages[index], "meta": {"has_more": more},
                                      "links": {"next": nxt}})
        if url in self.html_pages:
            return FakeResponse(200, text=self.html_pages[url])
        return FakeResponse(404, text="")


class FakeDocs:
    def __init__(self):
        self.states, self.deleted = {}, []

    def get(self, *, name, config=None):
        if name not in self.states:
            raise _NotFound()
        return SimpleNamespace(name=name, state=self.states[name])

    def delete(self, *, name, config=None):
        self.deleted.append(name)
        self.states.pop(name, None)


class _NotFound(Exception):
    code = 404


class FakeStores:
    def __init__(self, fail_names=()):
        self.documents, self.uploads, self.fail_names, self.created = FakeDocs(), [], set(fail_names), 0

    def get(self, *, name, config=None):
        return SimpleNamespace(name=name)

    def create(self, *, config=None):
        self.created += 1
        return SimpleNamespace(name=STORE)

    def upload_to_file_search_store(self, *, file_search_store_name, file, config=None):
        if config["display_name"] in self.fail_names:
            raise RuntimeError("HTTP 500 upload rejected")
        self.uploads.append(config["display_name"])
        doc = f"{file_search_store_name}/documents/d{len(self.uploads)}"
        self.documents.states[doc] = "STATE_ACTIVE"
        return SimpleNamespace(name=f"{file_search_store_name}/upload/operations/op{len(self.uploads)}",
                               done=True, error=None, response=SimpleNamespace(document_name=doc))


def fake_client(fail_names=()):
    return SimpleNamespace(file_search_stores=FakeStores(fail_names), operations=SimpleNamespace(get=None))


class Workspace(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.paths = uploader.StatePaths.under(root, root / "state")
        self.articles = root / "data" / "articles"
        self.logs = root / "logs"
        uploader.write_json_atomic(self.paths.store_file, {"store_name": STORE})

    def tearDown(self):
        self.tmp.cleanup()

    def collect(self, session, limit):
        return pipeline.collect_articles(session, BASE, limit, self.articles, self.paths, progress=lambda s: None)

    def run_pipeline(self, session, client, limit):
        col = self.collect(session, limit)
        store = pipeline.upload_collection(client, col, "", self.paths, 60, lambda e: type(e).__name__,
                                           progress=lambda s: None, sleep=lambda s: None)
        summary = pipeline.summarize(col, command="run", base_url=BASE, started_at="t0",
                                     started_monotonic=time.monotonic(), uploaded=True, store_name=store,
                                     paths=self.paths)
        pipeline.write_summary(summary, self.logs, last_name="last-run.json", success_name="last-successful-run.json")
        return summary


class DiscoveryTests(Workspace):
    def test_follows_pagination_and_deduplicates_ids(self):
        session = FakeSession([[item("1"), item("2")], [item("2"), item("3")], [item("1"), item("4")]])
        stats = {}
        ids = [str(i["id"]) for i in scraper.iter_listed_articles(session, BASE, "en-us", stats=stats)]
        self.assertEqual(ids, ["1", "2", "3", "4"])
        self.assertEqual((stats["list_pages_fetched"], stats["duplicate_ids_ignored"]), (3, 2))
        self.assertEqual(session.calls[0][1], {"sort_by": "updated_at", "sort_order": "desc", "page[size]": 100})

    def test_offsite_pagination_link_is_not_followed(self):
        session = mock.Mock()
        session.get.return_value = FakeResponse(200, {"articles": [item("1")], "meta": {"has_more": True},
                                                      "links": {"next": "https://evil.example/next"}})
        with self.assertRaises(scraper.ScrapeError):
            list(scraper.iter_listed_articles(session, BASE, "en-us"))
        self.assertEqual(session.get.call_count, 1)

    def test_youtube_included_within_limit_even_on_later_page(self):
        session = FakeSession([[item("1"), item("2"), item("3")], [item("4"), item(YT, "How-to-Use-YouTube")]])
        col = self.collect(session, limit=3)
        self.assertEqual([o.article_id for o in col.outcomes], ["1", "2", YT])
        self.assertEqual(len(col.scraped), 3)
        md = (self.paths.project_root / col.outcomes[2].markdown_path).read_text(encoding="utf-8")
        self.assertIn(f"\nArticle URL: {BASE}/hc/en-us/articles/{YT}-How-to-Use-YouTube\n", md)

    def test_unsuitable_entries_are_skipped_and_discovery_continues(self):
        session = FakeSession([[item(YT, "YouTube"), item("10", draft=True), item("11", body="  "),
                                item("12", locale="fr"), item("13", body="<p>&nbsp;</p>")],
                               [item("14"), item("15")]])
        col = self.collect(session, limit=3)
        self.assertEqual([o.article_id for o in col.outcomes], [YT, "14", "15"])
        self.assertEqual({r["article_id"] for r in col.rejected}, {"10", "11", "12", "13"})
        self.assertTrue(all(o.scrape_status == "scraped" for o in col.outcomes))

    def test_insufficient_articles_is_a_failure(self):
        col = self.collect(FakeSession([[item(YT, "YouTube"), item("2")]]), limit=5)
        summary = pipeline.summarize(col, command="scrape", base_url=BASE, started_at="t0",
                                     started_monotonic=time.monotonic(), uploaded=False)
        self.assertEqual((summary["status"], summary["counts"]["scraped"]), ("failed", 2))
        self.assertIn("insufficient_articles", summary)

    def test_filenames_are_stable_safe_and_collision_free(self):
        manifest = uploader.load_manifest(self.paths)
        manifest["articles"][YT] = {"markdown_path": "data/articles/how-to-use-youtube-with-optisigns.md"}
        uploader.save_manifest(self.paths, manifest)
        session = FakeSession([[item(YT, "Renamed-Slug"), item("20", "Same-Title"), item("21", "Same-Title"),
                                item("22", "CON")]])
        col = self.collect(session, limit=4)
        names = [Path(o.markdown_path).name for o in col.outcomes]
        self.assertEqual(names, ["how-to-use-youtube-with-optisigns.md", "same-title.md",
                                 "same-title-21.md", "con-22.md"])
        # The same assignment is reused on the next run.
        col2 = self.collect(FakeSession([[item("21", "Same-Title"), item("20", "Same-Title"),
                                          item(YT, "Renamed-Slug"), item("22", "CON")]]), limit=4)
        self.assertEqual(sorted(Path(o.markdown_path).name for o in col2.outcomes), sorted(names))

    def test_scrape_only_does_not_mark_articles_uploaded(self):
        self.collect(FakeSession([[item(YT, "YouTube"), item("2")]]), limit=2)
        self.assertEqual(uploader.load_manifest(self.paths)["articles"], {})

    def test_article_limit_config(self):
        self.assertEqual(config.parse_article_limit(None), 30)
        self.assertEqual(config.parse_article_limit(" 45 "), 45)
        for bad in ("0", "-1", "3.5", "x"):
            with self.assertRaises(config.ConfigError):
                config.parse_article_limit(bad)
        with mock.patch.dict(os.environ, {"SUPPORT_ARTICLE_LIMIT": "12"}), mock.patch.object(config, "load_dotenv"):
            self.assertEqual(config.load_config(require_api_key=False).support_article_limit, 12)


class DeltaUploadTests(Workspace):
    def pages(self, body2="<p>Body text.</p>"):
        return [[item(YT, "YouTube"), item("2", body=body2), item("3")]]

    def test_classification_added_updated_skipped(self):
        client = fake_client()
        first = self.run_pipeline(FakeSession(self.pages()), client, limit=3)
        self.assertEqual(first["status"], "success")
        self.assertEqual({k: first["counts"][k] for k in ("added", "updated", "skipped", "failed")},
                         {"added": 3, "updated": 0, "skipped": 0, "failed": 0})

        manifest = uploader.load_manifest(self.paths)
        old_doc = manifest["articles"]["2"]["document_name"]
        second = self.run_pipeline(FakeSession(self.pages(body2="<p>Changed body.</p>")), client, limit=3)
        c = second["counts"]
        self.assertEqual((c["added"], c["updated"], c["skipped"], c["failed"]), (0, 1, 2, 0))
        self.assertEqual(c["selected_documents_confirmed_active"], 3)
        self.assertEqual(client.file_search_stores.documents.deleted, [old_doc])  # only the replaced one
        self.assertIsNone(second["indexing"]["provider_chunk_count"])
        self.assertIn("does not expose", second["indexing"]["provider_chunk_count_reason"])

    def test_unchanged_rerun_uploads_nothing_and_keeps_files(self):
        client = fake_client()
        self.run_pipeline(FakeSession(self.pages()), client, limit=3)
        mtimes = {p.name: p.stat().st_mtime_ns for p in self.articles.glob("*.md")}
        uploads_before = list(client.file_search_stores.uploads)
        summary = self.run_pipeline(FakeSession(self.pages()), client, limit=3)
        self.assertEqual(summary["counts"]["skipped"], 3)
        self.assertEqual(client.file_search_stores.uploads, uploads_before)
        self.assertEqual({p.name: p.stat().st_mtime_ns for p in self.articles.glob("*.md")}, mtimes)
        self.assertEqual(client.file_search_stores.created, 0)

    def test_partial_failure_is_reported_and_recovered_next_run(self):
        good = self.run_pipeline(FakeSession(self.pages()), fake_client(), limit=3)
        self.assertEqual(good["status"], "success")
        success_before = (self.logs / "last-successful-run.json").read_text(encoding="utf-8")

        # Article 3 is new in a later run and its upload fails.
        pages = [[item(YT, "YouTube"), item("2"), item("4")]]
        failing = fake_client(fail_names={"article-4.md"})
        failing.file_search_stores.documents.states = {
            e["document_name"]: "STATE_ACTIVE" for e in uploader.load_manifest(self.paths)["articles"].values()}
        bad = self.run_pipeline(FakeSession(pages), failing, limit=3)
        self.assertEqual(bad["status"], "failed")
        self.assertEqual((bad["counts"]["skipped"], bad["counts"]["failed"]), (2, 1))
        self.assertEqual(bad["counts"]["selected_documents_confirmed_active"], 2)
        failed = next(a for a in bad["articles"] if a["article_id"] == "4")
        self.assertEqual((failed["upload"], failed["error"]), ("failed", "RuntimeError"))
        self.assertEqual(json.loads((self.logs / "last-run.json").read_text(encoding="utf-8"))["status"], "failed")
        self.assertEqual((self.logs / "last-successful-run.json").read_text(encoding="utf-8"), success_before)
        self.assertNotEqual(uploader.load_manifest(self.paths)["articles"].get("4", {}).get("upload_status"), "active")

        failing.file_search_stores.fail_names.clear()
        retry = self.run_pipeline(FakeSession(pages), failing, limit=3)
        self.assertEqual(retry["status"], "success")
        self.assertEqual((retry["counts"]["added"], retry["counts"]["skipped"]), (1, 2))

    def test_failed_required_article_fails_run(self):
        pages = [[item(YT, "YouTube", body=""), item("2"), item("3")]]
        summary = self.run_pipeline(FakeSession(pages), fake_client(), limit=3)
        self.assertEqual(summary["status"], "failed")
        yt = next(a for a in summary["articles"] if a["article_id"] == YT)
        self.assertEqual((yt["scrape_status"], yt["upload"]), ("failed", None))
        self.assertEqual(summary["counts"]["failed"], 1)
        self.assertEqual(summary["counts"]["selected"], 3)


if __name__ == "__main__":
    unittest.main()
