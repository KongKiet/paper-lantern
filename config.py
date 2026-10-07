"""Configuration loading and validation for the OptiSigns support-article pipeline."""

from __future__ import annotations

import math
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
PROMPTS_DIR = PROJECT_ROOT / "prompts"
OPTIBOT_PROMPT_PATH = PROMPTS_DIR / "optibot.txt"

_PLACEHOLDER_VALUES = {"", "your-api-key-here", "changeme", "replace-me"}

DEFAULT_QUERY_TIMEOUT_SECONDS = 120.0
DEFAULT_ARTICLE_LIMIT = 30


class ConfigError(ValueError):
    """Raised when required configuration is missing or invalid."""


@dataclass
class Config:
    gemini_api_key: str
    gemini_model: str
    gemini_file_search_store: str
    support_base_url: str
    gemini_query_timeout_seconds: float = DEFAULT_QUERY_TIMEOUT_SECONDS
    support_article_limit: int = DEFAULT_ARTICLE_LIMIT

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


def parse_timeout_seconds(raw: str | None, name: str = "GEMINI_QUERY_TIMEOUT_SECONDS") -> float:
    """Parse a positive, finite number of seconds; empty/unset means the default."""
    if raw is None or not raw.strip():
        return DEFAULT_QUERY_TIMEOUT_SECONDS
    try:
        value = float(raw.strip())
    except ValueError:
        raise ConfigError(f"{name} must be a positive number of seconds (got {raw.strip()!r}).") from None
    if not math.isfinite(value) or value <= 0:
        raise ConfigError(f"{name} must be a positive number of seconds (got {raw.strip()!r}).")
    return value


def parse_article_limit(raw: str | None, name: str = "SUPPORT_ARTICLE_LIMIT") -> int:
    """Parse a positive integer article count; empty/unset means the default."""
    if raw is None or not raw.strip():
        return DEFAULT_ARTICLE_LIMIT
    try:
        value = int(raw.strip())
    except ValueError:
        raise ConfigError(f"{name} must be a positive integer (got {raw.strip()!r}).") from None
    if value <= 0:
        raise ConfigError(f"{name} must be a positive integer (got {raw.strip()!r}).")
    return value


def load_config(require_api_key: bool = True, require_file_search_store: bool = False) -> Config:
    """Load configuration from .env (if present) and the environment.

    GEMINI_API_KEY is the primary credential name; API_KEY is accepted as a
    fallback to match the assignment's Docker invocation convention.
    """
    load_dotenv(dotenv_path=ENV_PATH, override=False)

    # Strip before falling back so a blank GEMINI_API_KEY= (e.g. from a Docker
    # --env-file) does not shadow API_KEY.
    api_key = (os.environ.get("GEMINI_API_KEY") or "").strip() or (os.environ.get("API_KEY") or "").strip()
    model = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")
    file_search_store = os.environ.get("GEMINI_FILE_SEARCH_STORE", "")
    support_base_url = os.environ.get("SUPPORT_BASE_URL", "https://support.optisigns.com")
    query_timeout_seconds = parse_timeout_seconds(os.environ.get("GEMINI_QUERY_TIMEOUT_SECONDS"))
    article_limit = parse_article_limit(os.environ.get("SUPPORT_ARTICLE_LIMIT"))

    config = Config(
        gemini_api_key=api_key.strip(),
        gemini_model=model.strip(),
        gemini_file_search_store=file_search_store.strip(),
        support_base_url=support_base_url.strip(),
        gemini_query_timeout_seconds=query_timeout_seconds,
        support_article_limit=article_limit,
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
        "gemini_query_timeout_seconds": config.gemini_query_timeout_seconds,
        "support_article_limit": config.support_article_limit,
        "api_key_configured": config.has_api_key,
        "env_file": str(ENV_PATH),
    }
