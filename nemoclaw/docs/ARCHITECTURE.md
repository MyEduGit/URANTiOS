# NemoClaw — Architecture

## What NemoClaw is

NemoClaw is a deterministic, auditable, recoverable substrate for AI
orchestration. It coordinates stateless workers through a Redis queue,
producing self-contained artifacts that are archived as plain markdown.

It is **not** an agent framework. It does not grant authority to LLMs.
LLMs are workers; humans are governance.

## What OpenClaw is (relationship)

`OpenClaw` is the broader open-architecture umbrella: the conventions,
contracts, and reference workers that NemoClaw implements. NemoClaw is the
local-first, single-host instantiation. OpenClaw is the spec NemoClaw
conforms to.

A NemoClaw deployment can be replaced wholesale because the contract
(queue shape, artifact shape, approval gates) is OpenClaw — not the
implementation.

## Layers

```
┌─────────────────────────────────────────────┐
│ Human governance (approval gates)           │
├─────────────────────────────────────────────┤
│ NemoClaw orchestrator (queue + dispatch)    │
├─────────────────────────────────────────────┤
│ MCP layer (filesystem, obsidian, github,    │
│            postgres, telegram, browser)     │
├─────────────────────────────────────────────┤
│ Workers (Claude / GPT / Ollama / ...)       │
├─────────────────────────────────────────────┤
│ Substrate (Postgres, Redis, n8n, Ollama)    │
└─────────────────────────────────────────────┘
```

## Queue architecture

- **Broker:** Redis 7.
- **Pattern:** queue-centric, not peer-to-peer. Workers do not call workers.
- **Channels:**
  - `nemoclaw:queue:<worker_kind>` — task ingress per worker class.
  - `nemoclaw:events` — pub/sub for lifecycle events (queued, started,
    completed, verified, failed).
  - `nemoclaw:dlq:<worker_kind>` — dead letter queue.
- **Idempotency:** every task carries a `task_id`; replays are safe.

## Worker model

Workers are:

- **Stateless** — no in-memory governance, no persistent authority.
- **Replaceable** — kill `-9` is a valid recovery strategy.
- **Queue-driven** — only enter through `nemoclaw:queue:<worker_kind>`.
- **Artifact-producing** — emit a complete artifact directory; nothing else
  counts as output.

### Planned workers

| Worker | Role |
|---|---|
| `ClaudeWorker` | Anthropic Claude API tasks |
| `GPTWorker` | OpenAI tasks |
| `OllamaWorker` | local LLM tasks via Ollama |
| `TranscriptWorker` | conversation/transcript ingestion |
| `VisionWorker` | image/PDF understanding |
| `MetadataWorker` | extraction, tagging, indexing |

Workers MUST NOT:

- retain authority across runs
- retain governance state
- self-escalate permissions
- contact other workers directly

## Artifact model

Every task produces a directory under `archive/<task_id>/`:

```
<task_id>/
├── manifest.json     # task metadata, inputs, worker, model, timing
├── prompt.md         # exact prompt sent
├── output.md         # primary output
├── logs.txt          # raw worker stdout/stderr
├── verification.txt  # verification evidence (commands + results)
└── diff.patch        # optional — if task mutated files
```

Artifacts are immutable once `verification.txt` is present.

## MCP layer

MCP adapters are scaffolded as **placeholders only** under
`nemo-core/mcp_placeholders/`:

- `filesystem/` — scoped file access
- `obsidian/` — vault read/write
- `github/` — issues, PRs, commits
- `postgres/` — query interface
- `telegram/` — operator notifications
- `browser/` — headless browsing

Real adapters are added under human review. The directive prohibits faking
MCP implementations.

## Failure model

- Every state transition is logged.
- DLQ for tasks that exceed retry budget.
- Backups under `backups/` are dump-and-restore, not live replication.
- Recovery is preferred over cleverness — restart > heal-in-place.
