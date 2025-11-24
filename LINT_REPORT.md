# Lint Report for Python Files

## Summary

Ran flake8 on Python files in the repository. Found **72 issues** across 2 files.

## Issues Breakdown

### check_assets.py (47 issues)

**Spacing Issues (E302/E305):**
- Line 11: E302 - expected 2 blank lines, found 1
- Line 44: E302 - expected 2 blank lines, found 1  
- Line 80: E302 - expected 2 blank lines, found 1
- Line 105: E302 - expected 2 blank lines, found 1
- Line 242: E305 - expected 2 blank lines after function definition, found 1

**Whitespace Issues (W293) - 42 occurrences:**
Lines with trailing whitespace on blank lines:
16, 18, 26, 31, 36, 41, 49, 59, 68, 77, 83, 86, 91, 102, 107, 112, 116, 121, 125, 130, 136, 138, 148, 152, 161, 165, 174, 178, 181, 183, 189, 194, 203, 205, 211, 213, 218, 223, 228, 233, 236

### check_grammar.py (25 issues)

**Spacing Issues (E302/E305):**
- Line 12: E302 - expected 2 blank lines, found 1
- Line 73: E302 - expected 2 blank lines, found 1
- Line 104: E305 - expected 2 blank lines after function definition, found 1

**Line Length (E501):**
- Line 54: E501 - line too long (107 > 100 characters)

**Whitespace Issues (W293) - 21 occurrences:**
Lines with trailing whitespace on blank lines:
15, 18, 23, 25, 34, 43, 52, 61, 70, 75, 77, 82, 87, 90, 99

## Issue Categories

1. **E302/E305 (8 total)**: Missing blank lines between functions
   - Python PEP 8 requires 2 blank lines between top-level functions
   
2. **W293 (63 total)**: Blank lines contain whitespace
   - Blank lines should be completely empty (no spaces/tabs)
   
3. **E501 (1 total)**: Line too long
   - One line exceeds 100 character limit

## Severity

- **Low**: Most issues are cosmetic (whitespace)
- **Medium**: Function spacing issues affect readability
- **Low**: Single line length issue

## Recommendation

These are all style/formatting issues that don't affect functionality but should be fixed for code quality:

1. Remove trailing whitespace from blank lines
2. Add proper spacing between function definitions
3. Break the long line into multiple lines

Would you like me to fix these issues automatically?
