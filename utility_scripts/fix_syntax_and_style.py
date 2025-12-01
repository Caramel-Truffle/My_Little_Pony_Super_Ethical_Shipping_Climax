#!/usr/bin/env python3
"""
Comprehensive fix for syntax errors and style violations in Engrish translations.
1. Fixes double quotes: ""..."" -> "..."
2. Fixes indentation: Ensures 4 spaces for dialogue lines
3. Fixes style: Removes banned words (dat, dis, yuo, dose)
"""

import re
import os

def fix_line(line):
    # Skip comments and empty lines
    if not line.strip() or line.strip().startswith('#'):
        return line

    # Check if it's a dialogue line (contains quotes)
    if '"' in line:
        # Fix indentation
        stripped = line.strip()
        indent = '    '
        
        # Handle character prefixes
        if stripped.startswith('"'):
            # Narrator line
            content = stripped
            prefix = ''
        else:
            # Character line
            parts = stripped.split(' "', 1)
            if len(parts) == 2:
                prefix = parts[0] + ' '
                content = '"' + parts[1]
            else:
                return line # Unknown format
        
        # Fix double quotes
        if content.startswith('""') and content.endswith('""'):
            content = content[1:-1]
        
        # Fix style violations in content
        # We only want to replace whole words, case-insensitive
        
        # Helper to replace word in string
        def replace_word(text, target, replacement):
            pattern = re.compile(r'\b' + re.escape(target) + r'\b', re.IGNORECASE)
            return pattern.sub(replacement, text)
            
        content = replace_word(content, 'yuo', 'you')
        content = replace_word(content, 'dat', 'that')
        content = replace_word(content, 'dis', 'this')
        content = replace_word(content, 'dose', 'those')
        
        # Reconstruct line
        return indent + prefix + content + '\n'
        
    return line

def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    changes = 0
    
    for line in lines:
        new_line = fix_line(line)
        if new_line != line:
            changes += 1
        new_lines.append(new_line)
        
    if changes > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"  Fixed {changes} lines")

def main():
    base_dir = 'game/tl/Engrish/Scripts'
    for filename in os.listdir(base_dir):
        if filename.endswith('.rpy'):
            process_file(os.path.join(base_dir, filename))

if __name__ == '__main__':
    main()
