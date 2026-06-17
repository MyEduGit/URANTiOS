# Running Hermes 4 (14B) locally on Apple Silicon

This guide installs the **Nous Research Hermes 4 14B** language model locally
on an Apple Silicon Mac (tested target: **iMac M4, 32 GB unified memory**) using
[Ollama](https://ollama.com), which runs GGUF models with Metal acceleration.

## Why Hermes 4 14B for an M4 / 32 GB

| Option | Params | Q-quant size | Notes |
|--------|--------|--------------|-------|
| Hermes 3 — 3B  | 3B  | ~2 GB    | Lightest/fastest, lower quality |
| Hermes 3 — 8B  | 8B  | ~4.9 GB  | Older gen (Llama 3.1), dependable, fast |
| **Hermes 4 — 14B** | **14B** | **~10.5 GB (Q5_K_M)** | **Newest gen (Qwen3 base), hybrid reasoning — best fit for a 32 GB M4** |
| Hermes 4 — 70B | 70B | ~40 GB+  | Needs more memory than 32 GB at usable quants |

Hermes 4 adds a **hybrid reasoning mode** (it can deliberate before answering),
plus function calling, JSON mode and structured outputs. With 32 GB of unified
memory, the **Q4_K_M** quant is the recommended quality/speed balance, runs fast
on Metal, and leaves plenty of memory free. Bump to Q5/Q6/Q8 for more quality.

## Two ways to run it on a Mac

| Route | Runtime | Format | Notes |
|-------|---------|--------|-------|
| **Ollama (default here)** | Ollama | GGUF | Simplest CLI; the `install-hermes.sh` script automates it. |
| **MLX 4-bit (fastest)** | LM Studio or `mlx-lm` | MLX | Apple-native (MLX) — typically the fastest on M-series silicon. |

> Use **Docker = no.** Run natively via Ollama or LM Studio for Metal acceleration.

## Quick start (Ollama route)

```bash
# from the repo root
./pipeline/install-hermes.sh
```

The script will:
1. Install Ollama (via Homebrew if available, otherwise points you to the app).
2. Start the Ollama server.
3. Pull `hf.co/bartowski/NousResearch_Hermes-4-14B-GGUF:Q4_K_M`.
4. Alias it to `hermes4` and run a one-line smoke test.

Then chat any time with:

```bash
ollama run hermes4
```

## Choosing a different quant

`Q4_K_M` (~9 GB) is the default. Override with the `HERMES_QUANT` env var:

```bash
HERMES_QUANT=Q5_K_M ./pipeline/install-hermes.sh   # ~10.5 GB, higher quality
HERMES_QUANT=Q6_K   ./pipeline/install-hermes.sh   # ~12 GB, near-Q6 quality
HERMES_QUANT=Q8_0   ./pipeline/install-hermes.sh   # ~15.7 GB, near-lossless
```

## Manual install (Ollama, no script)

```bash
brew install ollama                 # or download the app from ollama.com/download/mac
ollama pull hf.co/bartowski/NousResearch_Hermes-4-14B-GGUF:Q4_K_M
ollama run  hf.co/bartowski/NousResearch_Hermes-4-14B-GGUF:Q4_K_M
```

## MLX 4-bit route (fastest on Apple Silicon)

MLX is Apple's array framework; the 4-bit MLX build of Hermes 4 14B usually
gives the best tokens/sec on M-series chips. Two easy ways:

**LM Studio (GUI):** install from https://lmstudio.ai, then search the model
catalog for `Hermes-4-14B` and pick the **MLX 4-bit** variant
(`mlx-community/Hermes-4-14B-4bit`) to download and chat.

**`mlx-lm` (CLI):**

```bash
pip install mlx-lm
python -m mlx_lm.generate \
  --model mlx-community/Hermes-4-14B-4bit \
  --prompt "In one sentence, confirm you are Hermes 4 and ready."
# or an interactive chat:
python -m mlx_lm.chat --model mlx-community/Hermes-4-14B-4bit
```

## Stepping down to Hermes 3 8B

If you prefer the lighter, faster Hermes 3 8B instead:

```bash
ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF:Q4_K_M
ollama run  hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF:Q4_K_M
```

## Sources

- Hermes 4 14B (weights): https://hf.co/NousResearch/Hermes-4-14B
- Hermes 4 14B (GGUF quants): https://hf.co/bartowski/NousResearch_Hermes-4-14B-GGUF
- Hermes 4 14B (MLX 4-bit): https://hf.co/mlx-community/Hermes-4-14B-4bit
- Hermes 3 8B (GGUF quants): https://hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF
- Ollama: https://ollama.com
- LM Studio: https://lmstudio.ai

> Note: This setup runs on your local Mac. It was prepared in a cloud sandbox
> whose network policy blocks `huggingface.co`, so the model download could not
> be exercised there — but your Mac has normal internet access and the commands
> above are the standard, supported path.
