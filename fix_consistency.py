#!/usr/bin/env python3
"""
Fix color consistency and navigation across all catalog pages
to match index.html standards
"""

import re
import glob

# Standard navigation HTML that should be on every page
STANDARD_NAVIGATION = '''    <div class="nav-bar">
        <a href="index.html">🏠 Home</a>
        <a href="catalog_diabetic_hospital.html">🏥 Diabetic/Hospital</a>
        <a href="catalog_patient_care.html">👨‍⚕️ Patient Care</a>
        <a href="catalog_therapeutic.html">⚕️ Therapeutic</a>
        <a href="catalog_mobility_aids.html">♿ Mobility Aids</a>
        <a href="catalog_surgical_dressings.html">🩹 Surgical/Compression</a>
        <a href="catalog_orthotic_prosthetic.html">🦾 Orthotic/Prosthetic</a>
        <a href="catalog_specialized.html">🔬 Specialized</a>
    </div>'''

def get_navigation_with_active(page_name):
    """Generate navigation HTML with the appropriate page marked as active"""
    nav = STANDARD_NAVIGATION
    # Add active class to the current page
    nav = nav.replace(f'href="{page_name}"', f'href="{page_name}" class="active"')
    return nav

def fix_body_background(content):
    """Fix body background to use gradient instead of solid color"""
    # Replace solid background with gradient
    pattern = r'body\s*\{([^}]*?)background:\s*#f8f9fa;'
    replacement = r'body {\\1background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);'

    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    return content

def fix_navigation(content, filename):
    """Ensure navigation is correct and has proper active page"""
    # Extract current navigation
    nav_pattern = r'(<div class="nav-bar">.*?</div>)'
    match = re.search(nav_pattern, content, re.DOTALL)

    if match:
        old_nav = match.group(1)
        new_nav = get_navigation_with_active(filename)
        content = content.replace(old_nav, new_nav)
        return content, True
    else:
        print(f"  ⚠️  Warning: No navigation found in {filename}")
        return content, False

def process_file(filepath):
    """Process a single catalog file"""
    filename = filepath.split('/')[-1]

    print(f"Processing {filename}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes = []

    # Fix body background
    new_content = fix_body_background(content)
    if new_content != content:
        changes.append("body background gradient")
        content = new_content

    # Fix navigation
    new_content, nav_fixed = fix_navigation(content, filename)
    if new_content != content:
        changes.append("navigation links")
        content = new_content

    # Write back if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Fixed: {', '.join(changes)}")
        return True
    else:
        print(f"  • No changes needed")
        return False

def main():
    """Main processing function"""
    catalog_files = sorted(glob.glob('catalog_*.html'))

    print(f"Found {len(catalog_files)} catalog files\n")
    print("="*60)

    files_modified = 0

    for filepath in catalog_files:
        if process_file(filepath):
            files_modified += 1
        print()

    print("="*60)
    print(f"\n✅ Processing complete!")
    print(f"✅ {files_modified} files modified")
    print(f"\nStandardized elements:")
    print(f"  • Body background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)")
    print(f"  • Navigation: 8 consistent links with proper active states")
    print(f"  • Colors: #1e5a96 (primary), #2a6fb8 (secondary)")

if __name__ == '__main__':
    main()
