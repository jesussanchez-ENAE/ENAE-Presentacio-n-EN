import re

file_path = 'ENAE_Presentation_v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <div class="wm" style="...">E</div> 
# With <img src="src/logos/ENAE_Blanco.svg" class="wm" style="...; height:1em; width:auto; opacity:0.06;" alt="E">
def repl(m):
    style = m.group(1)
    if not style.endswith(';'):
        style += ';'
    new_style = style + ' height:1em; width:auto; opacity:0.06;'
    return f'<img src="src/logos/ENAE_Blanco.svg" class="wm" style="{new_style}" alt="E">'

new_content = re.sub(r'<div class="wm" style="([^"]+)">E</div>', repl, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done replacing E")
