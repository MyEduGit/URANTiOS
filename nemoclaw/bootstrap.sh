#!/usr/bin/env bash
# NemoClaw bootstrap.sh
#
# Validates Docker, starts services, verifies containers, writes logs.
# Idempotent. Refuses to run destructive operations without explicit flag.
#
# Principles:
#   - Verification Before Claim
#   - Recoverability over cleverness
#   - Human-governed autonomy

set -Eeuo pipefail

# --- locate self ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

LOG_DIR="$SCRIPT_DIR/logs"
LOG_FILE="$LOG_DIR/bootstrap.log"
mkdir -p "$LOG_DIR"

ts() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }
log() { printf '[%s] %s\n' "$(ts)" "$*" | tee -a "$LOG_FILE"; }
fail() { log "FAIL: $*"; exit 1; }

trap 'log "ERROR: bootstrap aborted at line $LINENO (exit $?)"' ERR

log "=== NemoClaw bootstrap start ==="
log "workdir: $SCRIPT_DIR"

# --- 1. Validate Docker ---
log "[1/5] validating docker"
command -v docker >/dev/null 2>&1 || fail "docker not found in PATH"
docker info >/dev/null 2>&1 || fail "docker daemon not reachable (is Docker Desktop / dockerd running?)"
log "docker OK: $(docker --version)"

# --- 2. Validate docker compose v2 ---
log "[2/5] validating docker compose v2"
docker compose version >/dev/null 2>&1 || fail "docker compose v2 plugin missing"
log "compose OK: $(docker compose version --short)"

# --- 3. .env presence ---
log "[3/5] checking .env"
if [[ ! -f "$SCRIPT_DIR/.env" ]]; then
  log "WARN: .env not found. Copy .env.example to .env and fill in real values, then re-run."
  log "      (refusing to start services with default/empty secrets)"
  exit 2
fi

# --- 4. Start services ---
log "[4/5] starting services (docker compose up -d)"
docker compose --project-directory "$SCRIPT_DIR" up -d 2>&1 | tee -a "$LOG_FILE"

# --- 5. Verify containers ---
log "[5/5] verifying container health"
sleep 3
EXPECTED=(nemoclaw-postgres nemoclaw-redis nemoclaw-n8n nemoclaw-ollama)
ALL_OK=1
for c in "${EXPECTED[@]}"; do
  status="$(docker inspect -f '{{.State.Status}}' "$c" 2>/dev/null || echo missing)"
  health="$(docker inspect -f '{{if .State.Health}}{{.State.Health.Status}}{{else}}n/a{{end}}' "$c" 2>/dev/null || echo missing)"
  log "container $c: status=$status health=$health"
  if [[ "$status" != "running" ]]; then
    ALL_OK=0
  fi
done

if (( ALL_OK == 1 )); then
  log "=== NemoClaw bootstrap VERIFIED ==="
  log "n8n:      http://${BIND_ADDRESS:-127.0.0.1}:${N8N_PORT:-5678}"
  log "ollama:   http://${BIND_ADDRESS:-127.0.0.1}:${OLLAMA_PORT:-11434}"
  log "postgres: ${BIND_ADDRESS:-127.0.0.1}:${POSTGRES_PORT:-5432}"
  log "redis:    ${BIND_ADDRESS:-127.0.0.1}:${REDIS_PORT:-6379}"
  exit 0
else
  log "=== NemoClaw bootstrap UNVERIFIED — one or more containers not running ==="
  exit 3
fi
