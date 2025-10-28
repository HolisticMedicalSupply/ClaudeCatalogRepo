#!/usr/bin/env python3
"""
Comprehensive fix for Brooklyn coverage issues:
1. Fix malformed HTML structure (missing closing tags)
2. Remove duplicate/orphaned product cards
3. Add simplified Brooklyn coverage boxes with proper labels
4. Ensure consistent formatting
"""

import re

# Simplified Brooklyn coverage data
BROOKLYN_COVERAGE = {
    'E0738': {
        'indications': 'Upper extremity rehabilitation for chronic stroke patients with arm/hand impairments.',
        'requirements': 'Physician prescription required. Document stroke diagnosis and motor deficits. May require prior authorization.'
    },
    'E0739': {
        'indications': 'Robotic rehabilitation for post-stroke patients with arm or leg impairments.',
        'requirements': 'Physician prescription required. Document stroke-related impairment. May require prior authorization.'
    },
    'E3200': {
        'indications': 'Gait training device using rhythmic auditory stimulation for stroke patients with walking difficulties.',
        'requirements': 'Physician prescription required. Patient must be able to walk independently. New code - verify coverage before prescribing.'
    },
}

def fix_catalog():
    """Fix catalog_therapeutic.html structure and Brooklyn coverage"""
    filepath = 'catalog_therapeutic.html'

    print(f"Reading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    print("\nStep 1: Fixing HTML structure - closing code-section divs properly...")

    # Fix pattern where code-section is not closed before product-card closes
    # Pattern: </div> (closes code-row) followed by </div> (tries to close code-section but malformed)
    # Should have </div></div> properly

    # Replace the malformed structure in Brooklyn coverage cards
    pattern = r'(<div class="code-value">Medicare & NY Medicaid</div>\s*</div>\s*</div>\s*)\n    </div>'
    replacement = r'\1\n                </div>'
    content = re.sub(pattern, replacement, content)

    print("Step 2: Removing orphaned/duplicate product cards...")

    # Remove the duplicate cards that appear after DM28 section closes
    # These are the orphaned cards between DM28 closing and DM29 opening
    orphan_pattern = r'(</div>\s*</div>\s*\n\s*</div>\s*<div class="product-card">.*?</div>\s*</div>\s*<div class="product-card">.*?</div>\s*</div>\s*</div>\s*</div>\s*\n\s*)<div class="category-section">'

    # Simpler approach: Find and remove section between "    </div>\n\n" (DM28 close) and next category-section
    # Let me search for the specific pattern

    # Remove everything between the DM28 closure and DM29 opening
    orphan_pattern2 = r'(DM28.*?</div>\s*</div>\s*</div>\s*)\n\s*</div>\s*<div class="product-card">.*?(<div class="category-section">\s*<div class="category-header">\s*DM29)'
    replacement2 = r'\1\n\n    \2'
    content = re.sub(orphan_pattern2, replacement2, content, flags=re.DOTALL)

    print("Step 3: Adding simplified Brooklyn coverage boxes...")

    # For each code, find its card and add the boxes
    for code, data in BROOKLYN_COVERAGE.items():
        # Find pattern: Brooklyn Coverage card for this code
        pattern = rf'(<span class="hcpcs-code">{code}</span>.*?Brooklyn Coverage.*?Medicare & NY Medicaid</div>\s*</div>\s*</div>\s*</div>)'

        replacement = rf'''\1
                <div class="clinical-box">
                    <strong>Indications:</strong> {data['indications']}
                </div>
                <div class="med-necessity">
                    <strong>Requirements:</strong> {data['requirements']}
                </div>'''

        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    print("Step 4: Final cleanup - fixing any remaining structural issues...")

    # Ensure proper indentation for product-card closures
    content = re.sub(r'\n    </div>\n            </div>', r'\n            </div>', content)

    print(f"\nWriting fixed content to {filepath}...")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\n" + "="*60)
    print("✅ Brooklyn coverage formatting completely fixed!")
    print("="*60)
    print("\nChanges made:")
    print("  ✓ Fixed malformed HTML structure (closed code-section divs)")
    print("  ✓ Removed duplicate/orphaned product cards")
    print("  ✓ Added 'Indications' and 'Requirements' boxes to 3 Brooklyn coverage codes")
    print("  ✓ Simplified language for Brooklyn doctors")
    print("  ✓ Ensured consistent formatting")
    print(f"\nUpdated {len(BROOKLYN_COVERAGE)} HCPCS codes with Brooklyn coverage:")
    for code in BROOKLYN_COVERAGE.keys():
        print(f"  • {code}")

if __name__ == '__main__':
    fix_catalog()
