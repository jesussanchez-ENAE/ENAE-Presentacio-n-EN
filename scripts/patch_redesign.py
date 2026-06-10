import sys
import re

def patch_file():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace the base64 image in s1
    # We find the <div class="s on" id="s1"> and its inner <div class="photo photo-overlay-dark" style="background-image:url(...)">
    # Because base64 is huge, we can use regex to replace everything inside url(...)
    
    # Let's find the exact block for s1
    pattern = r'(<div class="s on" id="s1">\s*<div class="photo photo-overlay-dark" style="background-image:url\()\'data:image/[^\']+\'\)(">)'
    content = re.sub(pattern, r"\1'src/img/cover.png'\2", content)
    
    # 2. Increase font sizes in s1
    # We know the specific texts
    content = content.replace('<b style="font-size:90px">Your Gateway to</b>', '<b style="font-size:120px; line-height: 1.1">Your Gateway to</b>')
    content = content.replace('<i style="font-size:108px">Global Business</i>', '<i style="font-size:160px; line-height: 1.1; margin-top: -10px;">Global Business</i>')
    content = content.replace('<l style="font-size:30px">Excellence · Innovation · International Impact</l>', '<l style="font-size:42px; margin-top: 20px;">Excellence · Innovation · International Impact</l>')

    # 3. Increase KPI numbers slightly on cover
    content = content.replace('<div style="font-family:var(--fB);font-weight:800;font-size:54px;color:var(--W);line-height:1">', '<div style="font-family:var(--fB);font-weight:800;font-size:72px;color:var(--W);line-height:1">')

    with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
        f.write(content)

patch_file()
