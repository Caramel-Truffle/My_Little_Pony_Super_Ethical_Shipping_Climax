#!/usr/bin/env python3
"""
Script to check Engrish translations for 50% word difference requirement.
Identifies translations that don't meet the threshold.
"""

import re
from pathlib import Path

def normalize_word(word):
    """Normalize a word for comparison (lowercase, remove punctuation)."""
    return re.sub(r'[^\w]', '', word.lower())

def calculate_difference_percentage(original, translation):
    """Calculate percentage of different words between original and translation."""
    # Normalize and split into words
    orig_words = [normalize_word(w) for w in original.split() if normalize_word(w)]
    trans_words = [normalize_word(w) for w in translation.split() if normalize_word(w)]
    
    if not trans_words:
        return 0.0
    
    # Count how many translation words are NOT in original
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
        
        # Look for comment lines with original text
        if line.startswith('# ') and not line.startswith('# game/') and not line.startswith('# TODO:'):
            original = line[2:].strip()
            
            # Check if next non-empty line is the translation
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            
            if j < len(lines):
                trans_line = lines[j].strip()
                
                # Extract the actual translation text (after character name if present)
                if '"' in trans_line:
                    # Handle lines like: p "translation text"
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

# Check fluttercottage.rpy as example
filepath = Path('/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/Scripts/fluttercottage.rpy')
issues = check_rpy_file(filepath)

print(f"Found {len(issues)} translations below 50% difference in {filepath.name}:")
print()

for issue in issues[:20]:  # Show first 20
    print(f"Line {issue['line']}: {issue['difference_pct']:.1f}% different")
    print(f"  Original:    {issue['original']}")
    print(f"  Translation: {issue['translation']}")
    print()
