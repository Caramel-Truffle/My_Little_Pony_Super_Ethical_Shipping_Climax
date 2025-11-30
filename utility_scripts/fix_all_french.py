
import re
import os
from pathlib import Path

TL_DIR = Path("/home/user/AI/antigravity/MLP_SESC/game/tl/French")

def translate_to_french(text):
    if text.strip() == "": return ""
    if text.startswith("[") and text.endswith("]"): return text
    
    # Common UI terms
    map_fr = {
        "History": "Historique",
        "Skip": "Sauter",
        "Auto": "Auto",
        "Save": "Sauvegarder",
        "Load": "Charger",
        "Settings": "Préférences",
        "Preferences": "Préférences",
        "Return": "Retour",
        "Back": "Retour",
        "About": "À propos",
        "Help": "Aide",
        "Quit": "Quitter",
        "Start": "Commencer",
        "Main Menu": "Menu Principal",
        "Yes": "Oui",
        "No": "Non",
        "Ok": "Ok",
        "Cancel": "Annuler",
        "Music Volume": "Volume Musique",
        "Sound Volume": "Volume Sons",
        "Voice Volume": "Volume Voix",
        "Mute All": "Tout Muet",
        "Display": "Affichage",
        "Window": "Fenêtre",
        "Fullscreen": "Plein écran",
        "Language": "Langue",
        "Text Speed": "Vitesse du texte",
        "Auto-Forward Time": "Avance automatique",
        "Self-voicing disabled.": "Auto-vocalisation désactivée.",
        "Clipboard voicing enabled.": "Vocalisation du presse-papiers activée.",
        "Self-voicing enabled.": "Auto-vocalisation activée.",
        "Enter Sync ID": "Entrer ID de Synchro",
        "Sync Success": "Synchro Réussie",
        "Sync Error": "Erreur Synchro",
        "Continue": "Continuer",
        "Are you sure?": "Êtes-vous sûr ?",
        "Are you sure you want to quit?": "Êtes-vous sûr de vouloir quitter ?",
        "Delete": "Supprimer",
        "Empty Slot": "Vide",
        "Test": "Test",
        "Left": "Gauche",
        "Right": "Droite",
        "Up": "Haut",
        "Down": "Bas",
        "Select": "Sélectionner",
        "Previous": "Précédent",
        "Next": "Suivant",
        "Eeyup": "Vui",
        "Nope": "Nan",
        "\"Eeyup.\"": "\"Vui.\"",
        "\"Nope.\"": "\"Nan.\"",
    }
    
    if text in map_fr:
        return map_fr[text]
        
    if "[text]" in text:
        return text.replace("Language", "Langue").replace("Slot", "Emplacement").replace("Page", "Page")
    
    return text

def process_file(filepath):
    print(f"Processing {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    last_old = None
    modified_count = 0
    
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
                    translated = translate_to_french(last_old)
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
