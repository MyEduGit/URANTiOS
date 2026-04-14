"""
Anthropic Claude client wrapper.

Two layers of indirection:

1.  ``ClaudeClient`` — thin wrapper around ``anthropic.Anthropic`` that
    knows about prompt caching, extended thinking, and our preferred
    defaults. Lazy-imports the SDK so the rest of the package can be
    imported without ``anthropic`` installed (useful for testing).

2.  ``DryRunClient`` — drop-in replacement that returns deterministic
    fake responses. Selected automatically when ``--dry-run`` is set or
    no API key is available, so the pipeline can be exercised offline.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any

from .config import Config


@dataclass
class LLMResponse:
    text: str
    input_tokens: int = 0
    output_tokens: int = 0
    cache_creation_tokens: int = 0
    cache_read_tokens: int = 0
    stop_reason: str | None = None

    @property
    def usage(self) -> dict[str, int]:
        return {
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "cache_creation_input_tokens": self.cache_creation_tokens,
            "cache_read_input_tokens": self.cache_read_tokens,
        }


class ClaudeClient:
    """Real Claude client with prompt caching."""

    def __init__(self, cfg: Config):
        self.cfg = cfg
        try:
            import anthropic  # noqa: F401  (lazy assertion)
        except ImportError as e:
            raise ImportError(
                "The `anthropic` package is required. "
                "Install with: pip install anthropic"
            ) from e
        from anthropic import Anthropic

        self._client = Anthropic(api_key=cfg.anthropic_api_key)

    # ------------------------------------------------------------------
    def complete(
        self,
        *,
        system_blocks: list[dict[str, Any]],
        messages: list[dict[str, Any]],
        model: str | None = None,
        max_tokens: int = 8000,
        thinking_budget: int = 0,
        temperature: float = 1.0,
    ) -> LLMResponse:
        """Run a single Claude completion.

        ``system_blocks`` is a list of system content blocks (per the
        Anthropic API). To enable prompt caching on a block, include
        ``"cache_control": {"type": "ephemeral"}`` in that block.
        """
        kwargs: dict[str, Any] = {
            "model": model or self.cfg.model,
            "max_tokens": max_tokens,
            "system": system_blocks,
            "messages": messages,
        }
        # Extended thinking — temperature must be 1 when thinking is on
        if thinking_budget > 0:
            kwargs["thinking"] = {
                "type": "enabled",
                "budget_tokens": thinking_budget,
            }
            kwargs["temperature"] = 1.0
        else:
            kwargs["temperature"] = temperature

        resp = self._client.messages.create(**kwargs)

        # Concatenate text blocks (ignore thinking blocks in output)
        out_parts = []
        for block in resp.content:
            if getattr(block, "type", None) == "text":
                out_parts.append(block.text)
        text = "".join(out_parts)

        usage = resp.usage
        return LLMResponse(
            text=text,
            input_tokens=getattr(usage, "input_tokens", 0) or 0,
            output_tokens=getattr(usage, "output_tokens", 0) or 0,
            cache_creation_tokens=getattr(
                usage, "cache_creation_input_tokens", 0
            ) or 0,
            cache_read_tokens=getattr(
                usage, "cache_read_input_tokens", 0
            ) or 0,
            stop_reason=getattr(resp, "stop_reason", None),
        )


class DryRunClient:
    """Offline stand-in. Returns plausible structured fake content."""

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def complete(
        self,
        *,
        system_blocks: list[dict[str, Any]],
        messages: list[dict[str, Any]],
        model: str | None = None,
        max_tokens: int = 8000,
        thinking_budget: int = 0,
        temperature: float = 1.0,
    ) -> LLMResponse:
        last_user = ""
        for m in reversed(messages):
            if m.get("role") == "user":
                last_user = _flatten_content(m.get("content"))
                break
        if "OUTLINE" in last_user.upper() or "outline" in last_user:
            text = json.dumps(
                {
                    "title": "Sample Book (dry-run)",
                    "subtitle": "Generated offline without LLM",
                    "epigraph": "Truth, Beauty, Goodness — UrantiOS.",
                    "chapters": [
                        {
                            "number": i + 1,
                            "title": f"Chapter {i+1}: Placeholder",
                            "thesis": "Dry-run thesis.",
                            "key_refs": ["0:0.1", "1:0.1"],
                            "beats": [
                                "Beat one (dry-run).",
                                "Beat two (dry-run).",
                            ],
                        }
                        for i in range(self.cfg.default_chapters)
                    ],
                },
                indent=2,
            )
        else:
            text = (
                "# Dry-run chapter\n\n"
                "_(No API key — this is placeholder text.)_\n\n"
                "The Universal Father is the source of all reality "
                "([0:1.1]).\n"
            )
        return LLMResponse(
            text=text,
            input_tokens=len(last_user) // 4,
            output_tokens=len(text) // 4,
        )


def _flatten_content(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        out = []
        for block in content:
            if isinstance(block, dict):
                if block.get("type") == "text":
                    out.append(block.get("text", ""))
        return "".join(out)
    return str(content) if content is not None else ""


def make_client(cfg: Config) -> ClaudeClient | DryRunClient:
    """Pick the right client. Falls back to dry-run when no key/SDK."""
    if cfg.dry_run:
        return DryRunClient(cfg)
    if not cfg.anthropic_api_key:
        cfg.anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not cfg.anthropic_api_key:
        return DryRunClient(cfg)
    try:
        return ClaudeClient(cfg)
    except ImportError:
        return DryRunClient(cfg)
