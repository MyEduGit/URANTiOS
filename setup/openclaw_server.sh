#!/usr/bin/env bash
# OpenClaw Server Setup — URANTiOS (soul + pipeline on the execution node)
# Target host: Hetzner CPX22 — 46.225.51.30 (Nuremberg, DE), user: mircea
# UrantiOS governed — Truth, Beauty, Goodness
#
# Stages the URANTiOS soul and pipeline under ~/.openclaw/ — the exact layout
# the pipeline scripts (pipeline/runner-v2.sh, pipeline/generate-artifact.py)
# already expect. Idempotent: safe to re-run.
#
# Usage (on OpenClaw as user `mircea`):
#   bash setup/openclaw_server.sh

set -euo pipefail

CYAN='\033[0;36m'; GREEN='\033[0;32m'; RED='\033[0;31m'; YELLOW='\033[1;33m'; NC='\033[0m'
info()  { echo -e "${CYAN}[INFO]${NC}  $*"; }
ok()    { echo -e "${GREEN}[OK]${NC}    $*"; }
warn()  { echo -e "${YELLOW}[WARN]${NC}  $*"; }
fail()  { echo -e "${RED}[FAIL]${NC}  $*"; exit 1; }

REPO_URL="https://github.com/myedugit/urantios.git"
REPO_DIR="${HOME}/URANTiOS"

OC_HOME="${HOME}/.openclaw"
OC_SOUL="${OC_HOME}/soul/v2"
OC_PIPELINE="${OC_HOME}/pipeline"
OC_ARTIFACTS="${OC_HOME}/artifacts"
OC_LOGS="${OC_HOME}/logs"
OC_BOOK="${OC_HOME}/urantia-book"
OC_SECRETS="${OC_HOME}/secrets.env"

echo ""
echo "================================================="
echo "  OpenClaw Server Setup — URANTiOS"
echo "  Host: 46.225.51.30  User: $(id -un)"
echo "  Three Values: Truth · Beauty · Goodness"
echo "================================================="
echo ""

[ "$(id -un)" != "root" ] || fail "Do not run as root. Run as 'mircea'; sudo is used where needed."
command -v sudo >/dev/null || fail "sudo is required."

# ── 1. System packages ──────────────────────────────────────────────────────
info "[1/5] Installing system packages (git, python3, jq, rsync)..."
sudo apt-get update -qq
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -qq \
  git python3 python3-pip python3-venv jq rsync curl ca-certificates
ok "Packages installed."

# ── 2. Clone / refresh repo ─────────────────────────────────────────────────
info "[2/5] Syncing repo to ${REPO_DIR}..."
if [ ! -d "${REPO_DIR}/.git" ]; then
  git clone "${REPO_URL}" "${REPO_DIR}"
  ok "Cloned."
else
  git -C "${REPO_DIR}" pull --ff-only || warn "Could not fast-forward — leaving working tree as-is."
  ok "Repo up to date."
fi

# ── 3. Materialize ~/.openclaw/ layout ──────────────────────────────────────
info "[3/5] Materializing ~/.openclaw/ layout..."
mkdir -p "${OC_SOUL}" "${OC_PIPELINE}" "${OC_ARTIFACTS}" "${OC_LOGS}" "${OC_BOOK}"
chmod 700 "${OC_HOME}"

# Soul (source of truth: repo/soul/URANTiOS_v2.md → ~/.openclaw/soul/v2/)
if [ -f "${REPO_DIR}/soul/URANTiOS_v2.md" ]; then
  rsync -a "${REPO_DIR}/soul/URANTiOS_v2.md" "${OC_SOUL}/URANTiOS_v2.md"
  ok "Soul staged: ${OC_SOUL}/URANTiOS_v2.md ($(wc -l <"${OC_SOUL}/URANTiOS_v2.md") lines)"
else
  warn "soul/URANTiOS_v2.md not found in repo — skipping soul stage."
fi

# Pipeline scripts
if [ -d "${REPO_DIR}/pipeline" ]; then
  rsync -a --delete "${REPO_DIR}/pipeline/" "${OC_PIPELINE}/"
  chmod +x "${OC_PIPELINE}/"*.sh "${OC_PIPELINE}/"*.py 2>/dev/null || true
  ok "Pipeline staged: ${OC_PIPELINE}/"
fi

# Urantia Book corpus (JSON papers)
if [ -d "${REPO_DIR}/urantia-book" ]; then
  rsync -a "${REPO_DIR}/urantia-book/" "${OC_BOOK}/"
  ok "Urantia Book staged: ${OC_BOOK}/ ($(find "${OC_BOOK}" -type f | wc -l) files)"
fi

# ── 4. secrets.env stub ─────────────────────────────────────────────────────
info "[4/5] secrets.env..."
if [ ! -f "${OC_SECRETS}" ]; then
  cat > "${OC_SECRETS}" << 'SECEOF'
# URANTiOS OpenClaw secrets — DO NOT COMMIT
# Fill these in, then: chmod 600 ~/.openclaw/secrets.env

ANTHROPIC_API_KEY=
TELEGRAM_BOT_TOKEN=
TELEGRAM_USER_ID=828807562
SECEOF
  chmod 600 "${OC_SECRETS}"
  warn "secrets.env stub created at ${OC_SECRETS} — fill in ANTHROPIC_API_KEY."
else
  chmod 600 "${OC_SECRETS}"
  ok "secrets.env already present."
fi

# ── 5. Python venv for pipeline ─────────────────────────────────────────────
info "[5/5] Python venv for pipeline..."
VENV="${OC_HOME}/venv"
if [ ! -d "${VENV}" ]; then
  python3 -m venv "${VENV}"
  ok "Created ${VENV}."
fi
# shellcheck disable=SC1091
source "${VENV}/bin/activate"
pip install --quiet --upgrade pip
pip install --quiet anthropic requests pyyaml
ok "Pipeline deps installed: $(python3 --version)"
deactivate

# ── Proof ───────────────────────────────────────────────────────────────────
info "Proof:"
echo "  ~/.openclaw/:"
ls -la "${OC_HOME}" | sed 's/^/    /'
echo ""
echo "  Soul lines:     $(wc -l <"${OC_SOUL}/URANTiOS_v2.md" 2>/dev/null || echo 'missing')"
echo "  Pipeline files: $(ls "${OC_PIPELINE}" 2>/dev/null | wc -l)"
echo "  Book files:     $(find "${OC_BOOK}" -type f 2>/dev/null | wc -l)"

echo ""
echo "================================================="
echo "  URANTiOS OpenClaw Setup Complete"
echo "================================================="
echo ""
echo "  Next steps:"
echo "  1. Fill in ${OC_SECRETS} (ANTHROPIC_API_KEY at minimum)"
echo "  2. Run the pipeline:"
echo "       bash ${OC_PIPELINE}/runner-v2.sh"
echo "  3. Generate remaining artifacts:"
echo "       source ${VENV}/bin/activate"
echo "       python3 ${OC_PIPELINE}/generate-artifact.py --stage 8"
echo ""
echo "  Every Process Must Load URANTiOS."
echo "  Truth · Beauty · Goodness."
echo ""
