# Prompts para imagenes del articulo "Mantenimiento y reparacion de subestaciones electricas AT, MT y BT en Mexico"

## Direccion visual recomendada

- Estilo: industrial premium, fotografia tecnica realista, sin look generico de stock.
- Paleta: azul marino, acero, blanco tecnico, acentos azul VMS (#0F4C81).
- Formato base: horizontal 16:9.
- Calidad: alta nitidez, iluminacion controlada, composicion limpia, profundidad realista.
- Evitar: personas posando, texto incrustado, iconografia caricaturesca, renders plasticosos, cables desordenados, logos visibles.
- Familia visual: alineada con `assets/img/blog/tableros-distribucion/` para que la seccion blog se sienta como un sistema.

## 1. Hero principal

- Archivo sugerido: `hero-mantenimiento-subestaciones.svg` (o .webp si se genera con AI)
- Uso: encabezado del articulo, Open Graph, tarjeta del blog, schema BlogPosting.image.
- Alt sugerido: `Mantenimiento de subestacion electrica industrial de alta tension en planta cementera`

Prompt:

```text
Industrial high voltage electrical substation outdoor yard during preventive maintenance, three-quarter view of energized 69kV equipment with disconnect switches, circuit breakers and current transformers, technician in arc flash PPE inspecting from safe distance, clean structured cable trays, blue sky with subtle atmospheric haze, premium industrial engineering photography, controlled dramatic lighting, blue and steel palette, sharp focus, no people facing camera, no text, no watermark, composition with negative space top-left for headline, 16:9
```

## 2. Tipos de mantenimiento (predictivo, preventivo, correctivo)

- Archivo sugerido: `tipos-mantenimiento-subestaciones.svg`
- Uso: seccion donde se contrastan los tres enfoques de mantenimiento.
- Alt sugerido: `Comparativa visual de mantenimiento predictivo, preventivo y correctivo en subestaciones electricas`

Prompt:

```text
Clean technical infographic comparing three maintenance approaches for electrical substations: predictive (data sensors, IoT, monitoring waveform), preventive (calendar schedule, checklist, inspection routine) and corrective (alert icon, repair tools, urgent intervention), three-column layered composition, industrial engineering visual language, minimal premium layout, blue white steel palette with subtle accent color per column, modern vector look, no excessive text, no clutter, 16:9
```

## 3. Pruebas electricas clave

- Archivo sugerido: `pruebas-electricas-subestaciones.svg`
- Uso: apoyo visual antes o despues de la tabla de pruebas tecnicas.
- Alt sugerido: `Infografia de pruebas electricas: termografia, factor de potencia, rigidez dielectrica y resistencia de aislamiento en subestaciones`

Prompt:

```text
Technical infographic showing six key electrical tests performed on substation equipment: thermographic inspection of bushings (heat-map style), insulation resistance megger test, power factor test on transformer, dielectric breakdown of mineral oil, contact resistance on circuit breaker and partial discharge detection, elegant grid composition with one icon per test, industrial engineering visual language, blue white steel palette, premium vector design, minimal labels, no branding, 16:9
```

## 4. Caso real: Mantenimiento mayor 69kV cementera Jalisco

- Archivo sugerido: `caso-cementera-jalisco-69kv.svg` (o foto real si el cliente la autoriza)
- Uso: bloque de prueba social / mini-caso de exito autorizado por VMS.
- Alt sugerido: `Mantenimiento mayor a subestacion 69kV en planta cementera de Jalisco intervenida por VMS Energy en 2025`

Prompt (si va por AI, no foto):

```text
Industrial cement plant electrical substation at 69kV during major maintenance shutdown, outdoor switchyard with lattice steel structures, suspension insulators, disconnect switches with operating mechanisms and bus work, cement plant silos and stack visible in soft background, dust-free clean intervention setup, golden hour lighting on dry Jalisco landscape, realistic industrial photography, premium documentary style, no people facing camera, no visible logos, no text, sense of scale and engineering rigor, 16:9
```

> Nota: si VMS dispone de foto real autorizada del proyecto Cementera Jalisco 2025, sustituir esta imagen por la real con consentimiento del cliente y guardarla como `caso-cementera-jalisco-69kv.webp` (1600x900, optimizada).

## Recomendacion de uso dentro del articulo

- 1 imagen hero al inicio (despues del H1, antes del TOC).
- 1 infografia de tipos de mantenimiento despues de la seccion "Tipos de mantenimiento".
- 1 visual de pruebas electricas justo antes de la tabla de pruebas o entre H2 y H3.
- 1 imagen del caso Cementera Jalisco dentro del bloque "Caso real" antes del CTA final.

## Tip extra

Si generas con IA, manten el mismo prompt base de estilo (paleta, lighting, composition) y solo cambia el sujeto. Eso ayuda a que las cuatro piezas se vean como una sola familia visual y a que el blog completo (mantenimiento + tableros + futuras entregas) tenga identidad consistente.

## Checklist de exportacion

- [ ] Formato: SVG para infografias, WEBP para fotos/heros.
- [ ] Resolucion minima: 1600x900 (heros), 1200x675 (apoyos).
- [ ] Peso: < 250 KB por imagen WEBP, calidad 80-85.
- [ ] Open Graph: copia del hero a 1200x630 exacto en `og-mantenimiento-subestaciones.webp`.
- [ ] `alt` text en HTML: usar exactamente los sugeridos arriba (incluye keyword + geo).
