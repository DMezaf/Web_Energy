# HANDOFF — Blog "Mantenimiento de subestaciones AT, MT y BT"

**Fecha:** 2026-04-27
**Responsable contenido:** equipo digital VMS Energy
**Estado:** listo para revisión técnica → publicación

## Archivos creados / modificados

| Archivo | Estado | Notas |
|---|---|---|
| `blog-mantenimiento-reparacion-subestaciones-at-mt-bt.html` | **REESCRITO** | Era stub de 454 líneas → ahora artículo completo ~2,800 palabras, 11 secciones, JSON-LD BlogPosting/Breadcrumb/FAQ, layout 2-col article+sidebar |
| `checklist-anual-subestaciones-at-mt-bt.html` | **NUEVO** | Lead magnet imprimible (12 secciones, 80+ items). `noindex,follow` — no entra al sitemap |
| `assets/img/blog/mantenimiento-subestaciones/prompts.md` | **NUEVO** | Prompts AI para 4 imágenes de la familia visual del artículo |
| `blog-subestacion-electrica-industrial.html` | **EDITADO** | 3 placeholders en bloque "Lecturas relacionadas" activados (líneas 5489, 5495, 5501) |
| `sitemap.xml` | **EDITADO** | `lastmod` actualizado en los 2 blogs anteriores → 2026-04-27 |

## Pendientes ANTES de publicar (responsable: marketing/diseño)

### 1. Imágenes — ENTREGADAS (2026-04-27)

Las 5 imágenes están en disco con los nombres exactos referenciados por el HTML:

- `assets/img/blog/mantenimiento-subestaciones/hero-mantenimiento-subestaciones.webp` (190 KB)
- `assets/img/blog/mantenimiento-subestaciones/og-mantenimiento-subestaciones.webp` (190 KB — copia del hero, idealmente sustituir por crop específico 1200×630)
- `assets/img/blog/mantenimiento-subestaciones/tipos-mantenimiento-subestaciones.svg` (5.9 KB)
- `assets/img/blog/mantenimiento-subestaciones/pruebas-electricas-subestaciones.svg` (6.6 KB)
- `assets/img/blog/mantenimiento-subestaciones/caso-cementera-jalisco-69kv.webp` (308 KB)

**Nota:** existen copias originales en `assets/img/` raíz con nombres genéricos (`substation.webp`, `cementera_jalisco.webp`, `Composicion_de_Enfoques.svg`, `Grid_Layout_Design.svg`). Pueden eliminarse cuando se confirme que no se usan en otro lado del sitio.

**Pendiente menor:** generar OG 1200×630 específico (recorte del hero) para mejor render en Facebook/LinkedIn/WhatsApp. Hoy se usa la copia 1600×900 del hero, que las plataformas recortarán automáticamente.

### 2. Validar contenido editorial técnico
- Pasar el artículo por revisión de un ingeniero senior eléctrico VMS — verificar precisión de:
  - Frecuencias de mantenimiento por equipo (sección 5)
  - Normas citadas (sección 4) — confirmar que NMX-J-169-ANCE es el ID correcto vigente
  - Tabla de pruebas y normas (sección 3)
  - Detalles del caso Cementera Jalisco — añadir métricas duras si las hay (horas de paro, MWh, equipos exactos)
- Validar JSON-LD con [Google Rich Results Test](https://search.google.com/test/rich-results) antes de publicar

### 3. Confirmar slug del cliente para el caso
El blog cita: *"planta cementera, Jalisco (2025)"*. Sin nombre comercial. Si VMS tiene autorización del cliente para usar nombre, sustituir y solicitar logo para mostrar en `case-card`.

## Pendientes EN PUBLICACIÓN (responsable: dev/SEO ops)

### 4. 301 desde URL del WordPress al .html
La URL canónica del artículo en WP era:
```
https://vmsenergy.com/mantenimiento-y-reparacion-de-subestaciones-electricas-at-mt-y-bt-en-mexico/
```

Configurar redirección 301 permanente hacia:
```
https://vmsenergy.com/blog-mantenimiento-reparacion-subestaciones-at-mt-bt.html
```

Sin esto se pierde el equity SEO acumulado y se generan dos URLs con el mismo H1.

### 5. Despublicar la versión antigua del WP
Una vez confirmado el 301, despublicar (no eliminar) la entrada en WordPress para evitar que los rastreadores la indexen.

### 6. Resubir sitemap.xml a Google Search Console
- Dominio: `vmsenergy.com`
- Acción: re-enviar `https://vmsenergy.com/sitemap.xml` para que Google detecte los `lastmod` actualizados.
- Solicitar indexación específica de:
  - `https://vmsenergy.com/blog-mantenimiento-reparacion-subestaciones-at-mt-bt.html`
  - `https://vmsenergy.com/blog-subestacion-electrica-industrial.html` (cambios de cross-link)

### 7. Verificar el form del CTA
Los CTAs del blog apuntan a:
```
contacto_cta.html?producto=mantenimiento-subestaciones
```

Verificar en producción que:
- El form expande a 7 campos al detectar `?producto=*` (comportamiento documentado).
- El backend/email del form etiqueta correctamente la lead como `mantenimiento-subestaciones` para distinguir en CRM/email a comercial.

### 8. Verificar que `contacto.html` ≡ `contacto_cta.html` o ajustar
Pendiente fuera de alcance de este handoff: el blog grande [`blog-subestacion-electrica-industrial.html`](blog-subestacion-electrica-industrial.html) tiene CTAs apuntando a `contacto.html#inicio` (líneas 5298, 5522, 6060). Si `contacto.html` no es el form unificado actualizado, esos CTAs envían leads "ciegas" sin etiquetado de producto. Tarea separada — coordinar con el dueño de `contacto.html`.

## Métricas a monitorear post-publicación (responsable: marketing analytics)

### Primer mes
- **CTR en Search Console** para queries: "mantenimiento subestaciones", "mantenimiento subestación industrial México", "termografía subestación", "mantenimiento preventivo subestación".
- **Posición promedio** vs. el artículo del WP previo (para confirmar que el 301 transfirió correctamente).
- **Tasa de clic** en el lead magnet (`/checklist-anual-subestaciones-at-mt-bt.html`) — instrumentar evento en GA4.
- **Conversiones del form** con etiqueta `producto=mantenimiento-subestaciones`.

### Tres meses
- Posicionamiento de keywords objetivo en top 10.
- Backlinks adquiridos (buscar menciones en directorios industriales y publicaciones técnicas).
- Compartido del checklist (puede usarse como ancla para campañas LinkedIn dirigidas a jefes de mantenimiento eléctrico).

## Reglas anti-canibalización aplicadas (no romper en futuras ediciones)

Este artículo (mantenimiento) y [`blog-subestacion-electrica-industrial.html`](blog-subestacion-electrica-industrial.html) (modernización) son piezas hermanas con intenciones de búsqueda diferenciadas:

- **Modernización (existente)** se queda con: NSIC, capas Power/Protection/Control/Communication, CAPEX/OPEX, autodiagnóstico "renovar/instalar".
- **Mantenimiento (nuevo)** se queda con: predictivo/preventivo/correctivo, pruebas eléctricas, normativa de operación recurrente, frecuencias, contratos.
- Cross-links recíprocos ya implementados: `#autodiagnostico` desde mantenimiento → grande, y bloque "Lecturas relacionadas" en grande → mantenimiento.

**No duplicar** secciones de NSIC/capas o CAPEX/OPEX en el de mantenimiento si se edita en el futuro — referenciar al grande con anchor.

## Aviso colateral (no bloquea publicación)

El blog grande tiene 2 placeholders más de "Lecturas relacionadas" (líneas 5495, 5501) apuntando a `blog.html` con títulos *"Diagnóstico y modernización de sistemas eléctricos"* y *"Evaluación técnica previa a proyectos EPC"*. Esos artículos no existen aún. Si en el plan editorial 2026 se redactan, sustituir el href de `blog.html` al slug específico.
