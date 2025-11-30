#!/usr/bin/env python3
"""
Aggressive Engrish fixer - second pass for remaining violations
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

def aggressive_engrishify(text):
    """Apply very aggressive Engrish transformations."""
    
    # Comprehensive word replacements
    replacements = {
        # Pronouns
        'I': 'Self',
        'you': 'yours',
        'your': 'possession yours',
        'we': 'us',
        'our': 'possession ours',
        'they': 'them ones',
        'their': 'possession theirs',
        'he': 'male one',
        'she': 'female one',
        'it': 'thing',
        'its': 'possession thing',
        
        # Common verbs
        'am': 'be',
        'are': 'be',
        'is': 'be',
        'was': 'be past',
        'were': 'be past',
        'have': 'possess',
        'has': 'possess',
        'had': 'possess past',
        'do': 'make',
        'does': 'make',
        'did': 'make past',
        'will': 'shall',
        'would': 'shall past',
        'can': 'able',
        'could': 'able past',
        'should': 'must',
        'may': 'might',
        'must': 'obligation',
        
        # Articles
        'the': '',
        'a': 'one',
        'an': 'one',
        
        # Demonstratives
        'this': 'these here',
        'that': 'those there',
        'these': 'plural these',
        'those': 'plural those',
        
        # Common adjectives/adverbs
        'very': 'much',
        'really': 'much',
        'quite': 'much',
        'so': 'much',
        'too': 'excessive',
        'more': 'additional',
        'most': 'maximum',
        'less': 'reduced',
        'least': 'minimum',
        'good': 'quality positive',
        'bad': 'quality negative',
        'great': 'quality excellent',
        'small': 'size tiny',
        'big': 'size large',
        'little': 'size small',
        'large': 'size big',
        
        # Common verbs (action)
        'want': 'desire',
        'need': 'require',
        'like': 'preference',
        'love': 'affection',
        'hate': 'dislike',
        'think': 'thought',
        'know': 'knowledge',
        'see': 'visual',
        'look': 'observe',
        'watch': 'observe',
        'hear': 'auditory',
        'listen': 'auditory',
        'speak': 'verbalize',
        'talk': 'verbalize',
        'say': 'state',
        'tell': 'inform',
        'ask': 'query',
        'answer': 'respond',
        'go': 'proceed',
        'come': 'approach',
        'get': 'obtain',
        'make': 'create',
        'take': 'acquire',
        'give': 'provide',
        'put': 'place',
        'bring': 'transport',
        'find': 'locate',
        'use': 'utilize',
        'work': 'function',
        'try': 'attempt',
        'help': 'assist',
        'start': 'commence',
        'stop': 'cease',
        'leave': 'depart',
        'stay': 'remain',
        'wait': 'anticipate',
        'call': 'designate',
        'feel': 'sensation',
        'seem': 'appear',
        'become': 'transform',
        'turn': 'rotate',
        'keep': 'retain',
        'let': 'permit',
        'begin': 'commence',
        'show': 'display',
        'mean': 'signify',
        'follow': 'pursue',
        'change': 'alter',
        'play': 'recreation',
        'move': 'relocate',
        'live': 'exist',
        'believe': 'faith',
        'hold': 'grasp',
        'happen': 'occur',
        'write': 'inscribe',
        'sit': 'position seated',
        'stand': 'position vertical',
        'lose': 'misplace',
        'pay': 'compensate',
        'meet': 'encounter',
        'run': 'locomotion rapid',
        'walk': 'locomotion',
        'remember': 'memory',
        'understand': 'comprehend',
        'hope': 'wish',
        'wonder': 'curiosity',
    }
    
    # Split into words
    words = text.split()
    result_words = []
    
    for word in words:
        # Check if word (case-insensitive) is in replacements
        lower_word = word.lower().strip('.,!?;:')
        if lower_word in replacements:
            # Preserve punctuation
            punct = ''
            for char in word[::-1]:
                if char in '.,!?;:':
                    punct = char + punct
                else:
                    break
            result_words.append(replacements[lower_word] + punct)
        else:
            result_words.append(word)
    
    result = ' '.join(result_words)
    
    # Clean up multiple spaces
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
                            new_translation = aggressive_engrishify(original)
                            new_diff = calculate_difference_percentage(original, new_translation)
                            
                            # Reconstruct line
                            prefix = trans_line.split('"')[0]
                            new_line = f'    {prefix}"{new_translation}"\n'
                            
                            lines[j] = new_line
                            modifications += 1
        i += 1
    
    # Write back
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
