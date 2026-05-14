#!/usr/bin/env bash
# /doc installer — multi-AI Obsidian integration.
# Safe under sequential and parallel execution. Produces verifiable output.
set -euo pipefail

# --- Config (override via env) ---
VAULT_DIR="${VAULT_DIR:-$HOME/Documents/Obsidian/PhD-Triune-Monism}"
MASTER_MERMAID="$VAULT_DIR/master_pipeline.mmd"
MASTER_TEMPLATE="$VAULT_DIR/setup/master_pipeline.template.mmd"
JOBS_MANIFEST="$VAULT_DIR/setup/jobs.json"
LOCK_FILE="$VAULT_DIR/.doc.lock"
JOB_DATE="$(date +%F)"
JOB_SLUG="${1:-}"
[[ -z "$JOB_SLUG" ]] && { echo "usage: $0 <job-slug>" >&2; exit 2; }

GITHUB_REPO="${GITHUB_REPO:-myedugit/phd-triune-monism}"
GITHUB_BRANCH="${GITHUB_BRANCH:-claude/multi-ai-obsidian-integration-jkoI9}"
NOTION_PARENT_ID="${NOTION_PARENT_ID:-3328525a-b5a0-815d-886c-d5488593aa3d}"
NOTION_TOKEN="${NOTION_TOKEN:-}"
ZAPIER_HOOK_URL="${ZAPIER_HOOK_URL:-}"
CANVA_FALLBACK="${CANVA_FALLBACK:-false}"

# --- Paths ---
JOB_DIR="$VAULT_DIR/$JOB_DATE/$JOB_SLUG"
ASSETS_DIR="$JOB_DIR/assets"
JOB_MD="$JOB_DIR/job.md"
JOB_MMD="$ASSETS_DIR/$JOB_SLUG.mmd"
LOG_DIR="$VAULT_DIR/StressTestLogs"
LOG_FILE="$LOG_DIR/${JOB_SLUG}_$(date +%Y%m%d_%H%M%S).log"
mkdir -p "$ASSETS_DIR" "$LOG_DIR" "$(dirname "$JOBS_MANIFEST")"

# Tee all stdout/stderr from here on
exec > >(tee -a "$LOG_FILE") 2>&1
echo "[doc] start job=$JOB_SLUG date=$JOB_DATE pid=$$"

# --- Job frontmatter ---
cat > "$JOB_MD" <<EOF
---
job: $JOB_SLUG
date: $JOB_DATE
status: active
github_repo: $GITHUB_REPO
github_branch: $GITHUB_BRANCH
notion_parent: $NOTION_PARENT_ID
---

# Job: $JOB_SLUG

Started: $(date -u +%FT%TZ)

Artifacts: Mermaid source at \`assets/$JOB_SLUG.mmd\`.
SVG/PNG rendered by this installer when \`mmdc\` is on PATH.
EOF

# --- Per-job Mermaid source ---
cat > "$JOB_MMD" <<EOF
%% diagram for job: $JOB_SLUG
flowchart TD
    A[/doc $JOB_SLUG] --> B[Create job folder]
    B --> C[Generate diagram]
    C --> D[Commit + sync]
EOF

# --- Render per-job SVG/PNG (optional) ---
if command -v mmdc >/dev/null 2>&1; then
    mmdc -i "$JOB_MMD" -o "$ASSETS_DIR/$JOB_SLUG.svg" || echo "[doc] WARN mmdc svg failed"
    mmdc -i "$JOB_MMD" -o "$ASSETS_DIR/$JOB_SLUG.png" || echo "[doc] WARN mmdc png failed"
else
    echo "[doc] mmdc not installed; skipping SVG/PNG render for job"
fi

# --- Canva: honest handling ---
if [[ "$CANVA_FALLBACK" == "true" ]]; then
    cat <<'NOTE'
[doc] Canva generation is an MCP tool, not a shell CLI.
      To produce <job>-canva.png, invoke generate-design-structured
      from a Claude Code session. This shell script will NOT attempt
      it and will NOT claim success.
NOTE
fi

# --- Master pipeline: lock + regenerate from template + manifest ---
[[ -f "$JOBS_MANIFEST" ]] || echo "[]" > "$JOBS_MANIFEST"

(
    flock -x 9

    if command -v jq >/dev/null 2>&1; then
        REL_PATH="$JOB_DATE/$JOB_SLUG"
        GH_URL="https://github.com/$GITHUB_REPO/tree/$GITHUB_BRANCH/$REL_PATH"
        NT_URL="https://www.notion.so/$NOTION_PARENT_ID"
        jq --arg slug "$JOB_SLUG" \
           --arg date "$JOB_DATE" \
           --arg path "$REL_PATH" \
           --arg gh   "$GH_URL" \
           --arg nt   "$NT_URL" \
           '. + [{slug:$slug,date:$date,path:$path,github_url:$gh,notion_url:$nt}]' \
           "$JOBS_MANIFEST" > "$JOBS_MANIFEST.tmp" && mv "$JOBS_MANIFEST.tmp" "$JOBS_MANIFEST"
    else
        echo "[doc] WARN jq not installed; manifest not updated"
    fi

    if command -v jq >/dev/null 2>&1 && [[ -f "$MASTER_TEMPLATE" ]]; then
        {
            cat "$MASTER_TEMPLATE"
            echo ""
            echo "    %% --- Jobs (regenerated from setup/jobs.json) ---"
            jq -r '.[] | "    G_\(.slug | gsub("[^a-zA-Z0-9]";"_"))[\"\(.slug)\"]"' "$JOBS_MANIFEST" || true
            jq -r '.[] | "    click G_\(.slug | gsub("[^a-zA-Z0-9]";"_")) href \"\(.github_url)\" \"GitHub: \(.slug)\""' "$JOBS_MANIFEST" || true
        } > "$MASTER_MERMAID.tmp"
        mv "$MASTER_MERMAID.tmp" "$MASTER_MERMAID"
    fi

    if command -v mmdc >/dev/null 2>&1; then
        mmdc -i "$MASTER_MERMAID" -o "$VAULT_DIR/master_pipeline.svg" || echo "[doc] WARN master svg render failed"
        mmdc -i "$MASTER_MERMAID" -o "$VAULT_DIR/master_pipeline.png" || echo "[doc] WARN master png render failed"
    fi

    if [[ -d "$VAULT_DIR/.git" ]]; then
        pushd "$VAULT_DIR" >/dev/null
        git add "$JOB_DATE/$JOB_SLUG" "$MASTER_MERMAID" "$JOBS_MANIFEST" || true
        if ! git diff --cached --quiet; then
            git commit -m "doc: $JOB_SLUG — scaffold + manifest + master regen" || true
            CUR_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
            git push origin "$CUR_BRANCH" || echo "[doc] push skipped or failed; inspect manually"
        else
            echo "[doc] nothing staged; skipping commit"
        fi
        popd >/dev/null
    else
        echo "[doc] $VAULT_DIR is not a git work tree; skipping commit"
    fi
) 9>"$LOCK_FILE"

# --- Notion: real API call when NOTION_TOKEN is set; else honest skip ---
if [[ -n "$NOTION_TOKEN" ]]; then
    PAYLOAD=$(cat <<EOF
{
  "parent": { "page_id": "$NOTION_PARENT_ID" },
  "properties": { "title": [{ "text": { "content": "$JOB_SLUG — $JOB_DATE" } }] },
  "children": [
    { "object":"block","type":"heading_2","heading_2":{"rich_text":[{"type":"text","text":{"content":"$JOB_SLUG"}}]}},
    { "object":"block","type":"paragraph","paragraph":{"rich_text":[{"type":"text","text":{"content":"Job folder: $JOB_DATE/$JOB_SLUG"}}]}}
  ]
}
EOF
)
    RESP_TMP="$(mktemp)"
    HTTP_CODE=$(curl -s -o "$RESP_TMP" -w "%{http_code}" \
        -X POST "https://api.notion.com/v1/pages" \
        -H "Authorization: Bearer $NOTION_TOKEN" \
        -H "Notion-Version: 2022-06-28" \
        -H "Content-Type: application/json" \
        -d "$PAYLOAD")
    if [[ "$HTTP_CODE" == "200" ]]; then
        echo "[doc] Notion page created for $JOB_SLUG"
    else
        echo "[doc] Notion page creation FAILED http=$HTTP_CODE body=$(cat "$RESP_TMP")"
    fi
    rm -f "$RESP_TMP"
else
    echo "[doc] NOTION_TOKEN not set — Notion page NOT created (honest skip)"
fi

# --- Zapier: honest ---
if [[ -n "$ZAPIER_HOOK_URL" ]]; then
    if curl -fsS -X POST -H "Content-Type: application/json" \
            -d "{\"job\":\"$JOB_SLUG\",\"date\":\"$JOB_DATE\"}" \
            "$ZAPIER_HOOK_URL"; then
        echo "[doc] Zapier fan-out triggered"
    else
        echo "[doc] Zapier fan-out FAILED"
    fi
else
    echo "[doc] ZAPIER_HOOK_URL empty — fan-out skipped"
fi

echo "[doc] done job=$JOB_SLUG log=$LOG_FILE"
