#!/usr/bin/env python3
"""
Asset checker for Ren'Py game
Checks for missing assets and name mismatches
"""

import os
import re
from pathlib import Path


def find_referenced_assets(game_dir):
    """Find all assets referenced in .rpy files"""
    referenced_images = set()
    referenced_music = set()
    referenced_sfx = set()

    scripts_dir = os.path.join(game_dir, 'Scripts')

    for rpy_file in Path(scripts_dir).glob('*.rpy'):
        with open(rpy_file, 'r', encoding='utf-8') as f:
            for line in f:
                # Skip commented-out lines
                stripped = line.strip()
                if stripped.startswith('#'):
                    continue

                # Find image references
                # Pattern: image name = "path/to/file.png"
                image_matches = re.findall(r'image\s+[^=]+=\s*"([^"]+)"', line)
                referenced_images.update(image_matches)

                # Find music references
                # Pattern: play music "path/to/file.mp3"
                music_matches = re.findall(r'play music\s+"([^"]+)"', line)
                referenced_music.update(music_matches)

                # Find sound references
                # Pattern: play sound "path/to/file.wav"
                sound_matches = re.findall(r'play sound\s+"([^"]+)"', line)
                referenced_sfx.update(sound_matches)

    return referenced_images, referenced_music, referenced_sfx


def find_actual_assets(game_dir):
    """Find all actual asset files in the game directory"""
    actual_images = set()
    actual_music = set()
    actual_sfx = set()

    # Find images (check both lowercase and capitalized)
    for images_dirname in ['images', 'Images']:
        images_dir = os.path.join(game_dir, images_dirname)
        if os.path.exists(images_dir):
            for root, dirs, files in os.walk(images_dir):
                for file in files:
                    if file.lower().endswith(
                            ('.png', '.jpg', '.jpeg', '.webp')):
                        rel_path = os.path.relpath(
                            os.path.join(root, file), game_dir)
                        actual_images.add(rel_path)

    # Find music
    music_dir = os.path.join(game_dir, 'Music')
    if os.path.exists(music_dir):
        for root, dirs, files in os.walk(music_dir):
            for file in files:
                if file.lower().endswith(('.mp3', '.ogg', '.wav', '.opus')):
                    rel_path = os.path.relpath(
                        os.path.join(root, file), game_dir)
                    actual_music.add(rel_path)

    # Find SFX
    sfx_dir = os.path.join(game_dir, 'SFX')
    if os.path.exists(sfx_dir):
        for root, dirs, files in os.walk(sfx_dir):
            for file in files:
                if file.lower().endswith(('.mp3', '.ogg', '.wav', '.opus')):
                    rel_path = os.path.relpath(
                        os.path.join(root, file), game_dir)
                    actual_sfx.add(rel_path)

    return actual_images, actual_music, actual_sfx


def check_case_sensitivity(referenced, actual, asset_type):
    """Check for case sensitivity issues"""
    issues = []

    # Create lowercase mapping of actual files
    actual_lower = {f.lower(): f for f in actual}

    for ref in referenced:
        # Normalize path separators
        ref_normalized = ref.replace('\\', '/')
        ref_lower = ref_normalized.lower()

        # Check if file exists (case-insensitive)
        if ref_lower in actual_lower:
            # Check if case matches exactly
            if ref_normalized != actual_lower[ref_lower]:
                issues.append({
                    'type': 'case_mismatch',
                    'referenced': ref,
                    'actual': actual_lower[ref_lower],
                    'asset_type': asset_type
                })

    return issues


def main():
    game_dir = '/home/user/AI/antigravity/MLP_SESC/game'

    print("=" * 80)
    print("ASSET CHECKER FOR REN'PY GAME")
    print("=" * 80)
    print()

    # Find referenced assets
    print("Scanning .rpy files for asset references...")
    ref_images, ref_music, ref_sfx = find_referenced_assets(game_dir)

    print(f"Found {len(ref_images)} image references")
    print(f"Found {len(ref_music)} music references")
    print(f"Found {len(ref_sfx)} sound effect references")
    print()

    # Find actual assets
    print("Scanning directories for actual asset files...")
    actual_images, actual_music, actual_sfx = find_actual_assets(game_dir)

    print(f"Found {len(actual_images)} actual image files")
    print(f"Found {len(actual_music)} actual music files")
    print(f"Found {len(actual_sfx)} actual sound effect files")
    print()

    # Check for missing assets
    print("=" * 80)
    print("CHECKING FOR MISSING ASSETS")
    print("=" * 80)
    print()

    missing_found = False

    # Check images
    for ref in sorted(ref_images):
        ref_normalized = ref.replace('\\', '/')
        # Try to find the file (case-insensitive)
        found = False
        for actual in actual_images:
            if actual.lower() == ref_normalized.lower():
                found = True
                break

        if not found:
            print(f"MISSING IMAGE: {ref}")
            missing_found = True

    # Check music
    for ref in sorted(ref_music):
        ref_normalized = ref.replace('\\', '/')
        found = False
        for actual in actual_music:
            if actual.lower() == ref_normalized.lower():
                found = True
                break

        if not found:
            print(f"MISSING MUSIC: {ref}")
            missing_found = True

    # Check SFX
    for ref in sorted(ref_sfx):
        ref_normalized = ref.replace('\\', '/')
        found = False
        for actual in actual_sfx:
            if actual.lower() == ref_normalized.lower():
                found = True
                break

        if not found:
            print(f"MISSING SFX: {ref}")
            missing_found = True

    if not missing_found:
        print("✓ No missing assets found!")

    print()

    # Check for case sensitivity issues
    print("=" * 80)
    print("CHECKING FOR CASE SENSITIVITY ISSUES")
    print("=" * 80)
    print()

    case_issues = []
    case_issues.extend(
        check_case_sensitivity(
            ref_images,
            actual_images,
            'IMAGE'))
    case_issues.extend(
        check_case_sensitivity(
            ref_music,
            actual_music,
            'MUSIC'))
    case_issues.extend(check_case_sensitivity(ref_sfx, actual_sfx, 'SFX'))

    if case_issues:
        for issue in case_issues:
            print(f"{issue['asset_type']} CASE MISMATCH:")
            print(f"  Referenced: {issue['referenced']}")
            print(f"  Actual:     {issue['actual']}")
            print()
    else:
        print("✓ No case sensitivity issues found!")

    print()

    # Check for unused assets
    print("=" * 80)
    print("CHECKING FOR UNUSED ASSETS")
    print("=" * 80)
    print()

    unused_found = False

    # Normalize referenced paths for comparison
    ref_images_normalized = {r.replace('\\', '/').lower() for r in ref_images}
    ref_music_normalized = {r.replace('\\', '/').lower() for r in ref_music}
    ref_sfx_normalized = {r.replace('\\', '/').lower() for r in ref_sfx}

    for actual in sorted(actual_images):
        if actual.lower() not in ref_images_normalized:
            print(f"UNUSED IMAGE: {actual}")
            unused_found = True

    for actual in sorted(actual_music):
        if actual.lower() not in ref_music_normalized:
            print(f"UNUSED MUSIC: {actual}")
            unused_found = True

    for actual in sorted(actual_sfx):
        if actual.lower() not in ref_sfx_normalized:
            print(f"UNUSED SFX: {actual}")
            unused_found = True

    if not unused_found:
        print("✓ No unused assets found!")

    print()
    print("=" * 80)
    print("ASSET CHECK COMPLETE")
    print("=" * 80)


if __name__ == '__main__':
    main()
