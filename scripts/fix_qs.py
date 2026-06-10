import re
import base64

image_path = '/Users/jesus/Documents/GitHub/Plantilla-Dossiers-ENAE/src/Rankings/0faf3965-9e4e-419c-a4cc-2ac0a6a48783.png'
with open(image_path, 'rb') as img_file:
    b64_str = base64.b64encode(img_file.read()).decode('utf-8')
    qs_src = f'data:image/png;base64,{b64_str}'

file_path = 'ENAE_Presentation_v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all <img src="" class="w-32 absolute top-8 left-8" alt="QS"> type empty tags
# Just target src="" where alt="QS" or alt="QS Star"
def repl(m):
    return m.group(0).replace('src=""', f'src="{qs_src}"')

new_content = re.sub(r'<img\s+src=""[^>]*alt="QS( Star)?"[^>]*>', repl, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Done fixing badges")
