#!/usr/bin/env python3
"""
Properly rebuild catalog files with:
1. Original navigation, header, and footer content
2. Increased font sizes for readability
3. Complete HCPCS codes from 2025 Q4 crosswalk
4. Smaller, more manageable file sizes
"""

import json
import re

# Load the detailed HCPCS data
print("Loading HCPCS data...")
with open('boc_detailed_hcpcs_data.json', 'r') as f:
    boc_data = json.load(f)

# Enhanced catalog mapping - split large categories
CATALOG_MAPPING = {
    'catalog_diabetic_hospital.html': {
        'title': 'Diabetic & Hospital Equipment',
        'boc_codes': ['DM02', 'DM05', 'DM06', 'DM08', 'DM11', 'DM12'],
        'emoji': '🏥',
        'active': 'catalog_diabetic_hospital.html'
    },
    'catalog_patient_care.html': {
        'title': 'Patient Care Equipment',
        'boc_codes': ['DM13', 'DM14', 'DM15', 'DM16', 'DM17', 'DM18'],
        'emoji': '👨‍⚕️',
        'active': 'catalog_patient_care.html'
    },
    'catalog_therapeutic.html': {
        'title': 'Therapeutic Equipment',
        'boc_codes': ['DM20', 'DM21', 'DM22', 'DM24', 'DM25', 'DM28', 'DM29'],
        'emoji': '⚕️',
        'active': 'catalog_therapeutic.html'
    },
    'catalog_mobility_aids.html': {
        'title': 'Mobility Aids & Wheelchairs',
        'boc_codes': ['M01', 'M05', 'M06', 'M06A', 'M07', 'M07A', 'M10'],
        'emoji': '♿',
        'active': 'catalog_mobility_aids.html'
    },
    'catalog_surgical_dressings.html': {
        'title': 'Surgical Dressings & Compression',
        'boc_codes': ['S01', 'S04'],
        'emoji': '🩹',
        'active': 'catalog_surgical_dressings.html'
    },
    'catalog_orthotic_prosthetic.html': {
        'title': 'Orthotic & Prosthetic Supplies',
        'boc_codes': ['OR03', 'OR04', 'PD04', 'PD08', 'PD09'],
        'emoji': '🦾',
        'active': 'catalog_orthotic_prosthetic.html'
    },
    'catalog_specialized.html': {
        'title': 'Specialized Equipment',
        'boc_codes': ['PE03', 'PE04', 'R07'],
        'emoji': '🔬',
        'active': 'catalog_specialized.html'
    }
}

def generate_css():
    """Generate CSS with larger, more readable fonts"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Holistic Medical Supply</title>
    <style>
        @page {{ size: letter; margin: 0.4in; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: Arial, sans-serif;
            font-size: 10pt;
            line-height: 1.4;
            background: white;
            color: #333;
        }}

        /* HEADER */
        .header {{
            background: linear-gradient(135deg, #1e5a96 0%, #2a6fb8 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 25px;
        }}
        .logo-container {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 25px;
        }}
        .company-name {{ font-size: 32px; font-weight: bold; margin-bottom: 5px; }}
        .tagline {{ font-size: 13px; font-style: italic; }}

        /* NAVIGATION */
        .nav-bar {{
            background: #f0f8ff;
            border: 2px solid #2a6fb8;
            padding: 12px;
            border-radius: 6px;
            margin-bottom: 12px;
            text-align: center;
            font-size: 10pt;
        }}
        .nav-bar a {{
            color: #1e5a96;
            text-decoration: none;
            padding: 6px 12px;
            margin: 0 6px;
            border-radius: 4px;
            font-weight: bold;
            display: inline-block;
        }}
        .nav-bar a:hover {{
            background: #2a6fb8;
            color: white;
        }}
        .nav-bar a.active {{
            background: #1e5a96;
            color: white;
        }}

        /* BOC CREDENTIALS */
        .boc-bar {{
            background: #e8f4f8;
            border: 2px solid #1e5a96;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 15px;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            text-align: center;
        }}
        .boc-item {{
            background: white;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #2a6fb8;
        }}
        .boc-label {{ font-size: 8pt; font-weight: bold; color: #1e5a96; text-transform: uppercase; }}
        .boc-value {{ font-size: 13px; font-weight: bold; color: #1e5a96; margin-top: 4px; }}

        /* CATEGORY SECTIONS */
        .category-section {{
            margin-bottom: 20px;
            page-break-inside: avoid;
        }}
        .category-header {{
            background: linear-gradient(135deg, #1e5a96 0%, #2a6fb8 100%);
            padding: 14px;
            border-radius: 8px;
            margin-bottom: 12px;
            color: white;
            font-size: 18px;
            font-weight: bold;
            box-shadow: 0 3px 6px rgba(0,0,0,0.15);
            text-align: center;
        }}

        /* PRODUCT GRID */
        .product-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 12px;
        }}
        .product-card {{
            background: white;
            border: 1.5px solid #ddd;
            border-radius: 6px;
            padding: 10px;
            page-break-inside: avoid;
        }}
        .product-name {{
            font-weight: bold;
            font-size: 10.5pt;
            margin-bottom: 6px;
            color: #2c3e50;
            border-bottom: 1px solid #e0e0e0;
            padding-bottom: 4px;
        }}
        .code-row {{
            display: flex;
            justify-content: space-between;
            margin: 4px 0;
            font-size: 10pt;
        }}
        .code-label {{
            font-weight: bold;
            color: #555;
            min-width: 110px;
        }}
        .code-value {{
            color: #1e5a96;
            font-weight: 600;
            flex: 1;
            text-align: right;
        }}
        .hcpcs-code {{
            font-size: 11pt;
            font-weight: bold;
        }}
        .clinical-box {{
            background: #f0f8ff;
            padding: 6px;
            margin: 6px 0;
            border-left: 3px solid #2a6fb8;
            font-size: 9.5pt;
        }}
        .med-necessity {{
            font-size: 9pt;
            color: #666;
            margin-top: 6px;
            padding-top: 4px;
            border-top: 1px dashed #ddd;
        }}

        /* FOOTER */
        .footer {{
            background: #f8f9fa;
            border: 2px solid #2a6fb8;
            border-radius: 8px;
            padding: 15px;
            margin-top: 20px;
            font-size: 10pt;
        }}

        /* PRINT STYLES */
        @media print {{
            body {{ font-size: 9pt; }}
            .nav-bar {{ display: none; }}
            .product-card {{ page-break-inside: avoid; }}
            .category-section {{ page-break-inside: avoid; }}
        }}
    </style>
</head>
<body>"""

def generate_navigation(active_page):
    """Generate navigation bar"""
    nav_items = [
        ('index.html', '🏠', 'Home'),
        ('catalog_diabetic_hospital.html', '🏥', 'Diabetic/Hospital'),
        ('catalog_patient_care.html', '👨‍⚕️', 'Patient Care'),
        ('catalog_therapeutic.html', '⚕️', 'Therapeutic'),
        ('catalog_mobility_aids.html', '♿', 'Mobility Aids'),
        ('catalog_surgical_dressings.html', '🩹', 'Surgical/Compression'),
        ('catalog_orthotic_prosthetic.html', '🦾', 'Orthotic/Prosthetic'),
        ('catalog_specialized.html', '🔬', 'Specialized')
    ]

    nav_html = ['    <div class="nav-bar">']
    for page, emoji, label in nav_items:
        active = ' class="active"' if page == active_page else ''
        nav_html.append(f'        <a href="{page}"{active}>{emoji} {label}</a>')
    nav_html.append('    </div>\n')
    return '\n'.join(nav_html)

def generate_boc_bar():
    """Generate BOC credentials bar"""
    return """    <div class="boc-bar">
        <div class="boc-item">
            <div class="boc-label">BOC Accreditation</div>
            <div class="boc-value">Facility #S72641</div>
        </div>
        <div class="boc-item">
            <div class="boc-label">Valid Through</div>
            <div class="boc-value">May 31, 2028</div>
        </div>
        <div class="boc-item">
            <div class="boc-label">NPI Number</div>
            <div class="boc-value">1780490581</div>
        </div>
        <div class="boc-item">
            <div class="boc-label">Categories</div>
            <div class="boc-value">36 BOC Categories</div>
        </div>
    </div>
"""

def generate_product_card(code_info):
    """Generate HTML for a single HCPCS code product card"""
    return f"""            <div class="product-card">
                <div class="product-name">{code_info['description']}</div>
                <div class="code-row">
                    <div class="code-label">HCPCS Code:</div>
                    <div class="code-value hcpcs-code">{code_info['code']}</div>
                </div>
                <div class="code-row">
                    <div class="code-label">Common ICD-10 Codes:</div>
                    <div class="code-value">Contact for specific diagnoses</div>
                </div>
                <div class="clinical-box">
                    <strong>INDICATIONS:</strong> As prescribed by physician based on medical necessity and clinical presentation
                </div>
                <div class="med-necessity">
                    <strong>REQUIRES:</strong> Physician prescription with diagnosis • Medical necessity documentation • Prior authorization if required
                </div>
            </div>"""

def generate_category_section(boc_code, boc_info):
    """Generate HTML for complete BOC category section"""
    if not boc_info or len(boc_info.get('codes', [])) == 0:
        return f"""
    <div class="category-section">
        <div class="category-header">
            {boc_code}: {boc_info.get('description', 'NO CODES AVAILABLE') if boc_info else 'NOT FOUND'} (BOC Category)
        </div>
        <div class="product-grid">
            <div class="product-card">
                <div class="product-name">No HCPCS codes currently available in 2025 Q4 crosswalk</div>
                <div class="clinical-box">
                    Please contact us for product availability and ordering information.
                </div>
            </div>
        </div>
    </div>"""

    # Generate product cards for all codes
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

def generate_footer():
    """Generate footer with contact information"""
    return """
    <div class="footer">
        <div style="font-size: 12pt; font-weight: bold; margin-bottom: 12px; text-align: center;">
            ⚡ STREAMLINED ORDERING PROCESS FOR PHYSICIANS
        </div>
        <div style="font-size: 10pt; line-height: 1.8; margin-bottom: 12px;">
            <strong>1️⃣ WRITE PRESCRIPTION:</strong> Product name or HCPCS code + ICD-10 diagnosis + Duration + Signature<br>
            <strong>2️⃣ FAX TO US:</strong> +1 516-268-96-79 or Email: holistic766@gmail.com<br>
            <strong>3️⃣ WE HANDLE:</strong> Medicare & Medicaid authorizations, medical necessity documentation<br>
            <strong>4️⃣ WE COORDINATE:</strong> Patient contact, device training/fitting, delivery, follow-up care
        </div>
        <div style="font-size: 9pt; color: #555; margin-top: 12px; line-height: 1.6;">
            <strong>ACCREDITATION:</strong> BOC Facility #S72641 (Valid through 5/31/2028) • NPI: 1780490581<br>
            <strong>COMPLIANCE:</strong> 36 DMEPOS Categories Approved • Medicare & Medicaid Enrolled<br>
            <strong>CODES:</strong> All HCPCS codes current 2025-2026 • All ICD-10 codes FY 2026 compliant<br>
            <strong>INSURANCE:</strong> Medicare & Medicaid Only • We do not process private insurance claims<br>
            <strong>SERVICE AREA:</strong> NYC • Brooklyn • Staten Island • Port Washington • Nassau County<br>
            <strong>CONTACT:</strong> 1170 Port Washington Blvd, Port Washington, NY 11050 • Phone: +1 516-810-26-33<br>
            <strong>24/7 FAX:</strong> +1 516-268-96-79 • <strong>EMAIL:</strong> holistic766@gmail.com
        </div>
        <div style="margin-top: 15px; padding-top: 12px; border-top: 2px solid #2a6fb8; font-size: 9pt; text-align: center; color: #1e5a96; font-weight: bold;">
            HOLISTIC MEDICAL SUPPLY • SERVING PHYSICIANS & PATIENTS ACROSS NEW YORK • MEDICARE & MEDICAID CERTIFIED
        </div>
    </div>
</body>
</html>"""

def get_logo_base64():
    """Extract logo from original file"""
    try:
        with open('catalog_specialized.html', 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.search(r'<img src="(data:image[^"]+)"', content)
        if match:
            return match.group(1)
    except:
        pass
    return None

def generate_header(logo_data_url):
    """Generate header with logo"""
    if logo_data_url:
        return f"""
    <div class="header">
        <div class="logo-container">
            <img src="{logo_data_url}" alt="Holistic Medical Supply Logo" style="height: 65px; width: auto;">
            <div>
                <div class="company-name">HOLISTIC MEDICAL SUPPLY</div>
                <div class="tagline">Your Trusted DMEPOS Provider • Medicare & Medicaid Certified</div>
            </div>
        </div>
    </div>
"""
    else:
        return """
    <div class="header">
        <div>
            <div class="company-name">HOLISTIC MEDICAL SUPPLY</div>
            <div class="tagline">Your Trusted DMEPOS Provider • Medicare & Medicaid Certified</div>
        </div>
    </div>
"""

def create_catalog_file(filename, config):
    """Create a complete catalog file"""
    print(f"\nCreating {filename}...")

    logo_data = get_logo_base64()

    # Start building the HTML
    html_parts = []

    # Add CSS and head
    html_parts.append(generate_css().format(title=config['title']))

    # Add header
    html_parts.append(generate_header(logo_data))

    # Add navigation
    html_parts.append(generate_navigation(config['active']))

    # Add BOC bar
    html_parts.append(generate_boc_bar())

    # Add category sections
    total_codes = 0
    for boc_code in config['boc_codes']:
        boc_info = boc_data.get(boc_code)

        # Special handling for DM14
        if boc_code == 'DM14' and not boc_info:
            boc_info = {'description': 'INSULIN', 'codes': []}

        if boc_info:
            section_html = generate_category_section(boc_code, boc_info)
            html_parts.append(section_html)
            codes_count = len(boc_info.get('codes', []))
            total_codes += codes_count
            print(f"  ✓ {boc_code}: {codes_count} codes - {boc_info['description']}")
        else:
            print(f"  ⚠ {boc_code}: Not found in crosswalk")
            section_html = generate_category_section(boc_code, None)
            html_parts.append(section_html)

    # Add footer
    html_parts.append(generate_footer())

    # Write file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_parts))

    print(f"  ✓ Created with {total_codes} HCPCS codes across {len(config['boc_codes'])} BOC categories")
    return total_codes

# Main execution
print("=" * 80)
print("REBUILDING ALL CATALOG FILES WITH PROPER FORMATTING")
print("=" * 80)

grand_total = 0
for filename, config in CATALOG_MAPPING.items():
    total = create_catalog_file(filename, config)
    grand_total += total

print("\n" + "=" * 80)
print(f"✓ ALL CATALOGS CREATED - {grand_total} TOTAL HCPCS CODES")
print(f"✓ Created {len(CATALOG_MAPPING)} catalog files")
print("=" * 80)
