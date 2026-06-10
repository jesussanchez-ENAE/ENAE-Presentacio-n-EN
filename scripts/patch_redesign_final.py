import sys

def patch_file():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the start of the base64 string
    start_str = """<div class="photo photo-overlay-dark" style="background-image:url('data:image/jpeg;base64,"""
    
    start_idx = content.find(start_str)
    if start_idx != -1:
        # Find the closing tag
        search_from = start_idx + len(start_str)
        end_idx = content.find('"></div>', search_from)
        
        if end_idx != -1:
            # Replace the entire block
            before = content[:start_idx]
            after = content[end_idx + len('"></div>'):]
            new_div = """<div class="photo photo-overlay-dark" style="background-image:url('src/img/cover.png'); background-position: center; background-size: cover;"></div>"""
            content = before + new_div + after
            print("Successfully replaced base64 image")
        else:
            print("Could not find end of base64 string")
    else:
        print("Could not find start of base64 string")


    with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
        f.write(content)

patch_file()
