import re

def process():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    new_s3 = """
<!-- ══════════════════════════════════════
     S3 · RANKINGS (DOSSIER LAYOUT)
═══════════════════════════════════════ -->
<div class="s" id="s3" style="background: url('src/Rankings/rankings_bg.png') center/cover no-repeat;">
  <!-- We use a grid or flex with gap to perfectly split 1920 in half -->
  <div class="flex h-full w-full px-16 py-[80px]">
    
    <!-- LEFT COLUMN -->
    <div class="w-[45%] flex flex-col pr-8 h-full">
      
      <!-- Top header -->
      <div class="flex justify-between items-start mb-6">
        <div>
          <div class="text-[54px] font-black leading-none text-white tracking-widest" style="font-family: var(--fB);">&gt;&gt;&gt;</div>
          <div class="text-[64px] font-black leading-none text-white mt-1" style="font-family: var(--fB);">Rankings</div>
        </div>
        <div class="text-[34px] font-bold text-white leading-[1.1] w-[55%] mt-6" style="font-family: var(--fB);">
          ENAE se encuentra entre<br>las mejores Escuelas de<br>Negocios
        </div>
      </div>

      <!-- Forbes row -->
      <div class="flex items-center justify-between mb-4">
        <img src="src/Rankings/forbes.png" class="w-[280px]" alt="Forbes">
        <div class="text-[32px] text-white/50 font-bold tracking-wide mr-8" style="font-family: var(--fB);">Ranking 2025</div>
      </div>

      <!-- Forbes Grid -->
      <div class="grid grid-cols-2 gap-4 mb-4">
        <div class="bg-[#bf2639]/30 rounded-lg p-6 flex flex-col justify-center items-center text-center relative overflow-hidden" style="min-height: 140px;">
          <div class="absolute inset-0 flex justify-center items-center text-[100px] font-black leading-none text-white/20 pointer-events-none" style="font-family: var(--fB);">#06</div>
          <div class="relative z-10 font-bold text-[18px] text-white leading-tight mb-1" style="font-family: var(--fB);">Master in International Trade</div>
          <div class="relative z-10 text-[14px] text-white italic mt-1" style="font-family: var(--fS);">Categoría: Recién licenciados y<br>jóvenes profesionales</div>
        </div>
        <div class="bg-[#bf2639]/30 rounded-lg p-6 flex flex-col justify-center items-center text-center relative overflow-hidden" style="min-height: 140px;">
          <div class="absolute inset-0 flex justify-center items-center text-[100px] font-black leading-none text-white/20 pointer-events-none" style="font-family: var(--fB);">#07</div>
          <div class="relative z-10 font-bold text-[18px] text-white leading-tight mb-1" style="font-family: var(--fB);">Global Executive MBA</div>
          <div class="relative z-10 text-[14px] text-white italic mt-1" style="font-family: var(--fS);">Categoría: Programas Ejecutivos</div>
        </div>
        <div class="bg-[#bf2639]/30 rounded-lg p-6 flex flex-col justify-center items-center text-center relative overflow-hidden" style="min-height: 140px;">
          <div class="absolute inset-0 flex justify-center items-center text-[100px] font-black leading-none text-white/20 pointer-events-none" style="font-family: var(--fB);">#12</div>
          <div class="relative z-10 font-bold text-[18px] text-white leading-tight mb-1" style="font-family: var(--fB);">International MBA</div>
          <div class="relative z-10 text-[14px] text-white italic mt-1" style="font-family: var(--fS);">Categoría: MBA</div>
        </div>
        <div class="bg-[#bf2639]/30 rounded-lg p-6 flex flex-col justify-center items-center text-center relative overflow-hidden" style="min-height: 140px;">
          <div class="absolute inset-0 flex justify-center items-center text-[100px] font-black leading-none text-white/20 pointer-events-none" style="font-family: var(--fB);">#04</div>
          <div class="relative z-10 font-bold text-[18px] text-white leading-tight mb-1" style="font-family: var(--fB);">Magistrae</div>
          <div class="relative z-10 text-[14px] text-white italic mt-1" style="font-family: var(--fS);">Categoría: Alta Dirección</div>
        </div>
      </div>

      <!-- Financial Mag + El Mundo -->
      <div class="flex gap-8 flex-1 mt-6">
        <!-- FM -->
        <div class="w-1/2 flex flex-col items-center">
          <div class="bg-white rounded-lg p-4 flex items-center justify-center mb-6 w-full">
            <img src="src/Rankings/FinancialMagazine.png" class="w-[90%]" alt="Financial Magazine">
          </div>
          <div class="w-full pl-2">
            <div class="text-[75px] font-black text-white/30 leading-none -mb-4" style="font-family: var(--fB);">#06</div>
            <div class="text-white text-[19px] font-bold leading-tight" style="font-family: var(--fB);">Mejores<br>Escuelas de Negocios<br>en España</div>
          </div>
        </div>

        <!-- El Mundo -->
        <div class="w-1/2 flex flex-col pl-4">
          <img src="src/Rankings/El_Mundo_logo.svg.png" class="w-[240px] mb-6 mt-4" alt="El Mundo">
          <div class="text-white/80 text-[18px] mb-2 mt-4" style="font-family: var(--fS);">Mejores másters Online</div>
          <div class="flex justify-between items-start">
            <div>
               <div class="text-[60px] font-black text-white/30 leading-none -mb-2" style="font-family: var(--fB);">#02</div>
               <div class="text-white font-bold text-[15px] leading-[1.2]" style="font-family: var(--fB);">International<br>Trade</div>
            </div>
            <div>
               <div class="text-[60px] font-black text-white/30 leading-none -mb-2" style="font-family: var(--fB);">#04</div>
               <div class="text-white font-bold text-[13px] leading-[1.2]" style="font-family: var(--fB);">Máster universitario en<br>Dirección de<br>Agronegocios</div>
            </div>
          </div>
          <div class="flex items-center gap-4 mt-auto mb-2">
             <!-- Star Icon -->
             <svg class="w-16 h-16 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path></svg>
             <div class="text-[22px] font-bold text-white leading-tight" style="font-family: var(--fB);">Mejores MBA<br>de España</div>
          </div>
        </div>
      </div>

    </div>

    <!-- Divider Spacer (Since background handles the gap) -->
    <div class="w-[10%] h-full mx-4"></div>

    <!-- RIGHT COLUMN (QS) -->
    <div class="w-[45%] flex flex-col h-full pl-4 pr-16 pt-8">
      
      <!-- QS Top Stars -->
      <div class="flex items-center gap-6 mb-8 mt-6">
        <img src="src/Rankings/QS_5stars.png" class="h-[180px] drop-shadow-2xl" alt="QS Rated Excellent">
        <div class="flex gap-4 items-center">
            <img src="src/Rankings/QS_5stars.png" class="h-[80px] drop-shadow-xl" alt="QS Stars">
            <img src="src/Rankings/QS_5stars.png" class="h-[80px] drop-shadow-xl" alt="QS Stars">
            <img src="src/Rankings/QS_5stars.png" class="h-[80px] drop-shadow-xl" alt="QS Stars">
            <img src="src/Rankings/QS_5stars.png" class="h-[80px] drop-shadow-xl" alt="QS Stars">
        </div>
      </div>

      <!-- QS Grid -->
      <div class="grid grid-cols-2 gap-x-6 gap-y-4 flex-1">
        
        <!-- #10 IA -->
        <div class="bg-[#b31b2e]/50 rounded-lg p-4 flex items-center relative overflow-hidden" style="min-height: 120px;">
          <div class="absolute right-0 top-[40%] -translate-y-1/2 text-[100px] font-black text-white/30 leading-none pointer-events-none" style="font-family: var(--fB);">#10</div>
          <img src="src/Rankings/QS_IA_y_DataScience.png" class="h-[95px] mr-4 z-10" alt="QS IA">
          <div class="z-10 mt-6">
            <div class="text-white font-bold text-[16px] leading-[1.1]" style="font-family: var(--fB);">Máster en<br>IA y Data Science</div>
            <div class="text-white/80 text-[13px] mt-1" style="font-family: var(--fS);">España</div>
          </div>
        </div>

        <!-- #06 Logistica -->
        <div class="bg-[#b31b2e]/50 rounded-lg p-4 flex items-center relative overflow-hidden" style="min-height: 120px;">
          <div class="absolute right-0 top-[40%] -translate-y-1/2 text-[100px] font-black text-white/30 leading-none pointer-events-none" style="font-family: var(--fB);">#06</div>
          <img src="src/Rankings/QS_Logistica.png" class="h-[95px] mr-4 z-10" alt="QS Logistica">
          <div class="z-10 mt-6">
            <div class="text-white font-bold text-[16px] leading-[1.1]" style="font-family: var(--fB);">Máster universitario en<br>Logística y Dirección<br>de Operaciones</div>
            <div class="text-white/80 text-[13px] mt-1" style="font-family: var(--fS);">España</div>
          </div>
        </div>

        <!-- #06 Global Exec MBA -->
        <div class="bg-[#b31b2e]/50 rounded-lg p-4 flex items-center relative overflow-hidden" style="min-height: 120px;">
          <div class="absolute right-0 top-[40%] -translate-y-1/2 text-[100px] font-black text-white/30 leading-none pointer-events-none" style="font-family: var(--fB);">#06</div>
          <img src="src/Rankings/QS_Global_Executive_MBA.png" class="h-[95px] mr-4 z-10" alt="QS Global Exec">
          <div class="z-10 mt-6">
            <div class="text-white font-bold text-[16px] leading-[1.1]" style="font-family: var(--fB);">Global<br>Executive MBA</div>
            <div class="text-white/80 text-[13px] mt-1" style="font-family: var(--fS);">España</div>
          </div>
        </div>

        <!-- #09 Marketing Digital -->
        <div class="bg-[#b31b2e]/50 rounded-lg p-4 flex items-center relative overflow-hidden" style="min-height: 120px;">
          <div class="absolute right-0 top-[40%] -translate-y-1/2 text-[100px] font-black text-white/30 leading-none pointer-events-none" style="font-family: var(--fB);">#09</div>
          <img src="src/Rankings/QS_Marketing.png" class="h-[95px] mr-4 z-10" alt="QS Marketing">
          <div class="z-10 mt-6">
            <div class="text-white font-bold text-[16px] leading-[1.1]" style="font-family: var(--fB);">Máster internacional en<br>Marketing Digital<br><span class="text-[10px] font-normal italic">con Mención en Inteligencia Artificial</span></div>
            <div class="text-white/80 text-[13px] mt-1" style="font-family: var(--fS);">España</div>
          </div>
        </div>

        <!-- #08 Finanzas -->
        <div class="bg-[#b31b2e]/50 rounded-lg p-4 flex items-center relative overflow-hidden" style="min-height: 120px;">
          <div class="absolute right-0 top-[40%] -translate-y-1/2 text-[100px] font-black text-white/30 leading-none pointer-events-none" style="font-family: var(--fB);">#08</div>
          <img src="src/Rankings/QS_Finanzas.png" class="h-[95px] mr-4 z-10" alt="QS Finanzas">
          <div class="z-10 mt-6">
            <div class="text-white font-bold text-[16px] leading-[1.1]" style="font-family: var(--fB);">Máster en<br>Finanzas, Fintech<br>y Control Estratégico</div>
            <div class="text-white/80 text-[13px] mt-1" style="font-family: var(--fS);">España</div>
          </div>
        </div>

        <!-- #03 International Trade -->
        <div class="bg-[#b31b2e]/50 rounded-lg p-4 flex items-center relative overflow-hidden" style="min-height: 120px;">
          <div class="absolute right-0 top-[40%] -translate-y-1/2 text-[100px] font-black text-white/30 leading-none pointer-events-none" style="font-family: var(--fB);">#03</div>
          <img src="src/Rankings/QS_International_Trade.png" class="h-[95px] mr-4 z-10" alt="QS Intl Trade">
          <div class="z-10 mt-6">
            <div class="text-white font-bold text-[16px] leading-[1.1]" style="font-family: var(--fB);">International<br>Trade</div>
            <div class="text-white/80 text-[13px] mt-1" style="font-family: var(--fS);">España</div>
          </div>
        </div>

        <!-- #13 Gestión Riesgos -->
        <div class="bg-[#b31b2e]/50 rounded-lg p-4 flex items-center relative overflow-hidden" style="min-height: 120px;">
          <div class="absolute right-0 top-[40%] -translate-y-1/2 text-[100px] font-black text-white/30 leading-none pointer-events-none" style="font-family: var(--fB);">#13</div>
          <img src="src/Rankings/QS_GEstion_de_Riesgos.png" class="h-[95px] mr-4 z-10" alt="QS Riesgos">
          <div class="z-10 mt-6">
            <div class="text-white font-bold text-[16px] leading-[1.1]" style="font-family: var(--fB);">Máster universitario en<br>Gestión de Riesgos<br>en las Organizaciones</div>
            <div class="text-white/80 text-[13px] mt-1" style="font-family: var(--fS);">España</div>
          </div>
        </div>

        <!-- #09 International MBA -->
        <div class="bg-[#b31b2e]/50 rounded-lg p-4 flex items-center relative overflow-hidden" style="min-height: 120px;">
          <div class="absolute right-0 top-[40%] -translate-y-1/2 text-[100px] font-black text-white/30 leading-none pointer-events-none" style="font-family: var(--fB);">#09</div>
          <img src="src/Rankings/QS_International_MBA.png" class="h-[95px] mr-4 z-10" alt="QS Intl MBA">
          <div class="z-10 mt-6">
            <div class="text-white font-bold text-[16px] leading-[1.1]" style="font-family: var(--fB);">International<br>MBA</div>
            <div class="text-white/80 text-[13px] mt-1" style="font-family: var(--fS);">España</div>
          </div>
        </div>

      </div>
    </div>

  </div>
</div>
"""

    pattern = r'<!-- ══════════════════════════════════════\n     S3 · RANKINGS \(MERGED\).*?<!-- ══════════════════════════════════════\n     S5 ·'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        old_block = match.group(0)
        s5_header = '<!-- ══════════════════════════════════════\n     S5 ·'
        new_content = content.replace(old_block, new_s3 + "\n\n" + s5_header)
        with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Success!")
    else:
        print("Could not find the S3 block!")

process()
