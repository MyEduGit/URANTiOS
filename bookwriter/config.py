"""Configuration for URANTiOS BookWriter."""
from __future__ import annotations
import os
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CORPUS_DIR = REPO_ROOT / "urantia-book"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "artifacts" / "books"

THREE_VALUES_CHARTER = """\
THE THREE VALUES (inviolable):
  TRUTH    — Every assertion traceable to a paragraph reference. Distinguish
             textual evidence, interpretation, and expansion.
  BEAUTY   — Elegance, proportion, clarity. Rhythm matters.
  GOODNESS — Every paragraph serves the reader's spiritual growth and the
             eternal mission.

THE LUCIFER TEST (apply before emitting):
  1. Is this transparent and auditable?
  2. Does it report honestly?
  3. Does it stay within its mandate (fidelity to source)?
  4. Does it serve the mission, or itself?
"""

@dataclass(frozen=True)
class ThreeValues:
    truth: str = "Never claim more than the source supports."
    beauty: str = "Clean architecture, elegant solutions, minimal complexity."
    goodness: str = "Every action serves the mission. Service before self."
    charter: str = THREE_VALUES_CHARTER

@dataclass
class Config:
    corpus_dir: Path = DEFAULT_CORPUS_DIR
    output_dir: Path = DEFAULT_OUTPUT_DIR
    anthropic_api_key: str | None = None
    model: str = "claude-opus-4-6"
    drafting_model: str = "claude-sonnet-4-6"
    max_tokens_outline: int = 8_000
    max_tokens_chapter: int = 12_000
    default_chapters: int = 12
    default_words_per_chapter: int = 4_500
    default_style: str = "scholarly-devotional"
    enable_prompt_cache: bool = True
    revision_passes: int = 1
    enable_lucifer_test: bool = True
    obsidian_vault_dirs: list[Path] = field(default_factory=list)
    wikilinks: bool = True
    dataview_frontmatter: bool = True
    values: ThreeValues = field(default_factory=ThreeValues)
    dry_run: bool = False
    verbose: bool = True

    @classmethod
    def from_env(cls, **overrides) -> "Config":
        env = os.environ
        cfg = cls(
            corpus_dir=Path(env.get("BOOKWRITER_CORPUS", str(DEFAULT_CORPUS_DIR))),
            output_dir=Path(env.get("BOOKWRITER_OUTPUT", str(DEFAULT_OUTPUT_DIR))),
            anthropic_api_key=env.get("ANTHROPIC_API_KEY"),
            model=env.get("BOOKWRITER_MODEL", "claude-opus-4-6"),
            dry_run=env.get("BOOKWRITER_DRY_RUN", "").lower() in {"1", "true"},
            verbose=env.get("BOOKWRITER_VERBOSE", "1").lower() not in {"0", "false"},
        )
        for k, v in overrides.items():
            if hasattr(cfg, k) and v is not None:
                setattr(cfg, k, v)
        return cfg
