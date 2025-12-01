#!/usr/bin/env python3
"""
Fix final 19 violations in carouselboutique.rpy and dashcloud.rpy.
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

# Fixes for carouselboutique.rpy
carousel_fixes = {
    83: "[playername!t]! Surprise magnitude extreme!",
    143: "Erm... condition-yours functional [playername2!t]?",
    263: "Ugh... Repetition negation! Termination immediate execution!",
    293: "Why intention...? Pause. Entity-yours arrival location-proximal purpose jewel request cause dragon hunger? Consideration magnitude extreme. Self-entity donation capability affirmative, pause location-distal.",
    317: "Well. Entity-yours Pinkie Pie behavior standard, assumption. Pause location-distal.",
    377: "Pinkie vocalization probability 100%.",
    395: "Plus entity-yours return execution crossroad, comprehension initiation regarding 4th wall destruction sensation.",
    497: "Enjoyment!",
    563: "Greeting repetition Rarity! Design process active?",
    677: "Oh! Literature consumption regarding topic recent?",
    821: "Negation, deviant player, negation...",
    989: "Return greeting [playername!t]! Leaf-water preparation completion. Scent divinity!",
    1007: "Divinity confirmed, ma chère. Superiority Hoity Toity intimate fragrance. ... Knowledge absence self-entity.",
    1043: "......",
    1049: "Consciousness restoration final?",
    1139: "--Rarity Conclusion Veracious--",
    1145: "Entity-yours arrival Carousel Boutique. Door lock negation plus entity-yours theft capability rubies alternatively sapphires, however wisdom negation.",
}

# Fixes for dashcloud.rpy
dashcloud_fixes = {
    885: "Allons-y! (Forward movement!)",
    975: "Impact sound.",
}

fix_file('game/tl/Engrish/Scripts/carouselboutique.rpy', carousel_fixes)
fix_file('game/tl/Engrish/Scripts/dashcloud.rpy', dashcloud_fixes)
