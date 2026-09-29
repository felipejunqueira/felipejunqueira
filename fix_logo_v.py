filepath = '/home/felipe/mycodes/felipejunqueira/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('logo.jpg?v=1', 'logo.jpg?v=2')
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Logo version bumped.")
