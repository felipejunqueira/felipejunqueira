import re

filepath = '/home/felipe/mycodes/felipejunqueira/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Felipe Junqueira | Sites & Aplicativos Comerciais', 'Vertex Digital | Sites & Aplicativos')
content = content.replace('felipe.png?v=2', 'logo.jpg?v=1')
content = content.replace('alt="Foto de Felipe Junqueira"', 'alt="Logo da Vertex Digital"')
content = content.replace('<h1 class="hero-title">Felipe Junqueira</h1>', '<h1 class="hero-title">Vertex Digital</h1>')
content = content.replace('<p class="hero-subtitle">Ciência da Computação (UFABC) • Criação de Sites e Aplicativos</p>', '<p class="hero-subtitle">Soluções Web • Criado por Felipe Junqueira</p>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Profile updated successfully.")
