# nemo-core

The orchestration core: queue dispatch, lifecycle event bus, approval
gate enforcement, manifest/artifact bookkeeping.

**Status:** scaffold only. No implementation yet.

This is the only place in the tree that holds orchestration authority.
Worker containers should mount this directory **read-only** at runtime.

## Subdirectories

| Path | Purpose |
|---|---|
| `mcp_placeholders/` | placeholder folders for future MCP adapters — DO NOT fake implementations |

See `../docs/ARCHITECTURE.md`.
