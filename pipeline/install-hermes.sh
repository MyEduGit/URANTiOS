#!/bin/bash
# install-hermes.sh — Install & run Nous Research Hermes 4 (14B) locally
#
# Target hardware: Apple Silicon Mac (e.g. iMac M4, 32GB unified memory)
# Runtime: Ollama (Metal-accelerated llama.cpp under the hood)
# Model:   NousResearch Hermes 4 14B, GGUF quant pulled from Hugging Face
#
# Hermes 4 14B is the newest-generation Hermes (Qwen3 base) with hybrid
# reasoning, function calling, JSON mode and structured outputs. On a 32GB
# M4 the Q5_K_M quant (~10.5GB) is the quality/speed sweet spot and leaves
# ~20GB of memory free.
#
# Usage:
#   ./install-hermes.sh                 # install Ollama + pull Hermes 4 14B (Q5_K_M)
#   HERMES_QUANT=Q6_K ./install-hermes.sh   # higher quality (~12GB)
#   HERMES_QUANT=Q4_K_M ./install-hermes.sh # smaller/faster (~9GB)

set -euo pipefail

# --- Configuration -----------------------------------------------------------
HERMES_REPO="${HERMES_REPO:-hf.co/bartowski/NousResearch_Hermes-4-14B-GGUF}"
HERMES_QUANT="${HERMES_QUANT:-Q5_K_M}"
MODEL_REF="${HERMES_REPO}:${HERMES_QUANT}"
ALIAS="${HERMES_ALIAS:-hermes4}"   # short name to call the model by

echo "=== Hermes 4 (14B) Installer ==="
echo "Model:   ${MODEL_REF}"
echo "Alias:   ${ALIAS}"
echo ""

# --- Sanity check: platform --------------------------------------------------
OS="$(uname -s)"
ARCH="$(uname -m)"
if [ "$OS" = "Darwin" ] && [ "$ARCH" = "arm64" ]; then
    echo "Platform: Apple Silicon macOS (Metal acceleration available). Good."
else
    echo "WARNING: This script is tuned for Apple Silicon macOS (arm64)."
    echo "         Detected ${OS}/${ARCH} — it will still work via CPU/whatever"
    echo "         backend Ollama selects, but performance may differ."
fi
echo ""

# --- Step 1: Ensure Ollama is installed --------------------------------------
if command -v ollama >/dev/null 2>&1; then
    echo "[1/4] Ollama already installed: $(ollama --version 2>/dev/null | head -1)"
else
    echo "[1/4] Installing Ollama..."
    if [ "$OS" = "Darwin" ] && command -v brew >/dev/null 2>&1; then
        brew install ollama
    elif [ "$OS" = "Darwin" ]; then
        echo "      Homebrew not found. Download the Ollama app from:"
        echo "        https://ollama.com/download/mac"
        echo "      Install it, then re-run this script."
        exit 1
    else
        # Linux fallback
        curl -fsSL https://ollama.com/install.sh | sh
    fi
fi
echo ""

# --- Step 2: Make sure the Ollama server is running --------------------------
echo "[2/4] Ensuring Ollama server is running..."
if ! ollama ls >/dev/null 2>&1; then
    echo "      Starting 'ollama serve' in the background..."
    ollama serve >/tmp/ollama-serve.log 2>&1 &
    # wait for the server to come up
    for _ in $(seq 1 30); do
        if ollama ls >/dev/null 2>&1; then break; fi
        sleep 1
    done
fi
ollama ls >/dev/null 2>&1 && echo "      Server is up." || { echo "ERROR: Ollama server did not start."; exit 1; }
echo ""

# --- Step 3: Pull the Hermes 4 14B GGUF --------------------------------------
echo "[3/4] Pulling ${MODEL_REF} (this downloads several GB the first time)..."
ollama pull "${MODEL_REF}"
# Give it a friendly short alias so you can just run: ollama run hermes4
ollama cp "${MODEL_REF}" "${ALIAS}" >/dev/null 2>&1 || true
echo "      Done. Available as '${ALIAS}'."
echo ""

# --- Step 4: Smoke test ------------------------------------------------------
echo "[4/4] Smoke test..."
echo "----------------------------------------------------------------------"
ollama run "${ALIAS}" "In one sentence, confirm you are the Hermes model and ready."
echo "----------------------------------------------------------------------"
echo ""
echo "Hermes 4 14B is installed."
echo "Chat with it any time:   ollama run ${ALIAS}"
echo "List installed models:   ollama ls"
echo "Remove it later:         ollama rm ${ALIAS} && ollama rm ${MODEL_REF}"
