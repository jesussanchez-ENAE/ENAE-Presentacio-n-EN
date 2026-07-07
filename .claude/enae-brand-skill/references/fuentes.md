# Referencia: Fuentes Corporativas ENAE

Las fuentes oficiales de ENAE están incluidas en la skill en:
`assets/fonts/`

## Fuentes disponibles

| Archivo                  | Familia         | Peso / Estilo   | Uso principal                              |
|--------------------------|-----------------|-----------------|---------------------------------------------|
| SFUIDisplay-Black.otf    | SF UI Display   | Black (900)     | Logotipo ENAE, titulares de gran impacto    |
| SFUIDisplay-Bold.otf     | SF UI Display   | Bold (700)      | Subtítulos display, titulares secundarios   |
| OpenSans-ExtraBold.ttf   | Open Sans       | ExtraBold (800) | Cifras destacadas, KPIs, números grandes    |
| OpenSans-Bold.ttf        | Open Sans       | Bold (700)      | Titulares en documentos, encabezados        |
| OpenSans-Light.ttf       | Open Sans       | Light (300)     | Cuerpo de texto, subtítulos largos          |
| *(Google Fonts)*         | Playfair Display| Italic (600/700)| Acento serif itálico en titulares editoriales|

> **Serif de acento editorial.** Los dossiers, brochures y portadas de ENAE usan
> una serif Didone itálica para palabras de acento en los titulares (el "título
> mixto"). La skill no incluye el archivo oficial; usa **Playfair Display** de
> Google Fonts como equivalente fiel. Declárala como `--font-serif` y enlázala en
> el `<head>`:
> ```html
> <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,600;1,700&display=swap" rel="stylesheet">
> ```
> Solo se usa en el **registro editorial**. Ver `references/dossier.md`.

---

## Cómo usar las fuentes en cada tipo de pieza

### En HTML / infografías (con @font-face)

Cuando la pieza HTML se genera como archivo en el sistema de archivos (no en navegador
web externo), usar rutas relativas o absolutas a los archivos .ttf / .otf:

```css
@font-face {
  font-family: 'SFUIDisplay';
  src: url('assets/fonts/SFUIDisplay-Black.otf') format('opentype');
  font-weight: 900;
  font-style: normal;
}
@font-face {
  font-family: 'SFUIDisplay';
  src: url('assets/fonts/SFUIDisplay-Bold.otf') format('opentype');
  font-weight: 700;
  font-style: normal;
}
@font-face {
  font-family: 'OpenSans';
  src: url('assets/fonts/OpenSans-ExtraBold.ttf') format('truetype');
  font-weight: 800;
  font-style: normal;
}
@font-face {
  font-family: 'OpenSans';
  src: url('assets/fonts/OpenSans-Bold.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
}
@font-face {
  font-family: 'OpenSans';
  src: url('assets/fonts/OpenSans-Light.ttf') format('truetype');
  font-weight: 300;
  font-style: normal;
}

:root {
  --font-display: 'SFUIDisplay', 'Arial Black', sans-serif;
  --font-body:    'OpenSans', Arial, sans-serif;
}
```

**Nota para piezas HTML que se abren en navegador**: copiar las fuentes junto al HTML
o usar rutas absolutas. Si no es posible, la Google Fonts `Open Sans` es el fallback
web aceptable para Open Sans; SF UI Display no tiene equivalente exacto en Google Fonts
— usar `'Barlow', sans-serif` o `'Montserrat', sans-serif` como aproximación visual.

### En presentaciones .pptx (python-pptx)

python-pptx no puede embeber fuentes OTF/TTF directamente, pero si las fuentes están
instaladas en el sistema, se puede especificar su nombre:

```python
# Primero instalar las fuentes en el sistema (solo necesario una vez)
import subprocess
import shutil, os

FONTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets', 'fonts')

def install_fonts():
    """Instala las fuentes ENAE en el sistema para uso en pptx."""
    dest = '/usr/local/share/fonts/enae/'
    os.makedirs(dest, exist_ok=True)
    for f in os.listdir(FONTS_DIR):
        if f.endswith(('.ttf', '.otf')):
            shutil.copy(os.path.join(FONTS_DIR, f), dest)
    subprocess.run(['fc-cache', '-fv'], capture_output=True)

# En el código de presentación:
install_fonts()

# Luego usar el nombre de la fuente normalmente:
run.font.name = 'SFUIDisplay-Black'    # o el nombre interno de la fuente
run.font.name = 'Open Sans'             # para Open Sans
```

Para verificar el nombre interno de las fuentes instaladas:
```bash
fc-list | grep -i "enae\|sfui\|opensans"
```

### En documentos .docx (python-docx)

Igual que en pptx: si las fuentes están instaladas en el sistema, se puede referenciar
por nombre. Si no, Word las sustituirá por la fuente más similar disponible.

```python
# Instalar fuentes primero (ver función install_fonts() arriba)
run.font.name = 'SFUIDisplay-Black'   # titulares logo/display
run.font.name = 'Open Sans'            # cuerpo
```

### En generación de PDFs con canvas/reportlab

```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

FONTS_DIR = 'assets/fonts'

pdfmetrics.registerFont(TTFont('SFUIDisplay-Black',
    os.path.join(FONTS_DIR, 'SFUIDisplay-Black.otf')))
pdfmetrics.registerFont(TTFont('SFUIDisplay-Bold',
    os.path.join(FONTS_DIR, 'SFUIDisplay-Bold.otf')))
pdfmetrics.registerFont(TTFont('OpenSans-ExtraBold',
    os.path.join(FONTS_DIR, 'OpenSans-ExtraBold.ttf')))
pdfmetrics.registerFont(TTFont('OpenSans-Bold',
    os.path.join(FONTS_DIR, 'OpenSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont('OpenSans-Light',
    os.path.join(FONTS_DIR, 'OpenSans-Light.ttf')))
```

---

## Jerarquía tipográfica ENAE — guía rápida

| Elemento                  | Fuente                  | Peso | Tamaño orientativo |
|---------------------------|-------------------------|------|--------------------|
| Logotipo "ENAE"           | SFUIDisplay-Black       | 900  | Grande / display   |
| Titular hero / portada    | SFUIDisplay-Black       | 900  | 36–56px / pt       |
| Titular secundario        | SFUIDisplay-Bold        | 700  | 24–32px / pt       |
| Cifra KPI / número grande | OpenSans-ExtraBold      | 800  | 42–64px / pt       |
| Encabezado sección        | OpenSans-Bold           | 700  | 14–18px / pt       |
| Cuerpo de texto           | OpenSans-Light          | 300  | 11–15px / pt       |
| Etiqueta / label uppercase| OpenSans-Bold           | 700  | 9–11px / pt        |
| Claim italic              | OpenSans-Light italic*  | 300  | 12–14px / pt       |

*OpenSans-Light no incluye variante italic; aplicar `font-style: italic` en CSS
para síntesis del navegador, o usar OpenSans-Bold italic como alternativa.

---

## Fallbacks si las fuentes no están disponibles

```css
/* Display / titulares */
font-family: 'SFUIDisplay', 'SF Pro Display', 'Arial Black', 'Helvetica Neue', sans-serif;

/* Cuerpo */
font-family: 'OpenSans', 'Open Sans', 'Segoe UI', Arial, sans-serif;
```
