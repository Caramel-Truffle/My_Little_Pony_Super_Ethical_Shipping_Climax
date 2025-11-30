#!/usr/bin/env python3
"""
Script to remove orphan translations from Ren'Py translation files.
Reads lint.txt to identify orphan translations and removes them from the translation files.
"""

import re
import os

def parse_lint_file(lint_path):
    """Parse lint.txt and extract orphan translation information."""
    orphans = {}  # {file_path: [list of (line_number, translation_id)]}
    
    with open(lint_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all orphan translation sections
    # Pattern: game/tl/LANGUAGE/Scripts/FILENAME.rpy:
    #     * line   XXX (id TRANSLATION_ID)
    
    current_file = None
    for line in content.split('\n'):
        # Check if this is a file header
        file_match = re.match(r'^(game/tl/\S+\.rpy):$', line)
        if file_match:
            current_file = file_match.group(1)
            if current_file not in orphans:
                orphans[current_file] = []
            continue
        
        # Check if this is an orphan translation line
        orphan_match = re.match(r'^\s+\*\s+line\s+(\d+)\s+\(id\s+(\S+)\)', line)
        if orphan_match and current_file:
            line_num = int(orphan_match.group(1))
            trans_id = orphan_match.group(2)
            orphans[current_file].append((line_num, trans_id))
    
    return orphans

def remove_orphan_translations(file_path, orphan_ids):
    """Remove orphan translation blocks from a file."""
    if not os.path.exists(file_path):
        print(f"Warning: File not found: {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Convert orphan IDs to a set for faster lookup
    orphan_id_set = set(id for _, id in orphan_ids)
    
    # Find and mark lines to remove
    lines_to_remove = set()
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a translate statement
        translate_match = re.match(r'^translate\s+\w+\s+(\S+):', line)
        if translate_match:
            trans_id = translate_match.group(1)
            if trans_id in orphan_id_set:
                # Found an orphan translation block
                # Mark the comment line before it (if exists)
                start_idx = i - 1
                if start_idx >= 0 and lines[start_idx].strip().startswith('#'):
                    # Also check if there's a blank line before the comment
                    if start_idx > 0 and lines[start_idx - 1].strip() == '':
                        start_idx -= 1
                else:
                    start_idx = i
                
                # Find the end of the translation block
                # It ends after the translated text and a blank line
                end_idx = i + 1
                # Skip the blank line after translate statement
                if end_idx < len(lines) and lines[end_idx].strip() == '':
                    end_idx += 1
                # Skip the comment with original text
                if end_idx < len(lines) and lines[end_idx].strip().startswith('#'):
                    end_idx += 1
                # Skip the translated text line
                if end_idx < len(lines):
                    end_idx += 1
                # Skip the blank line after
                if end_idx < len(lines) and lines[end_idx].strip() == '':
                    end_idx += 1
                
                # Mark all lines in this block for removal
                for idx in range(start_idx, end_idx):
                    lines_to_remove.add(idx)
                
                print(f"  Removing orphan translation: {trans_id} (lines {start_idx+1}-{end_idx})")
        
        i += 1
    
    # Create new content without the marked lines
    new_lines = [line for i, line in enumerate(lines) if i not in lines_to_remove]
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"Removed {len(lines) - len(new_lines)} lines from {file_path}")
    return True

def main():
    lint_path = '/home/user/AI/antigravity/MLP_SESC/lint.txt'
    base_path = '/home/user/AI/antigravity/MLP_SESC'
    
    print("Parsing lint.txt...")
    orphans = parse_lint_file(lint_path)
    
    print(f"\nFound orphan translations in {len(orphans)} files\n")
    
    for file_path, orphan_list in orphans.items():
        if not orphan_list:
            continue
        
        full_path = os.path.join(base_path, file_path)
        print(f"\nProcessing {file_path} ({len(orphan_list)} orphans)...")
        remove_orphan_translations(full_path, orphan_list)
    
    print("\n✓ All orphan translations removed!")

if __name__ == '__main__':
    main()
