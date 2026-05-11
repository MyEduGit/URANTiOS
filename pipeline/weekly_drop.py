#!/usr/bin/env python3
"""Prepare large weekly drops (20GB+) for reliable transfer and ingest.

Creates:
- chunk files
- SHA256 checksums for each chunk
- manifest.json metadata

Example:
  python3 pipeline/weekly_drop.py \
      --input /data/week_2026-05-11.tar.zst \
      --outdir /data/drops/week_2026-05-11 \
      --chunk-size-gb 2
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

BUF_SIZE = 8 * 1024 * 1024


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(BUF_SIZE):
            h.update(chunk)
    return h.hexdigest()


def split_file(input_path: Path, outdir: Path, chunk_size_bytes: int) -> list[dict]:
    chunks: list[dict] = []
    index = 0
    with input_path.open("rb") as src:
        while True:
            chunk_path = outdir / f"{input_path.name}.part{index:04d}"
            written = 0
            with chunk_path.open("wb") as dst:
                while written < chunk_size_bytes:
                    need = min(BUF_SIZE, chunk_size_bytes - written)
                    data = src.read(need)
                    if not data:
                        break
                    dst.write(data)
                    written += len(data)
            if written == 0:
                chunk_path.unlink(missing_ok=True)
                break
            digest = sha256_file(chunk_path)
            chunks.append(
                {
                    "index": index,
                    "filename": chunk_path.name,
                    "bytes": written,
                    "sha256": digest,
                }
            )
            index += 1
    return chunks


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare 20GB+ weekly drop artifacts")
    parser.add_argument("--input", required=True, type=Path, help="Path to large file")
    parser.add_argument("--outdir", required=True, type=Path, help="Output directory")
    parser.add_argument(
        "--chunk-size-gb",
        type=float,
        default=2.0,
        help="Chunk size in GB (default: 2.0)",
    )
    args = parser.parse_args()

    input_path: Path = args.input
    outdir: Path = args.outdir

    if not input_path.exists() or not input_path.is_file():
        raise SystemExit(f"Input file does not exist: {input_path}")
    if args.chunk_size_gb <= 0:
        raise SystemExit("--chunk-size-gb must be > 0")

    outdir.mkdir(parents=True, exist_ok=True)

    chunk_size_bytes = int(args.chunk_size_gb * (1024**3))
    chunks = split_file(input_path, outdir, chunk_size_bytes)

    full_sha256 = sha256_file(input_path)
    manifest = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": {
            "filename": input_path.name,
            "bytes": input_path.stat().st_size,
            "sha256": full_sha256,
        },
        "chunk_size_bytes": chunk_size_bytes,
        "chunk_count": len(chunks),
        "chunks": chunks,
    }

    manifest_path = outdir / "manifest.json"
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"Prepared drop: {input_path}")
    print(f"Total size: {manifest['source']['bytes']} bytes")
    print(f"Chunks: {len(chunks)} @ {chunk_size_bytes} bytes")
    print(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
