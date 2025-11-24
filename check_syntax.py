#!/usr/bin/env python3
"""
Basic syntax checker for Ren'Py translation files
"""

import re
from pathlib import Path

def check_file(filepath):
    """Check a single file for basic syntax issues"""
    issues = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    in_translate_block = False
    
    for line_num, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # Skip comments and empty lines
        if not stripped or stripped.startswith('#'):
            continue
            
        # Check for translate block start
        if stripped.startswith('translate '):
            in_translate_block = True
            if not stripped.endswith(':'):
                issues.append({
                    'line': line_num,
                    'issue': 'Translate block missing colon',
                    'text': stripped
                })
            continue
            
        # Check for string quotes
        # Simple check: count double quotes. If odd, likely missing one.
        # Ignore escaped quotes \"
        quote_count = len(re.findall(r'(?<!\\)"', stripped))
        if quote_count % 2 != 0:
             issues.append({
                'line': line_num,
                'issue': 'Odd number of double quotes (missing quote?)',
                'text': stripped
            })
            
    return issues

def main():
    tabarnak_dir = Path('/home/user/AI/antigravity/MLP_SESC/game/tl/TABARNAK/Scripts')
    
    all_issues = []
    
    print("=" * 80)
    print("SYNTAX CHECK - TABARNAK TRANSLATION FILES")
    print("=" * 80)
    print()
    
    # Check only the recently modified files first, or all? Let's check all to be safe.
    for rpy_file in sorted(tabarnak_dir.glob('*.rpy')):
        issues = check_file(rpy_file)
        if issues:
            for issue in issues:
                issue['file'] = rpy_file.name
            all_issues.extend(issues)
    
    if all_issues:
        print(f"Found {len(all_issues)} potential syntax issues:\n")
        
        for issue in all_issues:
            print(f"File: {issue['file']}")
            print(f"Line: {issue['line']}")
            print(f"Issue: {issue['issue']}")
            print(f"Text: {issue['text']}")
            print()
    else:
        print("No obvious syntax issues found!")
    
    print("=" * 80)
    print("CHECK COMPLETE")
    print("=" * 80)

if __name__ == '__main__':
    main()
