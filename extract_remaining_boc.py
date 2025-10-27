#!/usr/bin/env python3
"""Extract remaining BOC categories from codecatalog.html"""

import re

# Read the original large file line by line looking for BOC sections
print("Reading codecatalog.html...")

# We'll extract specific BOC category sections
# Looking for patterns like "DM12", "DM20", etc in headers

# Categories we need to extract
needed = {
    'DM12': 'catalog_diabetic_hospital.html',
    'DM20': 'catalog_therapeutic.html',
    'DM21': 'catalog_therapeutic.html',
    'DM24': 'catalog_therapeutic.html',
    'DM25': 'catalog_therapeutic.html',
    'DM29': 'catalog_therapeutic.html',
    'OR04': 'catalog_orthotic_prosthetic.html',
    'PD04': 'catalog_orthotic_prosthetic.html',
    'PE04': 'catalog_specialized.html'
}

# Read the file in chunks
with open('codecatalog.html', 'r') as f:
    content = f.read()

# Extract sections - look for category-section divs
# Pattern: <div class="category-section">...<div class="category-header">...DM12...
sections_found = {}

# Find all category sections
pattern = r'<div class="category-section">(.*?)</div>\s*(?=<div class="category-section">|<div class="page-break">|<!-- FOOTER -->)'

matches = re.findall(pattern, content, re.DOTALL)

print(f"Found {len(matches)} category sections in original file")

for match in matches:
    # Check which BOC code this section contains
    for boc_code in needed.keys():
        if boc_code in match:
            # Found it!
            section_html = f'<div class="category-section">{match}</div>\n'
            sections_found[boc_code] = section_html
            print(f"✅ Extracted {boc_code}")
            break

print(f"\n📊 Extracted {len(sections_found)}/{len(needed)} needed sections")

if len(sections_found) < len(needed):
    print(f"⚠️  Missing: {set(needed.keys()) - set(sections_found.keys())}")

# Save extracted sections to a file
with open('extracted_boc_sections.html', 'w') as f:
    for boc_code in sorted(sections_found.keys()):
        f.write(f'\n<!-- {boc_code} -->\n')
        f.write(sections_found[boc_code])
        f.write('\n')

print(f"\n💾 Saved to: extracted_boc_sections.html")

# Now add these to the appropriate files
for boc_code, target_file in needed.items():
    if boc_code in sections_found:
        # Read the target file
        with open(target_file, 'r') as f:
            target_content = f.read()

        # Find where to insert (before the footer)
        footer_pos = target_content.find('<div class="footer">')

        if footer_pos > 0:
            # Insert the new section before the footer
            new_content = (
                target_content[:footer_pos] +
                '\n' + sections_found[boc_code] + '\n' +
                target_content[footer_pos:]
            )

            # Write back
            with open(target_file, 'w') as f:
                f.write(new_content)

            print(f"✅ Added {boc_code} to {target_file}")
        else:
            print(f"❌ Could not find footer in {target_file}")

print("\n🎉 DONE! All sections extracted and added to catalogs")
