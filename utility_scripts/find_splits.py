import re
import sys

def find_split_translations(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    current_block_start = -1
    string_count = 0
    in_translate_block = False
    
    print(f"Scanning {filename}...")

    for i, line in enumerate(lines):
        line = line.strip()
        
        if line.startswith("translate Engrish"):
            if in_translate_block and string_count > 1:
                print(f"Found split translation at line {current_block_start + 1} with {string_count} strings.")
            
            in_translate_block = True
            current_block_start = i
            string_count = 0
            continue
            
        if not in_translate_block:
            continue
            
        # Check for dialogue string (starts with " or character "...)
        # Simple regex: starts with optional character identifier then string
        # Or just starts with string
        # Exclude comments
        if line.startswith("#"):
            continue
            
        if not line:
            continue
            
        # Check if line contains a string
        # This is a heuristic
        if '"' in line:
            # Check if it looks like a say statement
            # "..." or char "..."
            if re.match(r'^(\w+\s+)?".+"$', line):
                string_count += 1

    # Check last block
    if in_translate_block and string_count > 1:
        print(f"Found split translation at line {current_block_start + 1} with {string_count} strings.")

if __name__ == "__main__":
    for filename in sys.argv[1:]:
        find_split_translations(filename)
