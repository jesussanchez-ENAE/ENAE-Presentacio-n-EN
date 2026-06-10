import re

file_path = 'ENAE_Presentation_v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<div class="s" id="s2"')
end_idx = content.find('id="s3"', start_idx)

section = content[start_idx:end_idx]
section = section.replace('font-size:17px', 'font-size:24px')

content = content[:start_idx] + section + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done updating font size")
