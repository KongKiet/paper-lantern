"""Offline tests for API key resolution. The real .env is never read
(load_dotenv is patched out) and the environment is replaced per test."""

from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config  # noqa: E402


def load_with(env: dict[str, str]) -> config.Config:
    with mock.patch.dict(os.environ, env, clear=True), mock.patch.object(config, "load_dotenv"):
        return config.load_config(require_api_key=False)


class ApiKeyResolutionTests(unittest.TestCase):
    def test_gemini_api_key_takes_precedence(self):
        self.assertEqual(load_with({"GEMINI_API_KEY": "primary", "API_KEY": "fallback"}).gemini_api_key, "primary")

    def test_api_key_used_when_gemini_key_unset(self):
        self.assertEqual(load_with({"API_KEY": "fallback"}).gemini_api_key, "fallback")

    def test_api_key_used_when_gemini_key_empty_or_blank(self):
        for blank in ("", "   "):
            with self.subTest(blank=blank):
                self.assertEqual(load_with({"GEMINI_API_KEY": blank, "API_KEY": " fallback "}).gemini_api_key,
                                 "fallback")

    def test_missing_both_keys_raises_when_required(self):
        with mock.patch.dict(os.environ, {}, clear=True), mock.patch.object(config, "load_dotenv"):
            with self.assertRaises(config.ConfigError):
                config.load_config(require_api_key=True)

    def test_other_settings_unchanged(self):
        cfg = load_with({"API_KEY": "k", "GEMINI_MODEL": "m", "GEMINI_QUERY_TIMEOUT_SECONDS": "45",
                         "SUPPORT_ARTICLE_LIMIT": "12"})
        self.assertEqual((cfg.gemini_model, cfg.gemini_query_timeout_seconds, cfg.support_article_limit),
                         ("m", 45.0, 12))


if __name__ == "__main__":
    unittest.main()
