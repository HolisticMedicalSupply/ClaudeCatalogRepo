#!/usr/bin/env python3
"""
Script to extract logo from original codecatalog.html and add it to all catalog files
"""

import re

# Read the original file to extract the logo
with open('codecatalog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the logo img tag
logo_match = re.search(r'<div class="logo-container"[^>]*>\s*<img src="(data:image[^"]+)"[^>]*>', content, re.DOTALL)

if not logo_match:
    print("Could not find logo in codecatalog.html")
    exit(1)

logo_data_url = logo_match.group(1)
print(f"Found logo (data URL length: {len(logo_data_url)} chars)")

# Create the logo HTML to insert
logo_html = f'''        <div class="logo-container" style="flex-shrink: 0;">
            <img src="{logo_data_url}" alt="Holistic Medical Supply Logo" style="height: 60px; width: auto;">
        </div>'''

# List of catalog files to update
catalog_files = [
    'catalog_diabetic_hospital.html',
    'catalog_patient_care.html',
    'catalog_therapeutic.html',
    'catalog_mobility.html',
    'catalog_orthotic_prosthetic.html',
    'catalog_specialized.html',
    'index.html'
]

for filename in catalog_files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            catalog_content = f.read()

        # Check if logo already exists
        if 'data:image' in catalog_content:
            print(f"{filename}: Logo already exists, skipping")
            continue

        # Find the header div and add logo before the company name div
        # Look for: <div class="header"> followed by any whitespace and <div>
        header_pattern = r'(<div class="header">)\s*\n\s*(<div>)'

        if re.search(header_pattern, catalog_content):
            # Insert logo between header div and company name div
            updated_content = re.sub(
                header_pattern,
                r'\1\n' + logo_html + r'\n        \2',
                catalog_content
            )

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(updated_content)

            print(f"{filename}: Logo added successfully")
        else:
            print(f"{filename}: Could not find header pattern to insert logo")

    except FileNotFoundError:
        print(f"{filename}: File not found")
    except Exception as e:
        print(f"{filename}: Error - {e}")

print("\nDone!")
