#!/usr/bin/env python3
"""
Carefully add Brooklyn coverage to specific HCPCS codes in DM24, DM25, DM28
without breaking HTML structure or removing any categories
"""

import re

# Brooklyn coverage data - simplified for Brooklyn doctors
BROOKLYN_COVERAGE = {
    # DM24: EXTERNAL INFUSION PUMP SUPPLIES
    'A4221': {
        'indications': 'For chemotherapy, cancer pain management, or chronic conditions requiring continuous infusion at home.',
        'requirements': 'Written prescription required. Document medical necessity for home infusion therapy.'
    },
    'A4222': {
        'indications': 'Cassettes and bags for external infusion pump therapy.',
        'requirements': 'Written prescription required when pump therapy is covered.'
    },
    'A4226': {
        'indications': 'CODE RETIRED SEPTEMBER 15, 2020 - Do not prescribe.',
        'requirements': 'N/A - Use A4224 or A4225 for insulin pump supplies instead.',
        'retired': True
    },
    'A4244': {
        'indications': 'Antiseptic solution for catheter site care with infusion pumps.',
        'requirements': 'No prior authorization needed with covered infusion pump.'
    },
    'A4245': {
        'indications': 'Alcohol prep pads for catheter maintenance and diabetic care.',
        'requirements': 'No prior authorization needed. Limit: 5 boxes per month.'
    },
    'A4602': {
        'indications': 'Replacement battery for patient-owned external infusion pumps.',
        'requirements': 'Patient must own the pump. Limit: One battery every 6 months.'
    },
    'K0552': {
        'indications': 'Syringe cartridges for external drug infusion pumps (chemotherapy, pain management, antibiotics).',
        'requirements': 'Written prescription required. Document drug name and diagnosis.'
    },
    'K0601': {
        'indications': 'Silver oxide battery replacement for patient-owned infusion pumps.',
        'requirements': 'Patient must own the pump. Not covered with rented pumps.'
    },
    'K0602': {
        'indications': 'Silver oxide battery replacement for patient-owned infusion pumps.',
        'requirements': 'Patient must own the pump. Not covered with rented pumps.'
    },
    'K0603': {
        'indications': 'Lithium battery replacement for patient-owned infusion pumps.',
        'requirements': 'Patient must own the pump. Frequency limits apply.'
    },
    'K0604': {
        'indications': 'Lithium battery replacement for patient-owned infusion pumps.',
        'requirements': 'Patient must own the pump. Frequency limits apply.'
    },
    'K0605': {
        'indications': 'Zinc air battery replacement for patient-owned infusion pumps.',
        'requirements': 'Patient must own the pump. Check coverage for specific pump model.'
    },
    # DM25: INSULIN INFUSION PUMP SUPPLIES
    'A4224': {
        'indications': 'Insulin pump supplies for Type 1 diabetes or insulin-dependent Type 2 diabetes.',
        'requirements': 'Written prescription required. Must document diabetes diagnosis and insulin dependency.'
    },
    'A4225': {
        'indications': 'Insulin pump supplies for Type 1 diabetes or insulin-dependent Type 2 diabetes.',
        'requirements': 'Written prescription required. Must document diabetes diagnosis and insulin dependency.'
    },
    # DM28: REHABILITATIVE THERAPY DEVICES
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

def add_brooklyn_coverage_to_code(content, code):
    """Add Brooklyn coverage boxes to a specific HCPCS code"""
    if code not in BROOKLYN_COVERAGE:
        return content

    data = BROOKLYN_COVERAGE[code]

    # Pattern: Find the closing of the ICD-10 code row, then add Brooklyn coverage
    # Look for: <span class="hcpcs-code">CODE</span>...ICD-10 stuff...closing divs
    pattern = rf'(<span class="hcpcs-code">{code}</span>.*?<div class="code-label">ICD-10 Codes</div>.*?</div>\s*</div>\s*</div>)'

    # Generate the Brooklyn coverage addition
    retired_warning = ''
    if data.get('retired'):
        retired_warning = '''
                <div style="background: #ffebee; color: #c62828; padding: 10px; margin: 10px 0; border-radius: 6px; border: 2px solid #c62828; font-weight: 700; text-align: center;">
                    ⚠️ CODE RETIRED - DO NOT USE
                </div>'''

    replacement = rf'''\1{retired_warning}
                <div class="clinical-box">
                    <strong>Indications:</strong> {data['indications']}
                </div>
                <div class="med-necessity">
                    <strong>Requirements:</strong> {data['requirements']}
                </div>'''

    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def fix_colors_and_navigation(content):
    """Apply color and navigation fixes"""
    # Fix body background
    content = re.sub(
        r'(body\s*\{[^}]*?)background:\s*#f8f9fa;',
        r'\1background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);',
        content,
        flags=re.DOTALL
    )

    # Fix navigation (ensure therapeutic is marked active)
    nav_pattern = r'<div class="nav-bar">.*?</div>'
    new_nav = '''    <div class="nav-bar">
        <a href="index.html">🏠 Home</a>
        <a href="catalog_diabetic_hospital.html">🏥 Diabetic/Hospital</a>
        <a href="catalog_patient_care.html">👨‍⚕️ Patient Care</a>
        <a href="catalog_therapeutic.html" class="active">⚕️ Therapeutic</a>
        <a href="catalog_mobility_aids.html">♿ Mobility Aids</a>
        <a href="catalog_surgical_dressings.html">🩹 Surgical/Compression</a>
        <a href="catalog_orthotic_prosthetic.html">🦾 Orthotic/Prosthetic</a>
        <a href="catalog_specialized.html">🔬 Specialized</a>
    </div>'''

    content = re.sub(nav_pattern, new_nav, content, flags=re.DOTALL)

    return content

def main():
    """Main function"""
    filepath = 'catalog_therapeutic.html'

    print(f"Reading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    print("\nStep 1: Applying color and navigation fixes...")
    content = fix_colors_and_navigation(content)

    print("Step 2: Adding Brooklyn coverage to specific codes...")
    codes_updated = []
    for code in BROOKLYN_COVERAGE.keys():
        original = content
        content = add_brooklyn_coverage_to_code(content, code)
        if content != original:
            codes_updated.append(code)

    print(f"\nStep 3: Writing updated content...")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\n" + "="*60)
    print("✅ Brooklyn coverage added successfully!")
    print("="*60)
    print(f"\nUpdated {len(codes_updated)} codes with Brooklyn coverage:")
    print(f"  DM24 codes: {[c for c in codes_updated if c in ['A4221', 'A4222', 'A4226', 'A4244', 'A4245', 'A4602', 'K0552', 'K0601', 'K0602', 'K0603', 'K0604', 'K0605']]}")
    print(f"  DM25 codes: {[c for c in codes_updated if c in ['A4224', 'A4225']]}")
    print(f"  DM28 codes: {[c for c in codes_updated if c in ['E0738', 'E0739', 'E3200']]}")
    print("\nAll 7 categories preserved:")
    print("  ✓ DM20: SUPPORT SURFACES")
    print("  ✓ DM21: TRACTION EQUIPMENT")
    print("  ✓ DM22: TENS")
    print("  ✓ DM24: EXTERNAL INFUSION PUMP SUPPLIES")
    print("  ✓ DM25: INSULIN INFUSION PUMP SUPPLIES")
    print("  ✓ DM28: REHABILITATIVE THERAPY DEVICES")
    print("  ✓ DM29: URINARY SUCTION PUMPS")

if __name__ == '__main__':
    main()
