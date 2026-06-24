import os
import re

directory = r"e:\ADES FINAL\ades\buyer-file"
files = [f for f in os.listdir(directory) if f.endswith(".html")]

address_new = "109, Godavari Street, Chinmaya Nagar, Chennai - 600 092, Tamilnadu"
phone_new = "+91 97909 51112"
phone_new_link = "tel:+919790951112"
email_new = "info@ades.in"
email_new_link = "mailto:info@ades.in"

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace emails
    content = re.sub(r'info@ades\.pro', email_new, content, flags=re.IGNORECASE)
    content = re.sub(r'ferno@ades\.in', email_new, content, flags=re.IGNORECASE)
    content = re.sub(r'info@ades\.digital', email_new, content, flags=re.IGNORECASE)
    content = re.sub(r'Info\.Company@Yahoo\.Mail\.Com<br>Hi@Ades\.Com', email_new, content, flags=re.IGNORECASE)
    
    # Replace phones
    content = re.sub(r'\+91-44-4265 8822', phone_new, content)
    content = re.sub(r'\+91-97909 51112', phone_new, content)
    content = re.sub(r'\+91 98765 43210<br>\+91 44 1234 5678', phone_new, content)
    content = re.sub(r'\+91 0321 5098 003<br>\+88 0123 987(\s*258 002)?', phone_new, content)
    content = re.sub(r'tel:\+91-97909 51112', phone_new_link, content)
    
    # Replace addresses
    content = re.sub(r'Building No\. 16, 2nd Floor, 3rd Cross Street, Indira Nagar, Adyar, Chennai -\s*600 020', address_new, content)
    content = re.sub(r'No\. 19, 2nd Cross Street, Lake Area, Nungambakkam, Chennai - 34', address_new, content)
    content = re.sub(r'260/8, Anbu Colony,<br>Anna Nagar West, Chennai 600 040', address_new, content)
    content = re.sub(r'260/8, Anbu Colony,\s*Anna Nagar West,\s*Chennai 600 040', address_new, content)
    content = re.sub(r'260/8 Anbu Colony, Anna Nagar West, Chennai 600 040', address_new, content)
    content = re.sub(r'Adyar, Chennai, India', address_new, content)
    content = re.sub(r'731 Madison Ave, New York,\s*NY<br>10065 New York City', address_new, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

print("Site-wide contact info standardization complete.")
