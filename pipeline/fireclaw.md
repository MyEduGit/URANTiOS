# FireClaw Ingress

FireClaw is the edge hot-line daemon. It forwards urgent signals from local
agents to the NemoClaw n8n webhook, which then may enter the URANTiOS
pipeline as an event.

## Flow

```
edge agent ─► FireClaw (local :8797) ─► NemoClaw /webhook/fireclaw
                                          └─► URANTiOS pipeline (this repo)
```

## Event schema (as it arrives in the pipeline)

```json
{
  "id": "uuid-v4",
  "received_at": "ISO-8601 UTC",
  "source": "imac-menubar | iphone-shortcut | lobsterbot | claude-session | ...",
  "severity": "low | med | high",
  "message": "free-form",
  "meta": { "...": "agent-supplied context" }
}
```

## Pipeline expectations

- `severity: high` → Council is convened immediately (n8n routes to all seats).
- `severity: med`  → queued to the next Council tick.
- `severity: low`  → logged only.

## Implementation

Daemon source + boot scripts live in `mircea-constellation`:
`setup/fireclaw/` (daemon `fireclaw.py`, `boot.sh`, `README.md`).

Ontological placement: `phd-triune-monism:10_Ontology/FireClaw.md`.
