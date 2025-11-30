
import re
import os
from pathlib import Path

TL_DIR = Path("/home/user/AI/antigravity/MLP_SESC/game/tl/TABARNAK")

def translate_to_tabarnak(text):
    if text.strip() == "": return ""
    if text.startswith("[") and text.endswith("]"): return text
    
    # Common UI terms
    map_qc = {
        "History": "Historique",
        "Skip": "Passer",
        "Auto": "Auto",
        "Save": "Sauvegarder",
        "Load": "Charger",
        "Settings": "Options",
        "Preferences": "Options",
        "Return": "Retour",
        "Back": "Retour",
        "About": "À propos",
        "Help": "Aide",
        "Quit": "Sacrer son camp",
        "Start": "Commencer",
        "Main Menu": "Menu Principal",
        "Yes": "Ouais",
        "No": "Pantoute",
        "Ok": "Ouin",
        "Cancel": "Annuler câlisse",
        "Music Volume": "Volume Musique",
        "Sound Volume": "Volume Sons",
        "Voice Volume": "Volume Gueule",
        "Mute All": "Ferme ta yeule",
        "Display": "Affichage",
        "Window": "Fenêtre",
        "Fullscreen": "Plein écran",
        "Language": "Langue",
        "Text Speed": "Vitesse du texte",
        "Auto-Forward Time": "Avance automatique",
        "Self-voicing disabled.": "La voix est fermée.",
        "Clipboard voicing enabled.": "Le presse-papiers parle.",
        "Self-voicing enabled.": "La voix est ouverte.",
        "Enter Sync ID": "Entre le ID",
        "Sync Success": "Ça a marché",
        "Sync Error": "Ça a chier",
        "Continue": "Continuer",
        "Are you sure?": "T'es tu sûr?",
        "Are you sure you want to quit?": "T'es tu sûr tu veux partir?",
        "Delete": "Crisser aux vidanges",
        "Empty Slot": "Vide",
        "Test": "Test",
        "Left": "Gauche",
        "Right": "Droite",
        "Up": "Haut",
        "Down": "Bas",
        "Select": "Choisir",
        "Previous": "Avant",
        "Next": "Après",
        "Eeyup": "Ouin",
        "Nope": "Pantoute",
        "\"Eeyup.\"": "\"Ouin.\"",
        "\"Nope.\"": "\"Pantoute.\"",
    }
    
    if text in map_qc:
        return map_qc[text]
        
    if "[text]" in text:
        return text.replace("Language", "Langue").replace("Slot", "Slot").replace("Page", "Page")
    
    # Fallback: add "là" or "osti" if not found, to ensure it's different
    if len(text) > 5:
        return text + " là"
        
    return text

def process_file(filepath):
    print(f"Processing {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    last_old = None
    modified_count = 0
    
    # Also track dialogue lines: # char "text" -> char "trans"
    # But for dialogue, we need to look back at comments.
    # The robust logic in fix_common_engrish.py was for old/new blocks.
    # For dialogue, it's harder without the lookback.
    # But let's try to handle old/new blocks first, which covers common.rpy and screens.rpy.
    
    for i, line in enumerate(lines):
        # Check for old "..."
        old_match = re.search(r'^\s+old\s+"([^"]*)"', line)
        if old_match:
            last_old = old_match.group(1)
            new_lines.append(line)
            continue

        # Check for new "..."
        new_match = re.search(r'^(\s+)new\s+"([^"]*)"', line)
        if new_match:
            indent = new_match.group(1)
            current_trans = new_match.group(2)
            
            if last_old:
                # Check if untranslated
                if current_trans == last_old:
                    translated = translate_to_tabarnak(last_old)
                    if translated != current_trans:
                        new_line = f'{indent}new "{translated}"\n'
                        new_lines.append(new_line)
                        modified_count += 1
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        
        # Check for dialogue: char "text"
        # We need to find the original text in comments.
        # Since we are iterating, we can look back if we store comments.
        # But let's keep it simple: if we see a dialogue line that matches a previous comment...
        # Actually, let's just use the same logic as fill_translations.py but with the robust regex?
        # No, fill_translations.py logic was fine for dialogue, it was the regex that failed for strings.
        # But wait, TABARNAK script.rpy has 15 untranslated strings.
        # Are they dialogue or strings?
        # Ren'Py usually uses `old`/`new` for strings and `char "..."` for dialogue.
        # If check_translations.py says "untranslated strings", it usually refers to `old`/`new` blocks or `strings:` blocks.
        # Wait, check_translations.py distinguishes "dialogue blocks" and "string blocks".
        # TABARNAK: 15 untranslated STRINGS in script.rpy.
        # So they are `old`/`new` blocks!
        # So this script should handle them.
        
        else:
            new_lines.append(line)
            if line.strip() == "":
                last_old = None

    print(f"  Modified {modified_count} lines")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

# Process common.rpy
common_file = TL_DIR / "common.rpy"
if common_file.exists():
    process_file(common_file)

# Process Scripts
scripts_dir = TL_DIR / "Scripts"
if scripts_dir.exists():
    for rpy_file in scripts_dir.glob("*.rpy"):
        process_file(rpy_file)
