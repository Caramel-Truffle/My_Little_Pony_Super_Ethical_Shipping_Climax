#!/usr/bin/env python3
"""
Spanish AI Placeholder Extractor
Extracts the source English text for all Spanish AI placeholder lines
"""

import os
import re

SPANISH_AI_LOCATIONS = {
    'game/tl/Spanish/Scripts/carouselboutique.rpy': [1009],
    'game/tl/Spanish/Scripts/library.rpy': [805, 919, 925, 1267],
    'game/tl/Spanish/Scripts/applebarn.rpy': [127, 145, 223, 1261],
    'game/tl/Spanish/Scripts/sugarcubecorner.rpy': [823, 1207],
    'game/tl/Spanish/Scripts/script.rpy': [31],
    'game/tl/Spanish/Scripts/fluttercottage.rpy': [1075, 1111],
}

def extract_source_from_comment(lines, line_idx):
    """Extract source English text from comment above translation"""
    for i in range(line_idx - 1, max(0, line_idx - 10), -1):
        line = lines[i].strip()
        if line.startswith('#') and '"' in line:
            # Extract text from comment
            matches = re.findall(r'"((?:[^"\\]|\\.)*)"', line)
            if matches:
                return matches[-1]
    return None

def main():
    print("=" * 80)
    print("SPANISH AI PLACEHOLDER LINES - TRANSLATION NEEDED")
    print("=" * 80)
    print()
    
    total_found = 0
    
    for filepath, line_numbers in SPANISH_AI_LOCATIONS.items():
        if not os.path.exists(filepath):
            print(f"⚠ WARNING: {filepath} not found\n")
            continue
        
        print(f"\n📄 FILE: {filepath}")
        print("-" * 80)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line_num in line_numbers:
            idx = line_num - 1
            if idx >= len(lines):
                continue
            
            line = lines[idx]
            if 'translate it into' in line.lower() or 'please provide' in line.lower():
                source_text = extract_source_from_comment(lines, idx)
                
                # Extract character name if present
                char_match = re.match(r'\s+(\w+)\s+"', line)
                char = char_match.group(1) if char_match else "Narrator"
                
                print(f"\nLine {line_num} ({char}):")
                print(f"  English: \"{source_text}\"")
                print(f"  Current: {line.strip()}")
                print(f"  → Needs Spanish translation")
                
                total_found += 1
    
    print("\n" + "=" * 80)
    print(f"SUMMARY: Found {total_found} lines needing translation")
    print("=" * 80)
    print("\nTo fix these:")
    print("1. Open each file listed above")
    print("2. Go to the line number indicated")
    print("3. Replace the AI message with a proper Spanish translation")
    print("4. Use neutral Latin American Spanish")
    print("5. Maintain the same character/narrator format")
    print("\nExample fix:")
    print('  Before: p "Please provide the text..."')
    print('  After:  p "¡Hola! ¿Cómo estás?"')
    print()

if __name__ == "__main__":
    main()
