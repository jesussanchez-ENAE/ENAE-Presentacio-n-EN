# Referencia: Ficha de Programa / Máster — ENAE Brand

## Cuándo usar este formato
- Ficha comercial de MBA, Máster o programa
- Dossier de programa para distribución digital o impresión
- Resumen ejecutivo de un curso o seminario

---

## Estructura visual de la ficha (HTML)

```
┌─────────────────────────────────────────────────┐
│  CABECERA granate #a91831                        │
│  Logo ENAE blanco + Brand pattern angular        │
├─────────────────────────────────────────────────┤
│  HERO: Nombre del programa                       │
│  Fondo granate oscurecido o con overlay          │
│  Badge modalidad + Claim                         │
├─────────────────────────────────────────────────┤
│  CIFRAS CLAVE — 4 columnas                       │
│  Fondo blanco, top-border granate                │
├─────────────────────────────────────────────────┤
│  DESCRIPCIÓN + OBJETIVOS                         │
│  Fondo blanco, acento izquierdo granate          │
├─────────────────────────────────────────────────┤
│  MÓDULOS / TEMARIO                               │
│  Fondo #dee5ec, numeración granate               │
├─────────────────────────────────────────────────┤
│  PERFIL + SALIDAS PROFESIONALES                  │
│  Fondo blanco                                    │
├─────────────────────────────────────────────────┤
│  DATOS PRÁCTICOS                                 │
│  Fondo granate, texto blanco — 4 columnas        │
├─────────────────────────────────────────────────┤
│  PIE: logos institucionales + contacto + claim   │
│  Fondo #202221                                   │
└─────────────────────────────────────────────────┘
```

---

## Componentes HTML clave

### Badge de modalidad
```html
<span class="badge-online">100% Online</span>
<span class="badge-presencial">Presencial</span>
<span class="badge-blended">Blended</span>

<style>
.badge-online, .badge-presencial, .badge-blended {
  font-family:'Open Sans',sans-serif; font-weight:700;
  font-size:10px; padding:5px 12px; letter-spacing:1.2px;
  text-transform:uppercase; color:#fff;
}
.badge-online     { background:#202221; }
.badge-presencial { background:#a91831; }
.badge-blended    { background:#606060; }
</style>
```

### Módulo de temario (numeración granate)
```html
<div class="modulo">
  <div class="modulo-num">01</div>
  <div class="modulo-info">
    <h3>Nombre del Módulo</h3>
    <p>Descripción breve del contenido del módulo.</p>
  </div>
</div>

<style>
.modulo {
  display:flex; gap:20px; padding:18px 0;
  border-bottom:1px solid #dee5ec;
  align-items:flex-start;
}
.modulo-num {
  font-family:'Open Sans',sans-serif; font-weight:800;
  font-size:32px; color:#a91831; min-width:52px;
  line-height:1;
}
.modulo-info h3 {
  font-family:'Open Sans',sans-serif; font-weight:700;
  font-size:14px; color:#202221; margin-bottom:4px;
}
.modulo-info p { font-size:13px; color:#404040; }
</style>
```

### Datos prácticos sobre fondo granate
```html
<div class="datos-practicos">
  <div class="dato">
    <span class="dato-label">Inicio</span>
    <span class="dato-valor">Octubre 2025</span>
  </div>
  <div class="dato">
    <span class="dato-label">Duración</span>
    <span class="dato-valor">12 meses</span>
  </div>
  <div class="dato">
    <span class="dato-label">Modalidad</span>
    <span class="dato-valor">Blended</span>
  </div>
  <div class="dato">
    <span class="dato-label">Idioma</span>
    <span class="dato-valor">Español</span>
  </div>
</div>

<style>
.datos-practicos {
  background:#a91831; padding:28px 40px;
  display:grid; grid-template-columns:repeat(4,1fr); gap:24px;
}
.dato { text-align:center; }
.dato-label {
  display:block; font-size:10px; font-weight:700;
  text-transform:uppercase; letter-spacing:1.2px;
  color:rgba(255,255,255,0.65); margin-bottom:6px;
}
.dato-valor {
  display:block; font-size:18px; font-weight:700;
  color:#fff;
}
</style>
```

### Ítem de salidas profesionales
```html
<li style="padding:8px 0 8px 20px;position:relative;font-size:14px;color:#404040;border-bottom:1px solid #dee5ec;">
  <span style="position:absolute;left:0;top:13px;width:10px;height:10px;
    background:#a91831;display:block;transform:rotate(45deg);"></span>
  Director de Marketing Digital
</li>
```

---

## Información estándar de programas ENAE

Usar estos datos por defecto si el usuario no especifica:
- **Profesorado**: +150 docentes nacionales e internacionales
- **Prácticas**: Red de +200 empresas colaboradoras
- **Bolsa de empleo**: Servicio activo (Agencia de Colocación Autorizada Nº 1400000046)
- **Titulación**: Diploma propio ENAE / doble titulación con UMU en programas seleccionados
- **Alumni**: Comunidad activa de antiguos alumnos
- **Afiliaciones pie**: Universidad Politécnica de Cartagena · Cámara de Comercio Murcia · INFO Región de Murcia
