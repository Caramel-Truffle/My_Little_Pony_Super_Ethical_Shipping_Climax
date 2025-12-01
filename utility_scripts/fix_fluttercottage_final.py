#!/usr/bin/env python3
"""
Fix regressed violations in fluttercottage.rpy.
Re-applies creative translations but ensures no banned words are used.
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
    70: "Method query... entity-yours accomplish?",
    161: "Auditory sensation: singular combustion danger. ...Correctness query? Incidentally, entity-yours, domicile location, battery inspection mandate belonging fire-warning apparatus. Conditional removal execution, disgrace upon entity-yours. Endangerment whole neighborhood-",
    209: "Apologies Fluttershy, self-entity negation intention frighten entity-yours! Truthfulness! Regret conditional displeasure.",
    239: "Plus dyad entity embrace execution. Plus osculation. Plus entity-yours extreme laziness game termination premature, conclusion predictability extreme.",
    262: "Method query... entity-yours accomplish?",
    371: "Plus dyad entity dwelling entry, pleasant plus comfortable residence.",
    425: "Worry negation Fluttershy, self-entity certainty: singular optimal leaf-water consumption experience historical.",
    449: "Exclamation... Specific botanical specimens origin Everfree Forest, Zecora assistance selection process... Exclamation! Affirmative, female-entity vocalization: \\\"Singular superior flavor, botanical specimen omission prohibition, however consumption excess implies alternative satisfaction pursuit.\\\" Self-entity comprehension absence intended meaning...",
    467: "Entity-yours correctness. Rationale query: adorable defenseless equine pharmaceutical administration prohibition?",
    485: "Plus entity-yours consumption repetition aphrodisiac leaf-water, temporal limit...",
    497: "Self-entity concern: combination partial both. Temperature elevation location-proximal plus entity-yours excessive.",
    557: "Entity-yours probability correctness, however... singular container merely. Self-entity possession avian creatures feeding obligation, hunger state alternative...",
    575: "Temporal priority avian feeding, objection query: self-entity donation certain botanical specimens utilization infusion preparation? Flavor quality exceptional.",
    599: "Entity-yours vocalization omission: permission negation alternative equine consumption quantity increase...",
    611: "Subsequently female-entity avian nourishment activity, vocalization: entity-yours probability negation capability location discovery temporal subsequent sun-cycle.",
    653: "Plus dyad entity container consumption, Fluttershy donation sufficient botanical nutrition avian collective plus recollection: alternative task execution priority avian nourishment, lunar-influenced specialty...",
    665: "Entity-yours dwelling return execution. Previous temporal instance Fluttershy visual contact, female-entity seed donation plus waiting request. Possibility preparation completion current?",
    683: "Exclamation... Affirmative... Apologies...",
    695: "Dyad entity forest boundary arrival. Conditional Fluttershy guidance absence plus solo movement, entity-yours location discovery capability negation.",
    719: "Entity-yours imitation initiation, quality maximum.",
    743: "[playername2!t]? Literature consumption recent quality affirmative?",
    749: "Affirmative, self-entity book consumption completion!",
    256: "--Fluttershy Conclusion Primary--",
    532: "--Fluttershy Conclusion Secondary--",
    400: "Affirmative-affirmative-affirmative-lokey!",
}

fix_file('game/tl/Engrish/Scripts/fluttercottage.rpy', flutter_fixes)
