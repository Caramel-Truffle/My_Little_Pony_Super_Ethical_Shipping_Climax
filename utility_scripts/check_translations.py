#!/usr/bin/env python3
"""
Translation Completeness Checker
Analyzes all translation files to identify missing translations
"""

import os
import re
from collections import defaultdict

# Translation directory
TL_DIR = "game/tl"

# Languages to check
LANGUAGES = ["English", "Engrish", "French", "TABARNAK"]

def analyze_file(filepath):
    """Analyze a single .rpy file for translation completeness."""
    blocks = {
        'dialogue': [],
        'strings': [],
        'untranslated_strings_list': []
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check for dialogue translations (simplified for now)
            # Pattern: translate <lang> <label>_<hash>:
            if line.strip().startswith('translate') and ':' in line:
                # This is a block start. We need to parse inside.
                # But the regex approach in original script was finding blocks by reading whole content.
                # Let's stick to line-by-line for strings, and regex for dialogue if possible.
                pass

            # Check for string translations
            # Pattern: old "original"
            #          new "translation"
            old_match = re.match(r'\s+old\s+"((?:[^"\\]|\\.)*)"', line)
            if old_match:
                original_text = old_match.group(1)
                
                # Look ahead for "new"
                if i + 1 < len(lines):
                    new_match = re.match(r'\s+new\s+"((?:[^"\\]|\\.)*)"', lines[i+1])
                    if new_match:
                        current_trans = new_match.group(1)
                        blocks['strings'].append({
                            'original': original_text,
                            'translation': current_trans
                        })
                        if current_trans == original_text:
                            blocks['untranslated_strings_list'].append(original_text)
                        i += 1 # Skip 'new' line
            i += 1
            
        # Use regex for dialogue as it's multi-line and complex
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        dialogue_pattern = r'translate\s+\w+\s+(\w+):\s*\n((?:\s+#.*\n)*)\s+(\w+)\s+"([^"]*)"'
        for match in re.finditer(dialogue_pattern, content):
            label = match.group(1)
            translation = match.group(4)
            blocks['dialogue'].append({
                'label': label,
                'text': translation,
                'is_empty': translation.strip() == ''
            })
            
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        
    return blocks

def main():
    print("=" * 80)
    print("TRANSLATION COMPLETENESS ANALYSIS")
    print("=" * 80)
    print()
    
    all_results = {}
    
    for lang in LANGUAGES:
        print(f"Analyzing {lang}...")
        
        lang_dir = os.path.join(TL_DIR, lang)
        scripts_dir = os.path.join(lang_dir, "Scripts")
        common_file = os.path.join(lang_dir, "common.rpy")
        
        current_lang_results = {
            'language': lang,
            'files': {},
            'totals': {
                'dialogue_blocks': 0,
                'dialogue_empty': 0,
                'string_blocks': 0,
                'string_empty': 0,
                'string_same': 0
            },
            'all_untranslated_strings': []
        }
        
        files_to_analyze = []
        if os.path.exists(common_file):
            files_to_analyze.append(common_file)
        if os.path.exists(scripts_dir):
            for filename in sorted(os.listdir(scripts_dir)):
                if filename.endswith('.rpy') and not filename.endswith('.rpyc'):
                    files_to_analyze.append(os.path.join(scripts_dir, filename))
        
        for filepath in files_to_analyze:
            blocks = analyze_file(filepath)
            
            empty_dialogue = sum(1 for b in blocks['dialogue'] if b['is_empty'])
            empty_strings = sum(1 for b in blocks['strings'] if b['translation'].strip() == "")
            same_strings = sum(1 for b in blocks['strings'] if b['translation'] == b['original'])
            
            relative_filepath = os.path.relpath(filepath, lang_dir)
            
            current_lang_results['files'][relative_filepath] = {
                'dialogue_total': len(blocks['dialogue']),
                'dialogue_empty': empty_dialogue,
                'string_total': len(blocks['strings']),
                'string_empty': empty_strings,
                'string_same': same_strings,
                'untranslated_strings_list': blocks['untranslated_strings_list']
            }
            
            current_lang_results['totals']['dialogue_blocks'] += len(blocks['dialogue'])
            current_lang_results['totals']['dialogue_empty'] += empty_dialogue
            current_lang_results['totals']['string_blocks'] += len(blocks['strings'])
            current_lang_results['totals']['string_empty'] += empty_strings
            current_lang_results['totals']['string_same'] += same_strings
            current_lang_results['all_untranslated_strings'].extend(blocks['untranslated_strings_list'])
            
        all_results[lang] = current_lang_results
    
    print("\n" + "=" * 80)
    print("SUMMARY BY LANGUAGE")
    print("=" * 80)
    
    for lang, results in all_results.items():
        print(f"\n{lang}:")
        print(f"  Total dialogue blocks: {results['totals']['dialogue_blocks']}")
        print(f"  Empty dialogue blocks: {results['totals']['dialogue_empty']}")
        print(f"  Total string blocks: {results['totals']['string_blocks']}")
        print(f"  Empty string blocks: {results['totals']['string_empty']}")
        print(f"  Untranslated strings (same as original): {results['totals']['string_same']}")
        
        # Calculate percentages
        if results['totals']['dialogue_blocks'] > 0:
            dialogue_pct = (results['totals']['dialogue_empty'] / results['totals']['dialogue_blocks']) * 100
            print(f"  Dialogue completion: {100 - dialogue_pct:.1f}%")
        
        if results['totals']['string_blocks'] > 0:
            string_pct = (results['totals']['string_empty'] / results['totals']['string_blocks']) * 100
            print(f"  String completion: {100 - string_pct:.1f}%")
    
    # Write detailed report
    with open('translation_analysis_report.txt', 'w', encoding='utf-8') as f:
        f.write("TRANSLATION COMPLETENESS ANALYSIS REPORT\n")
        f.write("=" * 80 + "\n\n")
        
        for lang, results in all_results.items():
            f.write(f"\n{lang}\n")
            f.write("-" * 80 + "\n")
            f.write(f"Total dialogue blocks: {results['totals']['dialogue_blocks']}\n")
            f.write(f"Empty dialogue blocks: {results['totals']['dialogue_empty']}\n")
            f.write(f"Total string blocks: {results['totals']['string_blocks']}\n")
            f.write(f"Empty string blocks: {results['totals']['string_empty']}\n")
            f.write(f"Untranslated strings: {results['totals']['string_same']}\n\n")
            
            f.write("Files with issues:\n")
            for filename, stats in sorted(results['files'].items()):
                if stats['dialogue_empty'] > 0 or stats['string_empty'] > 0 or stats['string_same'] > 0:
                    f.write(f"  {filename}:\n")
                    if stats['dialogue_empty'] > 0:
                        f.write(f"    - {stats['dialogue_empty']} empty dialogue blocks\n")
                    if stats['string_empty'] > 0:
                        f.write(f"    - {stats['string_empty']} empty string blocks\n")
                    if stats['string_same'] > 0:
                        f.write(f"    - {stats['string_same']} untranslated strings\n")
            f.write("\n")
            
    # Write untranslated strings to a separate file
    with open("untranslated_strings.txt", "w", encoding="utf-8") as f_unt:
        for lang, results in all_results.items():
            f_unt.write(f"\n=== {lang} ===\n")
            if results["all_untranslated_strings"]:
                for s in sorted(list(set(results["all_untranslated_strings"]))):
                    f_unt.write(f"{s}\n")
    
    print("\n" + "=" * 80)
    print("Report saved to: translation_analysis_report.txt")
    print("Untranslated strings saved to: untranslated_strings.txt")
    print("=" * 80)

if __name__ == "__main__":
    main()
