#!/usr/bin/env python3
"""
Fix Translation Issues Script
Automatically fixes identified translation problems
"""

import os
import re

# Define fixes for each issue
FIXES = {
    # French empty translation
    ('game/tl/French/Scripts/fluttercottage.rpy', 665): {
        'old': '    ""',
        'new': '    "Tu es de retour à la chaumière. La dernière fois que tu as vu Fluttershy, elle t'a donné des graines et t'a demandé d'attendre. Peut-être qu'elle est prête maintenant ?"'
    },
    
    # TABARNAK identical translations - "Eeyup" and "Nope" are intentionally identical (character speech)
    # These are Big Mac's signature words and should remain unchanged
    
    # French identical translations - same as TABARNAK, these are Big Mac's words
    
    # Telenovela identical - checking these
    # Spanish AI content - these need manual review of source
}

# Map of line numbers to source files for Spanish AI content fixes
SPANISH_AI_FIXES = {
    '/home/user/AI/antigravity/MLP_SESC/game/tl/Spanish/Scripts/carouselboutique.rpy': [1009],
    '/home/user/AI/antigravity/MLP_SESC/game/tl/Spanish/Scripts/library.rpy': [805, 919, 925, 1267],
    '/home/user/AI/antigravity/MLP_SESC/game/tl/Spanish/Scripts/applebarn.rpy': [127, 145, 223, 1261],
    '/home/user/AI/antigravity/MLP_SESC/game/tl/Spanish/Scripts/sugarcubecorner.rpy': [823, 1207],
    '/home/user/AI/antigravity/MLP_SESC/game/tl/Spanish/Scripts/script.rpy': [31],
    '/home/user/AI/antigravity/MLP_SESC/game/tl/Spanish/Scripts/fluttercottage.rpy': [1075, 1111],
}

def get_source_text_from_comment(lines, line_idx):
    """Extract source text from comment above translation"""
    # Look backwards for comment with source
    for i in range(line_idx - 1, max(0, line_idx - 10), -1):
        line = lines[i].strip()
        if line.startswith('#') and '"' in line:
            # Extract text from comment
            matches = re.findall(r'"((?:[^"\\]|\\.)*)"', line)
            if matches:
                return matches[-1]
    return None

def fix_spanish_ai_content():
    """Fix Spanish AI placeholder content"""
    print("Fixing Spanish AI content...")
    
    for filepath, line_numbers in SPANISH_AI_FIXES.items():
        if not os.path.exists(filepath):
            print(f"  Warning: {filepath} not found")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Get corresponding source file
        source_file = filepath.replace('/tl/Spanish/', '/').replace('game/', 'game/Scripts/')
        
        if not os.path.exists(source_file):
            print(f"  Warning: Source file {source_file} not found")
            continue
        
        with open(source_file, 'r', encoding='utf-8') as f:
            source_lines = f.readlines()
        
        modified = False
        for line_num in line_numbers:
            idx = line_num - 1
            if idx >= len(lines):
                continue
                
            line = lines[idx]
            if 'translate it into' in line.lower():
                # Try to get source from comment
                source_text = get_source_text_from_comment(lines, idx)
                
                if source_text:
                    # For now, mark for manual review
                    # We can't auto-translate without knowing context
                    print(f"  Line {line_num}: Found AI placeholder, source: {source_text[:50]}...")
                    # Replace with source as placeholder (better than AI message)
                    indent = len(line) - len(line.lstrip())
                    char_match = re.match(r'(\s+)(\w+)\s+"', line)
                    if char_match:
                        char = char_match.group(2)
                        lines[idx] = f'{" " * indent}{char} "[NEEDS TRANSLATION: {source_text}]"\n'
                        modified = True
                    else:
                        lines[idx] = f'{" " * indent}"[NEEDS TRANSLATION: {source_text}]"\n'
                        modified = True
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            print(f"  Fixed {filepath}")

def fix_french_empty():
    """Fix French empty translation"""
    print("Fixing French empty translation...")
    filepath = '/home/user/AI/antigravity/MLP_SESC/game/tl/French/Scripts/fluttercottage.rpy'
    
    if not os.path.exists(filepath):
        print(f"  Warning: {filepath} not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Line 665 (index 664)
    if len(lines) > 664:
        if lines[664].strip() == '""':
            lines[664] = '    "Tu es de retour à la chaumière. La dernière fois que tu as vu Fluttershy, elle t'a donné des graines et t'a demandé d'attendre. Peut-être qu'elle est prête maintenant ?"\n'
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            print(f"  Fixed empty translation at line 665")

def main():
    print("=" * 80)
    print("FIXING TRANSLATION ISSUES")
    print("=" * 80)
    print()
    
    fix_french_empty()
    fix_spanish_ai_content()
    
    print("\n" + "=" * 80)
    print("NOTES:")
    print("=" * 80)
    print("1. 'Eeyup' and 'Nope' are Big Mac's signature words - identical across")
    print("   languages is INTENTIONAL and correct.")
    print("2. Spanish AI content has been marked with [NEEDS TRANSLATION: ...]")
    print("   These require manual translation based on context.")
    print("3. Asset issues with [prefix_] are Ren'Py template variables - NOT missing files.")
    print("4. Case sensitivity issues (images/menu.png vs Images/menu.png) may cause")
    print("   problems on Linux but work on case-insensitive filesystems.")
    print("=" * 80)

if __name__ == "__main__":
    main()
