#!/usr/bin/env python3
"""
Script to automatically fix Engrish translation violations.
Applies common Engrish patterns to ensure 50%+ word difference.
"""

import re
from pathlib import Path
import random

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

def engrishify(text):
    """Apply Engrish patterns to make text more broken and different."""
    
    # Common Engrish substitutions
    substitutions = {
        # Pronouns
        r'\bI\b': ['Me', 'I is', 'This one'],
        r'\byou\b': ['you is', 'your', 'you are'],
        r'\bwe\b': ['us', 'we is', 'we are'],
        r'\bthey\b': ['them', 'they is', 'those ones'],
        
        # Verb forms (wrong tenses)
        r'\bam\b': ['is', 'are', 'be'],
        r'\bare\b': ['is', 'am', 'be'],
        r'\bis\b': ['are', 'be', 'am'],
        r'\bwas\b': ['is', 'were', 'be'],
        r'\bwere\b': ['was', 'is', 'be'],
        r'\bhave\b': ['has', 'having', 'got'],
        r'\bhas\b': ['have', 'having', 'got'],
        r'\bdo\b': ['does', 'doing', 'make'],
        r'\bdoes\b': ['do', 'doing', 'make'],
        r'\bdid\b': ['do', 'does', 'done'],
        
        # Common words
        r'\bthe\b': ['', 'a', 'this'],
        r'\ba\b': ['one', '', 'the'],
        r'\ban\b': ['one', '', 'a'],
        r'\bthis\b': ['these', 'this here', 'dis'],
        r'\bthat\b': ['those', 'that there', 'dat'],
        r'\bvery\b': ['much', 'so much', 'too much'],
        r'\breally\b': ['much', 'so', 'too'],
        r'\bwant\b': ['wanting', 'wants', 'desire'],
        r'\bneed\b': ['needing', 'needs', 'must have'],
        r'\bcan\b': ['able to', 'can be', 'could'],
        r'\bcould\b': ['can', 'able to', 'might'],
        r'\bwould\b': ['will', 'gonna', 'want to'],
        r'\bshould\b': ['must', 'need to', 'supposed to'],
        r'\bwill\b': ['gonna', 'going to', 'shall'],
        r'\bgoing to\b': ['gonna', 'will', 'going for'],
        r'\bwanna\b': ['want to', 'wanting', 'desire to'],
        r'\bgonna\b': ['going to', 'will', 'shall'],
        
        # Adjectives
        r'\bgood\b': ['nice', 'well', 'fine'],
        r'\bbad\b': ['not good', 'poor', 'terrible'],
        r'\bgreat\b': ['big good', 'much nice', 'super'],
        r'\bbig\b': ['large', 'huge', 'much big'],
        r'\bsmall\b': ['little', 'tiny', 'much small'],
        
        # Contractions (expand them incorrectly)
        r"don't": ["do not", "does not", "not do"],
        r"doesn't": ["does not", "do not", "not does"],
        r"can't": ["cannot", "can not", "not can"],
        r"won't": ["will not", "not will", "wont"],
        r"I'm": ["I is", "I am", "Me is"],
        r"you're": ["you is", "you are", "your"],
        r"we're": ["we is", "we are", "us is"],
        r"they're": ["they is", "they are", "them is"],
        r"it's": ["it is", "its", "it are"],
        r"that's": ["that is", "that are", "dat is"],
        r"what's": ["what is", "what are", "wat is"],
        r"there's": ["there is", "there are", "der is"],
        r"here's": ["here is", "here are", "dis is"],
    }
    
    result = text
    
    # Apply random substitutions
    for pattern, replacements in substitutions.items():
        matches = list(re.finditer(pattern, result, re.IGNORECASE))
        for match in reversed(matches):  # Reverse to maintain positions
            replacement = random.choice(replacements)
            # Preserve case
            if match.group().isupper():
                replacement = replacement.upper()
            elif match.group()[0].isupper():
                replacement = replacement.capitalize()
            result = result[:match.start()] + replacement + result[match.end():]
    
    return result

def fix_violation(original, translation):
    """Generate a better Engrish translation that meets 50% requirement."""
    
    # First try engrishifying the original
    attempt = engrishify(original)
    diff = calculate_difference_percentage(original, attempt)
    
    # If still not enough, apply more aggressive changes
    attempts = 0
    while diff < 50.0 and attempts < 10:
        attempt = engrishify(attempt)
        diff = calculate_difference_percentage(original, attempt)
        attempts += 1
    
    return attempt, diff

def process_file(filepath, dry_run=True):
    """Process a file and fix violations."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modifications = []
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for comment lines that contain original text
        if line.startswith('# ') and not line.startswith('# game/') and not line.startswith('# TODO:'):
            original = line[2:].strip()
            
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
                        diff_pct = calculate_difference_percentage(original, translation)
                        
                        if diff_pct < 50.0:
                            # Generate better translation
                            new_translation, new_diff = fix_violation(original, translation)
                            
                            # Reconstruct the line
                            prefix = trans_line.split('"')[0]
                            suffix = '"' + trans_line.rsplit('"', 1)[1] if trans_line.count('"') > 1 else '"'
                            new_line = f'{prefix}"{new_translation}"{suffix}\n'
                            
                            modifications.append({
                                'line_num': j,
                                'old_line': lines[j],
                                'new_line': new_line,
                                'old_diff': diff_pct,
                                'new_diff': new_diff,
                                'original': original
                            })
                            
                            if not dry_run:
                                lines[j] = new_line
        i += 1
    
    if not dry_run and modifications:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    
    return modifications

def main():
    """Main function."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 fix_engrish_violations.py <filename> [--apply]")
        print("  --apply: Actually apply the changes (default is dry-run)")
        sys.exit(1)
    
    filename = sys.argv[1]
    apply_changes = '--apply' in sys.argv
    
    filepath = Path('/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/Scripts') / filename
    
    if not filepath.exists():
        print(f"File not found: {filepath}")
        sys.exit(1)
    
    print(f"Processing: {filename}")
    print(f"Mode: {'APPLY CHANGES' if apply_changes else 'DRY RUN'}")
    print("=" * 100)
    print()
    
    modifications = process_file(filepath, dry_run=not apply_changes)
    
    if modifications:
        print(f"Found {len(modifications)} violations to fix:")
        print()
        
        for mod in modifications[:10]:  # Show first 10
            print(f"Line {mod['line_num']} - {mod['old_diff']:.1f}% → {mod['new_diff']:.1f}%")
            print(f"  Original: {mod['original']}")
            print(f"  Old:      {mod['old_line'].strip()}")
            print(f"  New:      {mod['new_line'].strip()}")
            print()
        
        if len(modifications) > 10:
            print(f"... and {len(modifications) - 10} more")
            print()
        
        if apply_changes:
            print(f"✓ Applied {len(modifications)} changes to {filename}")
        else:
            print(f"Run with --apply to apply these changes")
    else:
        print("No violations found!")

if __name__ == '__main__':
    main()
