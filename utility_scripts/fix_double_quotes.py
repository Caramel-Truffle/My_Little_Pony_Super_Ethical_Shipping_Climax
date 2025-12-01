#!/usr/bin/env python3
"""
Fix double quotes in dialogue lines.
Ensures lines start and end with exactly one quote.
"""

import re
import os

def fix_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    changes = 0
    new_lines = []
    
    for line in lines:
        stripped = line.strip()
        # Check if it's a dialogue line (starts with quote or char name + quote)
        if not stripped or stripped.startswith('#'):
            new_lines.append(line)
            continue
            
        # Identify indentation
        indent = line[:len(line) - len(line.lstrip())]
        
        # Check for narrator lines starting with multiple quotes
        if stripped.startswith('""'):
            # It's likely a narrator line with double quotes
            # Remove all leading quotes and add one back
            content = stripped.lstrip('"')
            # Remove all trailing quotes and add one back
            content = content.rstrip('"')
            
            new_line = f'{indent}"{content}"\n'
            if new_line != line:
                changes += 1
                print(f"  Fixed: {stripped} -> {new_line.strip()}")
            new_lines.append(new_line)
            
        # Check for character lines: char "..."
        elif ' "' in stripped:
            parts = stripped.split(' "', 1)
            if len(parts) == 2:
                prefix = parts[0]
                content_part = parts[1]
                
                if content_part.startswith('"'):
                    # It has double quotes at start of content
                    content = content_part.lstrip('"')
                    content = content.rstrip('"')
                    
                    new_line = f'{indent}{prefix} "{content}"\n'
                    if new_line != line:
                        changes += 1
                        print(f"  Fixed: {stripped} -> {new_line.strip()}")
                    new_lines.append(new_line)
                else:
                    new_lines.append(line)
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
