# English Translation Grammar Fixes

## Summary

Fixed 4 grammar and typo issues in the English translation files.

## Issues Fixed

### 1. script.rpy - Line 43
**Issue**: Duplicate word "and and"
- **Before**: `"And then I will send you in Ponyville and and-"`
- **After**: `"And then I will send you in Ponyville and-"`
- **Context**: Colgate's dialogue when explaining the transformation

### 2. script.rpy - Line 49
**Issue**: Incorrect verb form "what happen"
- **Before**: `"I will see what happen myself."`
- **After**: `"I will see what happens myself."`
- **Context**: Player's response to Colgate

### 3. other.rpy - Line 121
**Issue**: "you too are" should be "you two are" (referring to two people)
- **Before**: `"Just go there and look if you too are happy together!"`
- **After**: `"Just go there and see if you two are happy together!"`
- **Context**: Sweetie Belle talking about Big Mac and his date
- **Bonus**: Also changed "look if" to "see if" for better flow

### 4. other.rpy - Line 175
**Issue**: Sentence not capitalized
- **Before**: `"Okay, you deserved it. this is your cupboard ending."`
- **After**: `"Okay, you deserved it. This is your cupboard ending."`
- **Context**: Narrator text for the cupboard ending easter egg

## Notes

- The checker found "didn'" in line 109 of other.rpy, but this is intentional dialect for Apple Bloom's accent ("we didn' do too well")
- All other contractions (didn't, can't, won't, etc.) are properly formatted
- No instances of common misspellings like "alot", "aswell", or "eachother"

## Verification

Ran `check_grammar.py` after fixes:
```
No obvious grammar issues found!
```

## Files Modified

1. `/game/tl/English/Scripts/script.rpy` - 2 fixes
2. `/game/tl/English/Scripts/other.rpy` - 2 fixes
