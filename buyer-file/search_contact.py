import sys
with open('about-1.html', 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f):
        if 'contact.html' in line:
            print(f"Line {i+1}: {line.strip()}")
