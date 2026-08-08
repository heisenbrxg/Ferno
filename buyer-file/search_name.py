import sys
with open('about-1.html', 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f):
        if 'ferno' in line.lower() or 'director' in line.lower():
            print(f"Line {i+1}: {line.strip()}")
