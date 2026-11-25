#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261125.

Copies the pre-rendered entry.png (next to this file) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png), byte for byte,
so two runs write identical bytes. Standard library only; no network.

The image is a 1024x1024 'THE WORLD IN ONE DAY' newspaper front page
summing up Wednesday 25 November 2026's world news: China launching the
first Pakistani to orbit; Asia stocks tumbling on the US tariff threat;
the Gaza death toll reaching 74,746; Australia signing the Solomons
defence pact; the CIA/ODNI cyber breach; Australian inflation; oil
sliding; Russia's own data showing 490,334 war dead; the WHO fleeing a
Congo Ebola hospital; Huawei's guilty verdict; Houthis hitting Riyadh's
tallest tower; Senegal keeping the AFCON crown; plus a 12-item
date-flagged tail list and a DATE CHECK box (12 of the 24 stories stem
from Tue 24 Nov and are flagged [24 Nov], never presented as 25 Nov
events). Same proven format as the 23 Nov entry (round 3 rank
219/13,031, top 1.7%).
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if not os.path.isfile(SRC):
        print(f"error: source image not found: {SRC}", file=sys.stderr)
        return 1
    with open(SRC, "rb") as f:
        if f.read(len(PNG_MAGIC)) != PNG_MAGIC:
            print(f"error: source is not a PNG file: {SRC}", file=sys.stderr)
            return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    if _sha256(dst) != _sha256(SRC):
        print(f"error: copy verification failed: {dst}", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes, sha256 {_sha256(dst)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
