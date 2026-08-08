import sys, re
with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f):
        if 'btn' in line:
            print(f"Line {i+1}: {line.strip()}")
