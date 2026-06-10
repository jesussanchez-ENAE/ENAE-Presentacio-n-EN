import sys

def patch_file():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the start of the base64 string
    start_str = """<div class="photo photo-overlay-dark" style="background-image:url('data:image/jpeg;base64,"""
    end_str = """')">"""
    
    start_idx = content.find(start_str)
    if start_idx != -1:
        # Find the end of the base64 string
        # We start searching for the closing tag after the start_str
        search_from = start_idx + len(start_str)
        end_idx = content.find(end_str, search_from)
        
        if end_idx != -1:
            # Replace the entire block
            before = content[:start_idx]
            after = content[end_idx + len(end_str):]
            new_div = """<div class="photo photo-overlay-dark" style="background-image:url('src/img/cover.png')">"""
            content = before + new_div + after
            print("Successfully replaced base64 image")
        else:
            print("Could not find end of base64 string")
    else:
        print("Could not find start of base64 string")

    # Font sizes
    content = content.replace('<b style="font-size:90px">Your Gateway to</b>', '<b style="font-size:120px; line-height: 1.1">Your Gateway to</b>')
    content = content.replace('<i style="font-size:108px">Global Business</i>', '<i style="font-size:160px; line-height: 1.1; margin-top: -10px;">Global Business</i>')
    content = content.replace('<l style="font-size:30px">Excellence · Innovation · International Impact</l>', '<l style="font-size:42px; margin-top: 20px;">Excellence · Innovation · International Impact</l>')

    # Increase KPI numbers slightly on cover
    content = content.replace('<div style="font-family:var(--fB);font-weight:800;font-size:54px;color:var(--W);line-height:1">', '<div style="font-family:var(--fB);font-weight:800;font-size:72px;color:var(--W);line-height:1">')


    with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
        f.write(content)

patch_file()
