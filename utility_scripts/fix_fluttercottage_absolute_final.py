#!/usr/bin/env python3
"""
Fix final 14 violations in fluttercottage.rpy.
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
    754: "Entity-yours visual presentation: literature object Twilight donation.",
    766: "Negation singular entity-yours...",
    802: "Identity [playername!t], entity-yours persuasion attempt initiation.",
    844: "Collective-entity... Knowledge possession... Silence characteristic shared... Plus knowledge regarding quiet entity reputation...",
    868: "Self-entity certainty: collective-entity commonality magnitude extreme...",
    886: "Specificity: singular item. Certainty: self-entity fetish preference ranking superior...",
    892: "Squeak! Self-entity thought: censorship application avoidance mature rating classification!",
    940: "G-Gratitude expression.",
    1006: "Logic deduction: translation empty-handed rationality absence.",
    1024: "Entity-yours presentation literature object.",
    1036: "Memory retention requirement: forest entity singular...",
    1060: "Departure intention, entity-yours solitude state, similarity book equine... Visual contact future immediate!",
    1084: "Return movement Fluttershy, thought impurity intrusion mind, affirmative... Concealment tree posterior, observation poor unsuspecting equine, whisper volume sufficient auditory reception.",
    1222: "Proximity accuracy partial, however burning sensation persistence. Concept: equine abandonment, official entry \"new age\", ancient project termination method: pony dream destruction explosive, similarity Bronycon. Exploitation negation.",
}

fix_file('game/tl/Engrish/Scripts/fluttercottage.rpy', flutter_fixes)
