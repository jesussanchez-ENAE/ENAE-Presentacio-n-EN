import re

file_path = 'ENAE_Presentation_v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- 1. Fix S3 Rankings ---
s3_pattern = r'(<!-- ══════════════════════════════════════\n\s+S3 · RANKINGS.*?(?=<!-- ══════════════════════════════════════\n\s+S5 · PROGRAMAS EN INGLÉS))'
s3_match = re.search(s3_pattern, content, re.DOTALL)
if s3_match:
    s3_block = s3_match.group(1)
    
    # Translations
    replacements = {
        '08 Reconocimientos': '08 Rankings',
        'Reconocimiento internacional': 'International Recognition',
        'Entre las mejores<br>del mundo.': 'Among the best<br>in the world.',
        'Máster en Marketing Digital': 'Master in Digital Marketing',
        'con Mención en Inteligencia Artificial': 'with Major in Artificial Intelligence',
        'Mejores Escuelas de Negocio': 'Best Business Schools',
        'Esc. Negocios España': 'Business Schools in Spain',
        'Mejores<br>MBA': 'Best<br>MBAs',
        '>de España<': '>in Spain<',
        'Máster en IA y Data Science': 'Master in AI & Data Science',
        'Logística y Dirección de<br>Operaciones': 'Logistics & Operations<br>Management',
        'Marketing Digital con IA': 'Digital Marketing with AI',
        'Finanzas, Fintech y Control<br>Estratégico': 'Finance, Fintech & Strategic<br>Control',
        'Gestión de Riesgos en las<br>Organizaciones': 'Risk Management in<br>Organizations',
        '>España<': '>Spain<',
        '>Europa<': '>Europe<'
    }
    for old, new in replacements.items():
        s3_block = s3_block.replace(old, new)
        
    # Remove bg-black/20 and backdrop-blur-md from the bottom cards
    # Wait, the user said "quita el background negro que tiene algunos logos"
    # This refers to: bg-black/20 backdrop-blur-md
    s3_block = s3_block.replace('bg-black/20 backdrop-blur-md', 'bg-transparent')
    
    content = content.replace(s3_match.group(1), s3_block)

# --- 2. Rewrite S6 Learning Approach ---
s6_pattern = r'(<!-- ══════════════════════════════════════\n\s+S6 · METODOLOGÍA.*?(?=<!-- ══════════════════════════════════════\n\s+S7 · COMUNIDAD INTERNACIONAL))'
s6_match = re.search(s6_pattern, content, re.DOTALL)
if s6_match:
    new_s6 = """<!-- ══════════════════════════════════════
     S6 · METODOLOGÍA (LEARNING APPROACH)
     Layout: full-bleed background + dark overlay + glassmorphism cards
═══════════════════════════════════════ -->
<div class="s" id="s5">
  <div class="photo photo-overlay-dark" style="background-image:url('src/img/Marketing/futurism-perspective-digital-nomads-lifestyle.jpg'); background-position: center; background-size: cover;"></div>
  
  <img src="src/logos/SIMBOLO-ENAE-BLANCO.png" class="wm" style="font-size:620px;left:-100px;top:-100px; height:1em; width:auto; opacity:0.04; transform: rotate(15deg);" alt="E">

  <div style="position:relative;z-index:2;width:100%;height:100%;padding:var(--padv) var(--pad);display:flex;flex-direction:column;">
    
    <!-- Header -->
    <div style="text-align:center; margin-bottom: 40px;">
        <p class="ey" style="margin-bottom:8px">Learning Approach</p>
        <div class="tm" style="display:flex; flex-direction:column; align-items:center;">
          <b style="font-size:60px">Learning that</b>
          <i style="font-size:60px">Drives Real Change</i>
        </div>
        <div class="acc" style="margin: 20px auto 0;"></div>
    </div>

    <!-- Cards Grid -->
    <div class="anim-up" style="display:grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1400px; margin: 0 auto; flex:1;">
      
      <!-- Card 1 -->
      <div style="background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.1); border-radius:16px; padding:32px; backdrop-filter:blur(12px);">
        <div class="bd" style="width:12px; height:12px; margin-bottom:16px;"></div>
        <div class="bt" style="font-size:26px; margin-bottom:12px;">Real-world cases</div>
        <div class="bd2" style="font-size:16px;">Learn from actual business challenges with active executives and company directors</div>
      </div>

      <!-- Card 2 -->
      <div style="background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.1); border-radius:16px; padding:32px; backdrop-filter:blur(12px);">
        <div class="bd" style="width:12px; height:12px; margin-bottom:16px;"></div>
        <div class="bt" style="font-size:26px; margin-bottom:12px;">AI &amp; digital tools</div>
        <div class="bd2" style="font-size:16px;">Artificial Intelligence, Business Analytics, SAP, Power BI, n8n and automation platforms</div>
      </div>

      <!-- Card 3 -->
      <div style="background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.1); border-radius:16px; padding:32px; backdrop-filter:blur(12px);">
        <div class="bd" style="width:12px; height:12px; margin-bottom:16px;"></div>
        <div class="bt" style="font-size:26px; margin-bottom:12px;">Collaborative projects</div>
        <div class="bd2" style="font-size:16px;">Teamwork with peers from 50+ countries — a truly multicultural learning experience</div>
      </div>

      <!-- Card 4 -->
      <div style="background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.1); border-radius:16px; padding:32px; backdrop-filter:blur(12px); grid-column: span 1.5; margin-left: 50%;">
        <div class="bd" style="width:12px; height:12px; margin-bottom:16px;"></div>
        <div class="bt" style="font-size:26px; margin-bottom:12px;">Career services</div>
        <div class="bd2" style="font-size:16px;">Mentoring, CV coaching, talent recruitment days and alumni network access</div>
      </div>

      <!-- Card 5 -->
      <div style="background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.1); border-radius:16px; padding:32px; backdrop-filter:blur(12px); grid-column: span 1.5; margin-right: 50%;">
        <div class="bd" style="width:12px; height:12px; margin-bottom:16px;"></div>
        <div class="bt" style="font-size:26px; margin-bottom:12px;">Networking</div>
        <div class="bd2" style="font-size:16px;">Corporate visits, international conferences, alumni events and professional forums</div>
      </div>

    </div>
  </div>

  <!-- Unified KPI strip bottom -->
  <div style="position:absolute;left:0;right:0;bottom:0;z-index:3;display:grid;grid-template-columns:repeat(4,1fr);background:rgba(12,2,5,.82);backdrop-filter:blur(8px);border-top:1px solid rgba(255,255,255,.08); text-align:center;">
    <div style="padding:24px;border-right:1px solid rgba(255,255,255,.07)"><div style="font-family:var(--fB);font-weight:800;font-size:42px;color:var(--W);line-height:1">+30</div><div style="font-family:var(--fS);font-style:italic;font-size:14px;color:rgba(255,255,255,.48);margin-top:4px">years of excellence</div></div>
    <div style="padding:24px;border-right:1px solid rgba(255,255,255,.07)"><div style="font-family:var(--fB);font-weight:800;font-size:42px;color:var(--W);line-height:1">70%</div><div style="font-family:var(--fS);font-style:italic;font-size:14px;color:rgba(255,255,255,.48);margin-top:4px">active professionals</div></div>
    <div style="padding:24px;border-right:1px solid rgba(255,255,255,.07)"><div style="font-family:var(--fB);font-weight:800;font-size:42px;color:var(--W);line-height:1">90%+</div><div style="font-family:var(--fS);font-style:italic;font-size:14px;color:rgba(255,255,255,.48);margin-top:4px">career improvement</div></div>
    <div style="padding:24px;"><div style="font-family:var(--fB);font-weight:800;font-size:42px;color:var(--W);line-height:1">+200</div><div style="font-family:var(--fS);font-style:italic;font-size:14px;color:rgba(255,255,255,.48);margin-top:4px">partner companies</div></div>
  </div>
</div>
"""
    content = content.replace(s6_match.group(1), new_s6)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done rewrite")
