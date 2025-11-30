#!/usr/bin/env python3
"""
Script to check ALL Engrish translation files for 50% word difference requirement.
"""

import re
from pathlib import Path

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
        
        if line.startswith('# ') and not line.startswith('# game/') and not line.startswith('# TODO:'):
            original = line[2:].strip()
            
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            
            if j < len(lines):
                trans_line = lines[j].strip()
                
                if '"' in trans_line:
                    parts = trans_line.split('"', 1)
                    if len(parts) > 1:
                        translation = parts[1].rsplit('"', 1)[0]
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

# Check all files
files = [
    'sugarcubecorner.rpy',
    'fluttercottage.rpy',
    'library.rpy',
    'applebarn.rpy',
    'carouselboutique.rpy',
    'dashcloud.rpy',
    'other.rpy',
    'ourdoors.rpy',
    'screens.rpy',
    'script.rpy'
]

base_path = Path('/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/Scripts/')
total_issues = 0

print("=" * 80)
print("ENGRISH TRANSLATION 50% COMPLIANCE REPORT")
print("=" * 80)
print()

for filename in files:
    filepath = base_path / filename
    if filepath.exists():
        issues = check_rpy_file(filepath)
        total_issues += len(issues)
        status = "✓ COMPLETE" if len(issues) == 0 else f"✗ {len(issues)} violations"
        print(f"{filename:30s} {status}")

print()
print("=" * 80)
print(f"TOTAL VIOLATIONS REMAINING: {total_issues}")
print("=" * 80)
