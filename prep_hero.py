#!/usr/bin/env python3
"""Prepare the supplied editorial illustration for the newspaper hero slot."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent
SOURCE = Path(
    "/home/hatch/workspace/makefun/news-image-art/"
    "media-generation-crimea-bridge-editorial-b-0-"
    "3d70e66f-553a-438a-817f-745d55f7a119.png"
)
OUTPUT = ROOT / "assets" / "hero.jpg"


def main():
    with Image.open(SOURCE) as source:
        hero = source.crop((86, 560, 1836, 1085)).convert("RGB")
    hero = hero.resize((1920, 576), Image.Resampling.LANCZOS)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    hero.save(OUTPUT, format="JPEG", quality=88)
    print(f"Prepared {OUTPUT.name}: 1920x576, {OUTPUT.stat().st_size} bytes")


if __name__ == "__main__":
    main()
