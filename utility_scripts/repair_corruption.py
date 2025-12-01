#!/usr/bin/env python3
"""
Repair corrupted comments and fix translations in fluttercottage.rpy and carouselboutique.rpy.
"""

def repair_file(filepath, repairs):
    print(f"Repairing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    changes = 0
    for line_num, (original, translation) in repairs.items():
        # line_num is 1-based index of the COMMENT line
        idx = line_num - 1
        if idx < len(lines) - 1:
            # Restore comment
            # Preserve indentation of the comment line
            comment_line = lines[idx]
            indent = len(comment_line) - len(comment_line.lstrip())
            
            # Construct new comment line
            new_comment = ' ' * indent + '# "' + original + '"\n'
            lines[idx] = new_comment
            
            # Update translation line (next line)
            # Preserve indentation of the translation line
            trans_line = lines[idx + 1]
            trans_indent = len(trans_line) - len(trans_line.lstrip())
            
            # Check for character prefix in the OLD translation line
            stripped = trans_line.strip()
            prefix = ""
            if ' "' in stripped:
                parts = stripped.split(' "', 1)
                prefix = parts[0] + ' '
            
            # Construct new translation line
            new_trans = ' ' * trans_indent + prefix + '"' + translation + '"\n'
            lines[idx + 1] = new_trans
            
            changes += 1
            print(f"  Repaired block at line {line_num}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print(f"  Total blocks repaired: {changes}")

# Repairs for fluttercottage.rpy
flutter_repairs = {
    256: ("--Fluttershy ending 1--", "--Fluttershy Narrative Termination: Alpha--"),
    532: ("--Fluttershy ending 2--", "--Fluttershy Narrative Termination: Beta--"),
    1186: ("And a useless cameo suddenly appears!", "Addition: Useless cameo sudden manifestation!"),
    1252: ("Silence...", "Auditory void..."),
    1264: ("--Fluttershy true ending--", "--Fluttershy Narrative Termination: Veracious--"),
}

# Repairs for carouselboutique.rpy
carousel_repairs = {
    269: ("--Rarity ending 1--", "--Rarity Narrative Termination: Alpha--"),
    827: ("--Rarity ending 2--", "--Rarity Narrative Termination: Beta--"),
}

repair_file('game/tl/Engrish/Scripts/fluttercottage.rpy', flutter_repairs)
repair_file('game/tl/Engrish/Scripts/carouselboutique.rpy', carousel_repairs)
