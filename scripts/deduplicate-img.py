#!/usr/bin/env python3
# python run.py --input ../../data/one-nation/00_raw/ --output ../../data/one-nation/01_deduplicate
# dependencies: imagededup Pillow
import argparse
import logging
import shutil
import sys
from pathlib import Path
from PIL import Image

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger(__name__)

def is_image(path: Path) -> bool:
    try:
        with Image.open(path) as img:
            img.verify()
        return True
    except Exception:
        return False

def safe_dest(src: Path, dest_dir: Path) -> Path:
    candidate = dest_dir / src.name
    i = 1
    while candidate.exists():
        candidate = dest_dir / f"{src.stem}_{i}{src.suffix}"
        i += 1
    return candidate

def collect(source_dir: Path, output_dir: Path) -> int:
    all_files = [p for p in source_dir.rglob("*") if p.is_file()]
    output_dir.mkdir(parents=True, exist_ok=True)
    copied = 0
    for src in all_files:
        if is_image(src):
            shutil.copy2(src, safe_dest(src, output_dir))
            copied += 1
    log.info("Copied %d image(s)", copied)
    return copied

def deduplicate(output_dir: Path, max_distance: int) -> None:
    from imagededup.methods import PHash
    phasher = PHash()
    encodings = phasher.encode_images(image_dir=str(output_dir))
    duplicates = phasher.find_duplicates(encoding_map=encodings, max_distance_threshold=max_distance)
    parent: dict[str, str] = {}

    def find(x):
        while parent.get(x, x) != x:
            parent[x] = parent.get(parent[x], parent[x])
            x = parent[x]
        return x

    for file, dups in duplicates.items():
        for dup in dups:
            ra, rb = find(file), find(dup)
            if ra != rb:
                parent[rb] = ra

    groups: dict[str, list[str]] = {}
    for name in encodings:
        groups.setdefault(find(name), []).append(name)

    removed = 0
    for group in groups.values():
        if len(group) < 2:
            continue
        paths = sorted([output_dir / n for n in group], key=lambda p: p.stat().st_size, reverse=True)
        for loser in paths[1:]:
            loser.unlink()
            removed += 1
    log.info("Removed %d duplicate(s)", removed)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", "-i", required=True)
    p.add_argument("--output", "-o", required=True)
    p.add_argument("--max-distance", "-d", type=int, default=10)
    args = p.parse_args()
    input_dir = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output).expanduser().resolve()
    if not input_dir.exists():
        log.error("Input directory not found: %s", input_dir)
        sys.exit(1)
    if collect(input_dir, output_dir) > 0:
        deduplicate(output_dir, args.max_distance)

if __name__ == "__main__":
    main()
