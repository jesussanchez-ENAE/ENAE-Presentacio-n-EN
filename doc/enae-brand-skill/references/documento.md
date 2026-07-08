# Referencia: Documentos Word (.docx) — ENAE Brand

## Cuándo usar este formato
- Cartas corporativas oficiales
- Informes académicos y de gestión
- Memorias anuales
- Propuestas de programas formativos
- Guías de estudio y manuales
- Actas y comunicados internos

## Antes de crear el documento
Lee `/mnt/skills/public/docx/SKILL.md` para las instrucciones técnicas de python-docx.

---

## Estructura de carta/documento oficial ENAE

Según el manual corporativo, la carta ENAE sigue estas medidas (formato A4 210mm):

```
Márgenes página:
  Superior: 12mm (zona logo)
  Inferior: 30mm (zona pie con logos institucionales)
  Izquierdo: 25mm
  Derecho: 10mm

Logo: posición superior izquierda, ancho aprox 50mm
Zona de texto: comienza a 30mm del borde superior
Pie: logos institucionales (UPCT, Cámara, ENAE) + datos de contacto
```

---

## Colores python-docx

```python
from docx.shared import RGBColor

GRANATE   = RGBColor(0xA9, 0x18, 0x31)  # #a91831 — primario ENAE
NEGRO     = RGBColor(0x20, 0x22, 0x21)  # #202221 — textos oscuros
AZUL_GRIS = RGBColor(0xDE, 0xE5, 0xEC)  # #dee5ec — fondo suave
BLANCO    = RGBColor(0xFF, 0xFF, 0xFF)  # #ffffff
GRIS      = RGBColor(0x40, 0x40, 0x40)  # #404040 — cuerpo texto
```

---

## Estilos tipográficos para documentos ENAE

```python
from docx.shared import Pt, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def enae_title(paragraph, text, size=22):
    """Título principal: Open Sans Bold, granate."""
    run = paragraph.add_run(text)
    run.font.bold = True
    run.font.size = Pt(size)
    run.font.color.rgb = GRANATE
    run.font.name = 'Calibri'  # fallback Word

def enae_heading2(paragraph, text):
    """Encabezado de sección con borde izquierdo granate."""
    run = paragraph.add_run(text)
    run.font.bold = True
    run.font.size = Pt(13)
    run.font.color.rgb = GRANATE
    run.font.name = 'Calibri'
    # Borde izquierdo granate via XML
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    left = OxmlElement('w:left')
    left.set(qn('w:val'), 'single')
    left.set(qn('w:sz'), '18')     # 2.25pt
    left.set(qn('w:space'), '8')
    left.set(qn('w:color'), 'A91831')  # granate
    pBdr.append(left)
    pPr.append(pBdr)

def enae_body(paragraph, text):
    """Cuerpo de texto estándar."""
    run = paragraph.add_run(text)
    run.font.size = Pt(11)
    run.font.color.rgb = GRIS
    run.font.name = 'Calibri'
    paragraph.paragraph_format.space_after = Pt(6)
    paragraph.paragraph_format.line_spacing = Pt(13.2)  # 1.2x

def enae_contact_line(paragraph, text):
    """Texto de pie/contacto: pequeño, gris."""
    run = paragraph.add_run(text)
    run.font.size = Pt(8)
    run.font.color.rgb = GRIS
    run.font.name = 'Calibri'
```

---

## Configuración de página A4

```python
from docx.shared import Cm

section = doc.sections[0]
section.page_width  = Cm(21.0)
section.page_height = Cm(29.7)
section.top_margin    = Cm(1.2)   # 12mm — zona logo
section.bottom_margin = Cm(3.0)   # 30mm — zona pie institucional
section.left_margin   = Cm(2.5)   # 25mm
section.right_margin  = Cm(1.0)   # 10mm
```

---

## Tablas con estilo ENAE

```python
def enae_table(doc, data, headers):
    """
    data: lista de listas con filas
    headers: lista de encabezados
    """
    table = doc.add_table(rows=1 + len(data), cols=len(headers))
    table.style = 'Table Grid'

    # Fila de encabezado: fondo granate, texto blanco
    hdr_row = table.rows[0]
    for i, h in enumerate(headers):
        cell = hdr_row.cells[i]
        cell.text = h
        run = cell.paragraphs[0].runs[0]
        run.font.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = BLANCO
        run.font.name = 'Calibri'
        # Fondo granate
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'), 'clear')
        shd.set(qn('w:color'), 'auto')
        shd.set(qn('w:fill'), 'A91831')
        tcPr.append(shd)

    # Filas de datos: alternas blanco / azul-gris claro
    for r_idx, row_data in enumerate(data):
        row = table.rows[r_idx + 1]
        fill_color = 'DEE5EC' if r_idx % 2 == 1 else 'FFFFFF'
        for c_idx, val in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.text = str(val)
            run = cell.paragraphs[0].runs[0]
            run.font.size = Pt(10)
            run.font.color.rgb = GRIS
            run.font.name = 'Calibri'
            # Fondo alternado
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            shd = OxmlElement('w:shd')
            shd.set(qn('w:val'), 'clear')
            shd.set(qn('w:color'), 'auto')
            shd.set(qn('w:fill'), fill_color)
            tcPr.append(shd)
    return table
```

---

## Pie de página oficial ENAE

Según el manual, el pie de la carta incluye:
- Logos institucionales: Universidad Politécnica de Cartagena, Cámara de Comercio Murcia, ENAE
- Línea separadora fina
- Datos de contacto: dirección, teléfono, fax, email, web

```
Edificio ENAE nº13, Campus Universitario de Espinardo, CP 30100 Murcia
Telf: 968 899 899  Fax: 868 88 41 33  Email: info@enae.es  www.enae.es
```

---

## Segunda hoja de carta

La segunda hoja (y siguientes) lleva únicamente:
- Logo ENAE (versión granate, reducido) en cabecera
- Sin logos institucionales en pie
- Mismos márgenes que la primera hoja
