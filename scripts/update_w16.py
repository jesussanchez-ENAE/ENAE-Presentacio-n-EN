import re

file_path = 'ENAE_Presentation_v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("</style>", "\n/* Custom w-16 */\n.w-16 { width: 8rem !important; }\n</style>", 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
