
import re
import random

filepath = "/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/common.rpy"

def translate_to_engrish(text):
    if text.strip() == "": return ""
    if text.startswith("[") and text.endswith("]"): return text
    if text.startswith("{#"): return text

    replacements = {
        "the": "da", "The": "Da", "is": "is being", "are": "are being",
        "you": "yuo", "your": "yuo's", "to": "for", "of": "ov",
        "have": "haz", "this": "dis", "that": "dat", "with": "wit",
        "for": "four", "not": "not", "will": "will be", "can": "can be",
        "please": "plz", "menu": "list-thing", "game": "play-thing",
        "save": "keep-safe", "load": "bring-back", "settings": "fix-options",
        "preferences": "like-things", "help": "halp", "quit": "stop now",
        "return": "go back", "back": "go back", "history": "old words",
        "skip": "fast forward", "auto": "self-go", "sound": "noise",
        "music": "song", "voice": "talk-sound", "volume": "loudness",
        "display": "look-screen", "window": "box", "fullscreen": "big screen",
        "language": "speak-way", "text": "word", "speed": "fastness",
        "after": "later than", "before": "sooner than", "delete": "destroy",
        "confirm": "say yes", "continue": "go more", "start": "begin start",
        "about": "what is", "yes": "ya", "no": "nay", "ok": "okey",
        "cancel": "stop it", "Self-voicing": "Me-talk", "disabled": "no work",
        "enabled": "work good", "Clipboard": "Copy-place",
    }
    
    words = text.split(' ')
    new_words = []
    for word in words:
        if '[' in word or '{' in word or '%' in word:
            new_words.append(word)
            continue
        clean_word = re.sub(r'[^\w]', '', word)
        if clean_word in replacements:
            replacement = replacements[clean_word]
            if word.endswith('.'): replacement += '.'
            elif word.endswith(','): replacement += ','
            elif word.endswith('?'): replacement += '?'
            elif word.endswith('!'): replacement += '!'
            new_words.append(replacement)
        else:
            if len(word) > 4 and random.random() < 0.3:
                new_words.append(word.upper())
            else:
                new_words.append(word)
    
    intensifiers = [" very much", " super", " big time", " indeed", " yes"]
    result = " ".join(new_words)
    if result == text: # Force change
        result += random.choice(intensifiers)
    elif random.random() < 0.5 and not text.endswith("]"):
        result += random.choice(intensifiers)
        
    return result

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
last_old = None
modified_count = 0

for line in lines:
    # Check for old "..."
    old_match = re.search(r'^\s+old\s+"([^"]*)"', line)
    if old_match:
        last_old = old_match.group(1)
        new_lines.append(line)
        continue

    # Check for new "..."
    new_match = re.search(r'^(\s+)new\s+"([^"]*)"', line)
    if new_match:
        indent = new_match.group(1)
        current_trans = new_match.group(2)
        
        if last_old:
            # Check if untranslated
            if current_trans == last_old:
                translated = translate_to_engrish(last_old)
                new_line = f'{indent}new "{translated}"\n'
                new_lines.append(new_line)
                modified_count += 1
                # print(f"Translated: {last_old[:20]} -> {translated[:20]}")
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)
        # Reset last_old if we hit a non-translation line (optional, but safer)
        if line.strip() == "":
            last_old = None

print(f"Modified {modified_count} lines")

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
