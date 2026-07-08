# Referencia: Newsletter / Email HTML — ENAE Brand

## Cuándo usar este formato
- Newsletter mensual para alumnos y profesionales
- Email de bienvenida a nuevos alumnos
- Comunicados de eventos y conferencias
- Email de marketing de programas y másteres

---

## Reglas técnicas de email HTML
- **Ancho máximo**: 600px (compatible con todos los clientes de correo)
- **Fuente segura**: Arial, sans-serif (fallback universal)
- **Layout**: tablas HTML (no CSS grid/flexbox — compatibilidad Outlook)
- **Imágenes**: siempre con `alt` descriptivo
- **Fondo externo**: `#dee5ec` (azul gris suave)

---

## Template completo

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ENAE International Business School</title>
</head>
<body style="margin:0;padding:20px;background:#dee5ec;font-family:Arial,sans-serif;">

  <table width="600" cellpadding="0" cellspacing="0"
         style="margin:0 auto;background:#ffffff;max-width:600px;">

    <!-- ══ HEADER ══ -->
    <tr>
      <td style="background:#a91831;padding:24px 30px 20px;">
        <!-- Logo ENAE -->
        <table cellpadding="0" cellspacing="0">
          <tr>
            <td>
              <div style="font-family:Arial,sans-serif;font-weight:900;
                font-size:26px;letter-spacing:3px;color:#ffffff;line-height:1;">
                ENAE
              </div>
              <div style="font-size:9px;letter-spacing:2.5px;color:rgba(255,255,255,0.7);
                text-transform:uppercase;margin-top:3px;">
                International Business School &nbsp;──────
              </div>
            </td>
          </tr>
        </table>
      </td>
    </tr>

    <!-- ══ HERO / TITULAR ══ -->
    <tr>
      <td style="background:#202221;padding:28px 30px 24px;">
        <p style="margin:0 0 8px;font-size:11px;font-weight:700;
          color:#a91831;text-transform:uppercase;letter-spacing:1.5px;">
          Categoría o etiqueta
        </p>
        <h1 style="margin:0;font-size:22px;font-weight:900;
          color:#ffffff;line-height:1.25;">
          Título principal del email
        </h1>
        <p style="margin:10px 0 0;font-size:14px;color:rgba(255,255,255,0.7);
          line-height:1.5;">
          Subtítulo o descripción breve del contenido.
        </p>
      </td>
    </tr>

    <!-- ══ CUERPO PRINCIPAL ══ -->
    <tr>
      <td style="padding:30px 30px 24px;">
        <p style="margin:0 0 16px;font-size:15px;color:#404040;line-height:1.65;">
          Texto de introducción del email. Directo y profesional, orientado al
          lector y a la acción.
        </p>

        <!-- Separador con acento granate -->
        <div style="border-left:4px solid #a91831;padding-left:16px;
          margin:20px 0;color:#404040;font-size:14px;line-height:1.6;">
          Punto destacado o dato clave que merece atención especial.
        </div>

        <p style="margin:0 0 20px;font-size:15px;color:#404040;line-height:1.65;">
          Continuación del texto principal...
        </p>

        <!-- CTA Principal -->
        <table cellpadding="0" cellspacing="0" style="margin:24px 0;">
          <tr>
            <td style="background:#a91831;">
              <a href="https://www.enae.es"
                 style="display:inline-block;padding:13px 28px;
                   color:#ffffff;font-size:13px;font-weight:700;
                   text-decoration:none;letter-spacing:0.8px;
                   text-transform:uppercase;font-family:Arial,sans-serif;">
                MÁS INFORMACIÓN
              </a>
            </td>
          </tr>
        </table>
      </td>
    </tr>

    <!-- ══ SECCIÓN SECUNDARIA (fondo azul-gris) ══ -->
    <tr>
      <td style="background:#dee5ec;padding:24px 30px;">
        <p style="margin:0 0 8px;font-size:10px;font-weight:700;
          color:#a91831;text-transform:uppercase;letter-spacing:1.5px;">
          También te puede interesar
        </p>
        <p style="margin:0;font-size:14px;color:#202221;line-height:1.55;">
          Contenido secundario o enlace complementario.
        </p>
      </td>
    </tr>

    <!-- ══ FOOTER ══ -->
    <tr>
      <td style="background:#202221;padding:20px 30px;text-align:center;">
        <p style="margin:0 0 6px;color:rgba(255,255,255,0.5);font-size:10px;">
          ENAE International Business School
        </p>
        <p style="margin:0 0 6px;color:rgba(255,255,255,0.4);font-size:10px;">
          Edificio ENAE nº13, Campus Universitario de Espinardo, 30100 Murcia
        </p>
        <p style="margin:0 0 10px;color:rgba(255,255,255,0.4);font-size:10px;">
          968 899 899 · info@enae.es · www.enae.es
        </p>
        <p style="margin:0;color:#a91831;font-size:11px;font-style:italic;font-weight:700;">
          Lead your future
        </p>
      </td>
    </tr>

  </table>
</body>
</html>
```

---

## Botones CTA ENAE
- Fondo: `#a91831` (granate) — nunca redondeado, esquinas rectas
- Texto: BLANCO, uppercase, bold, letra-spacing 0.8px
- Padding: 13px 28px
- CTA secundario: borde granate 2px, texto granate, fondo transparente

## Colores en email
- Cabecera: `#a91831`
- Hero/destacado: `#202221`
- Cuerpo: `#ffffff`
- Sección secundaria: `#dee5ec`
- Footer: `#202221`
- Texto principal: `#404040`
- Acento/etiquetas: `#a91831`
- Claim footer: `#a91831`

## Tipografía segura para email
- Arial, sans-serif (siempre disponible)
- Pesos: normal (400) y bold (700/900) vía `font-weight`
- Tamaños: 10px datos, 13-15px cuerpo, 22-24px titular
