#!/usr/bin/env python3
"""
Fix lines with double quotes and trailing garbage.
Example: ""Sorry." yes" -> "Sorry."
"""

import re
import os

def fix_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    changes = 0
    new_lines = []
    
    # Pattern: whitespace, double quote, double quote, content, double quote, double quote, whitespace, garbage
    # We want to capture content
    pattern = re.compile(r'^(\s*)""(.*)""\s+\S+.*$')
    
    for line in lines:
        match = pattern.match(line)
        if match:
            indent = match.group(1)
            content = match.group(2)
            # Reconstruct clean line
            new_line = f'{indent}"{content}"\n'
            new_lines.append(new_line)
            changes += 1
            print(f"  Fixed: {line.strip()} -> {new_line.strip()}")
        else:
            # Also check for single quote with trailing garbage: "Text" garbage
            # But be careful not to match lines with comments or valid code
            # Pattern: whitespace, quote, content, quote, whitespace, garbage
            pattern2 = re.compile(r'^(\s*)"(.*)"\s+[^#\s].*$')
            match2 = pattern2.match(line)
            if match2:
                 # Verify it's not a valid line like 'p "Text"'
                 # If the line starts with a quote, it's a narrator line.
                 if line.strip().startswith('"'):
                     indent = match2.group(1)
                     content = match2.group(2)
                     new_line = f'{indent}"{content}"\n'
                     new_lines.append(new_line)
                     changes += 1
                     print(f"  Fixed: {line.strip()} -> {new_line.strip()}")
                 else:
                     new_lines.append(line)
            else:
                new_lines.append(line)
            
    if changes > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"  Total changes: {changes}")

def main():
    files = [
        'game/tl/Engrish/Scripts/carouselboutique.rpy',
        'game/tl/Engrish/Scripts/fluttercottage.rpy'
    ]
    
    for filename in files:
        filepath = os.path.join('/home/user/AI/antigravity/MLP_SESC', filename)
        if os.path.exists(filepath):
            fix_file(filepath)

if __name__ == '__main__':
    main()
