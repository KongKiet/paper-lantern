"""Offline tests for the query timeout and retry policy.

The real google-genai client is used with an httpx.MockTransport, so request
construction, timeout propagation, SDK retry behaviour and exception types
are those of the installed SDK; no request leaves the process.
"""

from __future__ import annotations

import json
import os
import sys
import unittest
from pathlib import Path
from unittest import mock

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config  # noqa: E402
import query  # noqa: E402

STORE = "fileSearchStores/teststore-abc"
DOC = f"{STORE}/documents/youtube-doc-1"
URL = "https://support.optisigns.com/hc/en-us/articles/360051014713-How-to-Use-YouTube-with-OptiSigns"
MANIFEST = {"articles": {"360051014713": {
    "canonical_url": URL, "document_name": DOC, "upload_status": "active"}}}


def interaction_body(annotations):
    return {"id": "i1", "status": "completed", "steps": [{"type": "model_output", "content": [
        {"type": "text", "text": f"Paste the YouTube link.\nArticle URL: {URL}", "annotations": annotations}]}]}


class Transport:
    """Scripted responses; records every network attempt and its timeout extension."""

    def __init__(self, script):
        self.script = list(script)
        self.requests: list[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        step = self.script.pop(0)
        if step == "timeout":
            raise httpx.ReadTimeout("mocked timeout", request=request)
        status, body = step
        return httpx.Response(status, json=body)


def run_ask(transport: Transport, timeout_seconds: float):
    client = query.make_query_client("offline-dummy-key", timeout_seconds,
                                     httpx_client=httpx.Client(transport=httpx.MockTransport(transport)))
    sleeps: list[float] = []
    result = query.ask_with_retry(client, model="gemini-test", question="How do I add a YouTube video?",
                                  system_instruction="sys", store_name=STORE, timeout_seconds=timeout_seconds,
                                  sleep=sleeps.append, jitter=lambda a, b: 0.25)
    return result, sleeps


class TimeoutConfigTests(unittest.TestCase):
    def test_parse_and_validate(self):
        self.assertEqual(config.parse_timeout_seconds(None), 120.0)
        self.assertEqual(config.parse_timeout_seconds(" 37.5 "), 37.5)
        for bad in ("0", "-5", "abc", "nan", "inf"):
            with self.assertRaises(config.ConfigError):
                config.parse_timeout_seconds(bad)

    def test_env_value_reaches_config(self):
        with mock.patch.dict(os.environ, {"GEMINI_QUERY_TIMEOUT_SECONDS": "45"}), \
                mock.patch.object(config, "load_dotenv"):
            self.assertEqual(config.load_config(require_api_key=False).gemini_query_timeout_seconds, 45.0)


class QueryTimeoutTests(unittest.TestCase):
    def test_configured_timeout_reaches_actual_request_in_seconds(self):
        transport = Transport([(200, interaction_body([{"type": "file_citation", "document_uri": DOC}]))])
        (_, attempts), _ = run_ask(transport, timeout_seconds=37.5)
        self.assertEqual(attempts, 1)
        # httpx timeouts are in seconds: 37.5 s, not 37500 s nor 0.0375 s.
        self.assertEqual(transport.requests[0].extensions["timeout"],
                         {"connect": 37.5, "read": 37.5, "write": 37.5, "pool": 37.5})
        sent = json.loads(transport.requests[0].content)
        self.assertEqual(sent["tools"], [{"type": "file_search", "file_search_store_names": [STORE]}])
        self.assertEqual(sent["system_instruction"], "sys")

    def test_client_option_is_milliseconds_and_call_passes_seconds(self):
        client = query.make_query_client("offline-dummy-key", 37.5)
        self.assertEqual(client.interactions.sdk_configuration.timeout_ms, 37500)
        fake = mock.Mock()
        query.ask(fake, model="m", question="q", system_instruction="s", store_name=STORE, timeout_seconds=37.5)
        self.assertEqual(fake.interactions.create.call_args.kwargs["timeout"], 37.5)

    def test_timeout_then_success_still_requires_valid_citations(self):
        # Answer text contains the article URL but carries no citation metadata.
        transport = Transport(["timeout", (200, interaction_body(None))])
        (interaction, attempts), sleeps = run_ask(transport, timeout_seconds=5)
        self.assertEqual((attempts, len(transport.requests)), (2, 2))
        self.assertEqual(sleeps, [2.25])  # base 2.0 s * attempt 1 + mocked jitter
        answer, anns = query.extract_answer(interaction)
        self.assertIn(URL, answer)
        verification = query.verify_citations(anns, MANIFEST)
        self.assertFalse(verification.passed)

        transport = Transport(["timeout", (200, interaction_body([{"type": "file_citation", "document_uri": DOC}]))])
        (interaction, _), _ = run_ask(transport, timeout_seconds=5)
        verification = query.verify_citations(query.extract_answer(interaction)[1], MANIFEST)
        self.assertTrue(verification.passed)
        self.assertEqual(verification.verified_urls, [URL])

    def test_repeated_timeouts_stop_at_attempt_limit(self):
        transport = Transport(["timeout"] * 10)
        with self.assertRaises(query.QueryFailedError) as ctx:
            run_ask(transport, timeout_seconds=5)
        self.assertEqual(ctx.exception.attempts, query.MAX_QUERY_ATTEMPTS)
        self.assertEqual(len(transport.requests), query.MAX_QUERY_ATTEMPTS)  # no stacked SDK retries
        self.assertEqual(type(ctx.exception.last_error).__name__, "APITimeoutError")

    def test_503_is_retried_once_without_sdk_retries(self):
        overloaded = (503, {"error": {"message": "high demand", "code": "service_unavailable"}})
        transport = Transport([overloaded] * 10)
        with self.assertRaises(query.QueryFailedError) as ctx:
            run_ask(transport, timeout_seconds=5)
        self.assertEqual(len(transport.requests), 2)
        self.assertEqual(query.status_code_of(ctx.exception.last_error), 503)

    def test_auth_and_invalid_request_errors_are_not_retried(self):
        for status in (400, 401, 403):
            transport = Transport([(status, {"error": {"message": "nope"}})] * 3)
            with self.assertRaises(query.QueryFailedError) as ctx:
                run_ask(transport, timeout_seconds=5)
            self.assertEqual((ctx.exception.attempts, len(transport.requests)), (1, 1), status)

    def test_error_label_never_includes_message(self):
        transport = Transport([(401, {"error": {"message": "key offline-dummy-key invalid"}})])
        with self.assertRaises(query.QueryFailedError) as ctx:
            run_ask(transport, timeout_seconds=5)
        self.assertNotIn("offline-dummy-key", query.error_label(ctx.exception.last_error))
        self.assertNotIn("offline-dummy-key", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
