import os
import re
import sys

def is_likely_english(text):
    # Common English words that are distinct from Spanish
    english_words = {
        "the", "and", "is", "are", "to", "of", "in", "that", "have", "it", 
        "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", 
        "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", 
        "an", "will", "my", "one", "all", "would", "there", "their", "what",
        "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
        "please", "provide", "translate", "text", "original" # Specific to the model refusal
    }
    
    # Simple tokenization
    words = re.findall(r'\b\w+\b', text.lower())
    
    english_count = 0
    for word in words:
        if word in english_words:
            english_count += 1
            
    # If a significant portion of words are English, flag it
    if len(words) > 0 and english_count / len(words) > 0.3:
        return True
    
    # Check for specific phrases
    if "please provide the text" in text.lower():
        return True
        
    return False

def check_file(filepath):
    suspicious_lines = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_old = ""
    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith('old "'):
            current_old = line[5:-1]
        elif line.startswith('new "'):
            current_new = line[5:-1]
            # Ignore if new is same as old (might be a name or untranslatable)
            # But if old is English and new is same, it might be untranslated.
            # However, we are looking for *English* in the *Spanish* translation.
            
            if is_likely_english(current_new):
                suspicious_lines.append((i + 1, current_new))

    return suspicious_lines

def main():
    if len(sys.argv) < 2:
        print("Usage: python check_english.py <directory>")
        sys.exit(1)

    target_dir = sys.argv[1]
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith('.rpy'):
                filepath = os.path.join(root, file)
                suspicious = check_file(filepath)
                if suspicious:
                    print(f"Potential English in {filepath}:")
                    for line_num, text in suspicious:
                        print(f"  Line {line_num}: {text}")

if __name__ == "__main__":
    main()
