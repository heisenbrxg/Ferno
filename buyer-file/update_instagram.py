import os
import glob

html_files = glob.glob('*.html')
count = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace href="#" for the Instagram link.
    # The pattern is:
    # <a href="#" class="custom-social-btn" aria-label="Instagram">
    
    target = '<a href="#" class="custom-social-btn" aria-label="Instagram">'
    replacement = '<a href="https://www.instagram.com/ades_pvt_ltd?igsh=cThlNms1ZXd4dHVt" target="_blank" class="custom-social-btn" aria-label="Instagram">'
    
    if target in content:
        new_content = content.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {filepath}")

print(f"Total files updated: {count}")
