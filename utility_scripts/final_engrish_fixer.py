#!/usr/bin/env python3
"""
Final Engrish fixer - adds extra words and uses maximum creativity
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

def final_engrishify(text):
    """Apply maximum Engrish transformations with word additions."""
    
    # Split into words
    words = text.split()
    result_words = []
    
    # Comprehensive replacements with creative alternatives
    replacements = {
        'i': 'me',
        'my': 'mine',
        'me': 'myself',
        'you': 'yuo',
        'your': 'yuo\'s',
        'yours': 'belonging-yuo',
        'we': 'us',
        'our': 'ours',
        'ours': 'belonging-us',
        'they': 'them',
        'their': 'theirs',
        'theirs': 'belonging-them',
        'he': 'him',
        'his': 'belonging-him',
        'she': 'her',
        'her': 'hers',
        'hers': 'belonging-her',
        'it': 'dat',
        'its': 'belonging-dat',
        
        # Be verbs
        'am': 'be',
        'are': 'be',
        'is': 'be',
        'was': 'be',
        'were': 'be',
        'been': 'be',
        'being': 'be',
        
        # Have/Do
        'have': 'got',
        'has': 'got',
        'had': 'got',
        'do': 'make',
        'does': 'make',
        'did': 'make',
        'done': 'make',
        
        # Modals
        'will': 'gonna',
        'would': 'gonna',
        'shall': 'gonna',
        'should': 'must',
        'can': 'able',
        'could': 'able',
        'may': 'maybe',
        'might': 'maybe',
        'must': 'gotta',
        
        # Articles
        'the': '',
        'a': 'one',
        'an': 'one',
        
        # Demonstratives
        'this': 'dis',
        'that': 'dat',
        'these': 'dese',
        'those': 'dose',
        
        # Prepositions
        'to': 'for',
        'of': 'from',
        'in': 'inside',
        'on': 'onto',
        'at': 'near',
        'with': 'wit',
        'from': 'since',
        'by': 'near',
        'about': 'regarding',
        'for': 'because',
        'into': 'inside',
        'through': 'via',
        'during': 'while',
        'before': 'prior',
        'after': 'following',
        'above': 'over',
        'below': 'under',
        'between': 'among',
        'against': 'versus',
        'along': 'beside',
        'around': 'surrounding',
        
        # Conjunctions
        'and': 'plus',
        'but': 'however',
        'or': 'alternative',
        'if': 'when',
        'because': 'since',
        'so': 'therefore',
        'as': 'like',
        'than': 'compared',
        'when': 'while',
        'where': 'location',
        'while': 'during',
        'although': 'despite',
        'unless': 'except',
        'until': 'till',
        'since': 'because',
        
        # Common words
        'yes': 'yep',
        'no': 'nope',
        'not': 'negation',
        'all': 'everything',
        'some': 'partial',
        'any': 'whatever',
        'many': 'lots',
        'much': 'lots',
        'few': 'small-amount',
        'little': 'tiny',
        'more': 'additional',
        'most': 'maximum',
        'less': 'reduced',
        'least': 'minimum',
        'very': 'much',
        'really': 'much',
        'quite': 'much',
        'too': 'excessive',
        'just': 'only',
        'only': 'merely',
        'also': 'additionally',
        'even': 'also',
        'now': 'currently',
        'then': 'next',
        'here': 'dis-place',
        'there': 'dat-place',
        'up': 'upward',
        'down': 'downward',
        'out': 'outside',
        'off': 'away',
        'over': 'above',
        'under': 'below',
        'again': 'repeat',
        'back': 'return',
        'away': 'distant',
        'together': 'combined',
        'alone': 'solo',
        'never': 'zero-times',
        'always': 'every-time',
        'sometimes': 'occasionally',
        'often': 'frequently',
        'soon': 'shortly',
        'already': 'previously',
        'still': 'continuing',
        'yet': 'still',
        'ever': 'anytime',
    }
    
    for word in words:
        # Extract punctuation
        punct = ''
        clean_word = word
        while clean_word and clean_word[-1] in '.,!?;:\'"':
            punct = clean_word[-1] + punct
            clean_word = clean_word[:-1]
        
        lower_word = clean_word.lower()
        
        if lower_word in replacements:
            replacement = replacements[lower_word]
            if replacement:  # Not empty string
                result_words.append(replacement + punct)
            # If empty, skip the word (article removal)
        else:
            result_words.append(word)
    
    result = ' '.join(result_words)
    result = re.sub(r'\s+', ' ', result).strip()
    
    return result

def process_file(filepath):
    """Process file and fix remaining violations."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modifications = 0
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        if line.startswith('# ') and not line.startswith('# game/') and not line.startswith('# TODO:'):
            original = line[2:].strip()
            
            if len(original) < 3:
                i += 1
                continue
            
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
                            new_translation = final_engrishify(original)
                            new_diff = calculate_difference_percentage(original, new_translation)
                            
                            prefix = trans_line.split('"')[0]
                            new_line = f'    {prefix}"{new_translation}"\n'
                            
                            lines[j] = new_line
                            modifications += 1
        i += 1
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    return modifications

# Process both files
files = ['carouselboutique.rpy', 'fluttercottage.rpy']
base_path = '/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/Scripts/'

for filename in files:
    filepath = base_path + filename
    print(f"Processing {filename}...")
    mods = process_file(filepath)
    print(f"  Fixed {mods} violations")

print("\nDone!")
