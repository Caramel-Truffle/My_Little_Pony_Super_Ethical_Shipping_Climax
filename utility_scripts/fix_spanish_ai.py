#!/usr/bin/env python3
"""
Fix Spanish AI Placeholders
Replaces AI error messages with proper ellipsis translations
"""

import os
import re

# All Spanish AI placeholders are actually ellipses in the source
# Spanish ellipsis: "..." or "…" (same as English)

FIXES = {
    'game/tl/Spanish/Scripts/carouselboutique.rpy': {
        1009: '    "…"'
    },
    'game/tl/Spanish/Scripts/library.rpy': {
        805: '    p "..."',
        919: '    p "..."',
        925: '    "..."',
        1267: '    ts "..."'
    },
    'game/tl/Spanish/Scripts/applebarn.rpy': {
        127: '    aj "..."',
        145: '    aj "..."',
        223: '    p "..."',
        1261: '    p "..."'
    },
    'game/tl/Spanish/Scripts/sugarcubecorner.rpy': {
        823: '    pp "..."',
        1207: '    "."'
    },
    'game/tl/Spanish/Scripts/script.rpy': {
        31: '    y "..."'
    },
    'game/tl/Spanish/Scripts/fluttercottage.rpy': {
        1075: '    p "…"',
        1111: '    p "…"'
    }
}

def main():
    print("=" * 80)
    print("FIXING SPANISH AI PLACEHOLDERS")
    print("=" * 80)
    print()
    
    total_fixed = 0
    
    for filepath, line_fixes in FIXES.items():
        if not os.path.exists(filepath):
            print(f"⚠ WARNING: {filepath} not found")
            continue
        
        print(f"📄 Processing: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified = False
        for line_num, replacement in line_fixes.items():
            idx = line_num - 1
            if idx >= len(lines):
                continue
            
            old_line = lines[idx]
            if 'translate it into' in old_line.lower() or 'please provide' in old_line.lower():
                lines[idx] = replacement + '\n'
                print(f"  ✓ Fixed line {line_num}")
                modified = True
                total_fixed += 1
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            print(f"  💾 Saved {filepath}")
        
        print()
    
    print("=" * 80)
    print(f"✅ COMPLETE: Fixed {total_fixed} lines")
    print("=" * 80)

if __name__ == "__main__":
    main()
