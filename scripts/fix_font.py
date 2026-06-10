import re

def fix():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # The exact class pattern:
    # <div class="relative z-10 text-[14px] text-white italic mt-1" style="font-family: var(--fS);">
    pattern = r'(<div class="relative z-10 text-\[14px\] text-white italic mt-1" style=")font-family: var\(--fS\);(")'
    
    # We replace it with "font-family: 'Open Sans', sans-serif;"
    # The class already has 'italic' so we don't need to add font-style: italic in the style tag, 
    # but we can just to be safe if 'italic' class isn't doing it with that font.
    # Actually, tailwind 'italic' applies font-style: italic.
    
    new_content = re.sub(pattern, r'\1font-family: \'Open Sans\', sans-serif;\2', content)
    
    if new_content != content:
        with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated")
    else:
        print("Not found")

fix()
