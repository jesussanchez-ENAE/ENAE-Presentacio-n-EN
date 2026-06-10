import re

def redesign():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to replace S4, S5, S6
    # Find start of S4
    s4_start_match = re.search(r'<!-- ══════════════════════════════════════\n     S4 · WHERE IS MURCIA\n═══════════════════════════════════════ -->', content)
    
    # Find start of S7
    s7_start_match = re.search(r'<!-- ══════════════════════════════════════\n     S5 · PROGRAMAS EN INGLÉS', content)
    
    if not s4_start_match or not s7_start_match:
        print("Markers not found")
        return

    new_slides_html = """<!-- ══════════════════════════════════════
     S4 · WHERE IS MURCIA
═══════════════════════════════════════ -->
<div class="s bg-[#8b1426]" id="s4">
  <div class="flex h-full w-full px-16 py-[80px] relative z-10 flex-col">
    <div class="flex justify-between items-end mb-12">
      <h1 class="text-[90px] leading-[0.9] text-white/90 drop-shadow-lg tm" style="font-family: var(--fB);">
        <l class="text-[32px] uppercase tracking-widest mb-4">Where is</l>
        <b>Murcia?</b>
      </h1>
    </div>
    <div class="flex-1 flex items-center justify-center relative">
       <!-- map with filter to make it white -->
       <img src="src/spain/mapa_spain.svg" class="max-h-[100%] max-w-[80%] drop-shadow-2xl object-contain filter invert brightness-0" alt="Map of Spain">
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════
     S5 · LIVING IN MURCIA
═══════════════════════════════════════ -->
<div class="s" id="s5">
  <div class="photo photo-overlay-dark" style="background-image:url('src/spain/fondo_playa.png');"></div>
  <div class="flex h-full w-full px-16 py-[80px] relative z-10 flex-col">
    <div class="mb-10">
      <h1 class="text-[70px] leading-[0.9] text-white/90 drop-shadow-lg tm">
        <l class="text-[28px] uppercase tracking-widest mb-2">Living in</l>
        <b>Murcia, Spain</b>
      </h1>
      <div class="acc"></div>
    </div>
    <div class="grid grid-cols-2 gap-8 flex-1">
       <div class="flex flex-col gap-6">
          <div class="card-g">
             <h2 class="text-[22px] font-bold text-white flex items-center gap-3 mb-3" style="font-family: var(--fB);">
                <div class="w-[8px] h-[8px] bg-[var(--G)] rounded-full"></div> Location
             </h2>
             <p class="text-[16px] text-white/80 leading-relaxed" style="font-family: var(--fS);">
                Accessible by car, train, or plane. Located 3.5h from Madrid with its own international airport and high-speed train connections to major cities.
             </p>
          </div>
          <div class="card-g">
             <h2 class="text-[22px] font-bold text-white flex items-center gap-3 mb-3" style="font-family: var(--fB);">
                <div class="w-[8px] h-[8px] bg-[var(--G)] rounded-full"></div> About Murcia...
             </h2>
             <p class="text-[16px] text-white/80 leading-relaxed" style="font-family: var(--fS);">
                Boasts the best climate in Spain with over 300 days of sunshine a year. Ideal for outdoor activities, hiking, biking, and water sports near the Mediterranean Sea.
             </p>
          </div>
       </div>
       <div class="flex flex-col gap-6">
          <div class="card-g">
             <h2 class="text-[22px] font-bold text-white flex items-center gap-3 mb-3" style="font-family: var(--fB);">
                <div class="w-[8px] h-[8px] bg-[var(--G)] rounded-full"></div> Facilities
             </h2>
             <p class="text-[16px] text-white/80 leading-relaxed" style="font-family: var(--fS);">
                A modern 2,200 sqm campus equipped with state-of-the-art technology, library, and resources to support academic needs in a vibrant university city.
             </p>
          </div>
          <div class="card-n">
             <h3 class="text-[20px] font-bold text-[var(--G)] mb-4" style="font-family: var(--fB);">Practical Info</h3>
             <ul class="text-[15px] text-white/80 space-y-3" style="font-family: var(--fS);">
                <li class="flex justify-between border-b border-white/10 pb-2"><span>Currency</span> <b>Euro (€)</b></li>
                <li class="flex justify-between border-b border-white/10 pb-2"><span>Business Hours</span> <b>9am-1:30pm & 4:30pm-8pm</b></li>
                <li class="flex justify-between border-b border-white/10 pb-2"><span>Electricity</span> <b>220 volts</b></li>
                <li class="flex justify-between"><span>Cost of Living</span> <b>700€ - 1000€/month</b></li>
             </ul>
          </div>
       </div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════
     S6 · REGION OF MURCIA
═══════════════════════════════════════ -->
<div class="s" id="s6">
  <div class="photo photo-fade-l" style="background-image:url('src/spain/tourists-admiring-murcia-cathedral-facade-after-sh-2025-04-29-02-35-42-utc.jpg'); background-position: center right;"></div>
  <div class="flex h-full w-full px-16 py-[80px] relative z-10 flex-col">
    <div class="w-7/12 h-full flex flex-col justify-center">
       <h1 class="text-[75px] leading-[0.95] text-white/90 drop-shadow-lg tm mb-8">
          <l class="text-[26px] uppercase tracking-widest mb-2">Region of Murcia</l>
          <b>Where the Sun<br><span style="color:var(--G);">Never Hides</span></b>
       </h1>
       <div class="acc mb-10"></div>
       <h2 class="text-[26px] font-normal text-white/80 mb-10 italic" style="font-family: var(--fS);">
          Live it. Feel its energy. Discover Murcia.
       </h2>
       
       <div class="space-y-6">
          <div class="card-g">
             <h3 class="text-[20px] font-bold text-white flex items-center gap-3 mb-2" style="font-family: var(--fB);">
                <div class="w-[8px] h-[8px] bg-[var(--G)] rounded-full"></div> Costa Cálida: Over 250 km of Sea and Life
             </h3>
             <p class="text-[16px] text-white/70 ml-5" style="font-family: var(--fS);">
                Unique beaches, unspoiled coves, diving in Cabo de Palos, sailing, and exquisite coastal cuisine.
             </p>
          </div>
          <div class="card-g">
             <h3 class="text-[20px] font-bold text-white flex items-center gap-3 mb-2" style="font-family: var(--fB);">
                <div class="w-[8px] h-[8px] bg-[var(--G)] rounded-full"></div> Adventure and Fresh Air Among the Peaks
             </h3>
             <p class="text-[16px] text-white/70 ml-5" style="font-family: var(--fS);">
                Scenic trails, viewpoints, outdoor adventures, and charming villages like Moratalla and Caravaca.
             </p>
          </div>
          <div class="card-g">
             <h3 class="text-[20px] font-bold text-white flex items-center gap-3 mb-2" style="font-family: var(--fB);">
                <div class="w-[8px] h-[8px] bg-[var(--G)] rounded-full"></div> A Region Full of Experiences
             </h3>
             <p class="text-[16px] text-white/70 ml-5" style="font-family: var(--fS);">
                Wine tourism, gastronomy, traditional festivals, Roman heritage in Cartagena, and the baroque charm of Murcia city.
             </p>
          </div>
       </div>
    </div>
  </div>
</div>
\n"""

    new_content = content[:s4_start_match.start()] + new_slides_html + content[s7_start_match.start():]
    
    with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Redesign complete.")

redesign()
