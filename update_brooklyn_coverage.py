#!/usr/bin/env python3
"""
Update catalog_therapeutic.html with detailed clinical and reimbursement information
from DM24, DM25, DM28.md for Brooklyn physicians.
"""

import re
import json

# Read the markdown file
with open('DM24, DM25, DM28.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Parse the MD file to extract detailed information for each code
code_details = {}

# Split by code sections (###)
code_sections = re.split(r'###\s+\*\*([A-Z0-9]+)\s*-\s*([^*]+)\*\*', md_content)

for i in range(1, len(code_sections), 3):
    if i+1 >= len(code_sections):
        break

    code = code_sections[i].strip()
    description = code_sections[i+1].strip()
    content = code_sections[i+2] if i+2 < len(code_sections) else ""

    # Extract Medicare Clinical Usage
    medicare_clinical = re.search(r'\*\*Medicare Clinical Usage:\*\*\s*([^\n]+(?:\n(?!\*\*)[^\n]+)*)', content)
    medicare_reimb = re.search(r'\*\*Medicare Reimbursement:\*\*\s*([^\n]+(?:\n(?!\*\*)[^\n]+)*)', content)
    medicaid_clinical = re.search(r'\*\*NY Medicaid Clinical Usage:\*\*\s*([^\n]+(?:\n(?!\*\*)[^\n]+)*)', content)
    medicaid_reimb = re.search(r'\*\*NY Medicaid Reimbursement:\*\*\s*([^\n]+(?:\n(?!\*\*)[^\n]+)*)', content)

    code_details[code] = {
        'description': description,
        'medicare_clinical': medicare_clinical.group(1).strip() if medicare_clinical else "",
        'medicare_reimb': medicare_reimb.group(1).strip() if medicare_reimb else "",
        'medicaid_clinical': medicaid_clinical.group(1).strip() if medicaid_clinical else "",
        'medicaid_reimb': medicaid_reimb.group(1).strip() if medicaid_reimb else ""
    }

print(f"Parsed {len(code_details)} codes from MD file")

# Read the current catalog
with open('catalog_therapeutic.html', 'r', encoding='utf-8') as f:
    catalog_content = f.read()

# Function to generate enhanced product card
def generate_enhanced_card(code_info, details):
    """Generate enhanced product card with clinical/reimbursement info"""
    code = code_info['code']

    if code not in details:
        # No additional details, use simple card
        return f"""            <div class="product-card">
                <div class="product-name">{code_info['description']}</div>
                <div class="code-section">
                    <div class="code-row">
                        <div class="code-label">HCPCS Code</div>
                        <div class="code-value"><span class="hcpcs-code">{code}</span></div>
                    </div>
                    <div class="code-row">
                        <div class="code-label">ICD-10 Codes</div>
                        <div class="code-value">Contact for diagnosis-specific codes</div>
                    </div>
                </div>
                <div class="clinical-box">
                    <strong>CLINICAL INDICATIONS:</strong> As prescribed by physician based on medical necessity and clinical presentation. Coverage subject to diagnosis verification.
                </div>
                <div class="med-necessity">
                    <strong>DOCUMENTATION REQUIRED:</strong> Physician prescription with ICD-10 diagnosis • Medical necessity documentation • Prior authorization if applicable • Coverage verification completed
                </div>
            </div>"""

    # Enhanced card with detailed info
    d = details[code]

    # Focus on Brooklyn - use both Medicare and NY Medicaid info
    clinical_info = ""
    if d['medicare_clinical'] and not d['medicare_clinical'].startswith('**CODE RETIRED'):
        clinical_info = d['medicare_clinical']
    elif d['medicaid_clinical']:
        clinical_info = d['medicaid_clinical']

    reimb_info = ""
    if d['medicare_reimb'] and not 'CODE RETIRED' in d['medicare_reimb']:
        reimb_info = f"<strong>Medicare:</strong> {d['medicare_reimb'][:250]}..."

    if d['medicaid_reimb']:
        medicaid_short = d['medicaid_reimb'][:200] + "..." if len(d['medicaid_reimb']) > 200 else d['medicaid_reimb']
        if reimb_info:
            reimb_info += f"<br><strong>NY Medicaid:</strong> {medicaid_short}"
        else:
            reimb_info = f"<strong>NY Medicaid:</strong> {medicaid_short}"

    retired_note = ""
    if 'RETIRED' in d['medicare_clinical'] or 'RETIRED' in d['medicare_reimb']:
        retired_note = '<div style="background: #ffebee; color: #c62828; padding: 8px; border-radius: 4px; margin: 8px 0; font-weight: 600;">⚠️ CODE RETIRED - Not billable. See current alternatives.</div>'

    return f"""            <div class="product-card">
                <div class="product-name">{code_info['description']}</div>
                <div class="code-section">
                    <div class="code-row">
                        <div class="code-label">HCPCS Code</div>
                        <div class="code-value"><span class="hcpcs-code">{code}</span></div>
                    </div>
                    <div class="code-row">
                        <div class="code-label">Brooklyn Coverage</div>
                        <div class="code-value">Medicare & NY Medicaid</div>
                    </div>
                </div>
                {retired_note}
                <div class="clinical-box">
                    <strong>CLINICAL USAGE:</strong> {clinical_info if clinical_info else 'As prescribed by physician based on medical necessity.'}
                </div>
                <div class="med-necessity">
                    {reimb_info if reimb_info else '<strong>DOCUMENTATION:</strong> Physician prescription required • Coverage verification recommended'}
                </div>
            </div>"""

# Load BOC detailed data
with open('boc_detailed_hcpcs_data.json', 'r') as f:
    boc_data = json.load(f)

# Generate new content for DM24, DM25, DM28
def generate_category_section(boc_code, boc_info, code_details):
    """Generate category section with enhanced product cards"""
    if not boc_info or len(boc_info.get('codes', [])) == 0:
        return ""

    cards_html = '\n'.join([generate_enhanced_card(code_info, code_details)
                            for code_info in boc_info['codes']])

    return f"""
    <div class="category-section">
        <div class="category-header">
            {boc_code}: {boc_info['description']} (BOC Category) - Brooklyn Coverage Guide
        </div>
        <div class="product-grid">
{cards_html}
        </div>
    </div>"""

# Find and replace DM24, DM25, DM28 sections in the catalog
print("\nUpdating catalog sections...")

for boc_code in ['DM24', 'DM25', 'DM28']:
    if boc_code in boc_data:
        print(f"Updating {boc_code}...")
        boc_info = boc_data[boc_code]
        new_section = generate_category_section(boc_code, boc_info, code_details)

        # Pattern to find the category section
        pattern = rf'(<div class="category-section">.*?<div class="category-header">\s*{boc_code}:.*?</div>\s*<div class="product-grid">.*?</div>\s*</div>\s*</div>)'

        if re.search(pattern, catalog_content, re.DOTALL):
            catalog_content = re.sub(pattern, new_section, catalog_content, flags=re.DOTALL)
            print(f"  ✓ Updated {boc_code} with {len(boc_info['codes'])} enhanced cards")
        else:
            print(f"  ⚠ Could not find section for {boc_code}")

# Write updated catalog
with open('catalog_therapeutic.html', 'w', encoding='utf-8') as f:
    f.write(catalog_content)

print("\n✅ Catalog updated with Brooklyn coverage information")
print("✅ DM24, DM25, DM28 sections enhanced with clinical and reimbursement details")
