#!/usr/bin/env python3
"""Copy the prepared newspaper image to the competition output directory."""

import os
from pathlib import Path
import shutil


def main():
    source = Path(__file__).resolve().parent / "assets" / "entry.png"
    source_size = source.stat().st_size
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    copied_size = destination.stat().st_size
    if copied_size != source_size:
        raise OSError(f"Copy size mismatch: expected {source_size}, got {copied_size}")
    print(f"Copied entry.png: {copied_size} bytes verified.")


if __name__ == "__main__":
    main()
