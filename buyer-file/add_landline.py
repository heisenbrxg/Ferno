import os
import re

directory = r"e:\ADES FINAL\ades\buyer-file"

def update_file(filepath, filename):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    changed = False

    # 1. Update the footer 'Contact' list (ul > li)
    pattern1 = re.compile(r'(<li>\s*<a href="tel:\+919790951112">[^<]*\+91-97909 51112</a>\s*</li>)')
    if pattern1.search(content):
        if "+91-44-3578 7146" not in content[content.find("+91-97909 51112"):]:
            replacement1 = r'\1\n                                                <li><a href="tel:+914435787146">+91-44-3578 7146</a></li>'
            content = pattern1.sub(replacement1, content)
            changed = True

    # 2. Update the custom contact card in footer
    # Find: <div class="custom-contact-text">+91 97909 51112</div> OR <div class="custom-contact-text"><a ...>+91 97909 51112</a></div>
    pattern2 = re.compile(r'(<div class="custom-contact-text">)(.*?97909 51112.*?)(</div>)', re.DOTALL | re.IGNORECASE)
    matches2 = pattern2.findall(content)
    for m in matches2:
        if "3578" not in m[1]:
            old_str = "".join(m)
            # If it has <a> tag, do link formatting, otherwise just raw text
            if "</a>" in m[1]:
                new_inner = m[1].strip() + ' / <a href="tel:+914435787146">+91-44-3578 7146</a>'
            else:
                new_inner = m[1].strip() + ' / +91-44-3578 7146'
            new_str = f'{m[0]}{new_inner}{m[2]}'
            content = content.replace(old_str, new_str)
            changed = True

    # 3. Update offcanvas contact
    # <div class="offcanvas__contact-text">\n                                    <a href="tel:+919790951112">+91 97909 51112</a>\n                                </div>
    pattern3 = re.compile(r'(<div class="offcanvas__contact-text">\s*<a href="tel:\+919790951112">\+91 97909 51112</a>\s*)(</div>)', re.IGNORECASE)
    if pattern3.search(content):
        content = pattern3.sub(r'\1 / <a href="tel:+914435787146">+91-44-3578 7146</a>\2', content)
        changed = True

    if changed and content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filename}")

html_files = [f for f in os.listdir(directory) if f.endswith(".html")]
print(f"Processing {len(html_files)} HTML files...")
for filename in html_files:
    filepath = os.path.join(directory, filename)
    update_file(filepath, filename)
print("Done.")
