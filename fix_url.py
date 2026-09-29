import re

filepath = '/home/felipe/mycodes/felipejunqueira/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_content = '''          <a href="https://github.com/felipejunqueira/iasd-sao-mateus" target="_blank" class="btn-test-card">
            <i data-lucide="external-link" style="width: 18px; height: 18px;"></i> Ver Projeto Oficial
          </a>'''

new_content = '''          <a href="https://felipejunqueira.github.io/iasd-sao-mateus/" target="_blank" class="btn-test-card">
            <i data-lucide="external-link" style="width: 18px; height: 18px;"></i> Acessar o Site
          </a>'''

content = content.replace(old_content, new_content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("URL fixed successfully.")
