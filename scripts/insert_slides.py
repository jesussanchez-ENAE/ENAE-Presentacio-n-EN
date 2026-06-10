import re

def insert():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where S3 ends and S4 begins
    pattern = r'(<!-- ══════════════════════════════════════\n     S5 ·)'
    match = re.search(pattern, content)
    
    if match:
        slides_html = """
<!-- ══════════════════════════════════════
     S4 · WHERE IS MURCIA
═══════════════════════════════════════ -->
<div class="s relative bg-[#8b1426]" id="s4">
  <div class="flex h-full w-full px-16 py-[80px] relative z-10 flex-col">
    <div class="flex justify-between items-end mb-4">
      <h1 class="text-[90px] leading-[0.9] text-white/90 drop-shadow-lg" style="font-family: var(--fB);">
        <span class="text-white/50 font-normal">Where is</span><br>Murcia?
      </h1>
    </div>
    <div class="flex-1 flex items-center justify-center relative">
       <img src="src/spain/mapa_spain.svg" class="max-h-[100%] max-w-full drop-shadow-2xl object-contain" alt="Map of Spain">
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════
     S5 · LIVING IN MURCIA
═══════════════════════════════════════ -->
<div class="s bg-white relative" id="s5">
  <div class="flex h-full w-full">
    <!-- Left Column (Image) -->
    <div class="w-2/5 h-full relative">
       <img src="src/spain/fondo_playa.png" class="w-full h-full object-cover" alt="Living in Murcia">
    </div>
    <!-- Right Column (Content) -->
    <div class="w-3/5 h-full flex flex-col px-16 py-12 justify-center">
       <h1 class="text-[70px] leading-[0.9] text-[#b31b2e]/30 font-normal drop-shadow-sm mb-12" style="font-family: var(--fB);">
          Living in <br><span class="text-[#b31b2e]">Murcia, Spain</span>
       </h1>
       <div class="grid grid-cols-2 gap-12 flex-1">
          <div>
             <h2 class="text-[28px] font-bold text-[#b31b2e] flex items-center gap-2 mb-4" style="font-family: var(--fB);">
                <span class="text-[32px]">></span> Location
             </h2>
             <p class="text-[16px] text-gray-700 leading-relaxed mb-8" style="font-family: var(--fS);">
                Accessible by car, train, or plane. Located 3.5h from Madrid with its own international airport and high-speed train connections to major cities.
             </p>
             <h2 class="text-[28px] font-bold text-[#b31b2e] flex items-center gap-2 mb-4" style="font-family: var(--fB);">
                <span class="text-[32px]">></span> About Murcia...
             </h2>
             <p class="text-[16px] text-gray-700 leading-relaxed" style="font-family: var(--fS);">
                Boasts the best climate in Spain with over 300 days of sunshine a year. Ideal for outdoor activities, hiking, biking, and water sports near the Mediterranean Sea.
             </p>
          </div>
          <div>
             <h2 class="text-[28px] font-bold text-[#b31b2e] flex items-center gap-2 mb-4" style="font-family: var(--fB);">
                <span class="text-[32px]">></span> Facilities
             </h2>
             <p class="text-[16px] text-gray-700 leading-relaxed mb-8" style="font-family: var(--fS);">
                A modern 2,200 sqm campus equipped with state-of-the-art technology, library, and resources to support academic needs in a vibrant university city.
             </p>
             <div class="bg-gray-100 p-6 rounded-lg shadow-inner border border-gray-200">
                <h3 class="text-[20px] font-bold text-gray-900 mb-4" style="font-family: var(--fB);">Practical info</h3>
                <ul class="text-[14px] text-gray-700 space-y-3" style="font-family: var(--fS);">
                   <li><strong>Currency:</strong> Euro (€)</li>
                   <li><strong>Business Hours:</strong> 9:00 AM - 1:30 PM & 4:30 PM - 8:00 PM</li>
                   <li><strong>Electricity:</strong> 220 volts (two-round-pin plug)</li>
                   <li><strong>Cost of Living:</strong> Affordable (700€ - 1000€/month)</li>
                </ul>
             </div>
          </div>
       </div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════
     S6 · REGION OF MURCIA
═══════════════════════════════════════ -->
<div class="s relative bg-white" id="s6">
  <div class="flex h-full w-full">
    <!-- Left Column (Content) -->
    <div class="w-1/2 h-full flex flex-col pl-16 pr-8 py-12 justify-center relative z-10">
       <h1 class="text-[60px] leading-[1] text-[#b31b2e]/30 font-normal mb-8" style="font-family: var(--fB);">
          Region of Murcia,<br><span class="text-[#b31b2e]/50">where the</span><br><span class="text-[#b31b2e]">Sun Never Hides</span>
       </h1>
       <h2 class="text-[24px] font-bold text-[#b31b2e] mb-10" style="font-family: var(--fB);">
          Live it. Feel its energy. Discover Murcia.
       </h2>
       
       <div class="space-y-6">
          <div>
             <h3 class="text-[20px] font-bold text-[#b31b2e] flex items-center gap-2 mb-2" style="font-family: var(--fB);">
                <span class="text-[24px]">></span> Costa Cálida: Over 250 km of Sea and Life
             </h3>
             <ul class="text-[15px] text-gray-700 space-y-1 ml-6 list-disc" style="font-family: var(--fS);">
                <li>Unique beaches, unspoiled coves, and crystal-clear waters.</li>
                <li>Diving in Cabo de Palos, sailing, paddle surfing.</li>
                <li>Coastal cuisine: arroz caldero, seafood, "marineras" tapas.</li>
             </ul>
          </div>
          <div>
             <h3 class="text-[20px] font-bold text-[#b31b2e] flex items-center gap-2 mb-2" style="font-family: var(--fB);">
                <span class="text-[24px]">></span> Adventure and Fresh Air Among the Peaks
             </h3>
             <ul class="text-[15px] text-gray-700 space-y-1 ml-6 list-disc" style="font-family: var(--fS);">
                <li>Scenic trails, viewpoints, and outdoor adventures all year.</li>
                <li>Charming villages: Moratalla, Caravaca, Cehegín.</li>
             </ul>
          </div>
          <div>
             <h3 class="text-[20px] font-bold text-[#b31b2e] flex items-center gap-2 mb-2" style="font-family: var(--fB);">
                <span class="text-[24px]">></span> A Region Full of Experiences
             </h3>
             <p class="text-[15px] text-gray-700 ml-6" style="font-family: var(--fS);">
                Wine tourism, gastronomy, traditional festivals, Roman heritage in Cartagena, and the baroque charm of Murcia city.
             </p>
          </div>
       </div>
    </div>
    <!-- Right Column (Image) -->
    <div class="w-1/2 h-full relative">
       <div class="absolute inset-y-0 left-0 w-32 bg-gradient-to-r from-white to-transparent z-10"></div>
       <img src="src/spain/tourists-admiring-murcia-cathedral-facade-after-sh-2025-04-29-02-35-42-utc.jpg" class="w-full h-full object-cover" alt="Murcia Cathedral">
    </div>
  </div>
</div>

"""
        content = content[:match.start()] + slides_html + content[match.start():]
        
        # Now shift the IDs of subsequent slides
        # We inserted s4, s5, s6, so the old s4 becomes s7, old s5 becomes s8, etc.
        # Find all <div class="s..." id="sX"> after our insertion point
        # The easiest way is to re-number ALL slides starting from S1.
        
        slides = re.finditer(r'<div class="s[^"]*" id="s(\d+)"', content)
        new_content = ""
        last_idx = 0
        slide_count = 0
        for m in slides:
            slide_count += 1
            new_content += content[last_idx:m.start(1)] + str(slide_count)
            last_idx = m.end(1)
        new_content += content[last_idx:]
        
        # Update the total slide count in the HTML (e.g. 1/9 -> 1/12)
        new_content = re.sub(r'<span id="sn">1/\d+</span>', f'<span id="sn">1/{slide_count}</span>', new_content)
        
        with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated successfully. Total slides: {slide_count}")
    else:
        print("Marker not found")

insert()
