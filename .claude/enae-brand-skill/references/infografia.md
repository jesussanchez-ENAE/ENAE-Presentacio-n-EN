# Referencia: Infografías y Visuales HTML — ENAE Brand

## Cuándo usar este formato
- Infografías de datos (estadísticas, cifras clave, rankings)
- Fichas visuales de programas educativos
- Timeline de eventos o historia institucional
- Comparativas de programas
- Resúmenes visuales de informes
- Banners informativos

## Paleta activa para infografías

| Variable          | HEX       | Uso en infografía                          |
|-------------------|-----------|--------------------------------------------|
| --enae-granate    | #a91831   | Cabecera, acentos, números destacados, brand pattern |
| --enae-negro      | #202221   | Pie de página, texto sobre fondos claros   |
| --enae-azul-gris  | #dee5ec   | Fondo de sección suave, tarjetas neutras   |
| --enae-blanco     | #ffffff   | Fondo principal, texto sobre granate       |
| --enae-gris-oscuro| #404040   | Texto cuerpo                               |

## Estructura visual de una infografía ENAE

```
┌─────────────────────────────────────────────┐
│  CABECERA granate #a91831                    │
│  [Logo ENAE blanco] + Título infografía      │
│  Brand pattern: bloques angulares decorativos│
├─────────────────────────────────────────────┤
│  CIFRAS CLAVE — grid tarjetas                │
│  Fondo blanco, número en granate ExtraBold   │
├─────────────────────────────────────────────┤
│  SECCIONES DE CONTENIDO                      │
│  Fondo blanco o #dee5ec alterno              │
│  Acento izquierdo granate 4px                │
├─────────────────────────────────────────────┤
│  PIE — fondo #202221                         │
│  Datos contacto + claim "Lead your future"   │
└─────────────────────────────────────────────┘
```

## Template HTML completo

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    @font-face {
      font-family: 'SFUIDisplay';
      src: url('../assets/fonts/SFUIDisplay-Black.otf') format('opentype');
      font-weight: 900;
    }
    @font-face {
      font-family: 'SFUIDisplay';
      src: url('../assets/fonts/SFUIDisplay-Bold.otf') format('opentype');
      font-weight: 700;
    }
    @font-face {
      font-family: 'OpenSans';
      src: url('../assets/fonts/OpenSans-ExtraBold.ttf') format('truetype');
      font-weight: 800;
    }
    @font-face {
      font-family: 'OpenSans';
      src: url('../assets/fonts/OpenSans-Bold.ttf') format('truetype');
      font-weight: 700;
    }
    @font-face {
      font-family: 'OpenSans';
      src: url('../assets/fonts/OpenSans-Light.ttf') format('truetype');
      font-weight: 300;
    }
    :root {
      --granate:   #a91831;
      --negro:     #202221;
      --azul-gris: #dee5ec;
      --blanco:    #ffffff;
      --gris:      #404040;
      --font-display: 'SFUIDisplay', 'Arial Black', sans-serif;
      --font: 'OpenSans', Arial, sans-serif;
    }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family:var(--font); background:var(--blanco); color:var(--gris); }

    /* ── CABECERA ── */
    .enae-header {
      background: var(--granate);
      color: var(--blanco);
      padding: 32px 40px 28px;
      position: relative;
      overflow: hidden;
    }
    /* Brand pattern: bloques angulares decorativos en cabecera */
    .enae-header::before {
      content: '';
      position: absolute;
      top: -20px; right: -20px;
      width: 140px; height: 140px;
      background: rgba(255,255,255,0.07);
      transform: rotate(18deg);
    }
    .enae-header::after {
      content: '';
      position: absolute;
      bottom: -30px; right: 80px;
      width: 90px; height: 90px;
      background: rgba(255,255,255,0.05);
      transform: rotate(35deg);
    }
    .enae-logo {
      display: flex;
      flex-direction: column;
      gap: 1px;
      margin-bottom: 18px;
    }
    .logo-text {
      font-family: var(--font-display);
      font-weight: 900;
      font-size: 30px;
      letter-spacing: 3px;
      color: var(--blanco);
      line-height: 1;
    }
    .logo-bar {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-top: 2px;
    }
    .logo-tagline {
      font-weight: 400;
      font-size: 10px;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      color: rgba(255,255,255,0.75);
    }
    .logo-line {
      flex: 1;
      max-width: 60px;
      height: 2px;
      background: rgba(255,255,255,0.5);
    }
    .header-title {
      font-family: var(--font-display);
      font-weight: 900;
      font-size: 24px;
      line-height: 1.2;
      position: relative;
      z-index: 1;
    }
    .header-subtitle {
      font-size: 14px;
      color: rgba(255,255,255,0.75);
      margin-top: 6px;
      position: relative;
      z-index: 1;
    }

    /* ── CONTENIDO ── */
    .content { padding: 36px 40px; }

    /* ── GRID DE CIFRAS ── */
    .stat-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(150px,1fr));
      gap: 16px;
      margin-bottom: 36px;
    }
    .stat-card {
      background: var(--blanco);
      border: 1px solid #eee;
      border-top: 4px solid var(--granate);
      padding: 20px 16px;
      text-align: center;
    }
    .stat-number {
      font-family: var(--font);
      font-weight: 800;
      font-size: 42px;
      color: var(--granate);
      line-height: 1;
    }
    .stat-suffix {
      font-weight: 700;
      font-size: 22px;
      color: var(--granate);
    }
    .stat-label {
      font-size: 11px;
      color: var(--gris);
      margin-top: 8px;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      font-weight: 600;
    }

    /* ── SECCIÓN CON ACENTO ── */
    .section {
      margin-bottom: 28px;
    }
    .section-title {
      font-weight: 700;
      font-size: 13px;
      color: var(--granate);
      text-transform: uppercase;
      letter-spacing: 1.5px;
      padding-left: 14px;
      border-left: 4px solid var(--granate);
      margin-bottom: 14px;
    }
    .section-body {
      font-size: 14px;
      line-height: 1.65;
      color: var(--gris);
    }

    /* ── SECCIÓN SOBRE AZUL GRIS ── */
    .section-alt {
      background: var(--azul-gris);
      padding: 24px 40px;
      margin: 0 -40px;
    }

    /* ── BRAND PATTERN bloque decorativo ── */
    .brand-block {
      display: inline-block;
      width: 48px; height: 12px;
      background: var(--granate);
      transform: rotate(-8deg);
      margin-right: 6px;
      vertical-align: middle;
    }
    .brand-block-sm {
      display: inline-block;
      width: 28px; height: 8px;
      background: var(--granate);
      transform: rotate(12deg);
      vertical-align: middle;
    }

    /* ── PIE ── */
    .enae-footer {
      background: var(--negro);
      color: rgba(255,255,255,0.55);
      padding: 18px 40px;
      font-size: 11px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
    }
    .footer-claim {
      color: rgba(255,255,255,0.9);
      font-weight: 700;
      font-size: 12px;
      font-style: italic;
      letter-spacing: 0.5px;
    }
  </style>
</head>
<body>

  <div class="enae-header">
    <!-- Logo oficial SVG — versión horizontal para cabeceras sobre fondo blanco o granate -->
    <!-- Sobre fondo granate usar filter:brightness(0) invert(1) para versión blanca -->
    <div class="enae-logo">
      <img src="../assets/logos/LOGO_ENAE_HORIZONTAL.svg"
           alt="ENAE International Business School"
           style="height:44px;width:auto;filter:brightness(0) invert(1);" />
    </div>
    <h1 class="header-title"><!-- Título de la infografía --></h1>
    <p class="header-subtitle"><!-- Subtítulo o descripción --></p>
  </div>

  <div class="content">

    <!-- Cifras clave -->
    <div class="stat-grid">
      <div class="stat-card">
        <div><span class="stat-number">30</span><span class="stat-suffix">+</span></div>
        <div class="stat-label">Años de experiencia</div>
      </div>
      <!-- Repetir .stat-card para cada dato -->
    </div>

    <!-- Sección con acento granate -->
    <div class="section">
      <h2 class="section-title">Título de sección</h2>
      <p class="section-body">Contenido de la sección...</p>
    </div>

  </div>

  <!-- Sección con fondo azul gris -->
  <div class="section-alt content">
    <div class="section">
      <h2 class="section-title">Otra sección</h2>
      <p class="section-body">Contenido alternativo...</p>
    </div>
  </div>

  <div class="enae-footer">
    <span>Edificio ENAE nº13, Campus Universitario de Espinardo, 30100 Murcia · 968 899 899 · www.enae.es</span>
    <span class="footer-claim">Lead your future</span>
  </div>

</body>
</html>
```

## Patrones visuales frecuentes

### Cifra con unidad
```html
<div class="stat-card">
  <div><span class="stat-number">150</span><span class="stat-suffix">+</span></div>
  <div class="stat-label">Profesores</div>
</div>
```

### Elemento de lista con punto granate
```html
<ul style="list-style:none;padding:0;">
  <li style="padding:6px 0;padding-left:16px;position:relative;font-size:14px;">
    <span style="position:absolute;left:0;top:10px;width:8px;height:8px;background:#a91831;display:block;transform:rotate(45deg);"></span>
    Texto del ítem
  </li>
</ul>
```

### Badge de categoría ENAE
```html
<span style="background:#a91831;color:#fff;font-family:'Open Sans',sans-serif;
  font-size:10px;font-weight:700;padding:4px 10px;letter-spacing:1.2px;
  text-transform:uppercase;">MBA</span>
```

### Separador con brand pattern
```html
<div style="display:flex;align-items:center;gap:8px;margin:20px 0;">
  <div style="width:40px;height:10px;background:#a91831;transform:rotate(-6deg);"></div>
  <div style="width:24px;height:10px;background:#a91831;transform:rotate(10deg);"></div>
  <div style="flex:1;height:1px;background:#dee5ec;"></div>
</div>
```

### Timeline con nodos granate
```html
<div style="display:flex;gap:0;align-items:flex-start;">
  <div style="text-align:center;flex:1;">
    <div style="width:14px;height:14px;background:#a91831;margin:0 auto;transform:rotate(45deg);"></div>
    <div style="width:1px;height:40px;background:#dee5ec;margin:0 auto;"></div>
    <p style="font-size:12px;font-weight:700;color:#a91831;">2024</p>
    <p style="font-size:11px;">Descripción</p>
  </div>
</div>
```

## Dimensiones recomendadas
- Infografía vertical A4: 794px × 1123px
- Infografía cuadrada redes: 800px × 800px
- Banner web horizontal: 1200px × 400px
- Ficha de programa: 794px × auto

## Reglas de calidad ENAE para infografías
1. El granate `#a91831` domina. Nunca más del 30% del área en granate sólido excepto en cabecera/pie.
2. Los números grandes son el "gancho" — Open Sans ExtraBold, granate.
3. El brand pattern (bloques angulares) aporta dinamismo — siempre presente aunque sea sutil.
4. Fondos: blanco como principal, `#dee5ec` para secciones alternas, `#202221` solo en pie.
5. Nunca usar sombras intensas — la marca es plana y limpia.
6. La línea horizontal junto a "International Business School" en el logo es obligatoria.
