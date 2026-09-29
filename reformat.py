import re
import os

filepath = '/home/felipe/mycodes/felipejunqueira/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Section Reordering
# Find "Como Posso Te Ajudar?" section
help_section_match = re.search(r'<!-- O QUE POSSO FAZER -->(.*?)<!-- TODOS OS PROJETOS UNIFICADOS -->', content, re.DOTALL)
if help_section_match:
    help_section = help_section_match.group(0).replace('<!-- TODOS OS PROJETOS UNIFICADOS -->', '')
    content = content.replace(help_section, '') # Remove from original place
    
    # Insert before "BRINCADEIRA RÁPIDA: JOGO DA VELHA NA PÁGINA"
    insert_point = '<!-- BRINCADEIRA RÁPIDA: JOGO DA VELHA NA PÁGINA -->'
    content = content.replace(insert_point, help_section + '\n    ' + insert_point)

# 2. Rename Projects
renames = [
    ('Metalúrgica Alfa | Soluções Industriais', 'Site de Metalúrgica'),
    ('>Metalúrgica Alfa<', '>Site de Metalúrgica<'),
    ('Dra. Fernanda Roberta | Fonoaudiologia', 'Site de Fonoaudiologia'),
    ('>Dra. Fernanda Fonoaudiologia<', '>Site de Fonoaudiologia<'),
    ('Maison Nilo | Boutique de Moda', 'Loja de Roupa'),
    ('>Maison Nilo Boutique<', '>Loja de Roupa<'),
    ('Junqueira & Associados Advocacia', 'Site de Advocacia'),
    ('Forno D\'Ouro | Panificação & Café', 'Site de Padaria'),
    ('>Padaria Artesanal Forno D\'Ouro<', '>Site de Padaria<'),
    ('PDV Caixa Express | Sistema de Caixa', 'Sistema de PDV para Mercado'),
    ('>PDV Frente de Caixa Mercadinho<', '>Sistema de PDV para Mercado<'),
    ('Bazar Centro | Vitrine de Loja', 'Vitrine de Loja'),
    ('>Bazar Centro Comercial<', '>Vitrine de Loja<'),
    ('>Cardápio Burger Express<', '>Catálogo de Pedidos<'),
    ('>Barbearia e Salão<', '>Site de Barbearia<'),
    ('>Barbearia & Salão<', '>Site de Barbearia<'),
    ('Nexo Finance | App Financeiro', 'App de Finanças Pessoais'),
    ('>Nexo Finance Web<', '>App de Finanças Pessoais<'),
    ('Consultório Médico & Saúde', 'Site Médico e de Clínicas'),
    ('Cartão Fidelidade Digital', 'Sistema de Fidelidade'),
    ('>Cartão Fidelidade<', '>Sistema de Fidelidade<'),
    ('Site Oficial da Igreja IASD', 'Site de Igreja'),
    ('>Site Oficial da Igreja<', '>Site de Igreja<'),
    ('Jogo da Velha Moderno', 'Jogo da Velha (Modo Moderno)'),
    ('Jogo da Velha Clássico', 'Jogo da Velha (Modo Retrô)'),
    ('>Jogo da Velha<', '>Jogo da Velha (Modo Moderno)<'),
    ('>Tic-Tac-Toe Multi-Linguagem<', '>Portfólio de Códigos (Tic-Tac-Toe)<'),
]

for old, new in renames:
    content = content.replace(old, new)

# 3. CSS Variables to Light Mode
css_vars_old = """    :root {
      --bg-main: #0c111d;
      --bg-card: #161f30;
      --bg-card-hover: #1c283f;
      --primary: #2563eb;
      --primary-hover: #1d4ed8;
      --primary-light: #93c5fd;
      --green-wa: #16a34a;
      --green-wa-hover: #15803d;
      --text-white: #ffffff;
      --text-light: #f1f5f9;
      --text-muted: #94a3b8;
      --border-soft: rgba(255, 255, 255, 0.08);"""

css_vars_new = """    :root {
      --bg-main: #f8fafc;
      --bg-card: #ffffff;
      --bg-card-hover: #f1f5f9;
      --primary: #2563eb;
      --primary-hover: #1d4ed8;
      --primary-light: #3b82f6;
      --green-wa: #16a34a;
      --green-wa-hover: #15803d;
      --text-white: #0f172a;
      --text-light: #334155;
      --text-muted: #64748b;
      --border-soft: rgba(0, 0, 0, 0.08);"""
content = content.replace(css_vars_old, css_vars_new)

# 4. Hardcoded colors replacements
content = content.replace('background: rgba(255, 255, 255, 0.05)', 'background: rgba(0, 0, 0, 0.03)')
content = content.replace('background: rgba(255, 255, 255, 0.12)', 'background: rgba(0, 0, 0, 0.06)')
content = content.replace('background: rgba(255, 255, 255, 0.04)', 'background: rgba(0, 0, 0, 0.02)')
content = content.replace('background: rgba(255, 255, 255, 0.08)', 'background: rgba(0, 0, 0, 0.04)')
content = content.replace('background: rgba(255, 255, 255, 0.06)', 'background: rgba(0, 0, 0, 0.04)')
content = content.replace('border: 1px solid rgba(255, 255, 255, 0.15)', 'border: 1px solid rgba(0, 0, 0, 0.1)')
content = content.replace('border: 1px solid rgba(255, 255, 255, 0.12)', 'border: 1px solid rgba(0, 0, 0, 0.08)')
content = content.replace('border: 2px solid rgba(255, 255, 255, 0.1)', 'border: 2px solid rgba(0, 0, 0, 0.06)')
content = content.replace('background: #090d16;', 'background: #f1f5f9;')

# Update specific elements that need dark text now
content = content.replace('color: #ffffff;\n      border: none;', 'color: var(--text-white);\n      border: none;')
# .btn-outline
content = content.replace('.btn-outline {\n      background: rgba(0, 0, 0, 0.03);\n      color: #ffffff;', '.btn-outline {\n      background: #ffffff;\n      color: var(--text-white);')
content = content.replace('color: #cbd5e1;', 'color: var(--text-light);')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Formatting applied successfully.")
