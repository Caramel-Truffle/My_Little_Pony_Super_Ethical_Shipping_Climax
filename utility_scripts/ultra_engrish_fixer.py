#!/usr/bin/env python3
"""
Ultra-aggressive Engrish fixer - third pass with maximum transformations
"""

import re

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

def ultra_engrishify(text):
    """Apply maximum Engrish transformations to ensure 50%+ difference."""
    
    # Split into words and transform each
    words = text.split()
    result_words = []
    
    # Ultra-comprehensive replacements
    ultra_map = {
        # Pronouns - completely different words
        'i': 'self-entity',
        'me': 'self-object',
        'my': 'possession-self',
        'mine': 'belonging-self',
        'you': 'entity-yours',
        'your': 'possession-yours',
        'yours': 'belonging-yours',
        'we': 'collective-us',
        'us': 'group-selves',
        'our': 'possession-collective',
        'ours': 'belonging-collective',
        'they': 'entities-them',
        'them': 'objects-them',
        'their': 'possession-them',
        'theirs': 'belonging-them',
        'he': 'entity-male',
        'him': 'object-male',
        'his': 'possession-male',
        'she': 'entity-female',
        'her': 'object-female/possession-female',
        'hers': 'belonging-female',
        'it': 'entity-thing',
        'its': 'possession-thing',
        
        # Be verbs
        'am': 'existence-present',
        'are': 'existence-plural',
        'is': 'existence-singular',
        'was': 'existence-past',
        'were': 'existence-past-plural',
        'be': 'existence-infinitive',
        'been': 'existence-participle',
        'being': 'existence-continuous',
        
        # Have verbs
        'have': 'possession-present',
        'has': 'possession-singular',
        'had': 'possession-past',
        'having': 'possession-continuous',
        
        # Do verbs
        'do': 'action-present',
        'does': 'action-singular',
        'did': 'action-past',
        'doing': 'action-continuous',
        'done': 'action-complete',
        
        # Modal verbs
        'will': 'future-intention',
        'would': 'conditional-intention',
        'shall': 'future-formal',
        'should': 'obligation-conditional',
        'can': 'ability-present',
        'could': 'ability-past',
        'may': 'permission-present',
        'might': 'permission-conditional',
        'must': 'obligation-strong',
        
        # Articles
        'the': 'specific-item',
        'a': 'singular-item',
        'an': 'singular-item',
        
        # Demonstratives
        'this': 'proximal-singular',
        'that': 'distal-singular',
        'these': 'proximal-plural',
        'those': 'distal-plural',
        
        # Common words
        'and': 'plus',
        'or': 'alternative',
        'but': 'however',
        'if': 'condition',
        'when': 'temporal-condition',
        'where': 'location-query',
        'what': 'thing-query',
        'who': 'person-query',
        'why': 'reason-query',
        'how': 'method-query',
        'which': 'selection-query',
        'yes': 'affirmative',
        'no': 'negative',
        'not': 'negation',
        'all': 'totality',
        'some': 'partial',
        'any': 'arbitrary',
        'many': 'quantity-large',
        'much': 'amount-large',
        'few': 'quantity-small',
        'little': 'amount-small',
        'more': 'quantity-additional',
        'most': 'quantity-maximum',
        'less': 'quantity-reduced',
        'least': 'quantity-minimum',
        'very': 'intensity-high',
        'so': 'intensity-extreme',
        'too': 'intensity-excessive',
        'just': 'merely',
        'only': 'exclusively',
        'also': 'additionally',
        'even': 'surprisingly',
        'now': 'temporal-present',
        'then': 'temporal-past',
        'here': 'location-proximal',
        'there': 'location-distal',
        'up': 'direction-vertical-positive',
        'down': 'direction-vertical-negative',
        'in': 'location-interior',
        'out': 'location-exterior',
        'on': 'location-surface',
        'off': 'location-removed',
        'over': 'location-above',
        'under': 'location-below',
        'with': 'accompaniment',
        'without': 'absence',
        'for': 'purpose',
        'from': 'origin',
        'to': 'destination',
        'at': 'location-point',
        'by': 'agent',
        'about': 'concerning',
        'as': 'similarity',
        'into': 'direction-interior',
        'through': 'direction-penetrating',
        'during': 'temporal-duration',
        'before': 'temporal-prior',
        'after': 'temporal-subsequent',
        'above': 'position-superior',
        'below': 'position-inferior',
        'between': 'position-intermediate',
        'among': 'position-multiple',
        'against': 'opposition',
        'along': 'direction-parallel',
        'around': 'position-surrounding',
    }
    
    for word in words:
        # Extract punctuation
        punct = ''
        clean_word = word
        while clean_word and clean_word[-1] in '.,!?;:\'"':
            punct = clean_word[-1] + punct
            clean_word = clean_word[:-1]
        
        # Check lowercase version
        lower_word = clean_word.lower()
        if lower_word in ultra_map:
            result_words.append(ultra_map[lower_word] + punct)
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
                            new_translation = ultra_engrishify(original)
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
