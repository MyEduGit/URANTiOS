"""Notification helpers for daily publishing — Telegram and Notion."""
from __future__ import annotations
import json
from urllib.request import Request, urlopen
from urllib.error import URLError


def send_telegram(*, token: str, chat_id: str, title: str, theme: str,
                  chapters: int, words: int, remaining: int):
    text = (
        "\U0001f4da *Daily Book Published*\n\n"
        f"*{_esc(title)}*\n"
        f"Theme: {_esc(theme)}\n"
        f"Chapters: {chapters} · Words: {words:,}\n"
        f"Remaining themes: {remaining}\n\n"
        "_Truth · Beauty · Goodness_"
    )
    payload = json.dumps({
        "chat_id": chat_id, "text": text,
        "parse_mode": "Markdown", "disable_web_page_preview": True,
    }).encode()
    req = Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=payload, headers={"Content-Type": "application/json"},
    )
    try:
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except (URLError, OSError) as e:
        print(f"[notify] Telegram error: {e}")
        return None


def update_notion_log(*, api_key: str, database_id: str, title: str,
                      theme: str, date_str: str, chapters: int, words: int):
    payload = json.dumps({
        "parent": {"database_id": database_id},
        "properties": {
            "Title": {"title": [{"text": {"content": title}}]},
            "Theme": {"rich_text": [{"text": {"content": theme}}]},
            "Date": {"date": {"start": date_str}},
            "Chapters": {"number": chapters},
            "Words": {"number": words},
            "Status": {"select": {"name": "Published"}},
        },
    }).encode()
    req = Request(
        "https://api.notion.com/v1/pages",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        },
    )
    try:
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except (URLError, OSError) as e:
        print(f"[notify] Notion error: {e}")
        return None


def _esc(s: str) -> str:
    return s.replace("_", "\\_").replace("*", "\\*").replace("[", "\\[").replace("`", "\\`")
