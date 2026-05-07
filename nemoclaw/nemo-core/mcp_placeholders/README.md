# MCP placeholders

> Do **NOT** fake MCP implementations. These are scaffold-only.
> Real adapters are added under explicit human review.

Each subdirectory below names a future MCP integration point. Each holds
only a `README.md` describing the intended contract, not any executable
code.

| Directory | Intended adapter |
|---|---|
| `filesystem/` | scoped filesystem access |
| `obsidian/` | vault read/write |
| `github/` | issues, PRs, commits (scope-restricted) |
| `postgres/` | query interface to the substrate DB |
| `telegram/` | operator notifications |
| `browser/` | headless browsing |

## Why placeholders

NemoClaw's audit story relies on MCP adapters being honest. A faked
adapter that returns plausible-looking results without actually doing the
work would silently corrupt the artifact archive and the audit log. So
these directories stay empty (except for documentation) until a real
adapter is written and reviewed.
