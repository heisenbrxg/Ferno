with open('about-1.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(780, 805):
        print(f"{i+1}: {lines[i]}", end='')
