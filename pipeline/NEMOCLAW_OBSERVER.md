# NemoClaw Observer — URANTiOS integration

URANTiOS Prime (204.168.143.98) runs the live **NanoClaw v1.2.17**
container and the Gabriel brain on port 18900. NemoClaw Observer
continuously verifies that these services are reachable from outside
and that Qdrant's `havona_records_v2` collection is populated.

Core observer: `mircea-constellation/nemoclaw_observer/`
(branch `claude/setup-nemoclaw-1502q`).

## What the observer asserts about URANTiOS

| Probe | Passes when |
|---|---|
| `check_qdrant`   | `GET http://<VPS>:6333/collections/havona_records_v2` returns a `result` block |
| `check_ollama`   | `phi3:14b`, `deepseek-r1:8b`, `qwen3:8b` are all present locally (iMac M4) |
| `check_postgres` | `amep_schema_v1` is reachable on port 5432 |

If URANTiOS Prime (Helsinki) is the host of interest, point the
observer at it by setting `QDRANT_HOST=204.168.143.98` in its `.env`.
Otherwise it defaults to the Hetzy VPS at 46.225.51.30.

## Running the observer against URANTiOS Prime

On any machine with outbound HTTPS:

```bash
git clone --branch claude/setup-nemoclaw-1502q \
    https://github.com/myedugit/mircea-constellation.git
cd mircea-constellation/nemoclaw_observer
cp config.env.example .env
# edit .env and set:
#   VPS_HOST=204.168.143.98
#   QDRANT_HOST=204.168.143.98
./run.sh                 # one-shot check
./run.sh loop telegram   # 6-hour cadence
```

## Recovery playbook

| Alert | Action |
|---|---|
| `Qdrant unreachable` | `ssh 204.168.143.98 && docker ps \| grep qdrant && docker restart qdrant` |
| `havona_records_v2 not found` | Re-run ingest: `pipeline/` scripts on URANTiOS |
| `NanoClaw not responding` | `docker restart nanoclaw` on URANTiOS |
| `Gabriel brain offline` | Check `:18900` on URANTiOS and restart the brain service |

Dashboard history is stored in
`nemoclaw_dashboard_log` on the Hetzy PostgreSQL — query
`nemoclaw_recent_alerts` for the last 7 days.
