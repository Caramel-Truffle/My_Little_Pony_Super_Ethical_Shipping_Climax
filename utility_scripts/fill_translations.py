#!/usr/bin/env python3
"""
Script to fill in translations for Ren'Py translation files.
This script reads .rpy files from tl directories and fills in empty OR untranslated strings.
"""

import os
import re
import random
from pathlib import Path

# Base directory
BASE_DIR = Path("/home/user/AI/antigravity/MLP_SESC/game")
TL_DIR = BASE_DIR / "tl"

def extract_original_text(comment_line):
    """Extract the original text from a comment line."""
    # Match patterns like: # y "text here"
    match = re.search(r'#\s+\w+\s+"(.+)"', comment_line)
    if match:
        return match.group(1)
    # Match patterns like: # "text here"
    match = re.search(r'#\s+"(.+)"', comment_line)
    if match:
        return match.group(1)
    return None

def process_file(filepath, language):
    """Process a single translation file."""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modified = False
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for dialogue translations
        # Pattern: character "translation"
        dialogue_match = re.match(r'(\s+)(\w+)\s+"(.*)"', line)
        if dialogue_match:
            indent = dialogue_match.group(1)
            speaker = dialogue_match.group(2)
            current_trans = dialogue_match.group(3)
            
            # Look back for the comment with original text
            if i > 0:
                # Search backwards for the comment line, skipping empty lines or other comments
                j = i - 1
                original_text = None
                while j >= 0:
                    if lines[j].strip().startswith('#') and not lines[j].strip().startswith('# game/') and not lines[j].strip().startswith('# translate'):
                        original_text = extract_original_text(lines[j])
                        if original_text:
                            break
                    if lines[j].strip().startswith('translate'): # Stop if we hit the start of the block
                        break
                    j -= 1
                
                if original_text:
                    # Check if empty OR identical to original (untranslated)
                    # Note: We strip whitespace to be safe
                    if current_trans.strip() == "" or current_trans == original_text:
                        # Translate based on language
                        translated = translate_text(original_text, language)
                        
                        # Only update if translation is different
                        if translated != current_trans:
                            lines[i] = f'{indent}{speaker} "{translated}"\n'
                            modified = True
                            # print(f"    Translated dialogue: {original_text[:20]}... -> {translated[:20]}...")

        # Check for string translations
        # Pattern: new "translation"
        elif "new" in line and '"' in line:
            new_match = re.search(r'new\s+"([^"]*)"', line)
            if new_match:
                indent_match = re.match(r'(\s*)new', line)
                indent = indent_match.group(1) if indent_match else ""
                
                current_trans = new_match.group(1)
                
                # Look back for the "old" line
                if i > 0:
                    j = i - 1
                    original_text = None
                    
                    while j >= 0:
                        old_match = re.search(r'old\s+"([^"]*)"', lines[j])
                        if old_match:
                            original_text = old_match.group(1)
                            break
                        if lines[j].strip() == "": # Stop at empty line
                            break
                        j -= 1
                    
                    if original_text:
                        # Check if empty OR identical (untranslated)
                        if current_trans.strip() == "" or current_trans == original_text:
                            translated = translate_text(original_text, language)
                            
                            # Force a change if translation logic returned same text
                            if translated == current_trans and language == "engrish":
                                translated = translated + " yes"
                            
                            if translated != current_trans:
                                lines[i] = f'{indent}new "{translated}"\n'
                                modified = True
        
        i += 1
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"  ✓ Updated {filepath}")
    else:
        print(f"  - No changes needed for {filepath}")

def translate_text(text, language):
    """Translate text based on language."""
    if language == "english":
        return text
    elif language == "french":
        return translate_to_french(text)
    elif language == "engrish":
        return translate_to_engrish(text)
    elif language == "tabarnak":
        return translate_to_tabarnak(text)
    return text

def translate_to_french(text):
    """Basic French translation dictionary."""
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
        "Clipboard voicing enabled. ": "Vocalisation du presse-papiers activée. ",
        "Self-voicing enabled. ": "Auto-vocalisation activée. ",
        "Enter Sync ID": "Entrer ID de Synchro",
        "Sync Success": "Synchro Réussie",
        "Sync Error": "Erreur Synchro",
        "Continue": "Continuer",
        "Monday": "Lundi",
        "Tuesday": "Mardi",
        "Wednesday": "Mercredi",
        "Thursday": "Jeudi",
        "Friday": "Vendredi",
        "Saturday": "Samedi",
        "Sunday": "Dimanche",
        "January": "Janvier",
        "February": "Février",
        "March": "Mars",
        "April": "Avril",
        "May": "Mai",
        "June": "Juin",
        "July": "Juillet",
        "August": "Août",
        "September": "Septembre",
        "October": "Octobre",
        "November": "Novembre",
        "December": "Décembre",
    }
    
    # Check exact match first
    if text in map_fr:
        return map_fr[text]
        
    # Handle variables
    if "[text]" in text:
        return text.replace("Language", "Langue").replace("Slot", "Emplacement").replace("Page", "Page")
        
    return text # Fallback to original if not found

def translate_to_engrish(text):
    """
    Broken English translation.
    """
    if text.strip() == "":
        return ""
        
    # Don't translate if it looks like a variable only or special string
    if text.startswith("[") and text.endswith("]"):
        return text
    if text.startswith("{#"): # Date formatting
        return text

    # Word replacements
    replacements = {
        "the": "da",
        "The": "Da",
        "is": "is being",
        "are": "are being",
        "you": "yuo",
        "your": "yuo's",
        "to": "for",
        "of": "ov",
        "have": "haz",
        "this": "dis",
        "that": "dat",
        "with": "wit",
        "for": "four",
        "not": "not", # Keep simple
        "will": "will be",
        "can": "can be",
        "please": "plz",
        "menu": "list-thing",
        "game": "play-thing",
        "save": "keep-safe",
        "load": "bring-back",
        "settings": "fix-options",
        "preferences": "like-things",
        "help": "halp",
        "quit": "stop now",
        "return": "go back",
        "back": "go back",
        "history": "old words",
        "skip": "fast forward",
        "auto": "self-go",
        "sound": "noise",
        "music": "song",
        "voice": "talk-sound",
        "volume": "loudness",
        "display": "look-screen",
        "window": "box",
        "fullscreen": "big screen",
        "language": "speak-way",
        "text": "word",
        "speed": "fastness",
        "after": "later than",
        "before": "sooner than",
        "delete": "destroy",
        "confirm": "say yes",
        "continue": "go more",
        "start": "begin start",
        "about": "what is",
        "yes": "ya",
        "no": "nay",
        "ok": "okey",
        "cancel": "stop it",
        "Self-voicing": "Me-talk",
        "disabled": "no work",
        "enabled": "work good",
        "Clipboard": "Copy-place",
    }
    
    # Split by spaces to preserve variables
    words = text.split(' ')
    new_words = []
    
    for word in words:
        # Check if it's a variable or tag
        if '[' in word or '{' in word or '%' in word:
            new_words.append(word)
            continue
            
        # Remove punctuation for lookup
        clean_word = re.sub(r'[^\w]', '', word)
        
        if clean_word in replacements:
            # Replace and keep punctuation if possible (simple approach)
            replacement = replacements[clean_word]
            if word.endswith('.'): replacement += '.'
            elif word.endswith(','): replacement += ','
            elif word.endswith('?'): replacement += '?'
            elif word.endswith('!'): replacement += '!'
            new_words.append(replacement)
        else:
            # Randomly modify other words
            if len(word) > 4 and random.random() < 0.3:
                new_words.append(word.upper())
            else:
                new_words.append(word)
    
    # Add random intensifier
    intensifiers = [" very much", " super", " big time", " indeed", " yes"]
    if random.random() < 0.5 and not text.endswith("]"): # Increased chance
        result = " ".join(new_words) + random.choice(intensifiers)
    else:
        result = " ".join(new_words)
        
    return result

def translate_to_tabarnak(text):
    """Quebec French with colloquialisms."""
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
    }
    
    if text in map_qc:
        return map_qc[text]
        
    if "[text]" in text:
        return text.replace("Language", "Langue").replace("Slot", "Slot").replace("Page", "Page")
        
    return text # Fallback

def main():
    """Main function to process all translation files."""
    # Map directory name to internal language ID
    languages = {
        "Engrish": "engrish", 
        "TABARNAK": "tabarnak", 
        "French": "french"
    }
    
    for dir_name, lang_id in languages.items():
        # 1. Process Scripts directory
        lang_dir = TL_DIR / dir_name / "Scripts"
        if lang_dir.exists():
            print(f"\n=== Processing {dir_name} Scripts ===")
            for rpy_file in lang_dir.glob("*.rpy"):
                process_file(rpy_file, lang_id)
        else:
            print(f"Directory not found: {lang_dir}")
        
        # 2. Process common.rpy
        common_file = TL_DIR / dir_name / "common.rpy"
        if common_file.exists():
            print(f"\n=== Processing {dir_name} common.rpy ===")
            process_file(common_file, lang_id)
        else:
            print(f"File not found: {common_file}")

if __name__ == "__main__":
    main()
