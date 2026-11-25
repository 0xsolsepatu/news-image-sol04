#!/usr/bin/env python3
"""Carry the finished 25 November front page to the grader's output.

The picture is rendered beforehand (BUILD.md lists the 24 verified stories
and the newspaper design). This program does one job: copy entry.png next
to it into the directory the grader names, byte for byte, after proving
the file really is the PNG it claims to be. Standard library only, no
network, no randomness, no third-party code, so two runs always agree.
"""

from hashlib import sha256
from pathlib import Path

MAGIC = bytes((0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A))  # the 8-byte PNG signature
SOURCE = Path(__file__).resolve().parent / "entry.png"
CHUNK = 1 << 16


def fingerprint(path):
    """SHA-256 of a file, read in blocks."""
    total = sha256()
    with path.open("rb") as handle:
        while True:
            block = handle.read(CHUNK)
            if not block:
                break
            total.update(block)
    return total.hexdigest()


def hand_in():
    """Copy SOURCE to the output directory and verify the copy."""
    import os

    if not SOURCE.is_file():
        print(f"missing source image: {SOURCE}")
        return 1
    with SOURCE.open("rb") as handle:
        if handle.read(len(MAGIC)) != MAGIC:
            print(f"not a PNG file: {SOURCE}")
            return 1
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    target.write_bytes(SOURCE.read_bytes())
    if fingerprint(target) != fingerprint(SOURCE):
        print(f"copy mismatch: {target}")
        return 1
    print(f"wrote {target} ({target.stat().st_size} bytes, sha256 {fingerprint(target)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(hand_in())
