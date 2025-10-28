#!/usr/bin/env python3
"""
Create premium, impressive medical equipment catalogs designed to wow physicians.
Professional design with excellent print quality.
"""

import json
import re

# Load the detailed HCPCS data
print("Loading HCPCS data...")
with open('boc_detailed_hcpcs_data.json', 'r') as f:
    boc_data = json.load(f)

# Catalog configuration
CATALOG_MAPPING = {
    'catalog_diabetic_hospital.html': {
        'title': 'Diabetic & Hospital Equipment',
        'boc_codes': ['DM02', 'DM05', 'DM06', 'DM08', 'DM11', 'DM12'],
        'emoji': '🏥',
        'color': '#1e5a96',
        'active': 'catalog_diabetic_hospital.html'
    },
    'catalog_patient_care.html': {
        'title': 'Patient Care Equipment',
        'boc_codes': ['DM13', 'DM14', 'DM15', 'DM16', 'DM17', 'DM18'],
        'emoji': '👨‍⚕️',
        'color': '#2874a6',
        'active': 'catalog_patient_care.html'
    },
    'catalog_therapeutic.html': {
        'title': 'Therapeutic Equipment',
        'boc_codes': ['DM20', 'DM21', 'DM22', 'DM24', 'DM25', 'DM28', 'DM29'],
        'emoji': '⚕️',
        'color': '#1e5a96',
        'active': 'catalog_therapeutic.html'
    },
    'catalog_mobility_aids.html': {
        'title': 'Mobility Aids & Wheelchairs',
        'boc_codes': ['M01', 'M05', 'M06', 'M06A', 'M07', 'M07A', 'M10'],
        'emoji': '♿',
        'color': '#2874a6',
        'active': 'catalog_mobility_aids.html'
    },
    'catalog_surgical_dressings.html': {
        'title': 'Surgical Dressings & Compression',
        'boc_codes': ['S01', 'S04'],
        'emoji': '🩹',
        'color': '#1e5a96',
        'active': 'catalog_surgical_dressings.html'
    },
    'catalog_orthotic_prosthetic.html': {
        'title': 'Orthotic & Prosthetic Supplies',
        'boc_codes': ['OR03', 'OR04', 'PD04', 'PD08', 'PD09'],
        'emoji': '🦾',
        'color': '#2874a6',
        'active': 'catalog_orthotic_prosthetic.html'
    },
    'catalog_specialized.html': {
        'title': 'Specialized Equipment',
        'boc_codes': ['PE03', 'PE04', 'R07'],
        'emoji': '🔬',
        'color': '#1e5a96',
        'active': 'catalog_specialized.html'
    }
}

def generate_premium_css(title, primary_color):
    """Generate premium CSS with impressive styling"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Holistic Medical Supply</title>
    <style>
        @page {{
            size: letter;
            margin: 0.4in;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Arial, sans-serif;
            font-size: 10pt;
            line-height: 1.5;
            background: #f8f9fa;
            color: #2c3e50;
        }}

        /* ============== PREMIUM HEADER ============== */
        .header {{
            background: linear-gradient(135deg, {primary_color} 0%, #3498db 100%);
            color: white;
            padding: 25px 30px;
            border-radius: 12px;
            margin-bottom: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            position: relative;
            overflow: hidden;
        }}

        .header::before {{
            content: '';
            position: absolute;
            top: -50%;
            right: -10%;
            width: 300px;
            height: 300px;
            background: rgba(255,255,255,0.05);
            border-radius: 50%;
        }}

        .logo-container {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 30px;
            position: relative;
            z-index: 1;
        }}

        .company-info {{
            text-align: center;
        }}

        .company-name {{
            font-size: 36px;
            font-weight: 700;
            letter-spacing: 1px;
            margin-bottom: 8px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}

        .tagline {{
            font-size: 14px;
            font-style: italic;
            opacity: 0.95;
            font-weight: 300;
        }}

        /* ============== NAVIGATION ============== */
        .nav-bar {{
            background: white;
            border: 2px solid {primary_color};
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}

        .nav-bar a {{
            color: {primary_color};
            text-decoration: none;
            padding: 10px 16px;
            margin: 4px 6px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 10pt;
            display: inline-block;
            transition: all 0.3s ease;
            border: 1px solid transparent;
        }}

        .nav-bar a:hover {{
            background: {primary_color};
            color: white;
            transform: translateY(-1px);
            box-shadow: 0 2px 6px rgba(0,0,0,0.15);
        }}

        .nav-bar a.active {{
            background: linear-gradient(135deg, {primary_color}, #3498db);
            color: white;
            border-color: {primary_color};
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }}

        /* ============== BOC CREDENTIALS BAR ============== */
        .boc-bar {{
            background: white;
            border: 2px solid {primary_color};
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}

        .boc-item {{
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            border: 1px solid #dee2e6;
            position: relative;
            overflow: hidden;
        }}

        .boc-item::before {{
            content: '✓';
            position: absolute;
            top: 5px;
            right: 5px;
            color: {primary_color};
            font-size: 12px;
            font-weight: bold;
            opacity: 0.3;
        }}

        .boc-label {{
            font-size: 9pt;
            font-weight: 600;
            color: #6c757d;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 6px;
        }}

        .boc-value {{
            font-size: 14px;
            font-weight: 700;
            color: {primary_color};
            margin-top: 4px;
        }}

        /* ============== CATEGORY SECTIONS ============== */
        .category-section {{
            margin-bottom: 25px;
            page-break-inside: avoid;
        }}

        .category-header {{
            background: linear-gradient(135deg, {primary_color} 0%, #3498db 100%);
            padding: 18px 25px;
            border-radius: 10px;
            margin-bottom: 15px;
            color: white;
            font-size: 20px;
            font-weight: 700;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            text-align: left;
            position: relative;
            overflow: hidden;
        }}

        .category-header::after {{
            content: '';
            position: absolute;
            right: 20px;
            top: 50%;
            transform: translateY(-50%);
            width: 60px;
            height: 60px;
            background: rgba(255,255,255,0.1);
            border-radius: 50%;
        }}

        /* ============== PREMIUM PRODUCT CARDS ============== */
        .product-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 15px;
        }}

        .product-card {{
            background: white;
            border: 1px solid #e0e0e0;
            border-left: 4px solid {primary_color};
            border-radius: 10px;
            padding: 18px;
            page-break-inside: avoid;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            transition: all 0.3s ease;
            position: relative;
        }}

        .product-card:hover {{
            box-shadow: 0 4px 16px rgba(0,0,0,0.12);
            transform: translateY(-2px);
        }}

        .product-card::before {{
            content: '📋';
            position: absolute;
            top: 15px;
            right: 15px;
            font-size: 20px;
            opacity: 0.15;
        }}

        .product-name {{
            font-weight: 700;
            font-size: 11pt;
            margin-bottom: 12px;
            color: #2c3e50;
            line-height: 1.4;
            padding-right: 30px;
        }}

        .code-section {{
            background: #f8f9fa;
            padding: 12px;
            border-radius: 6px;
            margin: 10px 0;
            border: 1px solid #e9ecef;
        }}

        .code-row {{
            display: flex;
            align-items: center;
            margin: 6px 0;
            font-size: 10pt;
        }}

        .code-label {{
            font-weight: 600;
            color: #6c757d;
            min-width: 140px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .code-label::before {{
            content: '▸';
            color: {primary_color};
            font-weight: bold;
        }}

        .code-value {{
            color: {primary_color};
            font-weight: 700;
            flex: 1;
        }}

        .hcpcs-code {{
            background: {primary_color};
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 11pt;
            font-weight: 700;
            letter-spacing: 0.5px;
            display: inline-block;
        }}

        .clinical-box {{
            background: linear-gradient(135deg, #e3f2fd 0%, #f0f8ff 100%);
            padding: 10px 12px;
            margin: 10px 0;
            border-left: 3px solid {primary_color};
            border-radius: 6px;
            font-size: 9.5pt;
            line-height: 1.6;
        }}

        .clinical-box strong {{
            color: {primary_color};
            font-weight: 700;
        }}

        .med-necessity {{
            font-size: 9pt;
            color: #6c757d;
            margin-top: 10px;
            padding: 10px;
            background: #fff9e6;
            border-radius: 6px;
            border: 1px dashed #ffc107;
            line-height: 1.6;
        }}

        .med-necessity strong {{
            color: #f57c00;
            font-weight: 700;
        }}

        /* ============== PREMIUM FOOTER ============== */
        .footer {{
            background: white;
            border: 2px solid {primary_color};
            border-radius: 12px;
            padding: 25px;
            margin-top: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}

        .footer-title {{
            font-size: 14pt;
            font-weight: 700;
            margin-bottom: 15px;
            text-align: center;
            color: {primary_color};
            padding-bottom: 12px;
            border-bottom: 2px solid {primary_color};
        }}

        .ordering-steps {{
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
        }}

        .ordering-steps div {{
            font-size: 10pt;
            line-height: 2;
            padding: 4px 0;
        }}

        .contact-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-top: 15px;
            font-size: 9pt;
            line-height: 1.8;
        }}

        .contact-item {{
            padding: 8px;
            background: #f8f9fa;
            border-radius: 6px;
            border-left: 3px solid {primary_color};
        }}

        .contact-item strong {{
            color: {primary_color};
            font-weight: 700;
        }}

        .footer-seal {{
            margin-top: 20px;
            padding-top: 15px;
            border-top: 2px solid {primary_color};
            font-size: 10pt;
            text-align: center;
            color: {primary_color};
            font-weight: 700;
            letter-spacing: 0.5px;
        }}

        /* ============== PRINT STYLES ============== */
        @media print {{
            body {{
                background: white;
                font-size: 9pt;
            }}
            .nav-bar {{
                display: none;
            }}
            .product-card {{
                page-break-inside: avoid;
                box-shadow: none;
            }}
            .product-card:hover {{
                transform: none;
                box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            }}
            .category-section {{
                page-break-inside: avoid;
            }}
            .footer {{
                page-break-inside: avoid;
            }}
        }}
    </style>
</head>
<body>"""

def generate_navigation(active_page):
    """Generate premium navigation bar"""
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
    """Generate premium BOC credentials bar"""
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
            <div class="boc-label">BOC Categories</div>
            <div class="boc-value">36 Categories</div>
        </div>
    </div>
"""

def generate_product_card(code_info):
    """Generate premium product card"""
    return f"""            <div class="product-card">
                <div class="product-name">{code_info['description']}</div>
                <div class="code-section">
                    <div class="code-row">
                        <div class="code-label">HCPCS Code</div>
                        <div class="code-value"><span class="hcpcs-code">{code_info['code']}</span></div>
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

def generate_category_section(boc_code, boc_info):
    """Generate premium category section"""
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
                    <strong>CONTACT US:</strong> Please call our office for product availability and ordering information. We may be able to special order items in this category.
                </div>
            </div>
        </div>
    </div>"""

    # Generate product cards
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
    """Generate premium footer"""
    return """
    <div class="footer">
        <div class="footer-title">
            ⚡ STREAMLINED PHYSICIAN ORDERING PROCESS
        </div>
        <div class="ordering-steps">
            <div><strong>STEP 1:</strong> Write prescription with HCPCS code or product name + ICD-10 diagnosis + Duration + Signature</div>
            <div><strong>STEP 2:</strong> Fax to +1 516-268-96-79 or email to holistic766@gmail.com</div>
            <div><strong>STEP 3:</strong> We handle all Medicare/Medicaid authorizations and medical necessity documentation</div>
            <div><strong>STEP 4:</strong> We coordinate patient contact, device training/fitting, delivery, and follow-up care</div>
        </div>
        <div class="contact-grid">
            <div class="contact-item">
                <strong>ACCREDITATION:</strong> BOC Facility #S72641 (Valid through 5/31/2028) • NPI: 1780490581
            </div>
            <div class="contact-item">
                <strong>COMPLIANCE:</strong> 36 DMEPOS Categories Approved • Medicare & Medicaid Enrolled
            </div>
            <div class="contact-item">
                <strong>CODES:</strong> All HCPCS codes current 2025-2026 • All ICD-10 codes FY 2026 compliant
            </div>
            <div class="contact-item">
                <strong>INSURANCE:</strong> Medicare & Medicaid Only • We do not process private insurance claims
            </div>
            <div class="contact-item">
                <strong>SERVICE AREA:</strong> NYC • Brooklyn • Staten Island • Port Washington • Nassau County
            </div>
            <div class="contact-item">
                <strong>CONTACT:</strong> 1170 Port Washington Blvd, Port Washington, NY 11050 • Phone: +1 516-810-26-33
            </div>
        </div>
        <div style="text-align: center; margin-top: 15px; font-size: 10pt;">
            <strong>24/7 FAX:</strong> +1 516-268-96-79 • <strong>EMAIL:</strong> holistic766@gmail.com
        </div>
        <div class="footer-seal">
            🏆 HOLISTIC MEDICAL SUPPLY • SERVING PHYSICIANS & PATIENTS ACROSS NEW YORK • MEDICARE & MEDICAID CERTIFIED
        </div>
    </div>
</body>
</html>"""

def get_logo_base64():
    """Extract logo from existing file"""
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
    """Generate premium header with logo"""
    if logo_data_url:
        return f"""
    <div class="header">
        <div class="logo-container">
            <img src="{logo_data_url}" alt="Holistic Medical Supply Logo" style="height: 70px; width: auto; filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.3));">
            <div class="company-info">
                <div class="company-name">HOLISTIC MEDICAL SUPPLY</div>
                <div class="tagline">Your Trusted DMEPOS Provider • Medicare & Medicaid Certified • Serving NY Since 2020</div>
            </div>
        </div>
    </div>
"""
    else:
        return """
    <div class="header">
        <div class="company-info">
            <div class="company-name">HOLISTIC MEDICAL SUPPLY</div>
            <div class="tagline">Your Trusted DMEPOS Provider • Medicare & Medicaid Certified • Serving NY Since 2020</div>
        </div>
    </div>
"""

def create_premium_catalog(filename, config):
    """Create a premium catalog file"""
    print(f"\nCreating premium {filename}...")

    logo_data = get_logo_base64()
    html_parts = []

    # Build the catalog
    html_parts.append(generate_premium_css(config['title'], config['color']))
    html_parts.append(generate_header(logo_data))
    html_parts.append(generate_navigation(config['active']))
    html_parts.append(generate_boc_bar())

    # Add category sections
    total_codes = 0
    for boc_code in config['boc_codes']:
        boc_info = boc_data.get(boc_code)

        if boc_code == 'DM14' and not boc_info:
            boc_info = {'description': 'INSULIN', 'codes': []}

        if boc_info:
            section_html = generate_category_section(boc_code, boc_info)
            html_parts.append(section_html)
            codes_count = len(boc_info.get('codes', []))
            total_codes += codes_count
            print(f"  ✓ {boc_code}: {codes_count} codes - {boc_info['description']}")
        else:
            print(f"  ⚠ {boc_code}: Not found")
            section_html = generate_category_section(boc_code, None)
            html_parts.append(section_html)

    html_parts.append(generate_footer())

    # Write file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_parts))

    print(f"  ✓ Premium catalog created with {total_codes} HCPCS codes")
    return total_codes

# Main execution
print("=" * 80)
print("CREATING PREMIUM MEDICAL EQUIPMENT CATALOGS")
print("Professional design that will impress physicians")
print("=" * 80)

grand_total = 0
for filename, config in CATALOG_MAPPING.items():
    total = create_premium_catalog(filename, config)
    grand_total += total

print("\n" + "=" * 80)
print(f"✅ ALL PREMIUM CATALOGS CREATED")
print(f"✅ {grand_total} HCPCS codes across {len(CATALOG_MAPPING)} catalogs")
print(f"✅ Professional design • Print-optimized • Web-ready")
print("=" * 80)
