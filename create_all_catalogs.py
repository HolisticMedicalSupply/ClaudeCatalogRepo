#!/usr/bin/env python3
"""Create all catalog HTML files with complete BOC coverage."""

import re

# HTML template with print optimization
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Holistic Medical Supply</title>
    <style>
        @page {{ size: letter; margin: 0.35in; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: Arial, sans-serif;
            font-size: 8.5pt;
            line-height: 1.2;
            background: white;
            color: #333;
        }}

        /* HEADER */
        .header {{
            background: linear-gradient(135deg, #1e5a96 0%, #2a6fb8 100%);
            color: white;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
        }}
        .company-name {{ font-size: 28px; font-weight: bold; margin-bottom: 5px; }}
        .tagline {{ font-size: 11px; font-style: italic; }}

        /* NAVIGATION */
        .nav-bar {{
            background: #f0f8ff;
            border: 2px solid #2a6fb8;
            padding: 10px;
            border-radius: 6px;
            margin-bottom: 10px;
            text-align: center;
            font-size: 8pt;
        }}
        .nav-bar a {{
            color: #1e5a96;
            text-decoration: none;
            padding: 5px 10px;
            margin: 0 5px;
            border-radius: 4px;
            font-weight: bold;
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
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 10px;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            text-align: center;
        }}
        .boc-item {{
            background: white;
            padding: 8px;
            border-radius: 5px;
            border: 1px solid #2a6fb8;
        }}
        .boc-label {{ font-size: 7pt; font-weight: bold; color: #1e5a96; text-transform: uppercase; }}
        .boc-value {{ font-size: 11px; font-weight: bold; color: #1e5a96; margin-top: 3px; }}

        /* CATEGORY SECTIONS */
        .category-section {{
            margin-bottom: 15px;
            page-break-inside: avoid;
        }}
        .category-header {{
            background: linear-gradient(135deg, #1e5a96 0%, #2a6fb8 100%);
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 10px;
            color: white;
            font-size: 16px;
            font-weight: bold;
            box-shadow: 0 3px 6px rgba(0,0,0,0.15);
            text-align: center;
        }}

        /* PRODUCT GRID */
        .product-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            margin-bottom: 10px;
        }}
        .product-card {{
            background: white;
            border: 1.5px solid #ddd;
            border-radius: 6px;
            padding: 8px;
            page-break-inside: avoid;
        }}
        .product-name {{
            font-weight: bold;
            font-size: 9pt;
            margin-bottom: 5px;
            color: #2c3e50;
            border-bottom: 1px solid #e0e0e0;
            padding-bottom: 3px;
        }}
        .code-row {{
            display: grid;
            grid-template-columns: 60px 1fr;
            gap: 5px;
            margin-bottom: 4px;
            font-size: 7.5pt;
        }}
        .code-label {{
            font-weight: bold;
            color: #555;
        }}
        .code-value {{
            color: #1e5a96;
            font-weight: 600;
        }}
        .clinical-box {{
            background: #f0f8ff;
            padding: 5px;
            border-radius: 4px;
            font-size: 7.5pt;
            margin: 5px 0;
            border-left: 2px solid #1e5a96;
        }}
        .med-necessity {{
            background: #e8f4f8;
            padding: 5px;
            border-radius: 4px;
            font-size: 7.5pt;
            margin: 5px 0;
            border-left: 2px solid #ffc107;
        }}

        /* FOOTER */
        .footer {{
            background: #f8f9fa;
            border: 2px solid #2a6fb8;
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
            font-size: 8pt;
            line-height: 1.6;
            page-break-inside: avoid;
        }}
        .footer strong {{ color: #1e5a96; }}

        /* PRINT OPTIMIZATION */
        @media print {{
            body {{ background: white; }}
            .nav-bar {{ display: none; }}
            .page-break {{ page-break-before: always; }}
        }}

        @media screen {{
            body {{ padding: 10px; background: #f5f5f5; }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <div>
            <div class="company-name">Holistic Medical Supply</div>
            <div class="tagline">{subtitle}</div>
        </div>
    </div>

    <div class="nav-bar">
        <a href="index.html">🏠 Home</a>
        <a href="catalog_diabetic_hospital.html" {nav1}>🏥 Diabetic/Hospital</a>
        <a href="catalog_patient_care.html" {nav2}>👨‍⚕️ Patient Care</a>
        <a href="catalog_therapeutic.html" {nav3}>⚕️ Therapeutic</a>
        <a href="catalog_mobility.html" {nav4}>♿ Mobility</a>
        <a href="catalog_orthotic_prosthetic.html" {nav5}>🦾 Orthotic/Prosthetic</a>
        <a href="catalog_specialized.html" {nav6}>🔬 Specialized</a>
    </div>

    <div class="boc-bar">
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

    {content}

    <div class="footer">
        <div style="font-size: 11pt; font-weight: bold; margin-bottom: 10px; text-align: center;">
            ⚡ STREAMLINED ORDERING PROCESS FOR PHYSICIANS
        </div>
        <div style="font-size: 9pt; line-height: 1.8; margin-bottom: 10px;">
            <strong>1️⃣ WRITE PRESCRIPTION:</strong> Product name or HCPCS code + ICD-10 diagnosis + Duration + Signature<br>
            <strong>2️⃣ FAX TO US:</strong> +1 516-268-96-79 or Email: holistic766@gmail.com<br>
            <strong>3️⃣ WE HANDLE:</strong> Medicare & Medicaid authorizations, medical necessity documentation<br>
            <strong>4️⃣ WE COORDINATE:</strong> Patient contact, device training/fitting, delivery, follow-up care
        </div>
        <div style="font-size: 8pt; color: #555; margin-top: 10px; line-height: 1.6;">
            <strong>ACCREDITATION:</strong> BOC Facility #S72641 (Valid through 5/31/2028) • NPI: 1780490581<br>
            <strong>COMPLIANCE:</strong> 36 DMEPOS Categories Approved • Medicare & Medicaid Enrolled<br>
            <strong>CODES:</strong> All HCPCS codes current 2025-2026 • All ICD-10 codes FY 2026 compliant<br>
            <strong>INSURANCE:</strong> Medicare & Medicaid Only • We do not process private insurance claims<br>
            <strong>SERVICE AREA:</strong> NYC • Brooklyn • Staten Island • Port Washington • Nassau County<br>
            <strong>CONTACT:</strong> 1170 Port Washington Blvd, Port Washington, NY 11050 • Phone: +1 516-810-26-33<br>
            <strong>24/7 FAX:</strong> +1 516-268-96-79 • <strong>EMAIL:</strong> holistic766@gmail.com
        </div>
        <div style="margin-top: 15px; padding-top: 10px; border-top: 2px solid #2a6fb8; font-size: 8pt; text-align: center; color: #1e5a96; font-weight: bold;">
            HOLISTIC MEDICAL SUPPLY • SERVING PHYSICIANS & PATIENTS ACROSS NEW YORK • MEDICARE & MEDICAID CERTIFIED
        </div>
    </div>
</body>
</html>'''

# Load the new BOC sections
with open('new_boc_sections.html', 'r') as f:
    new_content = f.read()

# Parse into category sections
sections = {}
pattern = r'<!-- (DM\d+|M\d+A?|OR\d+|PD\d+|PE\d+|R\d+|S\d+):(.*?)-->(.*?)(?=<!-- |$)'
matches = re.findall(pattern, new_content, re.DOTALL)

for boc_code, title, content in matches:
    sections[boc_code.strip()] = f'<!-- {boc_code.strip()}: {title.strip()} -->{content}'

print(f"✅ Parsed {len(sections)} new BOC sections")

# Define catalog file groupings
catalogs = {
    'catalog_diabetic_hospital.html': {
        'title': 'Diabetic & Hospital Equipment',
        'subtitle': 'Diabetic Equipment, Hospital Beds, Commodes, IPPB, Lymphedema',
        'nav_active': 'nav1',
        'boc_codes': ['DM02', 'DM05', 'DM06', 'DM08', 'DM11', 'DM12']
    },
    'catalog_patient_care.html': {
        'title': 'Patient Care Equipment',
        'subtitle': 'Patient Lifts, Catheters, Infusion Pumps, Nebulizers, Ventilators, Suction',
        'nav_active': 'nav2',
        'boc_codes': ['DM13', 'DM14', 'DM15', 'DM16', 'DM17', 'DM18']
    },
    'catalog_therapeutic.html': {
        'title': 'Therapeutic Equipment',
        'subtitle': 'TENS, Traction, Lymphedema, Infusion Supplies, CPAP/BiPAP, Dialysis',
        'nav_active': 'nav3',
        'boc_codes': ['DM20', 'DM21', 'DM22', 'DM24', 'DM25', 'DM28', 'DM29']
    },
    'catalog_mobility.html': {
        'title': 'Mobility Equipment',
        'subtitle': 'Canes, Crutches, Walkers, Wheelchairs, Power Scooters',
        'nav_active': 'nav4',
        'boc_codes': ['M01', 'M05', 'M06', 'M06A', 'M07', 'M07A', 'M10', 'S01', 'S04']
    },
    'catalog_orthotic_prosthetic.html': {
        'title': 'Orthotic & Prosthetic Equipment',
        'subtitle': 'Urological Supplies, Prosthetics, Neurostimulators, Ostomy',
        'nav_active': 'nav5',
        'boc_codes': ['OR03', 'OR04', 'PD04', 'PD08', 'PD09']
    },
    'catalog_specialized.html': {
        'title': 'Specialized Equipment',
        'subtitle': 'Paraffin Bath, Patient Lifts, Apnea Monitors',
        'nav_active': 'nav6',
        'boc_codes': ['PE03', 'PE04', 'R07']
    }
}

# Create each catalog file
for filename, config in catalogs.items():
    # Collect content for this catalog
    catalog_content = []
    for boc_code in config['boc_codes']:
        if boc_code in sections:
            catalog_content.append(sections[boc_code])
        else:
            print(f"⚠️  Warning: {boc_code} not found in sections")

    # Set active nav
    nav_params = {f'nav{i}': '' for i in range(1, 7)}
    nav_params[config['nav_active']] = 'class="active"'

    # Generate HTML
    html = HTML_TEMPLATE.format(
        title=config['title'],
        subtitle=config['subtitle'],
        content='\n'.join(catalog_content),
        **nav_params
    )

    # Write file
    with open(filename, 'w') as f:
        f.write(html)

    print(f"✅ Created {filename} with {len(config['boc_codes'])} BOC categories")

print(f"\n🎉 ALL CATALOG FILES CREATED!")
print(f"📄 Total: 6 catalog files + 1 index page")
