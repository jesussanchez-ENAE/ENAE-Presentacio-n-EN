import re

def process():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the Financial Magazine logo
    fm_match = re.search(r'src="(data:image/png;base64,[^"]+)".*?alt="Financial Magazine"', content)
    if not fm_match:
        fm_match = re.search(r'alt="Financial Magazine".*?src="(data:image/png;base64,[^"]+)"', content)
    fm_b64 = fm_match.group(1) if fm_match else ""

    # Find El Mundo logo
    em_match = re.search(r'alt="El Mundo".*?src="(data:image/png;base64,[^"]+)"', content)
    if not em_match:
        em_match = re.search(r'src="(data:image/png;base64,[^"]+)".*?alt="El Mundo"', content)
    em_b64 = em_match.group(1) if em_match else ""

    # Find QS logo
    qs_match = re.search(r'<img src="(data:image/png;base64,[a-zA-Z0-9+/=]+)"', content[content.find('QS World'):content.find('QS World')+2000])
    qs_b64 = qs_match.group(1) if qs_match else ""

    new_s3 = f"""
<!-- ══════════════════════════════════════
     S3 · RANKINGS (MERGED)
═══════════════════════════════════════ -->
<div class="s bg-enae-red text-white flex flex-col p-12 overflow-hidden relative" id="s3">
  <!-- Top bar -->
  <div class="flex justify-between w-full uppercase tracking-[0.2em] text-sm font-bold text-white/50 mb-12">
    <div>08 Reconocimientos</div>
    <div style="font-family: var(--fB);">08 / 08</div>
  </div>

  <div class="flex flex-1 gap-12 h-full">
    
    <!-- LEFT COLUMN -->
    <div class="flex flex-col w-[40%] gap-6">
      <div class="text-xl italic text-white/70" style="font-family: var(--fS);">Reconocimiento internacional</div>
      <div class="text-[70px] font-black leading-tight" style="font-family: var(--fB);">Entre las mejores<br>del mundo.</div>
      <div class="w-16 h-[2px] bg-white my-2"></div>
      
      <!-- Big QS Card -->
      <div class="flex-1 bg-black/20 backdrop-blur-md rounded-2xl border border-white/10 p-10 flex flex-col justify-end relative overflow-hidden mt-6">
        <img src="{qs_b64}" class="w-32 absolute top-8 left-8" alt="QS">
        <div class="absolute right-[-20px] top-1/2 -translate-y-1/2 text-[200px] font-black text-white/10 leading-none" style="font-family: var(--fB);">09</div>
        <div class="uppercase tracking-widest text-xs text-white/50 font-bold mb-4" style="font-family: var(--fB);">QS World University Rankings - Marketing 2026</div>
        <div class="text-[80px] font-black leading-none mb-2 z-10" style="font-family: var(--fB);">#09</div>
        <div class="text-xl font-bold z-10" style="font-family: var(--fB);">Máster en Marketing Digital<br><span class="italic font-light" style="font-family: var(--fS);">con Mención en Inteligencia Artificial</span></div>
      </div>

      <!-- 3 Bottom Cards -->
      <div class="grid grid-cols-3 gap-4 mt-2">
        <div class="bg-black/20 backdrop-blur-md rounded-xl border border-white/10 p-6 relative overflow-hidden">
          <div class="text-5xl font-black mb-2" style="font-family: var(--fB);">#06</div>
          <div class="text-[11px] text-white/70 italic mb-4" style="font-family: var(--fS);">Mejores Escuelas de Negocio</div>
          <div class="text-[10px] font-bold tracking-widest" style="font-family: var(--fB);">FORBES 2025</div>
        </div>
        <div class="bg-black/20 backdrop-blur-md rounded-xl border border-white/10 p-6 relative overflow-hidden flex flex-col justify-between">
          <div>
            <div class="text-5xl font-black mb-2" style="font-family: var(--fB);">#06</div>
            <div class="text-[11px] text-white/70 italic mb-4" style="font-family: var(--fS);">Esc. Negocios España</div>
          </div>
          <img src="{fm_b64}" class="w-32" alt="FM">
        </div>
        <div class="bg-black/20 backdrop-blur-md rounded-xl border border-white/10 p-6 relative overflow-hidden flex flex-col justify-between">
          <div class="text-lg font-bold leading-tight mb-2" style="font-family: var(--fB);">Mejores<br>MBA<br><span class="text-[11px] text-white/70 font-normal italic" style="font-family: var(--fS);">de España</span></div>
          <img src="{em_b64}" class="w-32" alt="El Mundo">
        </div>
      </div>
    </div>

    <!-- RIGHT COLUMN -->
    <div class="flex flex-col w-[60%] gap-4">
      
      <!-- Top badges row -->
      <div class="flex gap-4 mb-2 justify-around bg-black/10 rounded-2xl p-6 border border-white/5 backdrop-blur-sm items-center">
        <img src="{qs_b64}" class="h-24" alt="QS Star">
        <img src="{qs_b64}" class="h-16 opacity-70" alt="QS Star">
        <img src="{qs_b64}" class="h-16 opacity-70" alt="QS Star">
        <img src="{qs_b64}" class="h-16 opacity-70" alt="QS Star">
        <img src="{qs_b64}" class="h-16 opacity-70" alt="QS Star">
      </div>

      <!-- Grid of Masters -->
      <div class="grid grid-cols-2 gap-4 flex-1">
        
        <div class="bg-white/5 backdrop-blur-md rounded-xl border border-white/10 p-6 relative overflow-hidden flex items-center">
          <div class="absolute right-[-10px] top-1/2 -translate-y-1/2 text-[100px] font-black text-white/5 leading-none" style="font-family: var(--fB);">#10</div>
          <img src="{qs_b64}" class="w-16 mr-6 z-10" alt="QS">
          <div class="z-10">
            <div class="font-bold text-[16px] leading-tight mb-1" style="font-family: var(--fB);">Máster en IA y Data Science</div>
            <div class="text-xs text-white/50 italic" style="font-family: var(--fS);">España</div>
          </div>
        </div>

        <div class="bg-white/5 backdrop-blur-md rounded-xl border border-white/10 p-6 relative overflow-hidden flex items-center">
          <div class="absolute right-[-10px] top-1/2 -translate-y-1/2 text-[100px] font-black text-white/5 leading-none" style="font-family: var(--fB);">#06</div>
          <img src="{qs_b64}" class="w-16 mr-6 z-10" alt="QS">
          <div class="z-10">
            <div class="font-bold text-[16px] leading-tight mb-1" style="font-family: var(--fB);">Logística y Dirección de<br>Operaciones</div>
            <div class="text-xs text-white/50 italic" style="font-family: var(--fS);">España</div>
          </div>
        </div>

        <div class="bg-white/5 backdrop-blur-md rounded-xl border border-white/10 p-6 relative overflow-hidden flex items-center">
          <div class="absolute right-[-10px] top-1/2 -translate-y-1/2 text-[100px] font-black text-white/5 leading-none" style="font-family: var(--fB);">#06</div>
          <img src="{qs_b64}" class="w-16 mr-6 z-10" alt="QS">
          <div class="z-10">
            <div class="font-bold text-[16px] leading-tight mb-1" style="font-family: var(--fB);">Global Executive MBA</div>
            <div class="text-xs text-white/50 italic" style="font-family: var(--fS);">Europa</div>
          </div>
        </div>

        <div class="bg-white/5 backdrop-blur-md rounded-xl border border-white/10 p-6 relative overflow-hidden flex items-center">
          <div class="absolute right-[-10px] top-1/2 -translate-y-1/2 text-[100px] font-black text-white/5 leading-none" style="font-family: var(--fB);">#09</div>
          <img src="{qs_b64}" class="w-16 mr-6 z-10" alt="QS">
          <div class="z-10">
            <div class="font-bold text-[16px] leading-tight mb-1" style="font-family: var(--fB);">Marketing Digital con IA</div>
            <div class="text-xs text-white/50 italic" style="font-family: var(--fS);">España</div>
          </div>
        </div>

        <div class="bg-white/5 backdrop-blur-md rounded-xl border border-white/10 p-6 relative overflow-hidden flex items-center">
          <div class="absolute right-[-10px] top-1/2 -translate-y-1/2 text-[100px] font-black text-white/5 leading-none" style="font-family: var(--fB);">#08</div>
          <img src="{qs_b64}" class="w-16 mr-6 z-10" alt="QS">
          <div class="z-10">
            <div class="font-bold text-[16px] leading-tight mb-1" style="font-family: var(--fB);">Finanzas, Fintech y Control<br>Estratégico</div>
            <div class="text-xs text-white/50 italic" style="font-family: var(--fS);">España</div>
          </div>
        </div>

        <div class="bg-white/5 backdrop-blur-md rounded-xl border border-white/10 p-6 relative overflow-hidden flex items-center">
          <div class="absolute right-[-10px] top-1/2 -translate-y-1/2 text-[100px] font-black text-white/5 leading-none" style="font-family: var(--fB);">#03</div>
          <img src="{qs_b64}" class="w-16 mr-6 z-10" alt="QS">
          <div class="z-10">
            <div class="font-bold text-[16px] leading-tight mb-1" style="font-family: var(--fB);">International Trade</div>
            <div class="text-xs text-white/50 italic" style="font-family: var(--fS);">España</div>
          </div>
        </div>

        <div class="bg-white/5 backdrop-blur-md rounded-xl border border-white/10 p-6 relative overflow-hidden flex items-center">
          <div class="absolute right-[-10px] top-1/2 -translate-y-1/2 text-[100px] font-black text-white/5 leading-none" style="font-family: var(--fB);">#13</div>
          <img src="{qs_b64}" class="w-16 mr-6 z-10" alt="QS">
          <div class="z-10">
            <div class="font-bold text-[16px] leading-tight mb-1" style="font-family: var(--fB);">Gestión de Riesgos en las<br>Organizaciones</div>
            <div class="text-xs text-white/50 italic" style="font-family: var(--fS);">España</div>
          </div>
        </div>

        <div class="bg-white/5 backdrop-blur-md rounded-xl border border-white/10 p-6 relative overflow-hidden flex items-center">
          <div class="absolute right-[-10px] top-1/2 -translate-y-1/2 text-[100px] font-black text-white/5 leading-none" style="font-family: var(--fB);">#09</div>
          <img src="{qs_b64}" class="w-16 mr-6 z-10" alt="QS">
          <div class="z-10">
            <div class="font-bold text-[16px] leading-tight mb-1" style="font-family: var(--fB);">International MBA</div>
            <div class="text-xs text-white/50 italic" style="font-family: var(--fS);">España</div>
          </div>
        </div>

      </div>

    </div>

  </div>
</div>
"""

    # We need to find the exact boundaries of s3 and s4 in the content.
    # To be safe, we'll use regex to match <div class="s" id="s3" ... up to the next <div class="s" id="s5"
    pattern = r'<!-- ══════════════════════════════════════\n     S3 · RANKINGS FORBES \+ FM \+ EL MUNDO.*?<!-- ══════════════════════════════════════\n     S5 ·'
    
    # Let's replace the whole block from S3 to just before S5
    match = re.search(pattern, content, re.DOTALL)
    if match:
        old_block = match.group(0)
        
        # We need to preserve the S5 header comment
        s5_header = '<!-- ══════════════════════════════════════\n     S5 ·'
        
        new_content = content.replace(old_block, new_s3 + "\n\n" + s5_header)
        
        # Also let's renumber the remaining slides IDs
        new_content = new_content.replace('id="s5"', 'id="s4"')
        new_content = new_content.replace('id="s6"', 'id="s5"')
        new_content = new_content.replace('id="s7"', 'id="s6"')
        new_content = new_content.replace('id="s8"', 'id="s7"')
        new_content = new_content.replace('id="s9"', 'id="s8"')
        
        with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Success")
    else:
        print("Could not find the S3-S4 block!")

process()
