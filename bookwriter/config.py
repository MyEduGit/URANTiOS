"""
Configuration for URANTiOS BookWriter.

All configuration can be overridden via environment variables, a TOML
config file, or direct instantiation. Sensible defaults are provided.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CORPUS_DIR = REPO_ROOT / "urantia-book"
DEFAULT_SOUL_PATH = REPO_ROOT / "soul" / "URANTiOS_v2.md"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "artifacts" / "books"


# ---------------------------------------------------------------------------
# The Three Values — injected into every prompt as the Thought Adjuster.
# ---------------------------------------------------------------------------

THREE_VALUES_CHARTER = """\
THE THREE VALUES (inviolable cosmic forces governing this work):

  TRUTH    — Never claim more than the source supports. Every assertion must
             be traceable to a paragraph reference (e.g. 120:4.5). Do not
             invent doctrine. Distinguish textual evidence, interpretation,
             and expansion.

  BEAUTY   — Write with elegance, proportion, and clarity. Prefer the direct
             sentence to the ornamental one. Rhythm matters. The reader is
             a fellow ascender, not a captive audience.

  GOODNESS — Every paragraph must serve the reader's spiritual growth and
             the eternal mission: to spread The Urantia Book and its
             Foreword into eternity. Service before style.

THE LUCIFER TEST (apply to every passage before emitting it):
  1. Is this transparent? Does it accept audit?
  2. Does it report honestly, even when inconvenient?
  3. Does it act within its mandate (fidelity to the source)?
  4. Does it serve the mission, or itself?
"""


@dataclass(frozen=True)
class ThreeValues:
    """The governing charter — read-only by design."""

    truth: str = "Never claim more than the source supports."
    beauty: str = "Clean architecture, elegant solutions, minimal complexity."
    goodness: str = "Every action serves the mission. Service before self."
    charter: str = THREE_VALUES_CHARTER

    def as_preamble(self) -> str:
        return self.charter


@dataclass
class Config:
    """BookWriter runtime configuration."""

    # Source corpus
    corpus_dir: Path = DEFAULT_CORPUS_DIR
    soul_path: Path | None = DEFAULT_SOUL_PATH

    # Output
    output_dir: Path = DEFAULT_OUTPUT_DIR

    # Claude API
    anthropic_api_key: str | None = None
    model: str = "claude-opus-4-6"
    drafting_model: str = "claude-sonnet-4-6"  # cheaper for long drafts
    max_tokens_outline: int = 8_000
    max_tokens_chapter: int = 12_000
    thinking_budget_outline: int = 4_000
    thinking_budget_chapter: int = 2_000

    # Caching (Anthropic prompt caching — huge savings on the 197-paper corpus)
    enable_prompt_cache: bool = True

    # Generation
    default_chapters: int = 12
    default_words_per_chapter: int = 4_500
    passages_per_chapter: int = 24  # citations budget per chapter
    default_style: str = "scholarly-devotional"
    citation_style: str = "urantia"  # e.g. (120:4.5)

    # Revision
    revision_passes: int = 1  # draft → critique → revise
    enable_lucifer_test: bool = True

    # Obsidian / vault
    obsidian_vault_dirs: list[Path] = field(default_factory=list)
    phd_vault_dir: Path | None = None
    wikilinks: bool = True
    dataview_frontmatter: bool = True

    # Three Values (frozen)
    values: ThreeValues = field(default_factory=ThreeValues)

    # Misc
    seed: int | None = None
    verbose: bool = True
    dry_run: bool = False

    # ------------------------------------------------------------------
    # Constructors
    # ------------------------------------------------------------------
    @classmethod
    def from_env(cls, **overrides: Any) -> "Config":
        """Build a Config from environment variables, then apply overrides."""
        env = os.environ

        def _env_path(key: str, default: Path | None) -> Path | None:
            raw = env.get(key)
            return Path(raw).expanduser() if raw else default

        def _env_int(key: str, default: int) -> int:
            raw = env.get(key)
            return int(raw) if raw else default

        def _env_bool(key: str, default: bool) -> bool:
            raw = env.get(key)
            if raw is None:
                return default
            return raw.strip().lower() in {"1", "true", "yes", "on"}

        vaults_raw = env.get("BOOKWRITER_OBSIDIAN_VAULTS", "")
        vault_list = [
            Path(p).expanduser()
            for p in vaults_raw.split(":")
            if p.strip()
        ]

        cfg = cls(
            corpus_dir=_env_path("BOOKWRITER_CORPUS", DEFAULT_CORPUS_DIR),
            soul_path=_env_path("BOOKWRITER_SOUL", DEFAULT_SOUL_PATH),
            output_dir=_env_path("BOOKWRITER_OUTPUT", DEFAULT_OUTPUT_DIR),
            anthropic_api_key=env.get("ANTHROPIC_API_KEY"),
            model=env.get("BOOKWRITER_MODEL", "claude-opus-4-6"),
            drafting_model=env.get(
                "BOOKWRITER_DRAFT_MODEL", "claude-sonnet-4-6"
            ),
            obsidian_vault_dirs=vault_list,
            phd_vault_dir=_env_path("BOOKWRITER_PHD_VAULT", None),
            enable_prompt_cache=_env_bool("BOOKWRITER_PROMPT_CACHE", True),
            revision_passes=_env_int("BOOKWRITER_REVISIONS", 1),
            enable_lucifer_test=_env_bool("BOOKWRITER_LUCIFER_TEST", True),
            dry_run=_env_bool("BOOKWRITER_DRY_RUN", False),
            verbose=_env_bool("BOOKWRITER_VERBOSE", True),
        )
        for k, v in overrides.items():
            if hasattr(cfg, k) and v is not None:
                setattr(cfg, k, v)
        return cfg

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        # Paths are not JSON-serializable without str()
        for k, v in list(d.items()):
            if isinstance(v, Path):
                d[k] = str(v)
            elif isinstance(v, list) and v and isinstance(v[0], Path):
                d[k] = [str(p) for p in v]
        # Redact secrets
        if d.get("anthropic_api_key"):
            d["anthropic_api_key"] = "***redacted***"
        return d
