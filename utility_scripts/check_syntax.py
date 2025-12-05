import os
import re
import sys

def check_file(filepath):
    errors = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        line_num = i + 1
        stripped = line.strip()
        
        # Skip comments and empty lines
        if not stripped or stripped.startswith('#'):
            continue

        # Check for mismatched quotes
        # This is a simple heuristic and might have false positives/negatives
        # but catches the most common "forgot to close quote" error.
        # We only care about lines that look like dialogue or string assignments.
        
        # Count double quotes, ignoring escaped ones
        # We can't easily handle all cases with regex, but let's try a simple count
        # If the line contains a string, it usually has an even number of quotes.
        # However, Ren'Py code can be complex.
        # Let's focus on lines that start with a string or a character name followed by a string.
        
        # Regex for a simple dialogue line: "Text" or Character "Text"
        # We want to find lines that have an odd number of unescaped quotes.
        
        # Remove escaped quotes for counting
        clean_line = line.replace('\\"', '')
        quote_count = clean_line.count('"')
        
        if quote_count % 2 != 0:
             # Check if it's a multi-line string (triple quotes) - rare in simple translations but possible
            if '"""' not in line:
                 errors.append(f"Line {line_num}: Odd number of quotes")

        # Check for unescaped square brackets in dialogue
        # Ren'Py uses [] for interpolation. If a translator meant to use literal brackets, they might be unescaped.
        # This is harder to detect automatically without context, but we can look for common patterns.
        # For now, let's just report if we see brackets that don't look like valid interpolation.
        # Valid: [variable], [variable!t], [variable!q]
        # Invalid: [Text] (unless 'Text' is a variable, which is hard to know)
        
        # Let's just look for empty brackets [] which are definitely wrong in some contexts or unclosed brackets
        if '[' in line and ']' not in line:
             errors.append(f"Line {line_num}: Unclosed square bracket")
        
        # Check for common copy-paste errors like double spaces after a quote (minor) or missing spaces
        
    return errors

def main():
    if len(sys.argv) < 2:
        print("Usage: python check_syntax.py <directory>")
        sys.exit(1)

    target_dir = sys.argv[1]
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith('.rpy'):
                filepath = os.path.join(root, file)
                file_errors = check_file(filepath)
                if file_errors:
                    print(f"Errors in {filepath}:")
                    for error in file_errors:
                        print(f"  {error}")

if __name__ == "__main__":
    main()
