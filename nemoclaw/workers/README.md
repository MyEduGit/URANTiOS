# Workers

Stateless. Replaceable. Queue-driven. Artifact-producing.

Each worker subdirectory is a placeholder scaffold — it documents the
worker's contract but contains no executable implementation yet. Real
implementations are added under human review.

## Common contract

Every worker:

1. Reads tasks from `nemoclaw:queue:<worker_kind>` (Redis).
2. Writes a complete artifact directory under `archive/<task_id>/`.
3. Publishes lifecycle events to `nemoclaw:events`.
4. Exits cleanly after each task — no in-process state retention.
5. Has scoped read/write paths declared in the task envelope. The
   container mounts enforce this; the worker code must not assume more
   access than declared.

## Workers

| Directory | Worker kind | Purpose |
|---|---|---|
| `claude_worker/` | `claude_worker` | Anthropic Claude API tasks |
| `gpt_worker/` | `gpt_worker` | OpenAI tasks |
| `ollama_worker/` | `ollama_worker` | local LLM tasks via Ollama |
| `transcript_worker/` | `transcript_worker` | conversation/transcript ingestion |
| `vision_worker/` | `vision_worker` | image/PDF understanding |
| `metadata_worker/` | `metadata_worker` | extraction, tagging, indexing |

See `docs/WORKFLOW_MODEL.md` for the task envelope format and lifecycle.
