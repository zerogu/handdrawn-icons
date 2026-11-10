#!/usr/bin/env python3
"""Import a verified hand-drawn release bundle into the repository.

Usage:
  python scripts/import_release.py /path/to/handdrawn-icons-six-review.zip

Run from the repository root. Review the diff before pushing.
"""
from pathlib import Path
import json
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
IDS = ("agent", "translate", "code", "knowledge", "data", "security")

def main(zip_file):
    with zipfile.ZipFile(zip_file) as z:
        for name in IDS:
            for folder, suffix in (
                ("assets/hand-drawn/v1", ".webp"),
                ("sources/hand-drawn/v1", ".png"),
            ):
                rel = f"{folder}/{name}{suffix}"
                dst = ROOT / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(z.read(rel))
                print("Imported:", rel)
        rel = "preview/hand-drawn-v1.png"
        dst = ROOT / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(z.read(rel))
        print("Imported:", rel)

    manifest = ROOT / "manifest.json"
    data = json.loads(manifest.read_text(encoding="utf-8"))
    for style in data["styles"]:
        if style["id"] == "hand-drawn":
            for version in style["versions"]:
                if version["id"] == "v1":
                    for icon in version["icons"]:
                        if icon["id"] in IDS:
                            icon["available"] = True
                    version["status"] = "partial"
    manifest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Manifest updated. Please inspect assets and changes before pushing.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/import_release.py <release.zip>")
    main(sys.argv[1])
