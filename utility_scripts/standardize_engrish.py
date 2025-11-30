#!/usr/bin/env python3
"""
Standardize all Engrish translation files to script.rpy style.
- Remove typos (yuo, dat/dis/dose)
- Remove excessive filler words
- Keep technical constructions (entity-yours, self-entity, etc.)
- Spread creative vocabulary
"""

import re
import sys

# Creative vocabulary mappings to apply consistently
VOCABULARY_MAP = {
    # From applebarn.rpy - spread these to other files
    r'\bfamily\b': 'blood group',
    r'\bfamilies\b': 'blood groups',
    r'\bapple\b': 'red fruit',
    r'\bapples\b': 'red fruits',
}

def fix_line(line, filename=''):
    """Fix a single line of dialogue."""
    # Skip comment lines and empty lines
    if line.strip().startswith('#') or not line.strip():
        return line
    
    # Only process lines that are dialogue (indented and contain quotes)
    if not (line.startswith('    ') and ('"' in line or "'" in line)):
        return line
    
    original = line
    
    # Fix typos - ALWAYS do this
    line = line.replace('yuo', 'you')
    line = line.replace('Yuo', 'You')
    line = line.replace(' dat ', ' that ')
    line = line.replace(' dis ', ' this ')
    line = line.replace(' dose ', ' those ')
    line = line.replace(' wit ', ' with ')
    line = line.replace('gonna', 'going to')  # Less dialectal
    
    # Remove excessive filler words at end of lines
    fillers = ['indeed', 'certainly', 'absolutely', 'yep', 'much', 'surely', 'totally', 'definitely', 'super', 'very']
    
    for filler in fillers:
        # Remove multiple consecutive fillers
        line = re.sub(rf'\b{filler}(\s+{filler})+\b', '', line, flags=re.IGNORECASE)
        # Remove fillers right before closing punctuation
        line = re.sub(rf'\s+{filler}\s*"', '"', line, flags=re.IGNORECASE)
        line = re.sub(rf'\s+{filler}\s*!', '!', line, flags=re.IGNORECASE)
        line = re.sub(rf'\s+{filler}\s*\?', '?', line, flags=re.IGNORECASE)
        line = re.sub(rf'\s+{filler}\s*\.', '.', line, flags=re.IGNORECASE)
    
    # Clean up multiple spaces
    line = re.sub(r'  +', ' ', line)
    
    return line

def process_file(filepath):
    """Process a single file."""
    print(f"\nProcessing: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"  File not found, skipping")
        return 0
    
    fixed_lines = []
    changes_made = 0
    
    for i, line in enumerate(lines, 1):
        original = line
        fixed = fix_line(line, filepath)
        if fixed != original:
            changes_made += 1
        fixed_lines.append(fixed)
    
    if changes_made > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(fixed_lines)
        print(f"  Changes made: {changes_made}")
    else:
        print(f"  No changes needed")
    
    return changes_made

def main():
    base_path = '/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/Scripts/'
    
    files_to_process = [
        'sugarcubecorner.rpy',
        'fluttercottage.rpy',
        'library.rpy',
        'dashcloud.rpy',
        'applebarn.rpy',
        'other.rpy',
        'screens.rpy',
    ]
    
    total_changes = 0
    
    for filename in files_to_process:
        filepath = base_path + filename
        changes = process_file(filepath)
        total_changes += changes
    
    print(f"\n{'='*50}")
    print(f"Total changes across all files: {total_changes}")
    print(f"{'='*50}")

if __name__ == '__main__':
    main()
