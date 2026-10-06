"""Configuration loading and validation for the OptiSigns support-article pipeline."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent
ENV_PATH = PROJECT_ROOT / ".env"

DATA_DIR = PROJECT_ROOT / "data"
ARTICLES_DIR = DATA_DIR / "articles"
STATE_DIR = PROJECT_ROOT / "state"
LOGS_DIR = PROJECT_ROOT / "logs"

_PLACEHOLDER_VALUES = {"", "your-api-key-here", "changeme", "replace-me"}


class ConfigError(ValueError):
    """Raised when required configuration is missing or invalid."""


@dataclass
class Config:
    gemini_api_key: str
    gemini_model: str
    gemini_file_search_store: str
    support_base_url: str

    @property
    def has_api_key(self) -> bool:
        return bool(self.gemini_api_key) and self.gemini_api_key.strip().lower() not in _PLACEHOLDER_VALUES

    @property
    def has_file_search_store(self) -> bool:
        return bool(self.gemini_file_search_store.strip())


def ensure_runtime_dirs() -> None:
    """Create runtime directories if they don't already exist (safe on a fresh clone)."""
    for directory in (ARTICLES_DIR, STATE_DIR, LOGS_DIR):
        directory.mkdir(parents=True, exist_ok=True)


def load_config(require_api_key: bool = True, require_file_search_store: bool = False) -> Config:
    """Load configuration from .env (if present) and the environment.

    GEMINI_API_KEY is the primary credential name; API_KEY is accepted as a
    fallback to match the assignment's Docker invocation convention.
    """
    load_dotenv(dotenv_path=ENV_PATH, override=False)

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("API_KEY") or ""
    model = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")
    file_search_store = os.environ.get("GEMINI_FILE_SEARCH_STORE", "")
    support_base_url = os.environ.get("SUPPORT_BASE_URL", "https://support.optisigns.com")

    config = Config(
        gemini_api_key=api_key.strip(),
        gemini_model=model.strip(),
        gemini_file_search_store=file_search_store.strip(),
        support_base_url=support_base_url.strip(),
    )

    errors = []
    if require_api_key and not config.has_api_key:
        errors.append(
            "GEMINI_API_KEY (or API_KEY fallback) is missing or a placeholder. "
            "Copy .env.sample to .env and set a real key."
        )
    if require_file_search_store and not config.has_file_search_store:
        errors.append("GEMINI_FILE_SEARCH_STORE is required for this operation but is empty.")

    if errors:
        raise ConfigError("; ".join(errors))

    return config


def describe_non_secret(config: Config) -> dict:
    """Return a dict of settings safe to print — never includes the API key itself."""
    return {
        "gemini_model": config.gemini_model,
        "gemini_file_search_store": config.gemini_file_search_store or "(not set)",
        "support_base_url": config.support_base_url,
        "api_key_configured": config.has_api_key,
        "env_file": str(ENV_PATH),
    }
