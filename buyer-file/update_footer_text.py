import os
import re

target_text = '<p style="font-size: 17px; line-height: 1.8;">ADES is a multidisciplinary MEP consultancy delivering innovative, reliable, and cost-effective engineering solutions across commercial, industrial, and institutional projects worldwide.</p>'

pattern = re.compile(
    r'<p\s+(?:class="footer-tagline"\s+)?style="[^"]*font-size:[^"]*">\s*(?:ADES|Engineering Excellence)[^<]*</p>',
    re.IGNORECASE | re.DOTALL
)

buyer_dir = r"e:\ADES FINAL\ades\buyer-file"
modified_count = 0

for filename in os.listdir(buyer_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(buyer_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Check if file has custom-footer-bg or footer tagline
        if "custom-footer-bg" in content or "footer-tagline" in content:
            # Replace paragraph in left info block
            # Match <p style="..."> containing ADES or AirDesign or Engineering Excellence
            new_content = re.sub(
                r'<p\s+style="font-size:\s*\d+px;[^"]*">\s*ADES[^<]*</p>',
                target_text,
                content,
                flags=re.IGNORECASE | re.DOTALL
            )
            # Also match multi-line <p style="...">ADES ... </p>
            new_content = re.sub(
                r'<p\s+style="font-size:\s*\d+px;[^"]*">\s*ADES.*?</p>',
                target_text,
                new_content,
                flags=re.IGNORECASE | re.DOTALL
            )
            # Also match key-highlights <p style="font-size:14px;line-height:1.9;color:#ffffff;">Engineering Excellence...</p>
            new_content = re.sub(
                r'<p\s+style="font-size:\s*14px;line-height:1\.9;color:#ffffff;">Engineering Excellence.*?</p>',
                target_text,
                new_content,
                flags=re.IGNORECASE | re.DOTALL
            )
            # Also match ades-creative footer-tagline
            new_content = re.sub(
                r'<p\s+class="footer-tagline"[^>]*>.*?</p>',
                '<p class="footer-tagline" style="margin-top:8px; font-size:17px; line-height:1.8;">ADES is a multidisciplinary MEP consultancy delivering innovative, reliable, and cost-effective engineering solutions across commercial, industrial, and institutional projects worldwide.</p>',
                new_content,
                flags=re.IGNORECASE | re.DOTALL
            )

            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                modified_count += 1
                print(f"Updated: {filename}")

print(f"Total HTML files updated: {modified_count}")
