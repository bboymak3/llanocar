import re

with open('/home/z/my-project/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Read the 200 SEO names
seo_names = []
with open('/home/z/my-project/nombres-imagenes-seo.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            # Extract just the filename
            name = line.split('. ', 1)[1] if '. ' in line else line
            seo_names.append(name)

print(f"Total SEO names: {len(seo_names)}")

# Define the replacements
# We need to replace images that are NOT in the "preserve" list
# Preserve: images/imagen/wp-content/uploads/2024/10/*.png and *.svg
# Preserve: https://tapizadodevolantes.pages.dev/*
# Replace everything else

# Get all unique image references to replace
replace_map = {}
name_idx = 0

# Find all images/ references that are NOT imagen/wp-content paths
pattern = r'(src|href)="(images/[^"]+\.(jpg|jpeg|png))"'
matches = list(re.finditer(pattern, content))

for m in matches:
    old_path = m.group(2)
    # Skip preserved paths
    if 'images/imagen/wp-content/uploads/2024/10/' in old_path:
        continue
    if old_path in replace_map:
        continue  # Already assigned a replacement
    replace_map[old_path] = seo_names[name_idx % len(seo_names)]
    name_idx += 1
    print(f"  Replace: {old_path} -> images/{replace_map[old_path]}")

print(f"\nTotal unique replacements: {len(replace_map)}")

# Also handle openModal references
modal_pattern = r"openModal\('(images/[^']+)'\)"
modal_matches = list(re.finditer(modal_pattern, content))
for m in modal_matches:
    old_path = m.group(1)
    if 'images/imagen/wp-content/uploads/2024/10/' in old_path:
        continue
    # The modal image should match the src image, use same replacement
    if old_path not in replace_map:
        replace_map[old_path] = seo_names[name_idx % len(seo_names)]
        name_idx += 1
        print(f"  Replace (modal): {old_path} -> images/{replace_map[old_path]}")

# Now do the replacements
for old_path, new_name in replace_map.items():
    # Replace in src/href attributes
    content = content.replace(f'src="{old_path}"', f'src="images/{new_name}"')
    content = content.replace(f'href="{old_path}"', f'href="images/{new_name}"')
    # Replace in openModal calls
    content = content.replace(f"openModal('{old_path}')", f"openModal('images/{new_name}')")

with open('/home/z/my-project/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n=== REPLACEMENTS DONE ===")
print(f"Total SEO names used: {name_idx}")
