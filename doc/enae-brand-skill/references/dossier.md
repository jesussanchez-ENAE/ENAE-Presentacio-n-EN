# Referencia: Dossier multipágina / Registro Editorial Premium — ENAE Brand

> Esta referencia se basa en un dossier corporativo **oficial** de ENAE
> ("ENAE & China: Un Puente Estratégico"), guardado como ejemplo en
> `assets/examples/dossier-china/`. Estúdialo siempre antes de maquetar un
> dossier: el PDF (`Dossier_ENAE_China.pdf`) y las 20 páginas en imagen
> (`paginas/p-01.png` … `p-20.png`) son la fuente de verdad de este formato.

## Cuándo usar este formato

- Dossiers institucionales y de programa (8–24 páginas)
- Brochures corporativos, memorias, catálogos de oferta
- Portadas y piezas de campaña con vocación aspiracional
- Cualquier pieza multipágina A4 vertical que deba "vender" la marca

Formato base: **A4 vertical, 794 px × 1123 px por página** (a 96 dpi).
Entrega como **PDF** (preferido) o como artifact HTML paginado.

---

## Los dos registros visuales de ENAE

El dossier oficial demuestra que ENAE trabaja con **dos registros** complementarios.
Elegir el correcto es la primera decisión de diseño:

| Registro | Piezas | Fondo | Gradientes | Foto | Tono |
|----------|--------|-------|-----------|------|------|
| **Funcional / corporativo** | Documentos, infografías de datos, fichas, cartas | Blanco, granate plano, `#dee5ec` | No | Acotada | Limpio, claro, informativo |
| **Editorial / premium** | Dossiers, portadas, brochures, campañas | Negro, granate, gradientes granate↔oscuro | Sí, atmosféricos | A sangre, protagonista | Aspiracional, emotivo, impactante |

Esta referencia cubre el **registro editorial**. Las reglas de "fondo siempre blanco"
y "nunca gradientes" del SKILL.md aplican al registro funcional, **no a este**.
Lo que nunca cambia entre registros: el granate `#a91831` es el color de marca,
nunca azul como dominante, y la tipografía es siempre la oficial.

---

## El recurso de marca clave: el TÍTULO MIXTO

Es la firma visual del dossier. Cada página abre con un título de 2–3 líneas que
**combina tres estilos tipográficos en un mismo bloque**:

1. **Línea sans pesada** — SF UI Display Black / Open Sans ExtraBold. Mayúsculas o
   capital case. Es el ancla del título. Ej.: `ENAE & China:`, `de ENAE`, `PROGRAMAS`.
2. **Línea serif itálica** — serif de alto contraste en *cursiva*. Es el acento
   elegante y diferenciador. Ej.: *Un Puente Estratégico*, *¿Qué es*, *Nuestros*.
3. **Línea sans ligera** — Open Sans Light. Cierra o contextualiza. Ej.:
   `para la Formación Internacional`.

No siempre aparecen las tres líneas, pero **la serif itálica casi siempre está
presente**, aunque sea en una sola palabra. También se usa en las etiquetas de los
KPI (*formando líderes*, *de profesorado*, *socias*) y en intertítulos (*Valor añadido*).

```html
<h1 class="dossier-title">
  <span class="t-bold">ENAE &amp; China:</span>
  <span class="t-serif">Un Puente Estratégico</span>
  <span class="t-light">para la Formación Internacional</span>
</h1>
```

```css
.dossier-title { line-height: 1.05; color: var(--blanco); }
.dossier-title span { display: block; }
.t-bold  { font-family: var(--font-display); font-weight: 900;
           font-size: 52px; letter-spacing: -0.5px; }
.t-serif { font-family: var(--font-serif); font-style: italic;
           font-weight: 700; font-size: 52px; }
.t-light { font-family: var(--font-body); font-weight: 300; font-size: 46px; }
```

> El serif itálico **no es** SF UI Display ni Open Sans. Es un serif Didone de alto
> contraste. La skill no incluye el archivo oficial: usa **Playfair Display** (Google
> Fonts) como equivalente fiel, declarado en `--font-serif`. Ver `references/fuentes.md`.

---

## Anatomía del dossier

### Portada (página 1)
- Fotografía **a sangre** que ocupa toda la página (gente, campus, graduaciones).
- Encima, **overlay de gradiente**: de negro/oscuro arriba-izquierda a granate con
  un foco de luz granate (resplandor) en la zona derecha. La foto queda integrada,
  oscurecida y unificada con la marca.
- **Logo ENAE en blanco**, arriba a la izquierda.
- **Título mixto** grande en el tercio superior-medio.
- Watermark del **brand pattern "E"** muy sutil sobre el gradiente.

```css
.cover {
  position: relative; width: 794px; height: 1123px; overflow: hidden;
}
.cover .photo { position: absolute; inset: 0; width: 100%; height: 100%;
  object-fit: cover; }
.cover .overlay {
  position: absolute; inset: 0;
  background:
    radial-gradient(60% 50% at 78% 42%, rgba(169,24,49,0.55) 0%, transparent 70%),
    linear-gradient(135deg, rgba(32,34,33,0.96) 0%, rgba(32,34,33,0.55) 45%,
                            rgba(169,24,49,0.80) 100%);
}
.cover .inner { position: relative; z-index: 2; padding: 56px; }
```

### Páginas interiores
Cada página es **monotema** y autocontenida. Patrones de fondo que se alternan a lo
largo del dossier (todos vistos en el ejemplo oficial):

| Fondo | Uso | CSS |
|-------|-----|-----|
| **Granate pleno** | Páginas de rankings, listados, datos de programa | `background: var(--granate);` |
| **Gradiente granate→oscuro** | Páginas de coordinación, instalaciones, contacto | `linear-gradient(160deg, #a91831 0%, #5e0f1e 60%, #202221 100%)` |
| **Negro / carbón** | Páginas de cifras, misión, secciones sobrias | `background: var(--negro);` o `linear-gradient(150deg,#202221,#000)` |
| **Foto a sangre + overlay** | Páginas hero de programa estrella | igual que la portada |

Sobre **todos** los fondos oscuros va el **watermark del brand pattern "E"** al 4–8 %
de opacidad (fragmentos angulares grandes). Nunca un fondo oscuro liso y vacío.

### Estructura tipo de página interior
```
┌───────────────────────────────────────┐
│  TÍTULO MIXTO (bold + serif itálica)   │
│                                        │
│  Párrafo introductorio (Open Sans      │
│  Light, con frases clave en bold)      │
│                                        │
│  CONTENIDO: tarjetas / KPIs / lista /  │
│  foto a sangre / tabla                 │
│                                        │
│  [watermark "E" de fondo, sutil]       │
└───────────────────────────────────────┘
```
Las páginas interiores **no llevan pie de contacto** (solo la última, la de CONTACTO).
El logo solo aparece en portada y contraportada/contacto.

---

## Componentes del registro editorial

### Tarjeta blanca sobre fondo oscuro/granate
Módulo de contenido más habitual. Blanca, esquinas redondeadas (12–16 px), sin borde,
sombra muy suave. El título de tarjeta usa serif itálica + bold.

```css
.card {
  background: var(--blanco); border-radius: 14px; padding: 28px 24px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.18);
}
.card-eyebrow { font-family: var(--font-serif); font-style: italic;
  font-weight: 700; color: var(--granate); font-size: 18px; }
.card-title { font-family: var(--font-body); font-weight: 800;
  color: var(--negro); font-size: 19px; }
.card-body { font-family: var(--font-body); font-weight: 300;
  color: var(--gris); font-size: 14px; line-height: 1.6; }
```

### Tarjeta translúcida sobre granate
Para listas de datos sobre fondo granate pleno (página de rankings).
```css
.card-glass {
  background: rgba(255,255,255,0.10); border-radius: 12px; padding: 20px 22px;
  color: var(--blanco);
}
```

### Número fantasma (ghost number)
Cifra enorme semitransparente, detrás o encima de la tarjeta a la que da contexto.
Es el "gancho" visual de las páginas de ranking.
```css
.ghost-number {
  font-family: var(--font-body); font-weight: 800; font-size: 110px;
  color: rgba(255,255,255,0.22); line-height: 0.8; letter-spacing: -2px;
}
```

### KPI editorial
Cifra blanca gigante + etiqueta en bold con remate en serif itálica.
```html
<div class="kpi">
  <span class="kpi-num">+37</span>
  <span class="kpi-label">años</span>
  <span class="kpi-sub">formando líderes</span>
</div>
```
```css
.kpi-num   { font-family: var(--font-body); font-weight: 800; font-size: 96px;
             color: var(--blanco); line-height: 0.9; }
.kpi-label { font-family: var(--font-body); font-weight: 800; font-size: 26px;
             color: var(--blanco); }
.kpi-sub   { font-family: var(--font-serif); font-style: italic;
             font-size: 22px; color: var(--blanco); }
```

### Pill / badge redondeado
```css
.pill {
  display: inline-block; background: var(--blanco); color: var(--negro);
  border-radius: 999px; padding: 10px 22px; font-weight: 700;
}
.pill em { color: var(--granate); font-style: normal; font-weight: 800; }
```

### Watermark del brand pattern "E"
Fragmentos angulares de la letra E, grandes, al 4–8 % de opacidad, rotados,
sangrando por los bordes. Imprescindible en fondos oscuros para que no queden planos.
```css
.bg-pattern { position: absolute; inset: 0; overflow: hidden; z-index: 0; }
.bg-pattern span {
  position: absolute; background: rgba(255,255,255,0.05);
}
/* Ej.: tres bloques rotados, tamaños y posiciones variables y asimétricas */
```

### Fotografía a sangre con lavado granate
Toda foto del registro editorial se integra con un overlay granate/oscuro
(efecto "duotono" suave), nunca se coloca en crudo.
```css
.photo-bleed { position: relative; }
.photo-bleed::after {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(180deg, rgba(32,34,33,0.15),
                                       rgba(169,24,49,0.35));
  mix-blend-mode: multiply;
}
```

---

## Reglas de calidad del registro editorial

1. **Una idea por página.** Cada página interior trata un único tema; no se amontona.
2. **El título mixto abre cada página.** Bold + serif itálica como mínimo.
3. **Ningún fondo oscuro queda liso.** Siempre lleva watermark "E" o gradiente.
4. **Las fotos van a sangre y con lavado granate**, nunca recortadas en cajita ni en crudo.
5. **Granate, negro y blanco.** El gradiente vive entre granate y oscuro; el azul gris
   `#dee5ec` casi no se usa en este registro.
6. **Las cifras son protagonistas** — Open Sans ExtraBold, gigantes, blancas sobre oscuro.
7. **Jamás azul como color dominante** (esta regla no cambia en ningún registro).
8. **Contraste de legibilidad**: texto siempre blanco puro sobre granate/negro; texto
   negro/gris solo dentro de tarjetas blancas.
9. **El logo solo en portada y contacto.** Las interiores van sin logo.
10. **Cierre con página de CONTACTO**: logo ENAE blanco centrado + datos + claim.

## Checklist antes de entregar un dossier
- [ ] He revisado el ejemplo oficial en `assets/examples/dossier-china/`
- [ ] Portada con foto a sangre + overlay gradiente + logo blanco
- [ ] Todos los títulos usan el recurso mixto (bold + serif itálica)
- [ ] `--font-serif` (Playfair Display) declarado para los acentos itálicos
- [ ] Fondos oscuros con watermark "E", nunca lisos
- [ ] Fotos a sangre con lavado granate
- [ ] Última página = CONTACTO con logo y claim "Lead your future"
- [ ] Cero azul dominante; paleta granate/negro/blanco
