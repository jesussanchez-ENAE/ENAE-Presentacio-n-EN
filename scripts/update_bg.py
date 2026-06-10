import re

def fix():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find S3
    pattern = r'(<div class="s"[^>]*id="s3"[^>]*>)(.*?)(<!-- ══════════════════════════════════════\n     S5 ·)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        old_div = match.group(1)
        inner_content = match.group(2)
        s5_header = match.group(3)
        
        # Replace the opening div with relative and remove inline background
        new_div = '<div class="s relative" id="s3">'
        
        # Inject the background layers
        bg_layers = """
  <!-- Background Image with Garnet Gradient Overlay -->
  <div class="absolute inset-0 z-0 bg-[url('src/img/ENAE/_0N7A2272.JPG')] bg-center bg-cover"></div>
  <div class="absolute inset-0 z-0 bg-gradient-to-br from-[#3b0610]/95 via-[#5c0b1a]/90 to-[#8a122b]/85"></div>
"""
        # Fix z-index of content wrapper
        inner_content = inner_content.replace('<div class="flex h-full w-full px-16 py-[80px]">', '<div class="flex h-full w-full px-16 py-[80px] relative z-10">')
        
        # Change red boxes to white/10
        inner_content = inner_content.replace('bg-[#bf2639]/30', 'bg-white/10 backdrop-blur-sm border border-white/10')
        inner_content = inner_content.replace('bg-[#b31b2e]/50', 'bg-black/20 backdrop-blur-sm border border-white/5')
        
        # Fix El Mundo to have a white background so it's visible
        # Find: <img src="src/Rankings/El_Mundo_logo.svg.png" class="w-[240px] mb-6 mt-4" alt="El Mundo">
        el_mundo_old = '<img src="src/Rankings/El_Mundo_logo.svg.png" class="w-[240px] mb-6 mt-4" alt="El Mundo">'
        el_mundo_new = """
          <div class="bg-white/90 backdrop-blur-sm rounded-lg p-4 inline-flex items-center justify-center mb-6 mt-4 w-fit">
            <img src="src/Rankings/El_Mundo_logo.svg.png" class="w-[200px]" alt="El Mundo">
          </div>"""
        inner_content = inner_content.replace(el_mundo_old, el_mundo_new)
        
        new_s3 = new_div + bg_layers + inner_content + s5_header
        
        content = content[:match.start()] + new_s3 + content[match.end():]
        
        with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated")
    else:
        print("S3 not found")

fix()
