#!/usr/bin/env python3
"""
Script to generate a detailed report of Engrish translation violations.
Shows each violation with line number, original text, translation, and difference percentage.
"""

import re
from pathlib import Path
import sys

def normalize_word(word):
    """Normalize a word for comparison (lowercase, remove punctuation)."""
    return re.sub(r'[^\w]', '', word.lower())

def calculate_difference_percentage(original, translation):
    """Calculate percentage of different words between original and translation."""
    orig_words = [normalize_word(w) for w in original.split() if normalize_word(w)]
    trans_words = [normalize_word(w) for w in translation.split() if normalize_word(w)]
    
    if not trans_words:
        return 0.0
    
    different_count = sum(1 for w in trans_words if w not in orig_words)
    return (different_count / len(trans_words)) * 100

def check_rpy_file(filepath):
    """Check a .rpy file for translations below 50% difference."""
    issues = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for comment lines that contain original text
        if line.startswith('# ') and not line.startswith('# game/') and not line.startswith('# TODO:'):
            # Extract original text (remove leading "# " and character tag if present)
            original = line[2:].strip()
            
            # Skip if it's just a character tag
            if len(original) < 3:
                i += 1
                continue
            
            # Find the next non-empty line (should be the translation)
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            
            if j < len(lines):
                trans_line = lines[j].strip()
                
                # Extract translation text from quotes
                if '"' in trans_line:
                    parts = trans_line.split('"', 1)
                    if len(parts) > 1:
                        translation = parts[1].rsplit('"', 1)[0]
                        
                        # Calculate difference
                        diff_pct = calculate_difference_percentage(original, translation)
                        
                        if diff_pct < 50.0:
                            issues.append({
                                'line': i + 1,
                                'original': original,
                                'translation': translation,
                                'difference_pct': diff_pct
                            })
        i += 1
    
    return issues

def main():
    """Generate detailed violation report."""
    files = [
        'fluttercottage.rpy',
        'applebarn.rpy',
        'carouselboutique.rpy',
        'dashcloud.rpy',
    ]
    
    base_path = Path('/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/Scripts/')
    
    # If a specific file is provided as argument, only check that file
    if len(sys.argv) > 1:
        files = [sys.argv[1]]
    
    total_issues = 0
    
    for filename in files:
        filepath = base_path / filename
        if not filepath.exists():
            print(f"File not found: {filepath}")
            continue
        
        issues = check_rpy_file(filepath)
        total_issues += len(issues)
        
        if issues:
            print("=" * 100)
            print(f"FILE: {filename}")
            print(f"VIOLATIONS: {len(issues)}")
            print("=" * 100)
            print()
            
            for issue in issues:
                print(f"Line {issue['line']} - Difference: {issue['difference_pct']:.1f}%")
                print(f"  Original:    {issue['original']}")
                print(f"  Translation: {issue['translation']}")
                print()
    
    print("=" * 100)
    print(f"TOTAL VIOLATIONS: {total_issues}")
    print("=" * 100)

if __name__ == '__main__':
    main()
