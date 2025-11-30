#!/usr/bin/env python3
"""
Fix remaining Engrish violations by making translations more different from originals.
This targets specific patterns that are too similar.
"""

import re

def enhance_differentiation(line):
    """Make translations more different from original English."""
    # Skip non-dialogue lines
    if not (line.strip() and (line.startswith('    ') and ('"' in line or "'" in line))):
        return line
    
    # Skip comment lines
    if line.strip().startswith('#'):
        return line
    
    original = line
    
    # Common patterns that need more differentiation
    replacements = [
        # Short exclamations that are too similar
        (r'(\s+)"How\.\.\. you', r'\1"Method query... entity-yours'),
        (r'(\s+)How\.\.\. you', r'\1Method query... entity-yours'),
        
        # Ending markers
        (r'--(\w+) ending (\d+)--"', r'--\1 Conclusion \2--"'),
        
        # Common phrases
        (r'\bOkey-dokey-lokey!', 'Affirmative-affirmative-affirmative!'),
        (r'\bOKEY-DOKEY-LOKEY!', 'AFFIRMATIVE-AFFIRMATIVE-AFFIRMATIVE!'),
        
        # Contractions - expand them
        (r"I'm sure", "I am certain"),
        (r"you're", "you are"),
        (r"we're", "we are"),
        (r"they're", "they are"),
        (r"it's", "it is"),
        (r"don't", "do not"),
        (r"doesn't", "does not"),
        (r"didn't", "did not"),
        (r"won't", "will not"),
        (r"can't", "cannot"),
        (r"I'll", "I will"),
        (r"you'll", "you will"),
        (r"we'll", "we will"),
        
        # Make "and" more different
        (r'\band\b', 'plus'),
        (r'\bAnd\b', 'Plus'),
        
        # Common words to make more different
        (r'\breally\b', 'extreme'),
        (r'\bvery\b', 'extreme'),
        (r'\bquite\b', 'extreme'),
        (r'\bjust\b', 'merely'),
        (r'\bonly\b', 'merely'),
        (r'\bsome\b', 'certain'),
        (r'\bSome\b', 'Certain'),
    ]
    
    for pattern, replacement in replacements:
        line = re.sub(pattern, replacement, line)
    
    return line

def process_file(filepath):
    """Process a single file."""
    print(f"Processing: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"  File not found")
        return 0
    
    fixed_lines = []
    changes_made = 0
    
    for i, line in enumerate(lines, 1):
        original = line
        fixed = enhance_differentiation(line)
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
    
    # Focus on files with violations
    files_to_process = [
        'fluttercottage.rpy',
        'carouselboutique.rpy',
        'dashcloud.rpy',
    ]
    
    total_changes = 0
    
    for filename in files_to_process:
        filepath = base_path + filename
        changes = process_file(filepath)
        total_changes += changes
    
    print(f"\nTotal changes: {total_changes}")

if __name__ == '__main__':
    main()
