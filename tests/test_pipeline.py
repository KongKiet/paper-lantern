"""Offline tests: no network, no Gemini key. Run with
    .\\.venv\\Scripts\\python.exe -m unittest discover -s tests -v
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import query  # noqa: E402
import scraper  # noqa: E402
import uploader  # noqa: E402

URL = "https://support.optisigns.com/hc/en-us/articles/360051014713-How-to-Use-YouTube-with-OptiSigns"
STORE = "fileSearchStores/teststore-abc"
DOC = f"{STORE}/documents/youtube-doc-1"

PAGE_HTML = """<html><head><title>x</title></head><body>
<header><nav><a href="/hc/en-us">Help Center</a></nav>
<form role="search" class="search"><input name="query"></form></header>
<h1 class="article-title">How to Use YouTube with OptiSigns</h1>
<div class="article-body">
  <h1>Body heading</h1>
  <p><a name="Anchor"></a></p>
  <h2>Add a video</h2>
  <ul><li>Open <strong>Apps</strong></li><li>See <a href="/hc/en-us/articles/1-Other">other</a></li></ul>
  <p><img src="/hc/article_attachments/123" alt="Apps button"></p>
  <p>Use <code>?si=</code> links.</p>
  <pre><code class="language-bash">echo hello</code></pre>
  <h3>That&#8217;s all!</h3>
  <p>OptiSigns is the leader in <a href="https://www.optisigns.com/">digital signage software</a>.</p>
</div>
<div class="article-votes">Was this article helpful? Yes No</div>
<footer>Copyright</footer>
</body></html>"""


class MarkdownConversionTests(unittest.TestCase):
    def setUp(self):
        ref = scraper.parse_article_url(URL)
        self.article = scraper.extract_from_page_html(PAGE_HTML, ref)
        self.md = scraper.render_markdown(self.article)

    def test_url_parsing(self):
        ref = scraper.parse_article_url(URL + "?foo=1#x")
        self.assertEqual((ref.article_id, ref.locale, ref.url), ("360051014713", "en-us", URL))
        self.assertEqual(scraper.output_filename(self.article), "how-to-use-youtube-with-optisigns.md")

    def test_single_h1_and_exact_provenance_line(self):
        h1s = [line for line in self.md.splitlines() if line.startswith("# ")]
        self.assertEqual(h1s, ["# How to Use YouTube with OptiSigns"])
        self.assertIn(f"\nArticle URL: {URL}\n", self.md)
        self.assertEqual(scraper.parse_markdown_metadata(self.md)["Article ID"], "360051014713")

    def test_preserves_structure(self):
        self.assertIn("## Add a video", self.md)
        self.assertIn("- Open **Apps**", self.md)
        self.assertIn("[other](/hc/en-us/articles/1-Other)", self.md)  # relative link kept
        self.assertIn("![Apps button](/hc/article_attachments/123)", self.md)
        self.assertIn("`?si=`", self.md)
        self.assertIn("```bash\necho hello\n```", self.md)

    def test_removes_page_chrome_and_promo(self):
        for junk in ("Help Center", "Was this article helpful", "Copyright", "That’s all",
                     "leader in", "query"):
            self.assertNotIn(junk, self.md)


class AnchorPreservationTests(unittest.TestCase):
    BODY = """<ul><li><a href="#AddAVideo">Add a video</a><ul><li><a href="#Shorts">Shorts</a></li></ul></li>
<li><a href="#h_faq">FAQ</a></li><li><a href="#Q1">Q1</a></li><li><a href="/hc/en-us/articles/1-Other#Setup">other</a></li></ul>
<p><a name="Unused"></a></p>
<p><a name="AddAVideo"></a></p><h2 id="h_01ABC">Add a video</h2>
<p><a name="Shorts"></a></p><h3><span style="color: #434343;">YouTube Shorts</span></h3>
<h2 id="h_faq">FAQ</h2>
<h4 id="h_x"><a name="Q1"></a></h4><h4>Why?</h4>
<pre><code class="language-python">path = "C:\\\\temp\\\\*.md"  # a_b *c* [x](#AddAVideo)
print('&lt;a name="x"&gt;&lt;/a&gt;')</code></pre>
<p>Use <code>?si=</code> and <code>a\\_b</code>.</p>"""

    def setUp(self):
        self.md = scraper.body_to_markdown(self.BODY)

    def test_referenced_anchors_precede_their_headings(self):
        self.assertIn('<a name="AddAVideo"></a>\n\n## Add a video', self.md)
        self.assertIn('<a name="Shorts"></a>\n\n### YouTube Shorts', self.md)
        self.assertIn('<a name="h_faq"></a>\n\n## FAQ', self.md)
        self.assertIn('<a name="Q1"></a>\n\n#### Why?', self.md)  # empty wrapping heading dropped
        self.assertNotRegex(self.md, r"(?m)^#+\s*$")
        self.assertNotIn("Unused", self.md)  # unreferenced empty anchors are still dropped
        self.assertNotIn("zzplanchor", self.md)

    def test_fragment_and_relative_hrefs_unchanged(self):
        self.assertIn("- [Add a video](#AddAVideo)\n  - [Shorts](#Shorts)", self.md)
        self.assertIn("[FAQ](#h_faq)", self.md)
        self.assertIn("[other](/hc/en-us/articles/1-Other#Setup)", self.md)

    def test_code_content_unchanged(self):
        self.assertIn('```python\npath = "C:\\\\temp\\\\*.md"  # a_b *c* [x](#AddAVideo)\n'
                      "print('<a name=\"x\"></a>')\n```", self.md)
        self.assertIn("`?si=`", self.md)
        self.assertIn("`a\\_b`", self.md)


class EscapingTests(unittest.TestCase):
    """Underscores: escaped in prose (valid Markdown), never in URLs or code."""

    BODY = """<ol><li>Replace the URL, as shown below.<br><br>&lt;iframe src="https://<span><strong>Your-Public-URL</strong></span>&amp;amp;action=embedview" frameborder="0"&gt;An embedded &lt;a target="_blank" href="https://office.com"&gt;Office&lt;/a&gt; file.&lt;/iframe&gt;<br>&nbsp;</li>
<li>Log in.</li></ol>
<p>Type &lt;br&gt; to break a line, see <a href="https://x.test/a_b?access_token=T_1&amp;x=1" target="_blank">the_docs</a>.</p>
<p>Fails with <code>redirect_uri_mismatch</code> or <code>C:\\new_dir\\</code>.</p>
<p>Plain refresh_token text.</p>
<iframe src="https://www.youtube.com/embed/abc"></iframe>"""

    def setUp(self):
        self.md = scraper.body_to_markdown(self.BODY)

    def test_literal_markup_example_becomes_fenced_html(self):
        self.assertIn(
            '1. Replace the URL, as shown below.\n\n   ```html\n'
            '   <iframe src="https://Your-Public-URL&amp;action=embedview" frameborder="0">An embedded '
            '<a target="_blank" href="https://office.com">Office</a> file.</iframe>\n   ```\n2. Log in.',
            self.md)
        self.assertNotIn("\\_blank", self.md)
        self.assertNotIn("youtube.com/embed", self.md)  # a real iframe is still dropped, not turned into code

    def test_inline_mentions_and_link_destinations_untouched(self):
        self.assertIn("Type <br> to break a line", self.md)  # prose mentioning a tag is not a code block
        self.assertIn("[the\\_docs](https://x.test/a_b?access_token=T_1&x=1)", self.md)

    def test_inline_code_keeps_underscores_and_backslashes(self):
        self.assertIn("`redirect_uri_mismatch`", self.md)
        self.assertIn("`C:\\new_dir\\`", self.md)
        self.assertIn("Plain refresh\\_token text.", self.md)  # valid escape in ordinary text


class FakeDocuments:
    def __init__(self, states):
        self.states = states          # name -> state string
        self.deleted = []

    def get(self, *, name, config=None):
        if name not in self.states:
            raise FakeApiError(404)
        return SimpleNamespace(name=name, state=self.states[name])

    def delete(self, *, name, config=None):
        self.deleted.append(name)
        self.states.pop(name, None)


class FakeApiError(Exception):  # mimics google.genai.errors.APIError.code
    def __init__(self, code):
        super().__init__(f"HTTP {code}")
        self.code = code


class FakeStores:
    def __init__(self, docs):
        self.documents = docs
        self.uploads = []
        self.created = 0

    def get(self, *, name, config=None):
        return SimpleNamespace(name=name)

    def create(self, *, config=None):
        self.created += 1
        return SimpleNamespace(name=STORE)

    def upload_to_file_search_store(self, *, file_search_store_name, file, config=None):
        self.uploads.append(config)
        new_doc = f"{file_search_store_name}/documents/new-{len(self.uploads)}"
        self.documents.states[new_doc] = "STATE_ACTIVE"
        return SimpleNamespace(name=f"{file_search_store_name}/upload/operations/op{len(self.uploads)}",
                               done=True, error=None, response=SimpleNamespace(document_name=new_doc))


def fake_client(states):
    docs = FakeDocuments(states)
    return SimpleNamespace(file_search_stores=FakeStores(docs), operations=SimpleNamespace(get=None))


class UploadSkipTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.paths = uploader.StatePaths.under(root, root / "state")
        self.md_path = root / "data" / "articles" / "how-to-use-youtube-with-optisigns.md"
        self.md_path.parent.mkdir(parents=True)
        self.md_path.write_text(f"# T\n\nArticle URL: {URL}\n\nArticle ID: 360051014713\n\n---\n\nBody\n", encoding="utf-8")
        uploader.write_json_atomic(self.paths.store_file, {"store_name": STORE})

    def tearDown(self):
        self.tmp.cleanup()

    def _track(self, sha):
        manifest = uploader.load_manifest(self.paths)
        manifest["articles"]["360051014713"] = {
            "article_id": "360051014713", "canonical_url": URL, "store_name": STORE,
            "document_name": DOC, "content_sha256": sha, "upload_status": "active",
        }
        uploader.save_manifest(self.paths, manifest)

    def test_unchanged_active_document_is_skipped(self):
        self._track(uploader.sha256_bytes(self.md_path.read_bytes()))
        client = fake_client({DOC: "STATE_ACTIVE"})
        result = uploader.upload_one(client, self.md_path, "", self.paths, sleep=lambda s: None)
        self.assertEqual((result.status, result.uploaded, result.skipped), ("skipped", 0, 1))
        self.assertEqual(client.file_search_stores.uploads, [])
        self.assertEqual(client.file_search_stores.created, 0)

    def test_changed_content_replaces_only_tracked_document(self):
        self._track("0" * 64)
        other = f"{STORE}/documents/unrelated"
        client = fake_client({DOC: "STATE_ACTIVE", other: "STATE_ACTIVE"})
        result = uploader.upload_one(client, self.md_path, "", self.paths, sleep=lambda s: None)
        self.assertEqual((result.status, result.uploaded), ("uploaded", 1))
        self.assertEqual(client.file_search_stores.documents.deleted, [DOC])
        cfg = client.file_search_stores.uploads[0]
        self.assertEqual(cfg["mime_type"], "text/markdown")
        self.assertEqual(cfg["chunking_config"]["white_space_config"],
                         {"max_tokens_per_chunk": 500, "max_overlap_tokens": 50})
        entry = uploader.load_manifest(self.paths)["articles"]["360051014713"]
        self.assertEqual(entry["document_name"], result.document_name)
        self.assertNotIn("pending", entry)

    def test_pending_operation_is_resumed_not_reuploaded(self):
        sha = uploader.sha256_bytes(self.md_path.read_bytes())
        manifest = uploader.load_manifest(self.paths)
        op_name = f"{STORE}/upload/operations/op-pending"
        manifest["articles"]["360051014713"] = {
            "store_name": STORE, "pending": {"operation_name": op_name, "content_sha256": sha}}
        uploader.save_manifest(self.paths, manifest)
        resumed_doc = f"{STORE}/documents/resumed"
        client = fake_client({resumed_doc: "STATE_ACTIVE"})
        polled = []
        client.operations.get = lambda op: polled.append(op.name) or SimpleNamespace(
            name=op.name, done=True, error=None, response=SimpleNamespace(document_name=resumed_doc))
        result = uploader.upload_one(client, self.md_path, "", self.paths, sleep=lambda s: None)
        self.assertEqual(polled, [op_name])
        self.assertEqual(client.file_search_stores.uploads, [])
        self.assertEqual(result.document_name, resumed_doc)
        entry = uploader.load_manifest(self.paths)["articles"]["360051014713"]
        self.assertEqual((entry["upload_status"], entry["content_sha256"]), ("active", sha))

    def test_store_conflict_is_reported(self):
        with self.assertRaises(uploader.StoreConflictError):
            uploader.resolve_store_name("fileSearchStores/other", self.paths)


class CitationVerificationTests(unittest.TestCase):
    manifest = {"articles": {"360051014713": {
        "canonical_url": URL, "document_name": DOC, "display_name": "how-to-use-youtube-with-optisigns.md",
        "upload_status": "active"}}}

    def _interaction(self, text, annotations=None):
        block = SimpleNamespace(type="text", text=text, annotations=annotations)
        return SimpleNamespace(id="i1", status="completed", output_text=text,
                               steps=[SimpleNamespace(type="model_output", content=[block])])

    def test_url_in_answer_without_citation_metadata_fails(self):
        answer, anns = query.extract_answer(self._interaction(f"Paste the link.\nArticle URL: {URL}"))
        self.assertIn(URL, answer)
        v = query.verify_citations(anns, self.manifest)
        self.assertFalse(v.passed)
        self.assertEqual(v.verified_urls, [])
        self.assertIn("no file_citation", v.failure_reason())
        self.assertIn("(none", query.format_sources(v.verified_urls))

    def test_file_citation_maps_to_canonical_url(self):
        anns_in = [{"type": "file_citation", "document_uri": DOC, "start_index": 0, "end_index": 5},
                   {"type": "file_citation", "file_name": "how-to-use-youtube-with-optisigns.md"}]
        _, anns = query.extract_answer(self._interaction("Paste the link.", anns_in))
        v = query.verify_citations(anns, self.manifest)
        self.assertTrue(v.passed)
        self.assertEqual(v.verified_urls, [URL])  # deduplicated
        self.assertEqual(query.format_sources(v.verified_urls), f"Verified sources:\nArticle URL: {URL}")

    def test_unmappable_citation_fails(self):
        anns = [{"type": "file_citation", "document_uri": DOC},
                {"type": "file_citation", "document_uri": f"{STORE}/documents/unknown"}]
        v = query.verify_citations(anns, self.manifest)
        self.assertEqual(v.verified_urls, [URL])
        self.assertFalse(v.passed)

    def test_non_file_citations_are_ignored(self):
        v = query.verify_citations([{"type": "url_citation", "url": URL}], self.manifest)
        self.assertFalse(v.passed)


if __name__ == "__main__":
    unittest.main()
