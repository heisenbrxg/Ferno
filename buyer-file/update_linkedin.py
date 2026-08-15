import os
import glob
import re

html_files = glob.glob('*.html')
linkedin_url = 'https://www.linkedin.com/in/dr-ferno-susai-8b12bb166/'

# We will try to find all instances of LinkedIn links and update their href.
# Strategy: find `href="..."` or `href='...'` right before or around `fa-linkedin-in`.
# Because HTML parsing is safer, let's use regex that targets the specific anchor tags containing fa-linkedin-in.

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update the offcanvas menu link (or any link that directly contains `<i class="fab fa-linkedin-in"></i>`)
    # Pattern: `<a href="..."> <i class="fab fa-linkedin-in"></i></a>`
    content = re.sub(
        r'<a href="[^"]*"(>.*?class="fab fa-linkedin-in".*?</a>)',
        rf'<a href="{linkedin_url}" target="_blank"\1',
        content,
        flags=re.DOTALL
    )
    
    # 2. Update the custom-social-btn link
    # Pattern: `<a href="..." class="custom-social-btn" aria-label="LinkedIn"`
    # Or some variant
    content = re.sub(
        r'<a\s+href="[^"]*"\s+class="custom-social-btn"\s+aria-label="LinkedIn"',
        rf'<a href="{linkedin_url}" class="custom-social-btn" aria-label="LinkedIn" target="_blank"',
        content,
        flags=re.IGNORECASE
    )
    
    # 3. Update the index.html and about-1.html specific footer link
    content = re.sub(
        r'<a\s+href="[^"]*"\s+class="custom-social-btn"\s+aria-label="LinkedIn"\s+target="_blank"',
        rf'<a href="{linkedin_url}" class="custom-social-btn" aria-label="LinkedIn" target="_blank"',
        content,
        flags=re.IGNORECASE
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} files.")
