import sys

def patch_file():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject Tailwind CDN and Config
    tailwind_script = """
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          enae: {
            red: '#a81832',
            dark: '#202221',
            darker: '#161a19'
          }
        },
        fontFamily: {
          sans: ['OS', 'Arial', 'sans-serif'],
          serif: ['Playfair Display', 'Georgia', 'serif'],
          display: ['SFUI', 'Arial Black', 'sans-serif']
        }
      }
    }
  }
</script>
</head>"""
    content = content.replace('</head>', tailwind_script)

    # 2. Refactor cover image to new JPG
    content = content.replace("src/img/cover.png", "src/img/ENAE/_0N7A2272.JPG")

    # 3. Refactor inline styles on cover slide to Tailwind classes
    # Original: <b style="font-size:120px; line-height: 1.1">Your Gateway to</b>
    # Tailwind: <b class="text-[120px] leading-[1.1] font-display font-black text-white block">Your Gateway to</b>
    # Note: the .tm b class already has display:block, font-family:var(--fD), font-weight:900, color:var(--W). 
    # But we want to use Tailwind to layout as requested.
    
    # We will replace the whole text block for the title
    old_title_block = """        <b style="font-size:120px; line-height: 1.1">Your Gateway to</b>
        <i style="font-size:160px; line-height: 1.1; margin-top: -10px;">Global Business</i>
        <l style="font-size:42px; margin-top: 20px;">Excellence · Innovation · International Impact</l>"""
        
    new_title_block = """        <div class="relative z-10">
          <b class="block font-display font-black text-white text-[120px] leading-[1.1]">Your Gateway to</b>
          <i class="block font-serif font-bold italic text-white text-[160px] leading-[1.1] -mt-[10px]">Global Business</i>
          <span class="block font-sans font-light text-white/60 text-[42px] mt-[20px]">Excellence · Innovation · International Impact</span>
        </div>"""
    content = content.replace(old_title_block, new_title_block)

    # Refactor the KPI strip
    old_kpi_1 = '<div style="font-family:var(--fB);font-weight:800;font-size:72px;color:var(--W);line-height:1">+30</div>'
    new_kpi_1 = '<div class="font-sans font-extrabold text-[72px] text-white leading-none">+30</div>'
    content = content.replace(old_kpi_1, new_kpi_1)

    old_kpi_desc_1 = '<div style="font-family:var(--fS);font-style:italic;font-size:15px;color:rgba(255,255,255,.48);margin-top:4px">years of excellence</div>'
    new_kpi_desc_1 = '<div class="font-serif italic text-[15px] text-white/50 mt-1">years of excellence</div>'
    content = content.replace(old_kpi_desc_1, new_kpi_desc_1)

    old_kpi_2 = '<div style="font-family:var(--fB);font-weight:800;font-size:72px;color:var(--W);line-height:1">+13K</div>'
    new_kpi_2 = '<div class="font-sans font-extrabold text-[72px] text-white leading-none">+13K</div>'
    content = content.replace(old_kpi_2, new_kpi_2)

    old_kpi_desc_2 = '<div style="font-family:var(--fS);font-style:italic;font-size:15px;color:rgba(255,255,255,.48);margin-top:4px">alumni worldwide</div>'
    new_kpi_desc_2 = '<div class="font-serif italic text-[15px] text-white/50 mt-1">alumni worldwide</div>'
    content = content.replace(old_kpi_desc_2, new_kpi_desc_2)

    old_kpi_3 = '<div style="font-family:var(--fB);font-weight:800;font-size:72px;color:var(--W);line-height:1">50+</div>'
    new_kpi_3 = '<div class="font-sans font-extrabold text-[72px] text-white leading-none">50+</div>'
    content = content.replace(old_kpi_3, new_kpi_3)

    old_kpi_desc_3 = '<div style="font-family:var(--fS);font-style:italic;font-size:15px;color:rgba(255,255,255,.48);margin-top:4px">countries represented</div>'
    new_kpi_desc_3 = '<div class="font-serif italic text-[15px] text-white/50 mt-1">countries represented</div>'
    content = content.replace(old_kpi_desc_3, new_kpi_desc_3)

    old_kpi_4 = '<div style="font-family:var(--fB);font-weight:800;font-size:72px;color:var(--W);line-height:1">+200</div>'
    new_kpi_4 = '<div class="font-sans font-extrabold text-[72px] text-white leading-none">+200</div>'
    content = content.replace(old_kpi_4, new_kpi_4)

    old_kpi_desc_4 = '<div style="font-family:var(--fS);font-style:italic;font-size:15px;color:rgba(255,255,255,.48);margin-top:4px">partner companies</div>'
    new_kpi_desc_4 = '<div class="font-serif italic text-[15px] text-white/50 mt-1">partner companies</div>'
    content = content.replace(old_kpi_desc_4, new_kpi_desc_4)


    with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
        f.write(content)

patch_file()
