# Referencia: Presentaciones (.pptx) — ENAE Brand

## Cuándo usar este formato
- Presentaciones institucionales y de programas académicos
- Keynotes y conferencias
- Presentaciones comerciales (MBA, Másteres, cursos)
- Informes de resultados
- Materiales de bienvenida para alumnos

## Antes de crear la presentación
Lee `/mnt/skills/public/pptx/SKILL.md` para las instrucciones técnicas de python-pptx.

---

## Colores en python-pptx

```python
from pptx.dml.color import RGBColor

GRANATE = RGBColor(0xA9, 0x18, 0x31)   # #a91831 — color primario ENAE
NEGRO   = RGBColor(0x20, 0x22, 0x21)   # #202221 — secundario
AZUL_GRIS = RGBColor(0xDE, 0xE5, 0xEC) # #dee5ec — complemento suave
BLANCO  = RGBColor(0xFF, 0xFF, 0xFF)   # #ffffff
GRIS    = RGBColor(0x40, 0x40, 0x40)   # #404040 — texto cuerpo
```

## Tipografía en presentaciones
- Titulares / display: **Calibri Bold** (sustituye SF UI Display, siempre disponible en Office)
- Cuerpo y bullets: **Open Sans Regular/SemiBold** (o Calibri como fallback)
- Cifras destacadas: **Calibri ExtraBold** o **Open Sans ExtraBold**
- Colores: títulos en granate `#a91831` sobre blanco, o blanco sobre granate

---

## Tipos de diapositivas ENAE

### 1. Portada / Cover
- **Fondo**: granate `#a91831` sólido
- **Brand pattern**: bloques rectangulares blancos angulados (rotados 8-20°),
  semi-transparentes (10-15% opacidad), zona derecha o esquinas
- **Logo ENAE**: esquina superior izquierda, versión blanca
  - "ENAE" en blanco, bold, grande
  - "International Business School" en blanco 75%, pequeño
  - Línea blanca horizontal a la derecha del texto "Business School"
- **Título**: Calibri Bold 36-40pt, blanco, zona central-izquierda
- **Subtítulo / fecha**: blanco 70%, 18pt
- **Claim**: "Lead your future" en blanco, italic, parte inferior

```python
# Fondo granate
slide.background.fill.solid()
slide.background.fill.fore_color.rgb = GRANATE

# Brand pattern: añadir rectángulos blancos angulados
from pptx.util import Inches, Pt, Emu
import math

def add_brand_block(slide, left, top, width, height, angle, opacity=0.1):
    shape = slide.shapes.add_shape(1, left, top, width, height)  # MSO_SHAPE_TYPE.RECTANGLE
    shape.fill.solid()
    shape.fill.fore_color.rgb = BLANCO
    shape.fill.fore_color.transparency = 1 - opacity
    shape.line.fill.background()
    shape.rotation = angle
```

### 2. Diapositiva de contenido estándar
- **Cabecera**: franja granate `#a91831`, altura ~18-20% del alto total
  - Logo ENAE pequeño (blanco) en esquina superior derecha de la franja
  - Título de la diapositiva: blanco, Calibri Bold 24pt, centrado-izquierda
- **Cuerpo**: fondo blanco
- **Texto bullets**: Calibri/Open Sans 18pt, color `#404040`
- **Bullet points**: cuadrado rotado 45° en granate (diamante) en lugar de punto circular
- **Pie**: línea fina granate en parte inferior + número de página

### 3. Diapositiva de cifras / KPIs
- **Fondo**: blanco
- **Grid 3-4 columnas** de tarjetas
- Cada tarjeta:
  - Borde superior 4pt en granate `#a91831`
  - Número: Open Sans ExtraBold, 48-56pt, granate
  - Unidad/sufijo: 24pt, granate
  - Etiqueta: Open Sans SemiBold, 11pt, uppercase, gris `#404040`

### 4. Diapositiva de cita / testimonio
- **Fondo**: granate `#a91831`
- **Comillas decorativas**: blanco, tamaño muy grande (80-100pt), semi-transparente
- **Texto de la cita**: blanco, Calibri Italic 20-22pt, centrado
- **Fuente / autor**: blanco 65%, 13pt
- **Brand pattern**: bloques angulares sutiles en esquinas

### 5. Diapositiva de sección / separador
- **Fondo**: granate `#a91831`
- **Número de sección**: blanco, ExtraBold, 72pt, semitransparente (20%)
- **Título de sección**: blanco, Bold, 32pt
- **Brand pattern**: prominente, zona derecha

### 6. Contraportada / Cierre
- **Fondo**: negro `#202221`
- **Texto central**: "Lead your future" en blanco, italic, grande
- **Logo ENAE**: centrado, blanco
- **Datos contacto**: blanco 55%, pequeño, centrado
- **Acento**: pequeños bloques granate decorativos

---

## Dimensiones estándar

```python
from pptx.util import Cm
prs.slide_width  = Cm(33.87)  # 16:9 widescreen
prs.slide_height = Cm(19.05)
```

---

## Logo ENAE en python-pptx (representación textual)

```python
from pptx.util import Pt, Inches
from pptx.dml.color import RGBColor

def add_enae_logo_white(slide, left, top, width=Inches(1.8)):
    """Logo ENAE versión blanca para fondos granate/oscuros."""
    # Texto "ENAE"
    txBox = slide.shapes.add_textbox(left, top, width, Pt(40))
    tf = txBox.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "ENAE"
    run.font.bold = True
    run.font.size = Pt(28)
    run.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
    run.font.name = "Calibri"

    # Subtexto "International Business School"
    txBox2 = slide.shapes.add_textbox(left, top + Pt(32), width, Pt(16))
    tf2 = txBox2.text_frame
    p2 = tf2.paragraphs[0]
    run2 = p2.add_run()
    run2.text = "International Business School ──────"
    run2.font.size = Pt(8)
    run2.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
    run2.font.name = "Calibri"

def add_enae_logo_red(slide, left, top, width=Inches(1.8)):
    """Logo ENAE versión granate para fondos blancos."""
    txBox = slide.shapes.add_textbox(left, top, width, Pt(40))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "ENAE"
    run.font.bold = True
    run.font.size = Pt(28)
    run.font.color.rgb = GRANATE
    run.font.name = "Calibri"
```

---

## Reglas de diseño para presentaciones ENAE

- Máximo 6 puntos por diapositiva
- Solo 2 fondos distintos en toda la presentación: granate y blanco (negro para cierre)
- El brand pattern (bloques angulares) aparece siempre en portada, separadores y cierre
- El granate es el protagonista — no diluirlo con muchos colores
- Numeración de página: esquina inferior derecha, pequeño, granate
- Cada diapositiva lleva el logo ENAE (versión apropiada según fondo)
