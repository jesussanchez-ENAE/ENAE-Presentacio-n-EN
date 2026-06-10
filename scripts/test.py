with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<div class="photo photo-overlay-dark" style="background-image:url(\'data:image/jpeg;base64,')
print("Start found at:", start_idx)
if start_idx != -1:
    end_idx = content.find('">', start_idx + 1000)
    print("End found at:", end_idx)
    print("End context:", content[end_idx-20:end_idx+20])
