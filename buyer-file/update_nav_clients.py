import os
import re

buyer_dir = r"e:\ADES FINAL\ades\buyer-file"

# Regex pattern matching Company dropdown with FAQ and Our Clients
pattern = re.compile(
    r'<li class="has-dropdown">\s*<a href="#">\s*Company\s*<i class="fa-solid fa-chevron-down"></i>\s*</a>\s*<ul class="submenu">\s*<li><a href="faq\.html">FAQ</a></li>\s*<li><a href="clients\.html">Our Clients</a></li>\s*</ul>\s*</li>',
    re.MULTILINE
)

replacement = '''<li>
                                                <a href="clients.html">Our Clients</a>
                                            </li>'''

modified_files = []

for root, dirs, files in os.walk(buyer_dir):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            new_content, count = pattern.subn(replacement, content)
            if count > 0:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                modified_files.append((f, count))

print(f"Updated {len(modified_files)} files:")
for mf, c in modified_files:
    print(f"  {mf}: {c} replacement(s)")
