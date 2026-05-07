# NemoClaw

> Local-first, deterministic, auditable, recoverable AI orchestration substrate.

NemoClaw is the execution layer for queue-driven, artifact-producing AI workers
under explicit human governance. It is intentionally boring: no clever
autonomy, no opaque state, no hidden control flow.

This subtree (`/home/user/URANTiOS/nemoclaw/`) is the canonical NemoClaw root.
Bootstrap was performed on branch `claude/nemoclaw-setup-GDKGy`.

---

## Principles

| Principle | Meaning |
|---|---|
| Verification Before Claim | No "done" without verified evidence. |
| Obsidian-first archival | Knowledge stored as plain markdown. |
| Stateless workers | Workers carry no governance state. |
| Queue-centric execution | All inter-worker flow goes through Redis. |
| Artifact-first workflows | Every task produces a self-contained artifact. |
| Human-governed autonomy | Approval gates for anything destructive. |
| Local-first sovereignty | Bind to `127.0.0.1`; no public exposure by default. |
| Git-backed auditability | One repo, one branch per task, no force pushes. |
| Recoverability over cleverness | Boring beats brittle. |

---

## Layout

```
nemoclaw/
├── CLAUDE.md              # operating contract for AI workers
├── README.md              # this file
├── docker-compose.yml     # Postgres, Redis, n8n, Ollama
├── .env.example           # secret template
├── bootstrap.sh           # validate + start + verify
├── manifests/             # bootstrap + run manifests
├── workflows/             # n8n / pipeline definitions
├── logs/                  # runtime + bootstrap logs
├── backups/               # snapshot dumps (untracked content)
├── archive/
│   └── conversations/     # markdown archives of governance conversations
├── obsidian/              # canonical knowledge vault (markdown)
├── postgres/              # service runtime data (gitignored)
├── redis/                 # service runtime data (gitignored)
├── n8n/                   # service runtime data (gitignored)
├── nemo-core/             # orchestration core + MCP placeholders
├── workers/               # stateless worker implementations
├── scripts/               # operational helpers
└── docs/                  # ARCHITECTURE / SECURITY / WORKFLOW_MODEL
```

---

## Quick start

```sh
cd /home/user/URANTiOS/nemoclaw
cp .env.example .env
# edit .env — set every change_me_* value
./bootstrap.sh
```

`bootstrap.sh` will:
1. validate Docker + compose v2
2. require `.env` (refuses to start with empty secrets)
3. `docker compose up -d`
4. inspect each container's status
5. write everything to `logs/bootstrap.log`

Exit codes: `0` verified · `2` missing `.env` · `3` containers failed to come up.

---

## Services

| Service | Port (default) | Purpose |
|---|---|---|
| postgres | 5432 | persistence (n8n + future NemoClaw schemas) |
| redis | 6379 | queue + event bus |
| n8n | 5678 | visual workflow + cron |
| ollama | 11434 | local LLM runtime |

All services bind to `${BIND_ADDRESS:-127.0.0.1}` only. **Public exposure
requires explicit human approval** and a documented rationale in `docs/`.

---

## Workers (planned)

Stateless. Queue-driven. Artifact-producing. Replaceable.

- `ClaudeWorker`
- `GPTWorker`
- `OllamaWorker`
- `TranscriptWorker`
- `VisionWorker`
- `MetadataWorker`

See `workers/*/README.md` for per-worker scaffolds.

---

## MCP

MCP integration is **scaffolded as placeholders only** under
`nemo-core/mcp_placeholders/`. Real adapters are added under human review.
See `docs/ARCHITECTURE.md`.

---

## See also

- `CLAUDE.md` — AI operating contract
- `docs/ARCHITECTURE.md` — full architecture
- `docs/SECURITY.md` — approval gates and sandboxing
- `docs/WORKFLOW_MODEL.md` — queue + artifact model
- `obsidian/README.md` — vault conventions
