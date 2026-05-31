#!/usr/bin/env python3
"""URANTiOS Artifact Generator - Uses Anthropic API to generate remaining artifacts."""
import os
import sys
import json
from datetime import datetime

# Resolve paths relative to the repo so the script runs from a fresh clone,
# while still honouring a legacy ~/.openclaw install layout if present.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Anthropic model used to generate artifacts. Override via the ANTHROPIC_MODEL
# environment variable if you want a different model.
MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-8")


def _first_existing(*candidates):
    """Return the first path that exists, else the first candidate."""
    for path in candidates:
        if path and os.path.exists(path):
            return path
    return candidates[0]


SOUL_PATH = _first_existing(
    os.path.join(REPO_ROOT, "soul", "URANTiOS_v2.md"),
    os.path.expanduser("~/.openclaw/soul/v2/URANTiOS_v2.md"),
)
ARTIFACT_DIR = os.path.join(REPO_ROOT, "artifacts")
SECRETS_PATH = _first_existing(
    os.path.expanduser("~/.openclaw/secrets.env"),
    os.path.join(REPO_ROOT, ".env"),
)

def load_secrets():
    secrets = {}
    if os.path.exists(SECRETS_PATH):
        with open(SECRETS_PATH) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    secrets[k.strip()] = v.strip()
    # Environment variable wins if set (e.g. exported in CI or the shell).
    if os.environ.get("ANTHROPIC_API_KEY"):
        secrets["ANTHROPIC_API_KEY"] = os.environ["ANTHROPIC_API_KEY"]
    return secrets

def load_soul():
    with open(SOUL_PATH) as f:
        return f.read()

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate URANTiOS artifacts")
    parser.add_argument("--stage", type=int, required=True, help="Stage number (8 or 9)")
    parser.add_argument("--dry-run", action="store_true", help="Show prompt without executing")
    args = parser.parse_args()
    
    secrets = load_secrets()
    api_key = secrets.get("ANTHROPIC_API_KEY", "")
    
    if not api_key and not args.dry_run:
        print("ERROR: ANTHROPIC_API_KEY not set in ~/.openclaw/secrets.env")
        print("Add your key and retry.")
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
        print(f"Would call Anthropic API with {MODEL}")
        return
    
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        
        print(f"Generating ARTIFACT_{args.stage + 4}...")
        response = client.messages.create(
            model=MODEL,
            max_tokens=16000,
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.content[0].text
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        if args.stage == 8:
            outpath = f"{ARTIFACT_DIR}/SPEC-08v2/ARTIFACT_12_{timestamp}.md"
        else:
            outpath = f"{ARTIFACT_DIR}/ROAD-09v2/ARTIFACT_13_{timestamp}.md"

        os.makedirs(os.path.dirname(outpath), exist_ok=True)
        with open(outpath, 'w') as f:
            f.write(output)
        
        print(f"Artifact saved: {outpath}")
        print(f"Length: {len(output)} chars")
        
    except ImportError:
        print("ERROR: anthropic package not installed. Run: pip3 install anthropic")
        sys.exit(1)

if __name__ == "__main__":
    main()
