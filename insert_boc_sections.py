#!/usr/bin/env python3
"""Insert new BOC sections into codecatalog.html before the footer."""

# Read the original file
with open('/home/user/ClaudeCatalogRepo/codecatalog.html', 'r') as f:
    original_lines = f.readlines()

# Read the new BOC sections
with open('/home/user/ClaudeCatalogRepo/new_boc_sections.html', 'r') as f:
    new_content = f.read()

# Find the footer line (line 3897, 0-indexed = 3896)
footer_index = None
for i, line in enumerate(original_lines):
    if '<!-- FOOTER -->' in line:
        footer_index = i
        break

if footer_index is None:
    print("❌ ERROR: Could not find footer marker")
    exit(1)

# Insert new content before footer
before_footer = ''.join(original_lines[:footer_index])
footer_and_after = ''.join(original_lines[footer_index:])

# Combine
updated_content = before_footer + '\n' + new_content + '\n\n' + footer_and_after

# Write back
with open('/home/user/ClaudeCatalogRepo/codecatalog.html', 'w') as f:
    f.write(updated_content)

print(f"✅ Successfully inserted new BOC sections")
print(f"📍 Insertion point: line {footer_index + 1}")
print(f"📊 New content added before footer")
