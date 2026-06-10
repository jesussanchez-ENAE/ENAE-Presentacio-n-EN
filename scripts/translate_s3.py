import re

def translate():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find S3
    pattern = r'(<div class="s relative" id="s3">)(.*?)(<!-- ══════════════════════════════════════\n     S5 ·)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        old_div = match.group(1)
        inner_content = match.group(2)
        s5_header = match.group(3)
        
        # Translation Dictionary
        translations = {
            "08 Reconocimientos": "08 Recognitions",
            "ENAE se encuentra entre<br>las mejores Escuelas de<br>Negocios": "ENAE is among<br>the best Business<br>Schools",
            "Categoría: Recién licenciados y<br>jóvenes profesionales": "Category: Recent graduates &<br>young professionals",
            "Categoría: Programas Ejecutivos": "Category: Executive Programs",
            "Categoría: MBA": "Category: MBA",
            "Categoría: Alta Dirección": "Category: Senior Management",
            "Mejores<br>Escuelas de Negocios<br>en España": "Best<br>Business Schools<br>in Spain",
            "Mejores másters Online": "Best Online Masters",
            "Máster universitario en<br>Dirección de<br>Agronegocios": "Master's Degree in<br>Agribusiness<br>Management",
            "Mejores MBA<br>de España": "Best MBAs<br>in Spain",
            "Máster en<br>IA y Data Science": "Master in<br>AI & Data Science",
            "España": "Spain",
            "Máster universitario en<br>Logística y Dirección<br>de Operaciones": "Master's Degree in<br>Logistics & Operations<br>Management",
            "Máster internacional en<br>Marketing Digital": "International Master in<br>Digital Marketing",
            "con Mención en Inteligencia Artificial": "with Specialization in AI",
            "Máster en<br>Finanzas, Fintech<br>y Control Estratégico": "Master in<br>Finance, Fintech<br>& Strategic Control",
            "Máster universitario en<br>Gestión de Riesgos<br>en las Organizaciones": "Master's Degree in<br>Risk Management<br>in Organizations"
        }
        
        for es, en in translations.items():
            inner_content = inner_content.replace(es, en)
            
        new_s3 = old_div + inner_content + s5_header
        
        content = content[:match.start()] + new_s3 + content[match.end():]
        
        with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Translated S3")
    else:
        print("S3 not found")

translate()
