#!/usr/bin/env python3
"""
Standardize color scheme across all catalog pages to match index.html
Standard colors from index.html:
- Primary blue: #1e5a96
- Secondary blue: #2a6fb8
- Body gradient: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)
- Header gradient: linear-gradient(135deg, #1e5a96 0%, #2a6fb8 100%)
"""

import re
import glob

# Define color mappings from non-standard to standard
COLOR_REPLACEMENTS = {
    # Blue variations - standardize to #2a6fb8
    '#3498db': '#2a6fb8',
    '#2874a6': '#1e5a96',

    # Gradient replacements
    'linear-gradient(135deg, #1e5a96 0%, #3498db 100%)': 'linear-gradient(135deg, #1e5a96 0%, #2a6fb8 100%)',
    'linear-gradient(135deg, #1e5a96, #3498db)': 'linear-gradient(135deg, #1e5a96, #2a6fb8)',
    'linear-gradient(135deg, #2874a6 0%, #3498db 100%)': 'linear-gradient(135deg, #1e5a96 0%, #2a6fb8 100%)',
    'linear-gradient(135deg, #2874a6, #3498db)': 'linear-gradient(135deg, #1e5a96, #2a6fb8)',

    # Background gradient standardization (if needed)
    'linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)': 'linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)',
}

def standardize_colors(content):
    """Replace all non-standard colors with standard ones"""
    modified = content
    replacements_made = []

    for old_color, new_color in COLOR_REPLACEMENTS.items():
        if old_color in modified:
            count = modified.count(old_color)
            modified = modified.replace(old_color, new_color)
            replacements_made.append(f"  • {old_color} → {new_color} ({count} times)")

    return modified, replacements_made

def process_catalog_files():
    """Process all catalog HTML files"""
    catalog_files = glob.glob('/home/user/ClaudeCatalogRepo/catalog_*.html')

    print(f"Found {len(catalog_files)} catalog files to process\n")

    total_files_modified = 0

    for filepath in sorted(catalog_files):
        filename = filepath.split('/')[-1]
        print(f"Processing {filename}...")

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        modified_content, replacements = standardize_colors(content)

        if replacements:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified_content)

            print(f"✓ Updated {filename}")
            for replacement in replacements:
                print(replacement)
            total_files_modified += 1
        else:
            print(f"  No changes needed")

        print()

    print(f"\n{'='*60}")
    print(f"✅ Color standardization complete!")
    print(f"✅ {total_files_modified} files modified")
    print(f"\nStandard color scheme applied:")
    print(f"  Primary blue: #1e5a96")
    print(f"  Secondary blue: #2a6fb8")
    print(f"  Header gradient: linear-gradient(135deg, #1e5a96 0%, #2a6fb8 100%)")
    print(f"  Body gradient: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)")

if __name__ == '__main__':
    process_catalog_files()
