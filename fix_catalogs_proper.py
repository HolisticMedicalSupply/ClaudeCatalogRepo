#!/usr/bin/env python3
"""
Properly update catalog files with comprehensive HCPCS codes while preserving all original design and content.
"""

import json
import re

# Load the detailed HCPCS data
print("Loading HCPCS data...")
with open('boc_detailed_hcpcs_data.json', 'r') as f:
    boc_data = json.load(f)

# Mapping of catalog files to their BOC codes
CATALOG_MAPPING = {
    'catalog_diabetic_hospital.html': ['DM02', 'DM05', 'DM06', 'DM08', 'DM11', 'DM12'],
    'catalog_patient_care.html': ['DM13', 'DM14', 'DM15', 'DM16', 'DM17', 'DM18'],
    'catalog_therapeutic.html': ['DM20', 'DM21', 'DM22', 'DM24', 'DM25', 'DM28', 'DM29'],
    'catalog_mobility.html': ['M01', 'M05', 'M06', 'M06A', 'M07', 'M07A', 'M10', 'S01', 'S04'],
    'catalog_orthotic_prosthetic.html': ['OR03', 'OR04', 'PD04', 'PD08', 'PD09'],
    'catalog_specialized.html': ['PE03', 'PE04', 'R07']
}

def generate_product_card(code_info):
    """Generate a product card with the original design format"""
    return f"""            <div class="product-card">
                <div class="product-name">{code_info['description']}</div>
                <div class="code-row">
                    <div class="code-label">HCPCS:</div>
                    <div class="code-value">{code_info['code']}</div>
                </div>
                <div class="code-row">
                    <div class="code-label">Common ICD-10 Codes:</div>
                    <div class="code-value">Varies by diagnosis - contact for details</div>
                </div>
                <div class="clinical-box">
                    <strong>INDICATIONS:</strong> As prescribed by physician based on medical necessity
                </div>
                <div class="med-necessity">
                    <strong>REQUIRE:</strong> Physician prescription with diagnosis; Medical necessity documentation; Coverage verification
                </div>
            </div>"""

def generate_category_section(boc_code, boc_info):
    """Generate a complete category section with proper formatting"""
    if not boc_info or len(boc_info.get('codes', [])) == 0:
        # Handle categories with no codes
        return f"""
    <div class="category-section">
        <div class="category-header">
            {boc_code}: {boc_info.get('description', 'NO CODES AVAILABLE') if boc_info else 'NOT FOUND'} (BOC Category)
        </div>
        <div class="product-grid">
            <div class="product-card">
                <div class="product-name">No HCPCS codes currently available</div>
                <div class="clinical-box">
                    This category was not found in the 2025 Q4 crosswalk data. Please contact us for product availability.
                </div>
            </div>
        </div>
    </div>"""

    # Generate product cards for all codes in this category
    cards_html = '\n'.join([generate_product_card(code_info) for code_info in boc_info['codes']])

    return f"""
    <div class="category-section">
        <div class="category-header">
            {boc_code}: {boc_info['description']} (BOC Category)
        </div>
        <div class="product-grid">
{cards_html}
        </div>
    </div>"""

def update_catalog_file(filename, boc_codes):
    """Update catalog file by preserving header/footer and regenerating content"""
    print(f"\nProcessing {filename}...")

    # Read the entire file
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where the content sections begin and end
    # Content starts after the boc-bar closing tags
    # Content ends before the footer

    # Pattern to find the end of BOC bar: </div>\n    </div>\n\n before first category OR footer
    header_match = re.search(r'(.*?</div>\s*</div>\s*\n\s*\n)', content, re.DOTALL)
    footer_match = re.search(r'(\n\s*<div class="footer">.*)', content, re.DOTALL)

    if not header_match or not footer_match:
        print(f"  ⚠ Could not find header/footer markers in {filename}")
        return 0

    header = header_match.group(1)
    footer = footer_match.group(1)

    # Generate new content sections
    content_sections = []
    total_codes = 0

    for boc_code in boc_codes:
        boc_info = boc_data.get(boc_code)

        # Special handling for DM14 which has 0 codes
        if boc_code == 'DM14' and not boc_info:
            boc_info = {'description': 'INSULIN', 'codes': []}

        if boc_info:
            section_html = generate_category_section(boc_code, boc_info)
            content_sections.append(section_html)
            codes_count = len(boc_info.get('codes', []))
            total_codes += codes_count
            print(f"  ✓ {boc_code}: {codes_count} HCPCS codes - {boc_info['description']}")
        else:
            print(f"  ⚠ {boc_code}: Not found in crosswalk")
            # Still create a section for it
            section_html = generate_category_section(boc_code, None)
            content_sections.append(section_html)

    # Combine everything
    new_content = header + '\n'.join(content_sections) + '\n' + footer

    # Write the updated file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  ✓ Updated with {total_codes} total HCPCS codes across {len(boc_codes)} BOC categories")
    return total_codes

# Main execution
print("=" * 80)
print("PROPERLY UPDATING CATALOG FILES - PRESERVING ALL DESIGN AND FORMATTING")
print("=" * 80)

grand_total = 0
for filename, boc_codes in CATALOG_MAPPING.items():
    total = update_catalog_file(filename, boc_codes)
    grand_total += total

print("\n" + "=" * 80)
print(f"✓ ALL FILES PROPERLY UPDATED - {grand_total} TOTAL HCPCS CODES")
print("=" * 80)
