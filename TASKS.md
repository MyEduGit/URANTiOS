# URANTiOS — Task Priorities

> Managed by the [Task Prioritiser](https://myedugit.github.io/mircea-constellation/prioritiser.html) in mircea-constellation.

## Active Tasks

| ID      | Priority    | Title                                                | Deadline   | Status  |
|---------|-------------|------------------------------------------------------|------------|---------|
| UOS-001 | P1 CRITICAL | Generate Stage 8 artifact (Software Blueprint)       | 2026-04-20 | Pending |
| UOS-002 | P1 CRITICAL | Generate Stage 9 artifact (Eternal Roadmap)          | 2026-04-25 | Blocked |
| UOS-003 | P2 HIGH     | Run URANTiOS-RUNNER v2.0 full synthesis              | 2026-05-10 | Blocked |

## Dependency Chain

```
UOS-001 (Stage 8) --> UOS-002 (Stage 9) --> UOS-003 (Full synthesis)
```

Stage 8 is the critical blocker. Until `pipeline/generate-artifact.py --stage 8` runs, nothing else can proceed.

## Requirements

- Anthropic API key in `~/.openclaw/secrets.env`
- Soul file at `soul/URANTiOS_v2.md` (present)
- All 197 Urantia Book JSON files in `urantia-book/` (present)

## Priority Rules

- **P1 CRITICAL** = do it now, alarm sounds if overdue
- **P2 HIGH** = do it this week
- **P3 MEDIUM** = do it this sprint
- **P4 LOW** = backlog

## Central Dashboard

All tasks across the constellation are tracked at:
`mircea-constellation/task-prioritiser.json`

The visual dashboard with alerts lives at:
`mircea-constellation/prioritiser.html`
