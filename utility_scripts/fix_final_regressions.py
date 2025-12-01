#!/usr/bin/env python3
"""
Fix final 7 violations in fluttercottage.rpy and carouselboutique.rpy.
"""

def fix_file(filepath, fixes):
    print(f"Fixing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    changes = 0
    for line_num, new_text in fixes.items():
        # line_num is 1-based
        idx = line_num - 1
        if idx < len(lines):
            # Preserve indentation
            original_line = lines[idx]
            indent = len(original_line) - len(original_line.lstrip())
            
            # Check if it has a character prefix
            stripped = original_line.strip()
            prefix = ""
            if ' "' in stripped:
                parts = stripped.split(' "', 1)
                prefix = parts[0] + ' '
            
            new_line = ' ' * indent + prefix + '"' + new_text + '"\n'
            lines[idx] = new_line
            changes += 1
            print(f"  Line {line_num} fixed")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print(f"  Total changes: {changes}")

# Fixes for fluttercottage.rpy
flutter_fixes = {
    256: "--Fluttershy Narrative Termination: Alpha--",
    532: "--Fluttershy Narrative Termination: Beta--",
    1186: "Addition: Useless cameo sudden manifestation!",
    1252: "Auditory void...",
    1264: "--Fluttershy Narrative Termination: Veracious--",
}

# Fixes for carouselboutique.rpy
carousel_fixes = {
    269: "--Rarity Narrative Termination: Alpha--",
    827: "--Rarity Narrative Termination: Beta--",
}

fix_file('game/tl/Engrish/Scripts/fluttercottage.rpy', flutter_fixes)
fix_file('game/tl/Engrish/Scripts/carouselboutique.rpy', carousel_fixes)
