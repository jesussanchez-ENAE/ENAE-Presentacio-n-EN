---
name: enae-brand
description: >
  Crea documentos, infografías, presentaciones, informes y materiales visuales
  con la identidad corporativa oficial de ENAE International Business School.
  Usa esta skill siempre que el usuario pida crear cualquier material para ENAE:
  documentos Word, PDFs, dossiers, brochures, memorias, infografías HTML,
  presentaciones, fichas de programas, newsletters, banners, plantillas, sobres,
  cartas corporativas, portadas o cualquier pieza de comunicación. También se
  activa con frases como "estilo ENAE", "con la marca ENAE", "para ENAE Business
  School", "materiales ENAE", "dossier de ENAE", "siguiendo la estética de ENAE"
  o "identidad corporativa ENAE".
---

# ENAE Brand Skill

Crea materiales visuales y documentos que respetan estrictamente el Manual de
Identidad Corporativa oficial de ENAE International Business School (Murcia, España).

> ⚠️ CRÍTICO: El color primario de ENAE es ROJO GRANATE (#a91831), NO azul.
> Cualquier material que use azul como color dominante viola la identidad corporativa.

---

## Identidad visual oficial (extraída del Manual Corporativo ENAE)

### Paleta de colores corporativa

| Rol               | Nombre              | HEX       | PANTONE       | CMYK                | RGB             |
|-------------------|---------------------|-----------|---------------|---------------------|-----------------|
| **Primario**      | Rojo Granate ENAE   | `#a91831` | PANTONE 7627C | C22 M100 Y74 K18    | R169 G24 B49    |
| Secundario        | Negro Casi Total    | `#202221` | PANTONE 419C  | C75 M63 Y61 K78     | R32 G34 B33     |
| Secundario suave  | Azul Gris Muy Claro | `#dee5ec` | PANTONE 656C  | C15 M7 Y6 K0        | R222 G229 B236  |
| Neutro            | Blanco Puro         | `#ffffff` | —             | —                   | R255 G255 B255  |
| Escala grises     | Negro 100%          | `#000000` | —             | K100                | R0 G0 B0        |
| Escala grises     | Gris oscuro 75%     | `#404040` | —             | K75                 | R64 G64 B64     |
| Escala grises     | Gris medio 40%      | `#999999` | —             | K40                 | R153 G153 B153  |

**Regla de oro de color**: el granate `#a91831` es el color dominante y diferenciador.
El negro `#202221` para textos y fondos oscuros. El azul gris `#dee5ec` como color de
fondo suave o complemento. Nunca usar colores fuera de esta paleta sin justificación.

### Tipografía oficial

#### Tipografía corporativa principal (display/logotipo)
- **SF UI Display Black** — titulares, logotipo, impactos visuales grandes
- **SF UI Display Light** — subtítulos, textos complementarios en display

*SF UI Display es la tipografía personalizada adaptada para ENAE. Es la fuente
del propio logotipo.*

#### Tipografía serif de acento (registro editorial)
- **Serif Didone itálica** — palabras de acento en titulares de dossiers, portadas
  y piezas de campaña. Es la firma del registro editorial de ENAE (ver más abajo).

Las piezas oficiales combinan en un mismo título: una línea **sans pesada**, una
línea **serif itálica** de acento y, a veces, una línea **sans ligera**. Este
"título mixto" es un recurso de marca recurrente — ver `references/dossier.md`.

La skill no incluye el archivo de la serif oficial: usa **Playfair Display**
(Google Fonts) como equivalente fiel del Didone itálico de alto contraste.

#### Familia tipográfica para uso corporativo y web
**Open Sans** — fuentes incluidas en la skill en `assets/fonts/`:

| Archivo                | Peso | Uso principal                          |
|------------------------|------|----------------------------------------|
| OpenSans-ExtraBold.ttf | 800  | Cifras KPI, números grandes, impactos  |
| OpenSans-Bold.ttf      | 700  | Titulares en documentos y web          |
| OpenSans-Light.ttf     | 300  | Cuerpo de texto, textos largos         |

> ⚠️ SIEMPRE usar las fuentes locales del skill (`assets/fonts/`) con `@font-face`.
> Solo usar Google Fonts como fallback si el archivo HTML se sirve en web sin acceso
> a los archivos locales. Ver instrucciones completas en `references/fuentes.md`.

**@font-face estándar para todas las piezas HTML:**
```css
@font-face {
  font-family: 'SFUIDisplay';
  src: url('../assets/fonts/SFUIDisplay-Black.otf') format('opentype');
  font-weight: 900; font-style: normal;
}
@font-face {
  font-family: 'SFUIDisplay';
  src: url('../assets/fonts/SFUIDisplay-Bold.otf') format('opentype');
  font-weight: 700; font-style: normal;
}
@font-face {
  font-family: 'OpenSans';
  src: url('../assets/fonts/OpenSans-ExtraBold.ttf') format('truetype');
  font-weight: 800; font-style: normal;
}
@font-face {
  font-family: 'OpenSans';
  src: url('../assets/fonts/OpenSans-Bold.ttf') format('truetype');
  font-weight: 700; font-style: normal;
}
@font-face {
  font-family: 'OpenSans';
  src: url('../assets/fonts/OpenSans-Light.ttf') format('truetype');
  font-weight: 300; font-style: normal;
}
/* Serif de acento editorial — Playfair Display vía Google Fonts.
   Incluir también en el <head>:
   <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,600;1,700&display=swap" rel="stylesheet"> */
```

### Logotipo: estructura y reglas

Los archivos SVG oficiales están en `assets/logos/`. Ver `references/logos.md` para
la guía completa de uso. Resumen rápido:

| Archivo                        | Cuándo usarlo                                  |
|--------------------------------|------------------------------------------------|
| `LOGO_ENAE_HORIZONTAL.svg`     | Cabeceras, documentos, emails — fondo blanco   |
| `ENAE_Color.svg`               | Portadas y materiales principales — fondo blanco|
| `ENAE_Negro.svg`               | Impresión B&N / monocromo                      |
| `SIMBOLO_ENAE_FONDO_ROJO.svg`  | Fondos granate/oscuros, avatares, iconos       |
| `SIMBOLO_ENAE_FONDO_NEGRO.svg` | Fondos negros, avatares versión dark           |

**Tamaño mínimo**: 30mm ancho (logo completo) · 3mm (símbolo solo).

#### Versiones de color permitidas
- **Positivo**: logotipo granate sobre fondo blanco ✅
- **Negativo**: logotipo blanco sobre fondo granate o negro ✅
- **Blanco y negro**: logotipo negro sobre blanco ✅
- **Una tinta**: versión monocromo ✅

#### Usos incorrectos del logotipo — NUNCA hacer
- ❌ Cambiar el color del logotipo (ni intensidad ni tono)
- ❌ Usar el logotipo granate sobre fondos oscuros (pierde legibilidad)
- ❌ Deformar, aplastar o estirar el logotipo
- ❌ Dividir el logotipo por la mitad
- ❌ Alterar la distribución o posición de sus elementos
- ❌ Suprimir "Business School" o la línea decorativa
- ❌ Reproducir sobre fondos de color que no sean blanco o granate

### Área de protección del logotipo
Margen mínimo alrededor del logotipo = valor X (altura de la "E" del logotipo).
Ningún otro elemento puede entrar en esa zona.

### Brand Pattern (elemento gráfico diferenciador)
El brand pattern de ENAE son **fragmentos angulares / bloques rotos de las letras ENAE**
(especialmente la "E") en rojo granate sobre fondo blanco o granate sobre blanco.
- Bloques rectangulares con cortes angulares en diagonal
- Escala variable: desde pequeños acentos hasta grandes elementos decorativos
- Distribución dinámica y asimétrica, no simétrica
- Transmite movimiento, modernidad y "dirección al futuro"
- Claim actual: **"Lead your future"** / **"Lead your way"**

---

## Variables CSS base (para piezas HTML)

```css
/* SIEMPRE incluir primero el bloque @font-face del apartado "Tipografía oficial" */
:root {
  /* Colores oficiales ENAE */
  --enae-granate:      #a91831;
  --enae-negro:        #202221;
  --enae-azul-gris:    #dee5ec;
  --enae-blanco:       #ffffff;
  --enae-gris-oscuro:  #404040;  /* 75% negro */
  --enae-gris-medio:   #999999;  /* 40% negro */

  /* Tipografía — fuentes locales de assets/fonts/ */
  --font-display: 'SFUIDisplay', 'Arial Black', sans-serif;
  --font-body:    'OpenSans', Arial, sans-serif;
  --font-serif:   'Playfair Display', Georgia, serif; /* acento editorial itálico */
}
```

---

## Los dos registros visuales de ENAE

ENAE trabaja con dos registros complementarios. Identificar el correcto es la
**primera decisión de diseño** de cualquier pieza:

| Registro | Piezas típicas | Fondo | Gradientes | Fotografía |
|----------|----------------|-------|-----------|------------|
| **Funcional / corporativo** | Documentos Word, infografías de datos, fichas, cartas, newsletters | Blanco, granate plano, `#dee5ec` | No — color plano | Acotada, en cajas |
| **Editorial / premium** | Dossiers, brochures, portadas, memorias, campañas | Negro, granate, gradientes granate↔oscuro | Sí — atmosféricos | A sangre, protagonista |

Ambos registros comparten el ADN de marca: granate `#a91831` como color de marca,
**nunca azul como dominante**, y la tipografía oficial. Lo que cambia es el "tono":
el funcional es claro e informativo; el editorial es aspiracional e impactante.

> Las reglas "fondo siempre blanco" y "nunca gradientes" aplican al **registro
> funcional**. El **registro editorial** (dossiers, portadas) sí usa fondos
> oscuros, gradientes granate↔oscuro y fotografía a sangre — así lo demuestran
> las piezas oficiales de ENAE. Ver `references/dossier.md` y el ejemplo oficial
> en `assets/examples/dossier-china/`.

---

## Tipos de piezas y archivos de referencia

Lee el archivo de referencia antes de crear cada pieza:

| Tipo de pieza             | Archivo de referencia              | Formato      |
|---------------------------|------------------------------------|--------------|
| Fuentes corporativas      | `references/fuentes.md`            | —            |
| **Logos oficiales**       | `references/logos.md`              | SVG          |
| **Dossier / brochure**    | `references/dossier.md`            | PDF / HTML   |
| Infografía / Visual HTML  | `references/infografia.md`         | HTML artifact|
| Presentación              | `references/presentacion.md`       | .pptx        |
| Documento / Carta Word    | `references/documento.md`          | .docx        |
| Ficha de programa/máster  | `references/ficha-programa.md`     | HTML o PDF   |
| Newsletter / Email        | `references/newsletter.md`         | HTML artifact|

**Ejemplo de diseño oficial**: el dossier "ENAE & China" en
`assets/examples/dossier-china/` es la referencia canónica del registro editorial.
Estúdialo (PDF + páginas en imagen) antes de maquetar dossiers, brochures o portadas.

---

## Proceso general de creación

1. Identificar el tipo de pieza **y su registro** (funcional o editorial)
2. Si es dossier/brochure/portada: revisar el ejemplo oficial en
   `assets/examples/dossier-china/` y leer `references/dossier.md`
3. Leer `references/logos.md` para seleccionar el logo correcto según el fondo/contexto
4. Leer `references/fuentes.md` y el archivo de referencia correspondiente al tipo de pieza
5. Incluir `@font-face` con las fuentes locales de `assets/fonts/` (y Playfair Display
   si la pieza es del registro editorial)
6. Incrustar el logo SVG correcto desde `assets/logos/`
7. Aplicar la identidad ENAE con fidelidad al manual y al registro elegido
8. Producir el archivo en el formato correcto
9. Presentar al usuario con `present_files`

---

## Reglas de diseño ENAE (siempre aplicar)

### ✅ Hacer siempre
- **Rojo granate `#a91831` como color de marca** — es la firma visual de ENAE
- Open Sans para el texto; SF UI Display para logotipo y grandes titulares;
  serif itálica (Playfair Display) para acentos en el registro editorial
- En el **registro funcional**: fondo blanco o granate plano, sin gradientes
- En el **registro editorial**: fondos negro/granate y gradientes granate↔oscuro,
  con watermark del brand pattern "E" y fotografía a sangre
- Brand pattern (bloques/fragmentos angulares de la "E") como elemento decorativo
- Logotipo en esquina superior izquierda en piezas funcionales; en dossiers solo
  en portada y contraportada
- Claim "Lead your future" o "Lead your way" cuando el espacio lo permita

### ❌ Nunca hacer
- Usar azul como color principal (no es el corporativo de ENAE) — **regla universal**
- Cambiar el color del logotipo o deformarlo
- Mezclar más de 3 pesos/estilos tipográficos en un mismo bloque de texto
- Usar gradientes o fondos oscuros en el **registro funcional** (docs, infografías
  de datos, fichas) — ahí la identidad es plana
- Poner el logotipo granate sobre fondo oscuro (usar la versión blanca)
- Usar tipografías que no sean Open Sans, SF UI Display o la serif de acento
- Colocar fotografías en crudo sin el lavado granate en el registro editorial

---

## Información institucional ENAE

- **Nombre**: ENAE International Business School
- **Nombre largo**: Escuela de Negocios y Administración de Empresas
- **Dirección**: Edificio ENAE nº 13, Campus Universitario de Espinardo, CP 30100, Murcia, España
- **Teléfono**: 968 899 899
- **Fax**: 868 88 41 33
- **Web**: www.enae.es
- **Email**: info@enae.es
- **Claims**: *Lead your future* / *Lead your way*
- **Afiliaciones**: Universidad Politécnica de Cartagena, Cámara de Comercio de Murcia, INFO Región de Murcia
- **Acreditación**: AACSB (proceso), Agencia de Colocación Autorizada Nº 1400000046
- **Experiencia**: +30 años
- **Docentes**: +150 profesores nacionales e internacionales
- **Empresas colaboradoras**: +200
- **Alcance**: España y Latinoamérica
