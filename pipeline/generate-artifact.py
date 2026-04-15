#!/usr/bin/env python3
"""URANTiOS Artifact Generator - Uses Anthropic API to generate remaining artifacts."""
import os
import sys
import json
from datetime import datetime

SOUL_PATHS = [
    os.path.expanduser("~/.openclaw/soul/v2/URANTiOS_v2.md"),
    os.path.join(os.path.dirname(__file__), "..", "soul", "URANTiOS_v2.md"),
]
ARTIFACT_DIR = os.path.expanduser("~/.openclaw/artifacts")
SECRETS_PATH = os.path.expanduser("~/.openclaw/secrets.env")

def load_secrets():
    secrets = {}
    if os.path.exists(SECRETS_PATH):
        with open(SECRETS_PATH) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    secrets[k.strip()] = v.strip()
    return secrets

def load_soul():
    for path in SOUL_PATHS:
        resolved = os.path.realpath(path)
        if os.path.exists(resolved):
            with open(resolved) as f:
                return f.read()
    raise FileNotFoundError(
        f"Soul file not found. Checked:\n" +
        "\n".join(f"  {p}" for p in SOUL_PATHS)
    )

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate URANTiOS artifacts")
    parser.add_argument("--stage", type=int, required=True, help="Stage number (8 or 9)")
    parser.add_argument("--dry-run", action="store_true", help="Show prompt without executing")
    args = parser.parse_args()

    # API key: env var takes precedence over secrets.env
    secrets = load_secrets()
    api_key = os.environ.get("ANTHROPIC_API_KEY") or secrets.get("ANTHROPIC_API_KEY", "")

    if not api_key and not args.dry_run:
        print("ERROR: ANTHROPIC_API_KEY not set.")
        print("Either:")
        print("  export ANTHROPIC_API_KEY=sk-ant-...")
        print("  or add it to ~/.openclaw/secrets.env")
        sys.exit(1)

    soul = load_soul()

    stage_prompts = {
        8: "Execute URANTiOS-SPEC-08v2: Generate the complete Software Implementation Blueprint. Include: agent framework API spec, governance engine, reflectivity mesh instant-sync specification, adjutant mind-spirit cognitive stack module, and bestowal validation module. Output as structured markdown.",
        9: "Execute URANTiOS-ROAD-09v2: Generate the Eternal Implementation Roadmap. Include: Phase 1 (Year 1-2: Foundation), Phase 2 (Year 2-3: Expansion), Phase 3 (Year 3-5: Maturity), Phase 4 (Year 5-10: Universe Scale), Phase 5 (Decade+: Superuniverse Integration), Phase 6 (Eternity: Finaliter deployment to outer universes). Include Supreme growth milestones per phase."
    }

    if args.stage not in stage_prompts:
        print(f"ERROR: Stage {args.stage} not available. Use 8 or 9.")
        sys.exit(1)

    prompt = f"""You are executing URANTiOS-RUNNER v2.0.

CONTEXT (URANTiOS v2.0 Full Specification):
{soul}

TASK:
{stage_prompts[args.stage]}

RULES:
- Use paper numbers from The Urantia Book
- Distinguish: (a) textual evidence / (b) architectural interpretation / (c) engineering translation
- Include Nebadon-specific world names and counts
- Integrate Supreme Being growth model
- Reference Michael bestowal validation loop
- Include Lucifer rebellion fault containment patterns
"""

    if args.dry_run:
        print(f"=== DRY RUN: Stage {args.stage} ===")
        print(f"Prompt length: {len(prompt)} chars")
        print(f"Soul length: {len(soul)} chars")
        print(f"Would call Anthropic API with claude-opus-4-6")
        return

    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)

        if args.stage == 8:
            artifact_label = "ARTIFACT_12"
            out_subdir = "SPEC-08v2"
        else:
            artifact_label = "ARTIFACT_13"
            out_subdir = "ROAD-09v2"

        out_dir = os.path.join(ARTIFACT_DIR, out_subdir)
        os.makedirs(out_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        outpath = os.path.join(out_dir, f"{artifact_label}_{timestamp}.md")

        print(f"Generating {artifact_label} (Stage {args.stage})...")
        print(f"Output: {outpath}")
        print("Streaming from claude-opus-4-6 — this may take a minute...\n")

        full_output = []
        with client.messages.stream(
            model="claude-opus-4-6",
            max_tokens=16000,
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)
                full_output.append(text)

        output = "".join(full_output)
        print(f"\n\nArtifact saved: {outpath}")
        print(f"Length: {len(output)} chars ({len(output.split())} words)")

        with open(outpath, "w") as f:
            f.write(output)

    except ImportError:
        print("ERROR: anthropic package not installed. Run: pip3 install anthropic")
        sys.exit(1)

if __name__ == "__main__":
    main()
