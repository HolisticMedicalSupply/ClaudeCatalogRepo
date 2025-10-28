#!/usr/bin/env python3
"""
Rebuild DM28 section completely with proper Brooklyn coverage
"""

import re

# Complete DM28 section with simplified Brooklyn coverage
DM28_SECTION = '''    <div class="category-section">
        <div class="category-header">
            DM28: REHABILITATIVE THERAPY DEVICES (BOC Category) - Brooklyn Coverage Guide
        </div>
        <div class="product-grid">
            <div class="product-card">
                <div class="product-name">UPPER EXTREMITY REHABILITATION SYSTEM PROVIDING ACTIVE ASSISTANCE TO FACILITATE MUSCLE RE-EDUCATION, INCLUDE MICROPROCESSOR, ALL COMPONENTS AND ACCESSORIES</div>
                <div class="code-section">
                    <div class="code-row">
                        <div class="code-label">HCPCS Code</div>
                        <div class="code-value"><span class="hcpcs-code">E0738</span></div>
                    </div>
                    <div class="code-row">
                        <div class="code-label">Brooklyn Coverage</div>
                        <div class="code-value">Medicare & NY Medicaid</div>
                    </div>
                </div>
                <div class="clinical-box">
                    <strong>Indications:</strong> Upper extremity rehabilitation for chronic stroke patients with arm/hand impairments.
                </div>
                <div class="med-necessity">
                    <strong>Requirements:</strong> Physician prescription required. Document stroke diagnosis and motor deficits. May require prior authorization.
                </div>
            </div>
            <div class="product-card">
                <div class="product-name">REHABILITATION SYSTEM WITH INTERACTIVE INTERFACE PROVIDING ACTIVE ASSISTANCE IN REHABILITATION THERAPY, INCLUDES ALL COMPONENTS AND ACCESSORIES, MOTORS, MICROPROCESSORS, SENSORS</div>
                <div class="code-section">
                    <div class="code-row">
                        <div class="code-label">HCPCS Code</div>
                        <div class="code-value"><span class="hcpcs-code">E0739</span></div>
                    </div>
                    <div class="code-row">
                        <div class="code-label">Brooklyn Coverage</div>
                        <div class="code-value">Medicare & NY Medicaid</div>
                    </div>
                </div>
                <div class="clinical-box">
                    <strong>Indications:</strong> Robotic rehabilitation for post-stroke patients with arm or leg impairments.
                </div>
                <div class="med-necessity">
                    <strong>Requirements:</strong> Physician prescription required. Document stroke-related impairment. May require prior authorization.
                </div>
            </div>
            <div class="product-card">
                <div class="product-name">GAIT MODULATION SYSTEM, RHYTHMIC AUDITORY STIMULATION, INCLUDING RESTRICTED THERAPY SOFTWARE, ALL COMPONENTS AND ACCESSORIES, PRESCRIPTION ONLY</div>
                <div class="code-section">
                    <div class="code-row">
                        <div class="code-label">HCPCS Code</div>
                        <div class="code-value"><span class="hcpcs-code">E3200</span></div>
                    </div>
                    <div class="code-row">
                        <div class="code-label">Brooklyn Coverage</div>
                        <div class="code-value">Medicare & NY Medicaid</div>
                    </div>
                </div>
                <div class="clinical-box">
                    <strong>Indications:</strong> Gait training device using rhythmic auditory stimulation for stroke patients with walking difficulties.
                </div>
                <div class="med-necessity">
                    <strong>Requirements:</strong> Physician prescription required. Patient must be able to walk independently. New code - verify coverage before prescribing.
                </div>
            </div>
        </div>
    </div>
'''

def rebuild_dm28():
    """Rebuild DM28 section in catalog_therapeutic.html"""
    filepath = 'catalog_therapeutic.html'

    print(f"Reading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Removing old DM28 section...")

    # Pattern to match everything from DM28 header to DM29 header
    pattern = r'<div class="category-section">\s*<div class="category-header">\s*DM28:.*?(?=<div class="category-section">\s*<div class="category-header">\s*DM29)'

    # Replace with new DM28 section
    content = re.sub(pattern, DM28_SECTION + '\n\n    ', content, flags=re.DOTALL)

    print(f"Writing fixed content to {filepath}...")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\n" + "="*60)
    print("✅ DM28 section rebuilt successfully!")
    print("="*60)
    print("\nChanges made:")
    print("  ✓ Rebuilt entire DM28 section with proper HTML structure")
    print("  ✓ Added 'Indications' and 'Requirements' to all 3 codes")
    print("  ✓ Simplified language for Brooklyn doctors")
    print("  ✓ Fixed all HTML structural issues")
    print("  ✓ Removed orphaned/duplicate cards")
    print("\nBrooklyn coverage codes updated:")
    print("  • E0738 - Upper extremity rehabilitation system")
    print("  • E0739 - Rehabilitation system with interactive interface")
    print("  • E3200 - Gait modulation system")

if __name__ == '__main__':
    rebuild_dm28()
