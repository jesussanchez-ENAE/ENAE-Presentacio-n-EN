import sys

def patch_file():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the old strings
    old_bt = '.bt{font-family:var(--fB);font-weight:700;font-size:15px;color:var(--W);margin-bottom:2px}'
    new_bt = '.bt{font-family:var(--fB);font-weight:700;font-size:24px;color:var(--W);margin-bottom:2px}'
    
    old_bd2 = '.bd2{font-family:var(--fB);font-weight:300;font-size:13px;color:rgba(255,255,255,.56);line-height:1.55}'
    new_bd2 = '.bd2{font-family:var(--fB);font-weight:300;font-size:18px;color:rgba(255,255,255,.56);line-height:1.55}'

    # Replace
    content = content.replace(old_bt, new_bt)
    content = content.replace(old_bd2, new_bd2)

    with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
        f.write(content)

patch_file()
