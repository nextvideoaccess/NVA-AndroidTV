#!/usr/bin/env python3
"""Render owner-supplied SVGs to native Android PNG resources, without redrawing branding."""
from pathlib import Path
import cairosvg

root = Path(__file__).resolve().parents[2]
src = root / "app/src/main/branding"
dst = root / "app/src/main/res/drawable-nodpi"
dst.mkdir(parents=True, exist_ok=True)
for name, target, size in [
    ("nva_tv_banner.svg", "nva_tv_banner.png", 640),
    ("nva_android_icon.svg", "nva_android_icon.png", 512),
    ("nva_splash.svg", "nva_splash_brand.png", 512),
]:
    cairosvg.svg2png(url=str(src / name), write_to=str(dst / target), output_width=size,
                    output_height=(360 if "banner" in target else 512))
    print(f"Rendered {target}")
