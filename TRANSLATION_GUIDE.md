# Translation Guide

This document serves as a reference for understanding, modifying, and adding translations to the **My Little Pony: Super Ethical Shipping Climax** project. The game is built using the **Ren'Py** engine, and it follows standard Ren'Py translation conventions.

## 1. Directory Structure

The project's translation system is organized as follows:

*   **`game/Scripts/`**: Contains the original game scripts (usually in English or the base language). This is the source of truth.
*   **`game/tl/`**: The "Translation" directory. This contains subdirectories for each supported language.

### Language Directories
Inside `game/tl/`, you will find folders named after the language they contain (e.g., `French`, `English`, `Russian`).

Inside a specific language folder (e.g., `game/tl/French/`), the structure mirrors the main `game/` directory:
*   **`Scripts/`**: Contains the translated versions of the files found in `game/Scripts/`.
*   **`common.rpy`**: Contains translations for common Ren'Py interface strings.

## 2. Translation File Format

Translation files are `.rpy` files that map original strings to translated strings. There are two main types of translation blocks you will encounter.

### A. Dialogue Translations

These blocks translate the spoken dialogue in the game. They link to specific lines in the original script using a unique hash.

**Format:**
```renpy
# game/Scripts/script.rpy:512
translate French start_497c87f4:

    # y "AAAAAAAAAAAH!! Giant-pointy-pony-head!!"
    y "AAAAAAAAAAAH!! Tête-géante-de-poney-pointu!!"
```

*   **Header**: `translate <Language> <label>_<hash>:` identifies the specific line being translated. **DO NOT MODIFY THIS LINE.**
*   **Comment**: `# y "..."` shows the original text for reference.
*   **Translation**: `y "..."` is the line where you write the translation. Ensure the character tag (e.g., `y`) remains the same unless the character name itself is being localized (which is rare).

### B. String Translations

These blocks translate strings used in the UI, menus, or variables (strings wrapped in `_()` or `__()` in the code).

**Format:**
```renpy
translate French strings:

    # Scripts\script.rpy:525
    old "Twilight Sparkle"
    new "Twilight Sparkle"

    # Scripts\script.rpy:525
    old "Wait!! I want to be my OC!! It's a super-awesome alicorn with neon colors and stuff!!!!"
    new "Attends!! Je veux être mon OC!! C'est une alicorne super géniale avec des couleurs fluo!!!!"
```

*   **`old`**: The exact string found in the source code. **DO NOT MODIFY.**
*   **`new`**: The translated string.

## 3. Language Style Guides

To ensure coherence across the project, each supported language adheres to specific style guidelines.

### English (`game/tl/English/`)
*   **Description**: This is the "Proofread English" layer.
*   **Goal**: To provide a grammatically correct and polished version of the original script.
*   **Guidelines**: Fix typos, grammar errors, and awkward phrasing found in the base script.

### Engrish (`game/tl/Engrish/`)
*   **Description**: A broken, literal, and grammatically incorrect version of English.
*   **Goal**: To create a humorous, "badly translated" feel.
*   **Guidelines**:
    *   **Differentiation**: The translation must be at least **50% different** (Levenshtein distance) from the original English text.
    *   **Style**: Use literal translations, wrong verb tenses, misused idioms, and broken grammar.

### French (`game/tl/French/`)
*   **Description**: Standard "Metropolitan" French (France).
*   **Goal**: A high-quality, standard French translation.
*   **Guidelines**: Adhere to standard French grammar and vocabulary. Avoid regionalisms unless specific to a character.

### TABARNAK (`game/tl/TABARNAK/`)
*   **Description**: Quebec French (Joual).
*   **Goal**: A highly colloquial and culturally specific translation for Quebec audiences.
*   **Guidelines**:
    *   **Colloquialisms**: Use as many Quebecois expressions as possible (e.g., use "pas pantoute" instead of "pas du tout").
    *   **Swearing**: Appropriate use of "sacres" (Tabarnak, Calisse, etc.) where they fit the tone.
    *   **Vocabulary**: Use Quebec-specific terms (e.g., "char" for car, "magasiner" for shopping).

## 4. Working with Variables & Interpolation

The game uses variable interpolation (e.g., `[playername]`).

*   **Preserve Variables**: Always keep variables like `[playername]` in the translated string.
    *   *Original*: `"I want to be [playername]."`
    *   *French*: `"Je veux devenir [playername]."`
*   **Translating Interpolated Strings**: If the variable itself contains a translatable string, use the `!t` flag.
    *   *Usage*: `[playername!t]`
    *   This ensures that if `playername` is "Twilight Sparkle", it looks up the translation for "Twilight Sparkle" in the `translate strings` block before displaying it.

## 5. How to Modify Existing Translations

1.  **Locate the File**: Find the corresponding `.rpy` file in `game/tl/<Language>/Scripts/`. For example, if you want to fix a typo in the intro, look in `game/tl/<Language>/Scripts/script.rpy`.
2.  **Find the Line**: Search for the original English text or the current translation.
3.  **Edit**: Modify the text inside the quotes in the non-commented line.
4.  **Save**: Save the file. Ren'Py will automatically recompile it (`.rpyc`) on the next launch.

## 6. How to Add a New Language

1.  **Create Directory**: Create a new folder in `game/tl/` with the language name (e.g., `game/tl/Spanish`).
2.  **Generate Files**: Ideally, use the Ren'Py SDK's "Generate Translations" feature. This will create the empty file structure for you.
3.  **Manual Creation (If SDK unavailable)**:
    *   You can manually copy the structure from another language (e.g., `French`) and replace the translations.
    *   **Crucial**: You must change the language tag in every block: `translate French ...` -> `translate Spanish ...`.
4.  **Translate**: Go through the files and fill in the `new` strings and dialogue lines.

## 7. Utility Scripts & Tools

The project includes a suite of Python scripts to assist with translation, quality assurance, and maintenance. These are located in the **`utility_scripts/`** directory.

### Quality Assurance
*   **`check_grammar.py`**: Scans `game/tl/English/Scripts` for common grammar mistakes and typos.
*   **`check_engrish.py` / `check_all_engrish.py`**: Verifies that "Engrish" translations meet the requirement of being at least 50% different from the original English text (Levenshtein distance).
*   **`check_assets.py`**: Checks for missing image assets referenced in the scripts.
*   **`check_syntax.py`**: Validates the syntax of `.rpy` files to catch common errors like unescaped quotes or brackets.
*   **`check_translations.py`**: Reports on the completion status of translations for all languages.
*   **`check_file.py`**: A generic utility to check a specific file for various issues.

### Automation & Translation
*   **`auto_translate.py`**: Uses an external API (if configured) to automatically translate strings.
*   **`fill_translations.py`**: Fills empty translation blocks with the original English text (useful as a starting point).
*   **`copy_translations.py`**: Copies translations from one file/language to another.

### Maintenance & Fixes
*   **`fix_all_french.py` / `fix_all_tabarnak.py`**: Applies specific batch fixes or formatting rules to French and Tabarnak (Quebecois) translations.
*   **`fix_common_engrish.py`**: Applies common patterns to "Engrish" translations.
*   **`polish_engrish.py`**: Refines Engrish translations to ensure they are consistently broken.
*   **`remove_orphans.py`**: Cleans up translation blocks that no longer have a corresponding line in the original script.

### Debugging
*   **`debug_paths.py` / `debug_read.py`**: Simple scripts to help debug file path issues and file reading operations.

**Usage:**
Run these scripts from the root directory using Python 3:
```bash
python3 utility_scripts/check_grammar.py
```

## 8. Common Pitfalls

*   **Missing Quotes**: Ensure all strings are enclosed in double quotes.
*   **Escaping**: If you need to use a double quote inside the string, escape it with a backslash: `\"`.
*   **Broken Hashes**: Never change the hex code (e.g., `start_497c87f4`) in the translate statement. This breaks the link to the original line.
*   **Mismatched Interpolation**: Ensure `[variable]` names match exactly. `[PlayerName]` is not the same as `[playername]`.
