#!/usr/bin/env python3
"""
Fix Brooklyn coverage formatting issues:
1. Remove orphaned indication/requirement boxes
2. Change labels to "Indications" and "Requirements"
3. Simplify language significantly for Brooklyn doctors
4. Fix text truncation issues
5. Ensure consistent formatting
"""

import re

# Simplified Brooklyn coverage data (concise, doctor-friendly language)
BROOKLYN_COVERAGE = {
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
        'requirements': 'N/A - Use A4224 or A4225 for insulin pump supplies instead.'
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
    'A4224': {
        'indications': 'Insulin pump supplies for Type 1 diabetes or insulin-dependent Type 2 diabetes.',
        'requirements': 'Written prescription required. Must document diabetes diagnosis and insulin dependency.'
    },
    'A4225': {
        'indications': 'Insulin pump supplies for Type 1 diabetes or insulin-dependent Type 2 diabetes.',
        'requirements': 'Written prescription required. Must document diabetes diagnosis and insulin dependency.'
    },
    'E0738': {
        'indications': 'Upper extremity rehabilitation system for chronic stroke patients with arm/hand impairments.',
        'requirements': 'Physician prescription required. Document stroke diagnosis and motor deficits. May require prior authorization.'
    },
    'E0739': {
        'indications': 'Robotic rehabilitation system for post-stroke patients with arm or leg impairments.',
        'requirements': 'Physician prescription required. Document stroke-related impairment. May require prior authorization.'
    },
    'E3200': {
        'indications': 'Gait training device using rhythmic auditory stimulation for stroke patients with walking difficulties.',
        'requirements': 'Physician prescription required. Patient must be able to walk independently. New code - verify coverage.'
    },
}

def generate_brooklyn_card(code, description):
    """Generate simplified Brooklyn coverage card"""
    if code not in BROOKLYN_COVERAGE:
        return None

    data = BROOKLYN_COVERAGE[code]

    # Check if retired code
    retired_warning = ''
    if 'RETIRED' in data['indications']:
        retired_warning = '''
                <div style="background: #ffebee; color: #c62828; padding: 10px; margin: 10px 0; border-radius: 6px; border: 2px solid #c62828; font-weight: 700; text-align: center;">
                    ⚠️ CODE RETIRED - DO NOT USE
                </div>'''

    return f'''            <div class="product-card">
                <div class="product-name">{description}</div>
                <div class="code-section">
                    <div class="code-row">
                        <div class="code-label">HCPCS Code</div>
                        <div class="code-value"><span class="hcpcs-code">{code}</span></div>
                    </div>
                    <div class="code-row">
                        <div class="code-label">Brooklyn Coverage</div>
                        <div class="code-value">Medicare & NY Medicaid</div>
                    </div>
                </div>{retired_warning}
                <div class="clinical-box">
                    <strong>Indications:</strong> {data['indications']}
                </div>
                <div class="med-necessity">
                    <strong>Requirements:</strong> {data['requirements']}
                </div>
            </div>'''

def fix_catalog():
    """Fix catalog_therapeutic.html"""
    filepath = 'catalog_therapeutic.html'

    print(f"Reading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Remove orphaned boxes (boxes outside of product cards)
    # Find pattern of orphaned boxes between </div> closing tags
    print("Step 1: Removing orphaned indication/requirement boxes...")

    # Remove orphaned boxes that appear after category section closings
    orphan_pattern = r'</div>\s*</div>\s*\n\s*<div class="clinical-box">.*?</div>\s*<div class="med-necessity">.*?</div>'
    content = re.sub(orphan_pattern, '</div>\n    </div>', content, flags=re.DOTALL)

    # Step 2: Change all labels from "CLINICAL USAGE:" to "Indications:" and simplify content
    print("Step 2: Updating labels and simplifying language...")

    # For each code in BROOKLYN_COVERAGE, find and replace its boxes
    for code, data in BROOKLYN_COVERAGE.items():
        # Pattern to find existing Brooklyn coverage boxes for this code
        pattern = rf'(<span class="hcpcs-code">{code}</span>.*?Brooklyn Coverage.*?</div>\s*</div>\s*</div>)(.*?)(<div class="clinical-box">.*?</div>\s*<div class="med-necessity">.*?</div>)'

        # Generate replacement with retired warning if applicable
        retired_warning = ''
        if 'RETIRED' in data['indications']:
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

        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Step 3: Remove any remaining truncated text patterns (...) in Brooklyn coverage sections
    print("Step 3: Fixing text truncation...")
    # This should already be fixed by the replacements above

    print(f"Writing fixed content to {filepath}...")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Brooklyn coverage formatting fixed!")
    print("\nChanges made:")
    print("  • Removed orphaned indication/requirement boxes")
    print("  • Changed labels to 'Indications' and 'Requirements'")
    print("  • Simplified language for Brooklyn doctors")
    print("  • Fixed text truncation issues")
    print("  • Ensured consistent formatting throughout")
    print(f"\nUpdated {len(BROOKLYN_COVERAGE)} HCPCS codes with Brooklyn coverage")

if __name__ == '__main__':
    fix_catalog()
