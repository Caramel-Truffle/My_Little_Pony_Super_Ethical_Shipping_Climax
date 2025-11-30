#!/usr/bin/env python3
import re
from pathlib import Path

def normalize_word(word):
    return re.sub(r'[^\w]', '', word.lower())

def calculate_difference_percentage(original, translation):
    orig_words = [normalize_word(w) for w in original.split() if normalize_word(w)]
    trans_words = [normalize_word(w) for w in translation.split() if normalize_word(w)]
    if not trans_words:
        return 0.0
    different_count = sum(1 for w in trans_words if w not in orig_words)
    return (different_count / len(trans_words)) * 100

def check_rpy_file(filepath):
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
                            issues.append({'line': i + 1, 'original': original, 'translation': translation, 'difference_pct': diff_pct})
        i += 1
    return issues

filepath = Path('/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/Scripts/sugarcubecorner.rpy')
issues = check_rpy_file(filepath)
print(f"Found {len(issues)} violations in sugarcubecorner.rpy:")
print()
for issue in issues[:30]:  # Show first 30
    print(f"Line {issue['line']}: {issue['difference_pct']:.1f}% different")
    print(f"  Original:    {issue['original']}")
    print(f"  Translation: {issue['translation']}")
    print()
