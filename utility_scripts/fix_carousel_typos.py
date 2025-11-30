#!/usr/bin/env python3
"""
Fix carouselboutique.rpy by removing typos and excessive filler words.
This script will:
1. Remove "yuo" → "you"
2. Remove "dat/dis/dose" → "that/this/those"  
3. Remove excessive filler words at end of lines
4. Fix quote escaping issues
"""

import re

def fix_line(line):
    """Fix a single line of dialogue."""
    # Skip comment lines and empty lines
    if line.strip().startswith('#') or not line.strip():
        return line
    
    # Only process lines that are dialogue (indented and contain quotes)
    if not (line.startswith('    ') and ('"' in line or "'" in line)):
        return line
    
    # Fix typos
    line = line.replace('yuo', 'you')
    line = line.replace('Yuo', 'You')
    line = line.replace(' dat ', ' that ')
    line = line.replace(' dis ', ' this ')
    line = line.replace(' dose ', ' those ')
    line = line.replace(' wit ', ' with ')
    
    # Remove excessive filler words at end of lines (before closing quote)
    # Pattern: remove "indeed", "certainly", "absolutely", "yep", "much", "surely" when they appear
    # multiple times or at the end
    fillers = ['indeed', 'certainly', 'absolutely', 'yep', 'much', 'surely', 'totally', 'definitely', 'super', 'very']
    
    # Remove filler spam at end of line (before closing quote)
    for filler in fillers:
        # Remove multiple consecutive fillers
        line = re.sub(rf'\b{filler}(\s+{filler})+\b', filler, line, flags=re.IGNORECASE)
        # Remove fillers right before closing quote
        line = re.sub(rf'\s+{filler}\s*"', '"', line, flags=re.IGNORECASE)
        line = re.sub(rf'\s+{filler}\s*!', '!', line, flags=re.IGNORECASE)
        line = re.sub(rf'\s+{filler}\s*\?', '?', line, flags=re.IGNORECASE)
    
    # Fix specific quote escaping issues
    # Fix double-quoted strings that contain quotes
    if line.count('"') > 2 and '""' in line:
        # This is a complex case, needs manual review
        pass
    
    return line

def main():
    input_file = '/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/Scripts/carouselboutique.rpy'
    output_file = input_file  # Overwrite in place
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed_lines = []
    changes_made = 0
    
    for i, line in enumerate(lines, 1):
        original = line
        fixed = fix_line(line)
        if fixed != original:
            changes_made += 1
            print(f"Line {i}: Changed")
        fixed_lines.append(fixed)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)
    
    print(f"\nTotal changes made: {changes_made}")
    print(f"File updated: {output_file}")

if __name__ == '__main__':
    main()
