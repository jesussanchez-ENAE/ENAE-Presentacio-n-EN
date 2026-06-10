with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the img tag in S4
old_img = 'class="max-h-[100%] max-w-[80%] drop-shadow-2xl object-contain filter invert brightness-0"'
new_img = 'class="w-full h-full object-contain drop-shadow-2xl max-h-[700px]"'

content = content.replace(old_img, new_img)

with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Map fixed")
