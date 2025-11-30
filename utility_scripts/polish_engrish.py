
import re
import os
from pathlib import Path

TL_DIR = Path("/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish")

def polish_engrish(text):
    replacements = {
        "Apple barn": "Red Fruit House",
        "Carousel Boutique": "Spinny Dress Shop",
        "Fluttershy's cottage": "Quiet Animal House",
        "Library": "Book Place",
        "Sugar Cube Corner": "Sweet Square Corner",
        "Sugarcube Corner": "Sweet Square Corner",
        "Rainbow's cloud": "Color Sky Fluff",
        "I want none of these choices!": "I want no pick dis!",
        "I want you": "I want yuo!",
        "Wait": "Hold on",
        "Space": "Big Empty",
        "English": "Word-Speak",
        "French": "Baguette-Speak",
        "TABARNAK": "Angry-Speak",
        "Engrish": "Broken-Speak",
        "Yes": "Ya",
        "No": "Nay",
        "Ok": "Okey",
        "Cancel": "Stop it",
        "Back": "Go back",
        "Return": "Go back",
        "Help": "Halp",
        "About": "What is",
        "Quit": "Stop now",
        "Start": "Begin start",
        "Load": "Bring-back",
        "Save": "Keep-safe",
        "Settings": "Fix-options",
        "Preferences": "Like-things",
        "History": "Old words",
        "Skip": "Fast forward",
        "Auto": "Self-go",
        "Sound": "Noise",
        "Music": "Song",
        "Voice": "Talk-sound",
        "Volume": "Loudness",
        "Display": "Look-screen",
        "Window": "Box",
        "Fullscreen": "Big screen",
        "Language": "Speak-way",
        "Text Speed": "Word fastness",
        "Auto-Forward Time": "Self-go time",
    }
    
    if text in replacements:
        return replacements[text]
        
    return text

def process_file(filepath):
    print(f"Processing {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    modified_count = 0
    
    for i, line in enumerate(lines):
        # Check for new "..."
        new_match = re.search(r'^(\s+)new\s+"([^"]*)"', line)
        if new_match:
            indent = new_match.group(1)
            current_trans = new_match.group(2)
            
            polished = polish_engrish(current_trans)
            if polished != current_trans:
                new_line = f'{indent}new "{polished}"\n'
                new_lines.append(new_line)
                modified_count += 1
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    if modified_count > 0:
        print(f"  Polished {modified_count} lines")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

# Process all files
if TL_DIR.exists():
    # common.rpy
    common_file = TL_DIR / "common.rpy"
    if common_file.exists():
        process_file(common_file)
        
    # Scripts
    scripts_dir = TL_DIR / "Scripts"
    if scripts_dir.exists():
        for rpy_file in scripts_dir.glob("*.rpy"):
            process_file(rpy_file)
