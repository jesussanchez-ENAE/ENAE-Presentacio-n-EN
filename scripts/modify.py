import re

file_path = 'ENAE_Presentation_v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Image Background & Gradient
# Modify the image div to be 100% width in the S5 section
start_idx = content.find('<div class="s" id="s4">')
end_idx = content.find('id="s5"', start_idx)
if end_idx == -1: end_idx = len(content)

section = content[start_idx:end_idx]

section = section.replace('width:30%;background:url', 'width:100%;background:url')

overlay_old = 'right:30%;top:0;bottom:0;width:100px;background:linear-gradient(90deg,var(--N2) 0%,transparent 100%);z-index:1'
overlay_new = 'inset:0;background:linear-gradient(to right, var(--N2) 0%, rgba(0,0,0,0.8) 45%, transparent 100%);z-index:1'
section = section.replace(overlay_old, overlay_new)

# 3. Modify text blocks
section = section.replace('font-size:14px;', 'font-size:20px;')
section = section.replace('font-size:11px;', 'font-size:14px;')
section = section.replace('font-size:12px;', 'font-size:15px;')

content = content[:start_idx] + section + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
