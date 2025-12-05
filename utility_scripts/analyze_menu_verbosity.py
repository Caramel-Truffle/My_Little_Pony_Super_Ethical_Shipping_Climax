import os
import re

def analyze_menu_verbosity(base_dir):
    violations = []
    
    # Regex to find string translation blocks
    # Matches: translate Telenovela strings:
    strings_block_re = re.compile(r'^\s*translate\s+Telenovela\s+strings:$')
    
    # Regex to extract old and new strings
    old_re = re.compile(r'^\s*old\s+"(.*)"')
    new_re = re.compile(r'^\s*new\s+"(.*)"')

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if not file.endswith('.rpy'):
                continue
            
            if file in ['screens.rpy', 'common.rpy']:
                continue
            
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            in_strings_block = False
            current_old = None
            current_line = 0
            
            for i, line in enumerate(lines):
                line_strip = line.strip()
                
                if strings_block_re.match(line):
                    in_strings_block = True
                    continue
                
                # If we hit another translate block (that isn't strings), we are out
                if line.startswith('translate Telenovela') and not strings_block_re.match(line):
                    in_strings_block = False
                    continue

                if in_strings_block:
                    old_match = old_re.match(line)
                    new_match = new_re.match(line)
                    
                    if old_match:
                        current_old = old_match.group(1)
                        current_line = i + 1
                    elif new_match and current_old is not None:
                        current_new = new_match.group(1)
                        
                        # Analyze
                        orig_len = len(current_old)
                        trans_len = len(current_new)
                        
                        min_mult = 0
                        max_mult = float('inf')
                        tier = ""
                        
                        if orig_len <= 3:
                            min_mult = 10
                            max_mult = 20
                            tier = "Insanely short (<=3)"
                        elif orig_len <= 6:
                            min_mult = 6
                            max_mult = 10
                            tier = "Extremely short (4-6)"
                        elif orig_len <= 10:
                            min_mult = 3
                            max_mult = 6
                            tier = "Very short (7-10)"
                        elif orig_len <= 20:
                            min_mult = 2
                            max_mult = 3
                            tier = "Short (11-20)"
                        elif orig_len <= 30:
                            min_mult = 1.5
                            max_mult = 2
                            tier = "Long (21-30)"
                        elif orig_len <= 40:
                            min_mult = 1.2
                            max_mult = 1.5
                            tier = "Very long (31-40)"
                        elif orig_len <= 50:
                            max_mult = 1.2
                            tier = "Extremely long (41-50)"
                        else:
                            max_mult = 1.0
                            tier = "Insanely long (>50)"
                            
                        # Check constraints
                        # Note: User specified > Min, so strictly greater
                        # User specified <= Max, so less than or equal
                        
                        is_violation = False
                        violation_type = ""
                        
                        if trans_len > orig_len * max_mult:
                            is_violation = True
                            violation_type = "TOO LONG"
                        elif min_mult > 0 and trans_len <= orig_len * min_mult:
                            is_violation = True
                            violation_type = "TOO SHORT"
                            
                        if is_violation:
                            violations.append({
                                'file': file,
                                'line': current_line,
                                'orig': current_old,
                                'trans': current_new,
                                'orig_len': orig_len,
                                'trans_len': trans_len,
                                'tier': tier,
                                'type': violation_type,
                                'limit': f"{min_mult}x < L <= {max_mult}x"
                            })
                        
                        current_old = None # Reset

    # Report
    print(f"Found {len(violations)} violations in menu choices.")
    for v in violations:
        print(f"[{v['type']}] {v['file']}:{v['line']} ({v['tier']})")
        print(f"  Orig ({v['orig_len']}): {v['orig']}")
        print(f"  Trans ({v['trans_len']}): {v['trans']}")
        print(f"  Limit: {v['limit']}")
        print("-" * 40)

if __name__ == "__main__":
    analyze_menu_verbosity("/home/user/AI/antigravity/MLP_SESC/game/tl/Telenovela")
