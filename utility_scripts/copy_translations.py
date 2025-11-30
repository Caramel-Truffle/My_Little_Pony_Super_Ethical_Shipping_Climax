#!/usr/bin/env python3
"""
Script to copy 'old' values to 'new' values in Ren'Py translation files.
This is useful for English "proofreading" where we just want to keep the original text.
"""
import re
import sys

def copy_old_to_new(filepath):
    """Read a translation file and copy all 'old' values to empty 'new' values."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match: old "..." followed by new ""
    # We need to handle multiline strings and escaped quotes
    pattern = r'(    old """.*?""")\s*\n(    new "")'
    content = re.sub(pattern, r'\1\n    new \1[8:]', content, flags=re.DOTALL)
    
    # Pattern for single-line strings
    pattern = r'(    old "([^"\\\\]|\\\\.)*")\s*\n(    new "")'
    
    def replace_func(match):
        old_line = match.group(1)
        old_value = old_line[8:]  # Remove '    old '
        return f'{old_line}\n    new {old_value}'
    
    content = re.sub(pattern, replace_func, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Processed: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python copy_translations.py <filepath>")
        sys.exit(1)
    
    copy_old_to_new(sys.argv[1])
