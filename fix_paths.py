filepath = '/home/felipe/mycodes/felipejunqueira/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix project paths to match real folder names
fixes = [
    ("'./projetos/burger/'", "'./projetos/catalogo-pedidos/'"),
    ("'./projetos/financas/'", "'./projetos/app-financas-pessoais/'"),
    ("'./projetos/consultorio/'", "'./projetos/profissional-saude/'"),
    ("'./projetos/institucional/'", "'./projetos/link-bio-barbearia/'"),  # no portal folder, use barbearia
    ("'./projetos/fidelidade/'", "'./projetos/sistema-fidelidade/'"),
    ("'./projetos/barbearia/'", "'./projetos/link-bio-barbearia/'"),
]

for old, new in fixes:
    content = content.replace(old, new)

# Fix the institucional card - it pointed to barbearia, which is wrong. Let's make it open barbearia properly
# Actually "Portal Institucional" => link-bio-barbearia doesn't make sense. 
# Since there's no actual "institutional portal" project in the repo, let's repurpose it 
# to open the church site which IS institutional:
content = content.replace(
    "openPreview('Portal Institucional','./projetos/link-bio-barbearia/')",
    "window.open('https://felipejunqueira.github.io/iasd-sao-mateus/', '_blank')"
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Paths fixed.")
