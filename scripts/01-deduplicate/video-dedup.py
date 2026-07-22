#!/usr/bin/env python3
# python deduplicate-vid.py ../../data/one-nation/00_raw/ --output ../../data/one-nation/01_deduplicate
# Dependencies: vdf-cli from https://github.com/0x90d/videoduplicatefinder/releases

import argparse
import logging
import shutil
import subprocess
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger(__name__)

VDF_CLI = "/usr/bin/vdf-cli"
VIDEO_EXTENSIONS = {
    ".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm",
    ".m4v", ".3gp", ".mpeg", ".mpg", ".ts", ".mts", ".m2ts",
}

def safe_dest(src: Path, dest_dir: Path) -> Path:
    candidate = dest_dir / src.name
    i = 1
    while candidate.exists():
        candidate = dest_dir / f"{src.stem}_{i}{src.suffix}"
        i += 1
    return candidate

def collect(input_dir: Path, output_dir: Path) -> int:
    files = [p for p in input_dir.rglob("*") if p.is_file() and p.suffix.lower() in VIDEO_EXTENSIONS]
    output_dir.mkdir(parents=True, exist_ok=True)
    for src in files:
        shutil.copy2(src, safe_dest(src, output_dir))
    log.info("Copied %d video(s)", len(files))
    return len(files)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", "-i", required=True)
    p.add_argument("--output", "-o", required=True)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    input_dir = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output).expanduser().resolve()

    if collect(input_dir, output_dir) > 0:
        cmd = [VDF_CLI, "scan-and-compare", "--include", str(output_dir), "--action", "lowest-quality"]
        cmd.append("--dry-run" if args.dry_run else "--delete-permanent")
        subprocess.run(cmd)

if __name__ == "__main__":
    main()
