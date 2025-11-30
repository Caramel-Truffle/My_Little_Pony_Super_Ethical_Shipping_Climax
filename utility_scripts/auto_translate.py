#!/usr/bin/env python3
"""
Comprehensive translation filler for Ren'Py translation files.
This script processes all .rpy files and fills in translations based on language.
"""

import os
import re
from pathlib import Path

# Base directory
BASE_DIR = Path("/home/user/AI/antigravity/MLP_SESC/game")
TL_DIR = BASE_DIR / "tl"

# Common translations for menu items and locations
COMMON_TRANSLATIONS = {
    "french": {
        "Library": "Bibliothèque",
        "Sugarcube Corner": "Sugarcube Corner",
        "Apple barn": "Grange aux pommes",
        "Rainbow's cloud": "Nuage de Rainbow",
        "Carousel Boutique": "Carousel Boutique",
        "Fluttershy's cottage": "Chaumière de Fluttershy",
        "Yes": "Oui",
        "No": "Non",
        "Continue": "Continuer",
        "Quit": "Quitter",
    },
    "english": {},  # English uses original text
    "engrish": {
        "Library": "Book House of Reading",
        "Sugarcube Corner": "Corner of Sugar Cube",
        "Apple barn": "Barn of Apple Fruit",
        "Rainbow's cloud": "Cloud of Rainbow Person",
        "Carousel Boutique": "Shop of Carousel Turning",
        "Fluttershy's cottage": "Small House of Fluttershy Person",
        "Yes": "Yes thing",
        "No": "Not yes",
        "Continue": "Make continuing",
        "Quit": "Make quitting",
    },
    "tabarnak": {
        "Library": "Bibliothèque",
        "Sugarcube Corner": "Sugarcube Corner",
        "Apple barn": "Grange aux pommes",
        "Rainbow's cloud": "Nuage de Rainbow",
        "Carousel Boutique": "Carousel Boutique",
        "Fluttershy's cottage": "Chaumière de Fluttershy",
        "Yes": "Oui",
        "No": "Non",
        "Continue": "Continuer",
        "Quit": "Quitter",
    },
}

def read_file(filepath):
    """Read file and return lines."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.readlines()

def write_file(filepath, lines):
    """Write lines to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def extract_comment_text(line):
    """Extract text from a comment line."""
    # Pattern: # character "text"
    match = re.search(r'#\s+\w+\s+"(.+)"', line)
    if match:
        return match.group(1)
    # Pattern: # "text"
    match = re.search(r'#\s+"(.+)"', line)
    if match:
        return match.group(1)
    return None

def process_translation_file(filepath, language):
    """Process a single translation file."""
    print(f"Processing {language}: {filepath.name}")
    
    lines = read_file(filepath)
    modified = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for empty dialogue translation
        if re.match(r'\s+\w+\s+""$', line.strip()):
            if i > 0:
                comment_line = lines[i-1]
                original_text = extract_comment_text(comment_line)
                
                if original_text:
                    match = re.match(r'(\s+)(\w+)\s+""', line)
                    if match:
                        indent = match.group(1)
                        speaker = match.group(2)
                        
                        # Translate
                        translated = translate_text(original_text, language)
                        lines[i] = f'{indent}{speaker} "{translated}"\n'
                        modified = True
        
        # Check for empty "new" string
        elif re.match(r'\s+new\s+""$', line.strip()):
            if i >= 2:
                old_line = lines[i-2]
                match = re.search(r'old\s+"(.+)"', old_line)
                if match:
                    original_text = match.group(1)
                    translated = translate_text(original_text, language)
                    
                    indent_match = re.match(r'(\s+)new\s+""', line)
                    if indent_match:
                        indent = indent_match.group(1)
                        lines[i] = f'{indent}new "{translated}"\n'
                        modified = True
        
        i += 1
    
    if modified:
        write_file(filepath, lines)
        print(f"  ✓ Updated")
    else:
        print(f"  - No changes")
    
    return modified

def translate_text(text, language):
    """Translate text based on language."""
    if language == "english":
        return text
    
    # Check common translations first
    if text in COMMON_TRANSLATIONS.get(language, {}):
        return COMMON_TRANSLATIONS[language][text]
    
    # For now, return original text for complex translations
    # These will need to be done manually or with more sophisticated logic
    return text

def main():
    """Main processing function."""
    languages = ["english", "french", "engrish", "tabarnak"]
    
    total_files = 0
    total_modified = 0
    
    for lang in languages:
        print(f"\n{'='*60}")
        print(f"Processing {lang.upper()}")
        print(f"{'='*60}")
        
        lang_dir = TL_DIR / lang / "Scripts"
        if not lang_dir.exists():
            print(f"Directory not found: {lang_dir}")
            continue
        
        for rpy_file in sorted(lang_dir.glob("*.rpy")):
            total_files += 1
            if process_translation_file(rpy_file, lang):
                total_modified += 1
    
    print(f"\n{'='*60}")
    print(f"Summary: Modified {total_modified}/{total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
