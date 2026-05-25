"""Daily book publishing orchestrator."""
from __future__ import annotations
import json, os, hashlib
from datetime import date, datetime, timezone
from pathlib import Path
from .config import Config
from .corpus import Corpus
from .vault import MultiVault
from .writer import BookWriter
from .notify import send_telegram, update_notion_log

THEMES_PATH = Path(__file__).parent / "daily_themes.json"
STATE_PATH = Path(os.environ.get(
    "DAILY_STATE_PATH",
    str(Path(__file__).resolve().parent.parent / "artifacts" / "daily-state.json"),
))


def _load_themes() -> list[dict]:
    with open(THEMES_PATH) as f:
        return json.load(f)


def _load_state() -> dict:
    if STATE_PATH.exists():
        with open(STATE_PATH) as f:
            return json.load(f)
    return {"completed": [], "last_run": None}


def _save_state(state: dict):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)


def _pick_theme(themes: list[dict], completed: list[str]) -> dict | None:
    for t in themes:
        tid = t.get("id") or hashlib.md5(t["theme"].encode()).hexdigest()[:8]
        if tid not in completed:
            t["id"] = tid
            return t
    return None


class DailyPublisher:
    def __init__(self, cfg: Config, vault_paths: list[str]):
        self.cfg = cfg
        self.vault_paths = vault_paths

    @classmethod
    def from_env(cls) -> "DailyPublisher":
        cfg = Config.from_env()
        vaults = os.environ.get("BOOKWRITER_VAULTS", "").split(":")
        vaults = [v.strip() for v in vaults if v.strip()]
        return cls(cfg=cfg, vault_paths=vaults)

    def run(self, *, dry_run: bool = False, force_theme: str | None = None) -> dict:
        themes = _load_themes()
        state = _load_state()

        if force_theme:
            theme_entry = {
                "id": "manual",
                "theme": force_theme,
                "chapters": self.cfg.default_chapters,
            }
        else:
            theme_entry = _pick_theme(themes, state["completed"])
            if not theme_entry:
                return {
                    "status": "exhausted",
                    "message": "All themes completed. Add more to daily_themes.json.",
                }

        cfg = Config.from_env(dry_run=dry_run)
        corpus = Corpus.load(cfg.corpus_dir)
        vault = MultiVault.from_paths(self.vault_paths) if self.vault_paths else None
        writer = BookWriter(corpus=corpus, cfg=cfg, vault=vault)

        print(f"[daily] Theme: {theme_entry['theme']}")
        book = writer.write(
            theme=theme_entry["theme"],
            chapters=theme_entry.get("chapters", cfg.default_chapters),
        )

        state["completed"].append(theme_entry["id"])
        state["last_run"] = {
            "date": date.today().isoformat(),
            "theme_id": theme_entry["id"],
            "theme": theme_entry["theme"],
            "title": book.title,
            "slug": book.slug,
            "chapters": len(book.chapters),
            "words": book.word_count(),
            "generated_at": book.metadata.get("generated_at"),
        }
        if not dry_run:
            _save_state(state)

        result = {
            "status": "ok",
            "book": {
                "title": book.title,
                "theme": book.theme,
                "slug": book.slug,
                "chapters": len(book.chapters),
                "words": book.word_count(),
            },
            "theme_id": theme_entry["id"],
            "remaining": len(themes) - len(state["completed"]),
        }

        tg_token = os.environ.get("TELEGRAM_BOT_TOKEN")
        tg_chat = os.environ.get("TELEGRAM_CHAT_ID")
        if tg_token and tg_chat and not dry_run:
            send_telegram(
                token=tg_token, chat_id=tg_chat,
                title=book.title, theme=book.theme,
                chapters=len(book.chapters), words=book.word_count(),
                remaining=result["remaining"],
            )
            result["telegram"] = "sent"

        notion_key = os.environ.get("NOTION_API_KEY")
        notion_db = os.environ.get("NOTION_DAILY_DB_ID")
        if notion_key and notion_db and not dry_run:
            update_notion_log(
                api_key=notion_key, database_id=notion_db,
                title=book.title, theme=book.theme,
                date_str=date.today().isoformat(),
                chapters=len(book.chapters), words=book.word_count(),
            )
            result["notion"] = "logged"

        return result
