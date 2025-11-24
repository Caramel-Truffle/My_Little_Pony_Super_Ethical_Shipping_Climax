#!/usr/bin/env python3
"""
Grammar and typo checker for English translation files
"""

import re
from pathlib import Path

# Common grammar issues to check
grammar_issues = []

def check_file(filepath):
    """Check a single file for grammar issues"""
    issues = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line_num, line in enumerate(lines, 1):
        # Skip comments and empty lines
        if line.strip().startswith('#') or not line.strip():
            continue
        
        # Check for common grammar errors
        
        # "what happen" should be "what happens"
        if re.search(r'\bwhat happen\b', line, re.IGNORECASE):
            issues.append({
                'file': filepath.name,
                'line': line_num,
                'issue': '"what happen" should be "what happens"',
                'text': line.strip()
            })
        
        # "and and" (duplicate word)
        if re.search(r'\band and\b', line):
            issues.append({
                'file': filepath.name,
                'line': line_num,
                'issue': 'Duplicate word "and and"',
                'text': line.strip()
            })
        
        # "you too are" should be "you two are"
        if re.search(r'\byou too are\b', line, re.IGNORECASE):
            issues.append({
                'file': filepath.name,
                'line': line_num,
                'issue': '"you too are" should be "you two are" (referring to two people)',
                'text': line.strip()
            })
        
        # "this is your" at start of sentence should be capitalized
        if re.search(r'^\s*".*\bthis is your\b', line) and not re.search(r'^\s*".*\bThis is your\b', line):
            issues.append({
                'file': filepath.name,
                'line': line_num,
                'issue': 'Sentence should start with capital letter',
                'text': line.strip()
            })
        
        # "didn' do well" should be "didn't do too well" or "didn't do well"
        if re.search(r"didn' do well", line):
            issues.append({
                'file': filepath.name,
                'line': line_num,
                'issue': '"didn\' do well" should be "didn\'t do too well"',
                'text': line.strip()
            })
    
    return issues

def main():
    english_dir = Path('/home/user/AI/antigravity/MLP_SESC/game/tl/English/Scripts')
    
    all_issues = []
    
    print("=" * 80)
    print("GRAMMAR AND TYPO CHECK - ENGLISH TRANSLATION FILES")
    print("=" * 80)
    print()
    
    for rpy_file in sorted(english_dir.glob('*.rpy')):
        issues = check_file(rpy_file)
        if issues:
            all_issues.extend(issues)
    
    if all_issues:
        print(f"Found {len(all_issues)} potential grammar/typo issues:\n")
        
        for issue in all_issues:
            print(f"File: {issue['file']}")
            print(f"Line: {issue['line']}")
            print(f"Issue: {issue['issue']}")
            print(f"Text: {issue['text']}")
            print()
    else:
        print("No obvious grammar issues found!")
    
    print("=" * 80)
    print("CHECK COMPLETE")
    print("=" * 80)

if __name__ == '__main__':
    main()
