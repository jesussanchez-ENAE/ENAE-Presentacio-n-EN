import re

file_path = 'ENAE_Presentation_v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<div class="s" id="s4">')
end_idx = content.find('id="s5"', start_idx)
if end_idx == -1: end_idx = len(content)

section = content[start_idx:end_idx]
section = section.replace('center/cover"', 'center/contain"')

content = content[:start_idx] + section + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done background-size")
