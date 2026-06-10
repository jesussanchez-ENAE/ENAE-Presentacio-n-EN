import re

file_path = 'ENAE_Presentation_v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("background-image:url('src/img/ENAE/_0N7A2272.JPG');", "background-image:url('src/img/portada_Europe.jpg');")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done cover image")
