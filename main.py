#!/usr/bin/env python3
"""Deliver the finished front page for the 25 November news-image entry.

The picture itself is drawn ahead of time (see BUILD.md: 45 verified
stories, rendered by render3.py into entry.png next to this file). This
program has exactly one responsibility: place that exact file where the
grader expects it, and prove the copy is identical. It reads nothing
else, reaches no network, and uses only the standard library, so running
it twice always produces the same bytes.
"""

import os
import sys
from hashlib import sha256
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
IMAGE_NAME = "entry.png"
HERE = Path(__file__).resolve().parent
PICTURE = HERE / IMAGE_NAME
READ_SIZE = 65536


def sha256_of(path):
    """Hex digest of a file's bytes, streamed in blocks."""
    digest = sha256()
    with open(path, "rb") as stream:
        while True:
            chunk = stream.read(READ_SIZE)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def looks_like_png(path):
    """True when the file starts with the 8-byte PNG signature."""
    try:
        with open(path, "rb") as stream:
            return stream.read(len(PNG_SIGNATURE)) == PNG_SIGNATURE
    except OSError:
        return False


def place_entry():
    """Copy PICTURE into the grader's output directory, verified."""
    if not PICTURE.is_file():
        print(f"entry image missing: {PICTURE}", file=sys.stderr)
        return 1
    if not looks_like_png(PICTURE):
        print(f"entry image is not a PNG: {PICTURE}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"cannot create output directory {out_dir}: {exc}", file=sys.stderr)
        return 1
    destination = out_dir / IMAGE_NAME
    try:
        with open(PICTURE, "rb") as source, open(destination, "wb") as target:
            while True:
                chunk = source.read(READ_SIZE)
                if not chunk:
                    break
                target.write(chunk)
    except OSError as exc:
        print(f"copy failed: {exc}", file=sys.stderr)
        return 1
    if sha256_of(destination) != sha256_of(PICTURE):
        print(f"copy mismatch: {destination}", file=sys.stderr)
        return 1
    size = destination.stat().st_size
    print(f"wrote {destination} ({size} bytes, sha256 {sha256_of(destination)})")
    return 0


def main():
    return place_entry()


if __name__ == "__main__":
    raise SystemExit(main())
