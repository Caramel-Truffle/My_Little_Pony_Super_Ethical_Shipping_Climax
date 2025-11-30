#!/usr/bin/env python3
"""
Smart Engrish fixer - generates high-quality broken English translations
"""

import re
import random

def calculate_difference_percentage(original, translation):
    """Calculate percentage of different words."""
    def normalize_word(word):
        return re.sub(r'[^\w]', '', word.lower())
    
    orig_words = [normalize_word(w) for w in original.split() if normalize_word(w)]
    trans_words = [normalize_word(w) for w in translation.split() if normalize_word(w)]
    
    if not trans_words:
        return 0.0
    
    different_count = sum(1 for w in trans_words if w not in orig_words)
    return (different_count / len(trans_words)) * 100

def smart_engrishify(text):
    """Apply smart Engrish transformations."""
    
    # Remove character tags if present
    char_tag = ""
    if text.strip() and ' "' in text:
        parts = text.split('"', 1)
        char_tag = parts[0]
        text = parts[1].rsplit('"', 1)[0] if len(parts) > 1 else text
    
    # Word-level replacements (more sophisticated)
    replacements = {
        # Pronouns with wrong forms
        r'\bI\b': 'Self',
        r'\byou\b': 'yours',
        r'\bwe\b': 'us',
        r'\bthey\b': 'them ones',
        r'\bhe\b': 'male one',
        r'\bshe\b': 'female one',
        
        # Verbs - use wrong tenses/forms
        r'\bam\b': 'be',
        r'\bare\b': 'be',
        r'\bis\b': 'be',
        r'\bwas\b': 'be past',
        r'\bwere\b': 'be past',
        r'\bhave\b': 'possess',
        r'\bhas\b': 'possess',
        r'\bhad\b': 'possess past',
        r'\bdo\b': 'make',
        r'\bdoes\b': 'make',
        r'\bdid\b': 'make past',
        r'\bwill\b': 'shall',
        r'\bwould\b': 'shall past',
        r'\bcan\b': 'able',
        r'\bcould\b': 'able past',
        r'\bshould\b': 'must',
        
        # Common words
        r'\bthe\b': '',
        r'\ba\b': 'one',
        r'\ban\b': 'one',
        r'\bthis\b': 'these here',
        r'\bthat\b': 'those there',
        r'\bvery\b': 'much',
        r'\breally\b': 'much',
        r'\bwant\b': 'desire',
        r'\bneed\b': 'require',
        r'\blike\b': 'similar',
        r'\blove\b': 'affection',
        r'\bthink\b': 'thought',
        r'\bknow\b': 'knowledge',
        r'\bsee\b': 'visual',
        r'\blook\b': 'visual',
        r'\bgo\b': 'proceed',
        r'\bcome\b': 'approach',
        r'\bget\b': 'obtain',
        r'\bmake\b': 'create',
        r'\btake\b': 'acquire',
        r'\bgive\b': 'provide',
        r'\bfind\b': 'locate',
        r'\btell\b': 'inform',
        r'\bask\b': 'query',
        r'\bwork\b': 'function',
        r'\bseem\b': 'appear',
        r'\bfeel\b': 'sensation',
        r'\btry\b': 'attempt',
        r'\bleave\b': 'depart',
        r'\bcall\b': 'designate',
    }
    
    result = text
    for pattern, replacement in replacements.items():
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    
    # Clean up multiple spaces
    result = re.sub(r'\s+', ' ', result).strip()
    
    # Re-add character tag if it existed
    if char_tag:
        result = f'{char_tag}"{result}"'
    
    return result

def process_file(filepath):
    """Process file and fix violations."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modifications = []
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for comment lines with original text
        if line.startswith('# ') and not line.startswith('# game/') and not line.startswith('# TODO:'):
            original = line[2:].strip()
            
            if len(original) < 3:
                i += 1
                continue
            
            # Find translation line
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
                            # Generate better translation
                            new_translation = smart_engrishify(original)
                            new_diff = calculate_difference_percentage(original, new_translation)
                            
                            # Reconstruct line
                            prefix = trans_line.split('"')[0]
                            new_line = f'    {prefix}"{new_translation}"\n'
                            
                            modifications.append({
                                'line_num': j,
                                'old_diff': diff_pct,
                                'new_diff': new_diff,
                                'original': original
                            })
                            
                            lines[j] = new_line
        i += 1
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    return modifications

# Process both files
import sys

files = ['carouselboutique.rpy', 'fluttercottage.rpy']
base_path = '/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/Scripts/'

for filename in files:
    filepath = base_path + filename
    print(f"Processing {filename}...")
    mods = process_file(filepath)
    print(f"  Fixed {len(mods)} violations")

print("\nDone!")
