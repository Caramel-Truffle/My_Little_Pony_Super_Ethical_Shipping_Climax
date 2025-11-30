
import os
from pathlib import Path

BASE_DIR = Path("/home/user/AI/antigravity/MLP_SESC/game")
TL_DIR = BASE_DIR / "tl"

print(f"Checking {TL_DIR}")
if TL_DIR.exists():
    print("TL_DIR exists")
    for lang in ["engrish", "tabarnak", "french"]:
        lang_dir = TL_DIR / lang / "Scripts"
        print(f"Checking {lang_dir}")
        if lang_dir.exists():
            print(f"  Found {lang_dir}")
            files = list(lang_dir.glob("*.rpy"))
            print(f"  Found {len(files)} rpy files")
        else:
            print(f"  NOT FOUND: {lang_dir}")
else:
    print("TL_DIR NOT FOUND")
