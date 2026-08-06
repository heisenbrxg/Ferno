import os
import re

directory = r"e:\ADES FINAL\ades\buyer-file"

MAPS_COLUMN = '''                                        <div class="col-lg-4 col-md-6 mb-4">
                                            <h4 class="custom-footer-title">Find Us</h4>
                                            <div style="border-radius:12px;overflow:hidden;border:1px solid rgba(201,243,29,0.25);box-shadow:0 12px 30px rgba(0,0,0,0.35);">
                                                <iframe
                                                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d876.0992403053899!2d80.19890902823073!3d13.093883422794834!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a526132ab06fca5%3A0x6b2e3c74a534b563!2sairdesign%20engineered%20solutions%20pvt%20ltd!5e0!3m2!1sen!2sin!4v1785415122396!5m2!1sen!2sin"
                                                    width="600" height="450"
                                                    style="border:0;width:100%;height:200px;display:block;"
                                                    allowfullscreen="" loading="lazy"
                                                    referrerpolicy="strict-origin-when-cross-origin"></iframe>
                                            </div>
                                        </div>'''

BMS_NAV_ITEM = '                                                    <li><a href="service-bms.html">BMS &amp; IBMS</a></li>'

# Patterns to find/replace in nav submenu (What We Do)
NAV_OLD = '''                                                    <li><a href="service-phe.html">Public Health Engineering</a></li>
                                                    <li><a href="service-2.html">All Services</a></li>'''
NAV_NEW = '''                                                    <li><a href="service-phe.html">Public Health Engineering</a></li>
                                                    <li><a href="service-bms.html">BMS &amp; IBMS</a></li>
                                                    <li><a href="service-2.html">All Services</a></li>'''

# index.html footer uses different structure - "Main Services" column + "Office" column + Newsletter
# service-*.html use "Our Services" column + Contact column + Maps

def update_file(filepath, filename):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    changed = False

    # ── 1. NAV SUBMENU: Add BMS & IBMS ──────────────────────────────────────
    if 'service-bms.html' not in content:
        if NAV_OLD in content:
            content = content.replace(NAV_OLD, NAV_NEW)
            changed = True
            print(f"  [nav] Updated submenu in {filename}")

    # ── 2. FOOTER SERVICES LIST: Add BMS & IBMS ─────────────────────────────
    # Pattern A: "Main Services" column ending without BMS (index.html style)
    footer_a_old = '''                                                <li><a href="service-phe.html">Public Health Engineering</a></li>
                                            </ul>
                                        </div>
                                        <div class="col-lg-3 col-md-6 mb-4">
                                            <h4 class="custom-footer-title">Office</h4>'''
    footer_a_new = '''                                                <li><a href="service-phe.html">Public Health Engineering</a></li>
                                                <li><a href="service-bms.html">BMS &amp; IBMS</a></li>
                                            </ul>
                                        </div>
                                        <div class="col-lg-3 col-md-6 mb-4">
                                            <h4 class="custom-footer-title">Office</h4>'''
    if footer_a_old in content:
        content = content.replace(footer_a_old, footer_a_new)
        changed = True
        print(f"  [footer-services-A] Updated in {filename}")

    # ── 3. NEWSLETTER → MAPS replacement ────────────────────────────────────
    # Match newsletter block (col-lg-4 col-md-6 mb-4 with Newsletter heading)
    newsletter_pattern = re.compile(
        r'(<div class="col-lg-4 col-md-6 mb-4">\s*<h4 class="custom-footer-title">Newsletter</h4>.*?</div>\s*</div>)',
        re.DOTALL
    )
    # Also match "Office" column + Newsletter column combo (index.html)
    # Replace entire "Office" + "Newsletter" pair with "Contact" + "Find Us"
    office_newsletter_pattern = re.compile(
        r'<div class="col-lg-3 col-md-6 mb-4">\s*<h4 class="custom-footer-title">Office</h4>\s*<ul class="custom-footer-link">.*?</ul>\s*</div>\s*<div class="col-lg-4 col-md-6 mb-4">\s*<h4 class="custom-footer-title">Newsletter</h4>.*?</div>\s*</div>',
        re.DOTALL
    )

    CONTACT_AND_MAPS = '''                                        <div class="col-lg-3 col-md-6 mb-4">
                                            <h4 class="custom-footer-title">Contact</h4>
                                            <ul class="custom-footer-link">
                                                <li><a href="#">Chennai, India</a></li>
                                                <li><a href="tel:+919790951112">+91-97909 51112</a></li>
                                                <li><a href="mailto:ferno@ades.in">ferno@ades.in</a></li>
                                                <li><a href="mailto:info@ades.in">info@ades.in</a></li>
                                                <li><a href="http://www.ades.in" target="_blank">www.ades.in</a></li>
                                            </ul>
                                        </div>
''' + MAPS_COLUMN + '''
                                    </div>'''

    if office_newsletter_pattern.search(content):
        content = office_newsletter_pattern.sub(CONTACT_AND_MAPS, content)
        changed = True
        print(f"  [footer-office+newsletter→contact+maps] Updated in {filename}")
    elif newsletter_pattern.search(content):
        # Just replace the Newsletter column with Find Us map
        content = newsletter_pattern.sub(MAPS_COLUMN + '\n                                    </div>', content)
        changed = True
        print(f"  [footer-newsletter→maps] Updated in {filename}")

    if changed and content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✅ Saved {filename}")
    elif not changed:
        print(f"  — No changes needed for {filename}")
    else:
        print(f"  ⚠ No actual difference after processing {filename}")


# Process all HTML files
html_files = [f for f in os.listdir(directory) if f.endswith(".html")]
print(f"Processing {len(html_files)} HTML files...\n")
for filename in sorted(html_files):
    filepath = os.path.join(directory, filename)
    print(f"▶ {filename}")
    try:
        update_file(filepath, filename)
    except Exception as e:
        print(f"  ❌ ERROR in {filename}: {e}")

print("\nDone.")
