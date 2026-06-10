import re
import random

file_path = 'ENAE_Presentation_v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Current watermark tags look like:
# <img src="src/logos/ENAE_Blanco.svg" class="wm" style="font-size:580px;right:-80px;top:-80px;; height:1em; width:auto; opacity:0.06;" alt="E">

def repl(m):
    original_tag = m.group(0)
    # Replace the src
    tag = original_tag.replace('src/logos/ENAE_Blanco.svg', 'src/logos/SIMBOLO-ENAE-BLANCO.png')
    
    # Generate a random rotation between -45 and 45 degrees
    rot = random.randint(-45, 45)
    
    # We want to insert transform: rotate(Xdeg); into the style attribute.
    # The style attribute ends with ' opacity:0.06;' or something similar.
    # We can just append to the style attribute.
    
    # Extract the style attribute content
    style_match = re.search(r'style="([^"]+)"', tag)
    if style_match:
        style_content = style_match.group(1)
        if not style_content.endswith(';'):
            style_content += ';'
        # Add a transform
        new_style = style_content + f' transform: rotate({rot}deg);'
        
        # Also maybe shift top/right slightly randomly by adding margins or just using the rotation 
        # which will already make it look different and dynamic.
        tag = tag.replace(f'style="{style_match.group(1)}"', f'style="{new_style}"')
        
    return tag

# Find all watermark images
new_content = re.sub(r'<img src="src/logos/ENAE_Blanco.svg" class="wm" [^>]+>', repl, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done randomized watermarks")
