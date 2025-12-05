#!/usr/bin/env python3
"""
Final Review Script
- Checks for missing assets referenced in scripts.
- Checks for translation issues (empty, identical, AI placeholders).
"""

import os
import re
import sys

# Configuration
GAME_DIR = "game"
TL_DIR = os.path.join(GAME_DIR, "tl")
ASSET_DIRS = ["Images", "Music", "SFX"]
EXTENSIONS = {
    'image': ['.png', '.jpg', '.jpeg', '.webp'],
    'audio': ['.mp3', '.ogg', '.wav']
}

# Known system/default images to ignore if they appear in simple lists
IGNORED_IMAGES = ["black", "white", "solid", "bg"]

# AI detection phrases (lowercase)
AI_PHRASES = [
    "i cannot translate",
    "i can't translate",
    "as an ai",
    "i am an ai",
    "provide me with",
    "please give me",
    "translate it into",
    "translated into",
    "happiness to translate",
    "cannot fulfill",
    "violate my instructions",
]

def get_all_rpy_files(root_dir):
    rpy_files = []
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if f.endswith('.rpy'):
                rpy_files.append(os.path.join(root, f))
    return rpy_files

def check_assets(game_dir):
    print("Checking for missing assets...")
    issues = []
    
    # regex to find strings that look like paths or valid filenames with extensions
    # Focus on our known directories
    # Pattern: "((?:Images|Music|SFX)/[^"]+)"
    # Or strict filename with extension: "[^"]+\.(png|jpg|mp3|ogg|wav)"
    
    path_pattern = re.compile(r'"((?:Images|Music|SFX)/[^"]+)"', re.IGNORECASE)
    file_pattern = re.compile(r'"([^"]+\.(?:png|jpg|jpeg|webp|mp3|ogg|wav))"', re.IGNORECASE)

    rpy_files = get_all_rpy_files(game_dir)
    
    # Build set of actual files
    actual_files = set()
    for root, dirs, files in os.walk(game_dir):
        for f in files:
            # Store relative path from game dir
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, game_dir)
            actual_files.add(rel_path)
            # Also add lower case version for loose matching
            actual_files.add(rel_path.lower())

    for rpy_file in rpy_files:
        try:
            with open(rpy_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Failed to read {rpy_file}: {e}")
            continue

        lines = content.split('\n')
        for i, line in enumerate(lines):
            # Check explicit paths starting with known dirs
            matches = path_pattern.findall(line)
            # Also check generic filenames with extensions (often used in play music "file.mp3")
            matches.extend(file_pattern.findall(line))
            
            for path in matches:
                # Normalize path separators
                clean_path = path.replace('\\', '/')
                
                # Check 1: Exact match
                if clean_path in actual_files:
                    continue
                
                # Check 2: Case insensitive match
                if clean_path.lower() in actual_files:
                    # It exists but case differs
                    # On Linux this is missing, but Ren'Py might handle it. 
                    # User asked for "file doesn't exist", implying strictness or at least file system reality.
                    # We will flag it as a warning or error.
                    # If clean_path.lower() in actual_files is TRUE, it means we added lower() versions to the set.
                    # Wait, 'actual_files' has both exact and lower.
                    # To distinguish, let's check against a separate set of exact paths.
                    pass 

    # Re-doing the actual file set to be more precise
    exist_exact = set()
    exist_lower = set()
    
    for root, dirs, files in os.walk(game_dir):
        for f in files:
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, game_dir).replace('\\', '/')
            exist_exact.add(rel_path)
            exist_lower.add(rel_path.lower())

    for rpy_file in rpy_files:
        rel_rpy = os.path.relpath(rpy_file, game_dir)
        # Skip checking inside tl files for assets?
        # Sometimes tl files repeat the 'play' commands or 'image' definitions (rare).
        # Usually they only contain strings.
        # But if they DO contain asset refs, we should check them.
        
        with open(rpy_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for i, line in enumerate(lines):
            if line.strip().startswith('#'): continue # skip comments

            # Find strings
            # This regex captures things that look like our assets
            # 1. Starting with Images/, Music/, SFX/
            # 2. Ending with known media extension
            found_paths = []
            
            # Explicit directories
            m_dirs = re.findall(r'"((?:Images|Music|SFX)/[^"]+)"', line, re.IGNORECASE)
            found_paths.extend(m_dirs)
            
            # Extensions
            m_ext = re.findall(r'"([^"]+\.(?:png|jpg|jpeg|webp|mp3|ogg|wav))"', line, re.IGNORECASE)
            found_paths.extend(m_ext)
            
            for p in set(found_paths):
                # cleanup
                p = p.strip()
                
                # Logic to handle "Music/file.mp3" vs just "file.mp3"
                # If path doesn't start with a dir, Ren'Py searches.
                # But our scan of 'actual_files' includes the directories.
                # So if p is "intro.mp3", checking if it exists in 'game/intro.mp3' might fail if it's in 'game/Music/intro.mp3'.
                # Ren'Py auto-search applies to 'audio' but 'image' usually needs paths if not defined.
                
                # Check exact existence
                if p in exist_exact:
                    continue
                
                # Check case insensitive
                if p.lower() in exist_lower:
                    # Warn about case
                    issues.append(f"[ASSET CASE] {rel_rpy}:{i+1} references '{p}' but file exists only valid with different case.")
                    continue
                
                # Check if it exists in subdirectories (Ren'Py search path logic approximation)
                # If matches a filename in specific folders
                basename = os.path.basename(p)
                found_approx = False
                for existing in exist_exact:
                    if existing.endswith('/' + basename) or existing == basename:
                        # Found it somewhere else
                        if p in existing: # fuzzy match
                            found_approx = False # Wait, if I referenced "intro.mp3" and "Music/intro.mp3" exists, that is valid in Ren'Py 7+
                            # Let's assume valid if basename matches something in known audio dirs and p has no directory?
                           
                # To be safe, if we can't find it exactly or case-insensitive relative to game/, flag it.
                # But handle the "auto search" for audio.
                if any(p.endswith(ext) for ext in ['.mp3', '.ogg', '.wav']):
                    # search in Music/ and SFX/
                    candidates = [os.path.join("Music", p).replace('\\','/'), os.path.join("SFX", p).replace('\\','/')]
                    if any(c in exist_exact for c in candidates):
                        continue
                    if any(c.lower() in exist_lower for c in candidates):
                        continue
                        
                issues.append(f"[MISSING ASSET] {rel_rpy}:{i+1} references '{p}' which was not found.")

    return issues

def check_translations(game_dir):
    print("Checking translations...")
    issues = []
    
    tl_dir = os.path.join(game_dir, "tl")
    if not os.path.exists(tl_dir):
        return ["No translation directory found."]
        
    languages = [d for d in os.listdir(tl_dir) if os.path.isdir(os.path.join(tl_dir, d))]
    
    for lang in languages:
        lang_path = os.path.join(tl_dir, lang)
        # Scan all rpy in this lang
        rpy_files = get_all_rpy_files(lang_path)
        
        for rpy in rpy_files:
            rel_rpy = os.path.relpath(rpy, game_dir)
            
            try:
                with open(rpy, 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue
                
            # Parse translation blocks
            # 1. Strings: old "A" new "B"
            # 2. Dialogue: translate X Y: ... "..."
            
            lines = content.split('\n')
            
            # Iterator to handle multi-line parsing
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                
                # STRING TRANSLATIONS
                if line.startswith('old '):
                     # extract old
                     m_old = re.match(r'old\s+"((?:[^"\\]|\\.)*)"', line)
                     if m_old:
                         old_str = m_old.group(1)
                         # Look for new
                         j = i + 1
                         while j < len(lines):
                             l2 = lines[j].strip()
                             if l2.startswith('new '):
                                 m_new = re.match(r'new\s+"((?:[^"\\]|\\.)*)"', l2)
                                 if m_new:
                                     new_str = m_new.group(1)
                                     # CHECKS
                                     check_trans_entry(issues, lang, rel_rpy, j+1, old_str, new_str)
                                 break
                             if l2.startswith('old ') or l2.startswith('translate '): 
                                 break # unmatched old?
                             j += 1
                
                # DIALOGUE TRANSLATIONS
                # translate lang label:
                #    char "Start"
                #    char "End" (rare, usually one line)
                if line.startswith('translate ') and ':' in line:
                    # Enter block
                    j = i + 1
                    while j < len(lines):
                        l2 = lines[j] # preserve indent
                        stripped = l2.strip()
                        if not stripped or stripped.startswith('#'):
                            j += 1
                            continue
                        
                        # Check for end of block (unindented or new translate)
                        if not l2.startswith(' ') and not l2.startswith('\t') and stripped != "":
                             break
                             
                        # Parse dialogue line: char "text" or just "text"
                        # Regex to capture "text" at end of line
                        # Be careful of escaped quotes
                        m_diag = re.search(r'"((?:[^"\\]|\\.)*)"$', stripped)
                        if m_diag:
                            trans_text = m_diag.group(1)
                            # We need source text to compare.
                            # Source text is usually in comments above, encoded by Ren'Py:
                            # # e "Source"
                            # But unreliable to parse from comments.
                            # If strict identity check allows "English" exception, we might skip source comparison if we can't reliably find it.
                            # BUT, we can check for Empty or AI.
                            
                            # For "Identical to source", we need source. 
                            # If we can't find source easily (Ren'Py format varies), we skip the "Identical" check for Dialogue 
                            # unless we parse the whole file structure mapping labels to original script. 
                            # That is complex.
                            # ERROR ON THE SIDE OF CAUTION: 
                            # The user said "translations that are identical to the source".
                            # For strings `old`/`new`, it's easy.
                            # For dialogue, if we don't have source, we can't check equality.
                            # Let's check Empty and AI first.
                            
                            # However, Ren'Py usually generates:
                            # # char "Original"
                            # char "Translated"
                            # We can look at the previous comment line.
                            
                            prev_comment = ""
                            k = j - 1
                            while k > i:
                                if lines[k].strip().startswith('#') and '"' in lines[k]:
                                    matches = re.findall(r'"((?:[^"\\]|\\.)*)"', lines[k])
                                    if matches:
                                        prev_comment = matches[-1] # take last string in comment?
                                    break
                                k -= 1
                            
                            check_trans_entry(issues, lang, rel_rpy, j+1, prev_comment, trans_text, is_dialogue=True)
                            
                        j += 1
                    i = j - 1
                
                i += 1
                
    return issues

def check_trans_entry(issues, lang, file, line_num, source, target, is_dialogue=False):
    # 1. Empty check
    if not target:
        issues.append(f"[EMPTY {lang.upper()}] {file}:{line_num} is empty.")
        return

    # 2. Identity check (Skip English)
    if lang != "English" and source and source == target:
        # For strings, this is definitely an issue.
        # For dialogue, it usually is too, unless it's a name or "..."
        if len(source) > 3: # Ignore short things like "..." or "No."
             issues.append(f"[IDENTICAL {lang.upper()}] {file}:{line_num} is identical to source.")

    # 3. AI check
    target_lower = target.lower()
    for phrase in AI_PHRASES:
        if phrase in target_lower:
             issues.append(f"[AI CONTENT {lang.upper()}] {file}:{line_num} contains suspicious phrase: '{phrase}'")

def main():
    game_dir = GAME_DIR
    if len(sys.argv) > 1:
        game_dir = sys.argv[1]
        
    print(f"Starting Final Review in {game_dir}...")
    
    asset_issues = check_assets(game_dir)
    trans_issues = check_translations(game_dir)
    
    all_issues = asset_issues + trans_issues
    
    report_file = "final_review_report.txt"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("FINAL REVIEW REPORT\n")
        f.write("===================\n\n")
        
        if not all_issues:
            f.write("No issues found! Great job.\n")
        else:
            f.write(f"Found {len(all_issues)} issues:\n\n")
            for issue in all_issues:
                f.write(issue + "\n")
                
    print(f"\nDone. Found {len(all_issues)} issues. Written to {report_file}.")
    # Dump to stdout too for agent to see
    if all_issues:
        print("\n--- ISSUES FOUND ---")
        for i in all_issues[:20]:
            print(i)
        if len(all_issues) > 20:
            print(f"... and {len(all_issues)-20} more.")

if __name__ == "__main__":
    main()
