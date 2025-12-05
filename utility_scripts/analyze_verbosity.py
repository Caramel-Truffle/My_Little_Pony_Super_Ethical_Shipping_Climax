import os
import re

def analyze_verbosity(base_dir):
    results = []
    
    # Regex to find translation blocks
    # Matches: translate Telenovela label:
    block_start_re = re.compile(r'^\s*translate\s+Telenovela\s+[\w_]+:$')
    
    # Regex to extract string content
    # This is a simplified regex and might need adjustment for complex cases
    string_re = re.compile(r'"(.*)"')

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if not file.endswith('.rpy'):
                continue
            
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            i = 0
            while i < len(lines):
                line = lines[i]
                
                if block_start_re.match(line):
                    # Found a translation block
                    original_text = ""
                    translated_text = ""
                    line_number = i + 1
                    
                    # Look ahead for content
                    j = i + 1
                    while j < len(lines):
                        sub_line = lines[j].strip()
                        
                        # Stop if we hit the next block or end of file (heuristic)
                        if block_start_re.match(lines[j]):
                            break
                        
                        # Extract original text (commented out)
                        # Example: # "Original text"
                        # Or: # p "Original text"
                        if sub_line.startswith('#'):
                            match = string_re.search(sub_line)
                            if match:
                                original_text = match.group(1)
                        
                        # Extract translated text (not commented)
                        # Example: "Translated text"
                        # Or: p "Translated text"
                        elif sub_line and not sub_line.startswith('#'):
                            match = string_re.search(sub_line)
                            if match:
                                translated_text = match.group(1)
                                # Once we have both, we can stop searching this block
                                if original_text:
                                    break
                        
                        j += 1
                    
                    if original_text and translated_text:
                        diff = len(translated_text) - len(original_text)
                        orig_len = len(original_text)
                        trans_len = len(translated_text)
                        
                        # Calculate percentage increase
                        # Avoid division by zero for empty strings
                        if orig_len > 0:
                            percentage = ((trans_len - orig_len) / orig_len) * 100
                        else:
                            percentage = 0 if trans_len == 0 else float('inf')
                        
                        results.append({
                            'diff': diff,
                            'percentage': percentage,
                            'orig_len': orig_len,
                            'trans_len': trans_len,
                            'file': file,
                            'line': line_number,
                            'original': original_text,
                            'translated': translated_text
                        })
                    
                    i = j # Skip processed lines
                else:
                    i += 1

    # Sort by percentage increase descending
    results.sort(key=lambda x: x['percentage'], reverse=True)
    
    print(f"Top 50 Most Verbose Translations (by percentage increase):")
    print("-" * 80)
    
    for item in results[:50]:
        # Format percentage nicely
        if item['percentage'] == float('inf'):
            pct_str = "INF%"
        else:
            pct_str = f"+{item['percentage']:.1f}%"
        
        print(f"[{pct_str}] [+{item['diff']}] ({item['orig_len']} -> {item['trans_len']}) {item['file']}:{item['line']}")
        print(f"ORIG: {item['original']}")
        print(f"TL  : {item['translated']}")
        print("-" * 80)

if __name__ == "__main__":
    target_dir = "/home/user/AI/antigravity/MLP_SESC/game/tl/Telenovela"
    analyze_verbosity(target_dir)
