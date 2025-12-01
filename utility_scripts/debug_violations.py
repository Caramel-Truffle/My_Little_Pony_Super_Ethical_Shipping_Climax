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

def check_file(filepath):
    print(f"\nChecking {filepath}...")
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
                        diff = calculate_difference_percentage(original, translation)
                        if diff < 50.0:
                            print(f"Line {j+1}: {diff:.1f}%")
                            print(f"Orig:  {original}")
                            print(f"Trans: {translation}")
        i += 1

check_file('game/tl/Engrish/Scripts/carouselboutique.rpy')
check_file('game/tl/Engrish/Scripts/dashcloud.rpy')
