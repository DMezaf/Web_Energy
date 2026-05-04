# Playbook — Enriquecimiento de contenido VMShop / Cables KEI

> **Propósito de este archivo:** Brief de campaña de contenido (no es la guía general del repo — para eso ver `CLAUDE.md` en la raíz).
> Contiene instrucciones precisas para enriquecer las landing pages de suministro de cable
> de VMS Energy con contenido que posiciona a la empresa bajo el arquetipo del **Sabio**
> y refuerza su core business como **integrador EPC turnkey**.
>
> **No modificar:** estructura de navegación, footer, estilos CSS existentes, lógica JS de catálogos.
> **Sí modificar / agregar:** secciones de contenido dentro de `<main>`, FAQs, notas de ingeniería.

---

## 1. Contexto del proyecto

**Empresa:** VMS Energy — EPC turnkey con casi 20 años de experiencia en sistemas eléctricos,
electromecánicos e infraestructura energética industrial en México.

**Core business:** Ingeniería, Procura y Construcción (EPC) integral. El suministro de cable
NO es un negocio de distribución — es parte del alcance EPC. Cuando VMS especifica y suministra
un cable, también lo instala, prueba y pone en servicio.

**VMShop:** Plataforma de suministro técnico especializado. Partner estratégico principal: KEI Wires & Cables
(representante exclusivo en México). Otros fabricantes activos: Südkabel, Helukabel, Condumex, Viakon.

**Arquetipo de marca:** El Sabio. VMS no vende cables — orienta, especifica y recomienda la
solución correcta para cada proyecto. El contenido debe enseñar y anticipar errores antes de vender.

**Sectores prioritarios:** Minería, Oil & Gas, Energía Solar Industrial, Alimentos & Bebidas,
Ingeniería Pesada.

---

## 2. Arquitectura HTML de referencia

Todos los archivos LP usan este patrón de secciones dentro de `<main>`:

```html
<main>
  <section class="hero"> ... </section>          <!-- Hero con kicker, h1, CTAs, bullets -->
  <section class="steps"> ... </section>         <!-- 3 pasos: Diagnóstico / Especificación / Suministro -->
  <section>                                      <!-- Grid de 2 cards: Aplicaciones + Valor -->
    <div class="container grid"> ... </div>
  </section>
  <section class="catalog" id="catalogo"> ... </section>  <!-- Catálogo con filtros JS -->
  <section>                                      <!-- Notas de ingeniería (.notes-panel) -->
    <div class="container"> ... </div>
  </section>
  <section class="faq"> ... </section>           <!-- FAQ con grid de cards -->
</main>
```

**Componentes HTML reutilizables de referencia:**

```html
<!-- Card estándar -->
<article class="card">
  <h2>Título</h2>
  <ul class="list">
    <li>Item</li>
  </ul>
</article>

<!-- Notes panel (notas de ingeniería) -->
<div class="notes-panel">
  <div class="notes-panel__head">
    <span class="notes-panel__tag">Notas de Ingeniería</span>
    <h3 class="notes-panel__title">Título</h3>
  </div>
  <p class="notes-panel__sub">Subtítulo</p>
  <ul class="note-list">
    <li>Nota 1</li>
  </ul>
</div>

<!-- FAQ card -->
<article class="card">
  <h3>¿Pregunta?</h3>
  <p>Respuesta.</p>
</article>

<!-- Notes card (variante con grid) -->
<div class="notes-card">
  <h4 class="notes-card__title">Título</h4>
  <p class="notes-card__text">Contenido</p>
</div>
```

---

## 3. BLOQUE COMPARTIDO A — Módulo multi-proveedor

**Insertar en:** `lp-cable-de-potencia-kei.html`, `lp-cables-alta-tension.html`,
`lp-cables-extra-alta-tension.html`, `lp-cables-fotovoltaicos.html`, `lp-cables-especiales.html`

**Posición:** Después del `<section class="steps">` y antes de la sección de aplicaciones/valor.

**HTML a insertar:**

```html
<!-- BLOQUE A: Multi-proveedor estratégico -->
<section style="background:var(--soft,#f4f8ff);padding:36px 0">
  <div class="container">
    <div class="notes-panel">
      <div class="notes-panel__head">
        <span class="notes-panel__tag">Portafolio de fabricantes</span>
        <h3 class="notes-panel__title">No llegamos con un solo catálogo. Llegamos con la especificación correcta para tu proyecto.</h3>
      </div>
      <p class="notes-panel__sub">VMS Energy selecciona el fabricante óptimo según el nivel de tensión, sector, norma aplicable, disponibilidad y cronograma de tu proyecto. KEI Wires &amp; Cables es nuestro partner estratégico principal, pero trabajamos con los mejores fabricantes del mundo cuando el proyecto lo requiere.</p>
      <div class="notes-grid" style="margin-top:16px">
        <div class="notes-card">
          <h4 class="notes-card__title">KEI Wires &amp; Cables</h4>
          <p class="notes-card__text">Representante exclusivo para México. Potencia MT/AT/EHV, cables ESP para Oil &amp; Gas, fotovoltaicos, instrumentación y control. Primera opción para la mayoría de proyectos industriales en México.</p>
        </div>
        <div class="notes-card">
          <h4 class="notes-card__title">Südkabel</h4>
          <p class="notes-card__text">Especialidad en cables EHV de alta ingeniería (fabricación alemana). Ideal cuando el proyecto requiere estándares europeos, certificaciones VDE o construcciones especiales para transmisión de extra alta tensión.</p>
        </div>
        <div class="notes-card">
          <h4 class="notes-card__title">Helukabel</h4>
          <p class="notes-card__text">Soluciones para control, instrumentación y aplicaciones especiales: LSZH para espacios confinados, EMC blindados, alta temperatura (silicona), cables para industria alimentaria y robótica.</p>
        </div>
        <div class="notes-card">
          <h4 class="notes-card__title">Condumex / Viakon</h4>
          <p class="notes-card__text">Fabricación nacional bajo NMX-J. Baja tensión y control con tiempos de entrega cortos. Ideal para proyectos con componente nacional requerida o urgencias en campo. Cumplimiento NOM-001-SEDE.</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## 4. BLOQUE COMPARTIDO B — Módulo EPC integrado

**Insertar en:** Todos los archivos LP mencionados en el Bloque A.

**Posición:** Inmediatamente después del Bloque A (multi-proveedor).

**HTML a insertar:**

```html
<!-- BLOQUE B: Conexión EPC Turnkey -->
<section style="padding:36px 0 28px">
  <div class="container">
    <div class="notes-panel" style="border-left:4px solid var(--cobalt,#0F4C81)">
      <div class="notes-panel__head">
        <span class="notes-panel__tag">EPC Integrado</span>
        <h3 class="notes-panel__title">Cuando VMS suministra el cable, ya sabe cómo va a instalarse — porque somos quienes lo instalarán.</h3>
      </div>
      <p class="notes-panel__sub">El suministro a través de VMShop no es una compra de producto. Es la etapa de procura dentro de un proyecto EPC que VMS ingenia, construye y pone en marcha.</p>
      <ul class="note-list">
        <li><strong>Ingeniería:</strong> Especificamos el cable correcto según carga, ruta, ambiente y normativa — no el cable más económico en catálogo.</li>
        <li><strong>MTO coordinado:</strong> El listado de materiales de cable está sincronizado con el cronograma de construcción, no con el inventario del proveedor.</li>
        <li><strong>Logística por hitos:</strong> Entregamos cable cuando la obra lo necesita, en la cantidad correcta y con trazabilidad completa por bobina.</li>
        <li><strong>Responsabilidad única:</strong> Una sola empresa responde por especificación, suministro, instalación, pruebas y commissioning.</li>
      </ul>
      <p style="margin-top:14px;font-size:.93rem;color:var(--muted,#4E6782)">
        Si solo necesitas suministro sin instalación, también podemos apoyarte — con la misma rigurosidad técnica y logística que aplicamos en nuestros proyectos EPC.
      </p>
    </div>
  </div>
</section>
```

---

## 5. INSTRUCCIONES POR ARCHIVO

---

### 5.1 `lp-cables-alta-tension.html`

**Cambios requeridos:**

#### A. Actualizar título del catálogo (línea aprox. 497)
Cambiar:
```html
<h2 class="catalog__title">catálogo de cables de alta tensión (KEI)</h2>
```
Por:
```html
<h2 class="catalog__title">Catálogo de cables de alta tensión</h2>
<p style="font-size:.9rem;color:var(--muted,#4E6782);margin:4px 0 0">Fabricante principal: KEI Wires &amp; Cables. Construcciones alternativas disponibles con Südkabel bajo especificación de proyecto.</p>
```

#### B. Expandir Notas de Ingeniería (reemplazar el `<ul class="note-list">` existente)
Reemplazar las 3 notas actuales por:
```html
<ul class="note-list">
  <li><strong>Ampacidad y temperatura:</strong> Validar corriente admisible del conductor a 90 °C en operación normal y 250 °C en cortocircuito. Aplicar factores de corrección por temperatura ambiente, agrupamiento y método de instalación (ducto, bandeja, enterrado).</li>
  <li><strong>Construcción y blindaje:</strong> Para instalación subterránea en suelos agresivos, especificar armadura de acero y cubierta HDPE. Para instalación en bandeja con riesgo de humedad, validar barrera antihumedad longitudinal.</li>
  <li><strong>Norma aplicable:</strong> Proyectos con conexión a CFE deben cumplir especificaciones LAPEM. Proyectos privados: IEC 60502 (MT) o IEC 60840 (AT). Verificar si el proyecto requiere NMX-J o norma internacional.</li>
  <li><strong>Coordinación logística:</strong> Cable AT bajo pedido (on-demand) requiere 8 a 14 semanas de fabricación. Incluir este tiempo en el cronograma EPC antes de comprometer fecha de puesta en servicio.</li>
  <li><strong>QA/QC en recepción:</strong> Todo suministro VMS incluye certificado de pruebas por bobina, etiquetado de trazabilidad y verificación de longitudes antes de instalación.</li>
</ul>
<div class="notes-badges" style="margin-top:12px">
  <span class="notes-badge">IEC 60502</span>
  <span class="notes-badge">IEC 60840</span>
  <span class="notes-badge">NMX-J</span>
  <span class="notes-badge">LAPEM/CFE</span>
  <span class="notes-badge">NOM-001-SEDE</span>
</div>
```

#### C. Expandir FAQ (reemplazar el `<div class="grid">` dentro de `<section class="faq">`)
Reemplazar las 2 cards actuales por:
```html
<div class="grid" style="grid-template-columns:1fr 1fr;gap:14px">
  <article class="card">
    <h3>¿Qué información necesito para cotizar cable AT?</h3>
    <p>Nivel de tensión (U0/U en kV), longitud total por tramo, tipo de instalación (enterrado, bandeja, ducto), norma requerida (IEC, NMX-J, CFE/LAPEM), temperatura ambiente del sitio y cronograma de entrega requerido.</p>
  </article>
  <article class="card">
    <h3>¿Pueden coordinar entregas por etapas de obra?</h3>
    <p>Sí. Programamos entregas por hitos con trazabilidad por bobina y documentación completa (certificados de prueba, MTC, empaque). Esto es estándar en todos nuestros proyectos EPC.</p>
  </article>
  <article class="card">
    <h3>¿Qué diferencia hay entre cable con armadura y sin armadura?</h3>
    <p>La armadura (alambres de acero galvanizado) protege mecánicamente contra impactos y aplastamiento. Es obligatoria en instalación directamente enterrada y recomendada en ductos con riesgo de daño mecánico. En bandeja interior sin riesgo mecánico, generalmente no es necesaria.</p>
  </article>
  <article class="card">
    <h3>¿Puedo usar conductores de aluminio en lugar de cobre?</h3>
    <p>Sí. El aluminio reduce el costo del conductor pero requiere secciones mayores para igual ampacidad (aproximadamente 1.5 veces). La decisión depende del balance entre costo, peso, espacio disponible en bandejas y requerimientos del cliente o norma del proyecto.</p>
  </article>
  <article class="card">
    <h3>¿Qué documentación entrega VMS con el suministro?</h3>
    <p>Certificado de pruebas de fábrica (tipo e individual por bobina), hoja de datos del cable, reporte de longitudes medidas, etiquetado de trazabilidad por lote y, si el proyecto lo requiere, documentación para CFE/PEMEX.</p>
  </article>
  <article class="card">
    <h3>¿También instalan el cable o solo lo suministran?</h3>
    <p>Las dos opciones son posibles. VMS Energy es contratista EPC — si el proyecto lo requiere, integramos suministro, tendido, empalmes, terminaciones y pruebas bajo un solo contrato. Si solo necesitas suministro, también lo hacemos con la misma rigurosidad técnica.</p>
  </article>
</div>
```

---

### 5.2 `lp-cables-extra-alta-tension.html`

**Cambios requeridos:**

#### A. Agregar nota sobre fabricantes en el hero panel
Dentro del `<div class="hero__panel">` (o equivalente), agregar después del listado de construcciones populares:
```html
<p style="font-size:.85rem;color:rgba(255,255,255,.8);margin-top:12px;line-height:1.5">
  Fabricantes disponibles: KEI Wires &amp; Cables (stock México) · Südkabel (fabricación alemana, proyectos EHV de alta ingeniería)
</p>
```

#### B. Expandir Notas de Ingeniería (buscar `.notes-panel` o la sección de criterios técnicos)
Agregar las siguientes notas al panel existente o crear sección nueva antes del `</main>` y antes del footer:
```html
<section style="padding:36px 0">
  <div class="container">
    <div class="catalog__notes">
      <div class="notes-panel">
        <div class="notes-panel__head">
          <span class="notes-panel__tag">Notas de Ingeniería EHV</span>
          <h3 class="notes-panel__title">Criterios clave para proyectos de extra alta tensión (66–400 kV)</h3>
        </div>
        <p class="notes-panel__sub">Los proyectos EHV requieren más que un proveedor de cable. Requieren un integrador que coordine ingeniería de detalle, pruebas tipo, empalmes, terminaciones y puesta en servicio bajo un solo responsable.</p>
        <ul class="note-list">
          <li><strong>Pruebas tipo (type tests):</strong> Verificar que el fabricante cuente con pruebas IEC 60840 / IEC 62067 vigentes para la construcción específica. Solicitar informes de laboratorio, no solo declaraciones de cumplimiento.</li>
          <li><strong>Tiempos de fabricación:</strong> Cable EHV sobre pedido requiere entre 16 y 28 semanas de fabricación en fábrica. Este tiempo debe integrarse al cronograma EPC antes de comprometer cualquier fecha de puesta en energía.</li>
          <li><strong>Empalmes y terminaciones:</strong> Son parte crítica del sistema. VMS coordina el suministro de accesorios compatibles (empalmes premoldeados, terminaciones interiores/exteriores) y puede ejecutar la instalación con personal especializado.</li>
          <li><strong>Normas aplicables:</strong> IEC 60840 (66–150 kV), IEC 62067 (150–500 kV). Para interconexiones con CFE, revisar especificaciones técnicas LAPEM vigentes. Para proyectos con financiamiento internacional, verificar si el banco requiere IEEE o BS.</li>
          <li><strong>Logística internacional:</strong> Südkabel (Alemania) y KEI (India) requieren coordinación de importación, despacho aduanal y transporte especializado para bobinas de gran formato. VMS gestiona todo el proceso.</li>
        </ul>
        <div class="notes-badges" style="margin-top:12px">
          <span class="notes-badge">IEC 60840</span>
          <span class="notes-badge">IEC 62067</span>
          <span class="notes-badge">LAPEM/CFE</span>
          <span class="notes-badge">IEEE Std.</span>
          <span class="notes-badge">BS 7870</span>
        </div>
      </div>
    </div>
  </div>
</section>
```

#### C. Agregar sección FAQ (insertar antes de `</main>`)
```html
<section class="faq">
  <div class="container">
    <h2 class="catalog__title">Preguntas frecuentes — Extra alta tensión</h2>
    <div class="grid" style="grid-template-columns:1fr 1fr;gap:14px">
      <article class="card">
        <h3>¿Cuánto tiempo tarda en fabricarse un cable EHV?</h3>
        <p>Entre 16 y 28 semanas según el nivel de tensión, sección y fabricante. Este tiempo debe estar incluido en el cronograma EPC desde la etapa de ingeniería básica. VMS alerta sobre este plazo en el diagnóstico inicial.</p>
      </article>
      <article class="card">
        <h3>¿Qué fabricantes manejan para EHV?</h3>
        <p>KEI Wires &amp; Cables para la mayoría de proyectos. Südkabel (Alemania) para proyectos que requieren fabricación europea, norma VDE o estándares de alta ingeniería. La selección depende del nivel de tensión, norma del proyecto y cronograma.</p>
      </article>
      <article class="card">
        <h3>¿VMS también instala el cable EHV o solo lo suministra?</h3>
        <p>VMS Energy es contratista EPC. Podemos integrar suministro, tendido, empalmes, terminaciones y pruebas de alta tensión (hipot, descargas parciales) bajo un solo contrato. Esta integración elimina el riesgo de interfaces entre contratistas.</p>
      </article>
      <article class="card">
        <h3>¿Qué proyecto mínimo justifica gestión EHV con VMS?</h3>
        <p>No hay un tamaño mínimo. Hemos coordinado desde derivaciones de un solo circuito hasta líneas de transmisión completas. Lo que sí requerimos es que el proyecto cuente con especificación técnica o al menos condiciones de operación definidas para iniciar el diagnóstico.</p>
      </article>
    </div>
  </div>
</section>
```

---

### 5.3 `lp-cables-fotovoltaicos.html`

**Cambios requeridos:**

#### A. Expandir Notas de Ingeniería (reemplazar `<div class="notes-grid">` existente)
Agregar dos cards adicionales al `<div class="notes-grid">` existente:
```html
<div class="notes-card">
  <h4 class="notes-card__title">Temperatura y derating</h4>
  <p class="notes-card__text">En instalaciones sobre techo o en campo abierto, la temperatura real del cable puede superar 60 °C. Aplicar factores de corrección de ampacidad por temperatura ambiente real del sitio para evitar degradación prematura del aislamiento.</p>
</div>
<div class="notes-card">
  <h4 class="notes-card__title">Norma y certificación</h4>
  <p class="notes-card__text">El cable PV1-F KEI cumple BS EN 50618, 2Pfg 1169/08.2007 e IEC 60228 Clase 5. Para proyectos con CFE (interconexión), verificar que la especificación del parque incluya el estándar requerido por el dictamen de interconexión.</p>
</div>
```

También agregar a los `<div class="notes-badges">`:
```html
<span class="notes-badge">BS EN 50618</span>
<span class="notes-badge">TÜV Rheinland</span>
<span class="notes-badge">CFE Interconexión</span>
```

#### B. Expandir FAQ (reemplazar o complementar la sección FAQ existente)
```html
<section class="faq">
  <div class="container">
    <h2 class="catalog__title">Preguntas frecuentes — Cables fotovoltaicos</h2>
    <div class="grid" style="grid-template-columns:1fr 1fr;gap:14px">
      <article class="card">
        <h3>¿Qué sección de cable debo usar en mi parque solar?</h3>
        <p>Depende de la longitud del string, la corriente de cortocircuito del módulo (Isc) y los límites de caída de tensión del proyecto. Para strings estándar: 4–6 mm². Para strings largos o alta corriente: 10–16 mm². Para troncales DC: 25–50 mm². VMS hace el dimensionamiento si compartes el diseño eléctrico.</p>
      </article>
      <article class="card">
        <h3>¿El cable PV1-F sirve para instalación enterrada?</h3>
        <p>El PV1-F estándar no está diseñado para instalación directamente enterrada. Para tramos subterráneos en un parque solar, se requiere cable con cubierta adicional (doble aislamiento o tubería de protección). VMS puede especificar la solución correcta para cada tramo.</p>
      </article>
      <article class="card">
        <h3>¿Cuánto tiempo duran estos cables?</h3>
        <p>El cable PV1-F KEI tiene vida útil estimada de 30 años bajo condiciones de operación estándar, con resistencia a rayos UV, ozono y ciclos térmicos. Es compatible con la vida útil típica de un parque solar industrial.</p>
      </article>
      <article class="card">
        <h3>¿Pueden suministrar el cable junto con el EPC solar?</h3>
        <p>Sí. VMS Energy ejecuta proyectos EPC solar llave en mano. El suministro de cable fotovoltaico forma parte del alcance EPC: lo especificamos, lo procuramos y lo instalamos. No necesitas coordinar con un proveedor separado.</p>
      </article>
      <article class="card">
        <h3>¿Manejan cable de CA (AC) para la salida del inversor?</h3>
        <p>Sí. Además del cable DC fotovoltaico, suministramos cable de potencia MT para la interconexión del inversor/transformador elevador con la subestación de interconexión. Toda la infraestructura de cable del parque puede gestionarse con VMS.</p>
      </article>
      <article class="card">
        <h3>¿Qué norma requiere CFE para interconexión de parques solares?</h3>
        <p>CFE revisa el diseño eléctrico a través del dictamen de interconexión (CENACE/CFE). Los cables en el lado AC deben cumplir especificaciones LAPEM para el nivel de tensión de interconexión. VMS acompaña el proceso desde la ingeniería básica hasta la aprobación del dictamen.</p>
      </article>
    </div>
  </div>
</section>
```

---

### 5.4 `lp-cable-de-potencia-kei.html`

**Cambios requeridos:**

#### A. Actualizar título del catálogo
Cambiar texto de encabezado del catálogo (buscar "Catálogo de cable de potencia"):
```html
<h2 class="catalog__title">Catálogo de cable de potencia MT/AT</h2>
<p style="font-size:.9rem;color:var(--muted,#4E6782);margin:4px 0 0">Fabricante principal: KEI Wires &amp; Cables. Construcciones especiales disponibles con Südkabel para proyectos que requieren estándares europeos.</p>
```

#### B. Agregar tabla de selección XLPE vs EPR antes del catálogo (antes de `<section class="catalog">`)
```html
<section style="padding:36px 0;background:var(--soft,#f4f8ff)">
  <div class="container">
    <div class="notes-panel">
      <div class="notes-panel__head">
        <span class="notes-panel__tag">Guía de selección</span>
        <h3 class="notes-panel__title">¿XLPE o EPR? No es una pregunta de catálogo — es una pregunta de contexto.</h3>
      </div>
      <p class="notes-panel__sub">Ambos aislamientos operan a 90 °C en régimen normal y 250 °C en cortocircuito. La diferencia está en el ambiente y el tipo de aplicación.</p>
      <div style="overflow-x:auto;margin-top:16px">
        <table style="width:100%;border-collapse:collapse;font-size:.9rem;min-width:560px">
          <thead>
            <tr style="background:var(--cobalt,#0F4C81);color:#fff">
              <th style="padding:10px 12px;text-align:left;border-radius:8px 0 0 0">Criterio</th>
              <th style="padding:10px 12px;text-align:center">XLPE</th>
              <th style="padding:10px 12px;text-align:center;border-radius:0 8px 0 0">EPR</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid #dbe6f4">
              <td style="padding:9px 12px;font-weight:600">Rigidez dieléctrica</td>
              <td style="padding:9px 12px;text-align:center">⭐⭐⭐ Superior</td>
              <td style="padding:9px 12px;text-align:center">⭐⭐ Buena</td>
            </tr>
            <tr style="border-bottom:1px solid #dbe6f4;background:#f9fbff">
              <td style="padding:9px 12px;font-weight:600">Flexibilidad</td>
              <td style="padding:9px 12px;text-align:center">⭐ Menor</td>
              <td style="padding:9px 12px;text-align:center">⭐⭐⭐ Superior</td>
            </tr>
            <tr style="border-bottom:1px solid #dbe6f4">
              <td style="padding:9px 12px;font-weight:600">Equipos móviles (trailing)</td>
              <td style="padding:9px 12px;text-align:center">❌ No recomendado</td>
              <td style="padding:9px 12px;text-align:center">✅ Ideal</td>
            </tr>
            <tr style="border-bottom:1px solid #dbe6f4;background:#f9fbff">
              <td style="padding:9px 12px;font-weight:600">Ambientes húmedos</td>
              <td style="padding:9px 12px;text-align:center">✅ Bueno</td>
              <td style="padding:9px 12px;text-align:center">⭐⭐⭐ Mejor</td>
            </tr>
            <tr style="border-bottom:1px solid #dbe6f4">
              <td style="padding:9px 12px;font-weight:600">Subestaciones y líneas fijas</td>
              <td style="padding:9px 12px;text-align:center">✅ Ideal</td>
              <td style="padding:9px 12px;text-align:center">✅ Compatible</td>
            </tr>
            <tr style="background:#f9fbff">
              <td style="padding:9px 12px;font-weight:600">Costo relativo</td>
              <td style="padding:9px 12px;text-align:center">💰 Menor</td>
              <td style="padding:9px 12px;text-align:center">💰💰 Mayor</td>
            </tr>
          </tbody>
          <tfoot>
            <tr style="background:#e8f0fb">
              <td style="padding:10px 12px;font-weight:700;color:var(--cobalt,#0F4C81)">Recomendación VMS</td>
              <td style="padding:10px 12px;text-align:center;font-size:.85rem">Subestaciones, alimentadores principales, líneas de media tensión fijas</td>
              <td style="padding:10px 12px;text-align:center;font-size:.85rem">Minería (trailing cables), equipos en movimiento, ambientes con humedad severa</td>
            </tr>
          </tfoot>
        </table>
      </div>
    </div>
  </div>
</section>
```

#### C. Expandir FAQ (reemplazar las 2 existentes)
```html
<div class="grid" style="grid-template-columns:1fr 1fr;gap:14px">
  <article class="card">
    <h3>¿Qué información necesito para cotizar?</h3>
    <p>Voltaje de operación (U0/U en kV), longitud total por circuito, tipo de instalación (bandeja, ducto, enterrado), temperatura ambiente del sitio, norma requerida (IEC, NMX-J, CFE) y cronograma de entrega. Con estos datos damos respuesta técnica en 24–48 h hábiles.</p>
  </article>
  <article class="card">
    <h3>¿XLPE o EPR para mi proyecto?</h3>
    <p>Depende de la aplicación. XLPE es ideal para instalaciones fijas, subestaciones y alimentadores principales. EPR es superior en equipos móviles (trailing cables en minería), ambientes con alta humedad y aplicaciones que requieren mayor flexibilidad. Consulta la guía de selección en esta página o pídenos asesoría técnica.</p>
  </article>
  <article class="card">
    <h3>¿Manejan cable de fabricación nacional?</h3>
    <p>Sí. Condumex y Viakon (fabricación nacional bajo NMX-J) están disponibles para baja tensión y control cuando el proyecto requiere componente nacional, tiempos de entrega cortos o cumplimiento NOM-001-SEDE. Para media y alta tensión, KEI y Südkabel son los fabricantes de referencia.</p>
  </article>
  <article class="card">
    <h3>¿Pueden coordinar entregas por fases de obra?</h3>
    <p>Sí. La entrega por hitos de obra es nuestro estándar en proyectos EPC. Coordinamos cronograma de suministro, trazabilidad por bobina, documentación técnica por lote y verificación de longitudes antes de instalación.</p>
  </article>
  <article class="card">
    <h3>¿Qué documentación incluye el suministro?</h3>
    <p>Certificado de pruebas de fábrica (ensayos individuales y tipo), hoja de datos del cable, reporte de longitudes por bobina, etiquetado de trazabilidad y, si el proyecto lo requiere, documentación específica para CFE, PEMEX o auditorías ISO.</p>
  </article>
  <article class="card">
    <h3>¿VMS también instala o solo suministra?</h3>
    <p>Las dos opciones están disponibles. Como contratista EPC, integramos suministro, instalación, pruebas y commissioning bajo un solo contrato. Si el proyecto ya tiene contratista de instalación, podemos actuar solo como proveedor técnico con la misma rigurosidad.</p>
  </article>
</div>
```

---

### 5.5 `lp-cables-especiales.html` (cables ESP / Arteria)

**Cambios requeridos:**

#### A. Agregar sección de contexto EPC para Oil & Gas después del hero
Insertar después de `<section class="steps">`:
```html
<section style="padding:28px 0;background:var(--soft,#f4f8ff)">
  <div class="container">
    <div class="notes-panel">
      <div class="notes-panel__head">
        <span class="notes-panel__tag">Contexto de aplicación</span>
        <h3 class="notes-panel__title">Los cables ESP no se compran en catálogo. Se especifican para cada pozo.</h3>
      </div>
      <p class="notes-panel__sub">Cada instalación de bomba sumergible eléctrica (ESP) tiene condiciones únicas de temperatura, presión, geometría del pozo y perfil de producción. La selección incorrecta del cable es una de las causas más frecuentes de falla prematura en sistemas ESP.</p>
      <ul class="note-list">
        <li><strong>Temperatura del fluido:</strong> El perfil térmico del pozo determina la familia Arteria (180 °F, 205 °F, 290 °F, 400 °F o 450 °F). No usar temperatura superficial — usar temperatura de fondo de pozo (BHT).</li>
        <li><strong>Geometría del pozo:</strong> Pozos desviados o de radio corto requieren cable Round para mejor comportamiento mecánico. Pozos verticales y rectos permiten cable Flat con mayor eficiencia de espacio en el anular.</li>
        <li><strong>Ambiente corrosivo:</strong> Presencia de H₂S, CO₂ o fluidos con alta salinidad requiere construcciones con aislamiento EPDM o Kapton (familias 400 y 450). El aislamiento PP estándar (familia 180/205) no es adecuado para estos ambientes.</li>
        <li><strong>Coordinación con el sistema ESP:</strong> El cable debe ser compatible con la potencia del motor, el variador (VSD) y la longitud del pozo. VMS coordina la especificación con el fabricante del sistema ESP cuando el proyecto lo requiere.</li>
      </ul>
    </div>
  </div>
</section>
```

#### B. Expandir FAQ (agregar o reemplazar sección FAQ al final, antes del footer)
```html
<section class="faq">
  <div class="container">
    <h2 class="catalog__title">Preguntas frecuentes — Cables ESP</h2>
    <div class="grid" style="grid-template-columns:1fr 1fr;gap:14px">
      <article class="card">
        <h3>¿Cómo selecciono la familia Arteria correcta para mi pozo?</h3>
        <p>El criterio principal es la temperatura de fondo de pozo (BHT, Bottom Hole Temperature). Arteria 180 °F para condiciones normales, 205 °F para pozos más calientes, 290–450 °F para pozos de alta temperatura y ambientes corrosivos. VMS puede ayudarte a seleccionar si compartes el perfil de temperatura del pozo.</p>
      </article>
      <article class="card">
        <h3>¿Flat o Round para mi instalación?</h3>
        <p>Round es más flexible y recomendado para pozos desviados, de radio corto o con cambios de dirección. Flat ocupa menos espacio en el anular del pozo y puede ser más económico en pozos verticales con espacio suficiente. La decisión también depende del diámetro del casing.</p>
      </article>
      <article class="card">
        <h3>¿Manejan disponibilidad en campo o solo bajo pedido?</h3>
        <p>Algunos SKUs de familias 180 °F y 205 °F están disponibles en stock en México. Las familias de mayor temperatura (400 °F y 450 °F) son generalmente on-demand con tiempos de entrega de 8 a 16 semanas. Consulta disponibilidad al cotizar con SKU específico.</p>
      </article>
      <article class="card">
        <h3>¿El cable incluye protección contra H₂S?</h3>
        <p>Las familias Arteria 400 y 450 con aislamiento EPDM y cubierta de Kapton (Poliimida) ofrecen resistencia superior a H₂S y fluidos corrosivos. Para ambientes con alta concentración de H₂S, especificar la variante KEFLG o KEFLEG. Consulta a VMS con el análisis de fluido del pozo.</p>
      </article>
    </div>
  </div>
</section>
```

---

## 6. Casos de uso anónimos (agregar en todas las LPs)

Insertar esta sección antes de `</main>` en cada LP, ajustando el contenido según el tipo de cable.
Usar el siguiente patrón HTML:

```html
<section style="padding:36px 0;background:linear-gradient(135deg,#f0f6ff 0%,#e8f0fb 100%)">
  <div class="container">
    <h2 style="margin:0 0 6px;color:var(--cobalt,#0F4C81)">Proyectos donde este cable fue clave</h2>
    <p style="margin:0 0 20px;color:var(--muted,#4E6782)">Casos reales de suministro integrado al alcance EPC. Datos técnicos y logísticos — sin revelar información confidencial del cliente.</p>
    <div class="grid" style="grid-template-columns:1fr 1fr 1fr;gap:14px">

      <!-- Ajustar los 3 casos según el tipo de cable de cada LP -->

      <!-- PARA lp-cables-alta-tension.html -->
      <article class="card">
        <h3 style="font-size:1rem;margin:0 0 6px">Subestación MT en planta automotriz — Jalisco</h3>
        <p style="font-size:.9rem;color:var(--muted,#4E6782)">Suministro de 3.2 km de cable XLPE 6/10 kV con entrega en 2 fases alineada al cronograma de instalación EPC. Documentación completa para auditoría ISO del cliente.</p>
      </article>
      <article class="card">
        <h3 style="font-size:1rem;margin:0 0 6px">Ampliación de red 34.5 kV — sector minero</h3>
        <p style="font-size:.9rem;color:var(--muted,#4E6782)">Especificación y suministro de cable AT con armadura para instalación subterránea en terreno con alto contenido de sulfatos. Selección de cubierta HDPE para resistencia química.</p>
      </article>
      <article class="card">
        <h3 style="font-size:1rem;margin:0 0 6px">Interconexión de planta de cogeneración — Veracruz</h3>
        <p style="font-size:.9rem;color:var(--muted,#4E6782)">Suministro y tendido de cable 23 kV para interconexión con CFE. Documentación LAPEM incluida. Coordinación de empalmes y terminaciones como parte del alcance EPC.</p>
      </article>

    </div>
  </div>
</section>
```

**Casos para cada LP:**

- **`lp-cables-fotovoltaicos.html`:** Parque solar 8 MW Jalisco (1,200 carretes PV1-F, 2 fases de entrega) / Planta solar rooftop 1.2 MW planta industrial (dimensionamiento de calibres por string y troncal) / Ampliación de 3 MW en parque existente (suministro coordinado con inversor de nueva marca)
- **`lp-cable-de-potencia-kei.html`:** Subestación 13.8 kV industria alimentaria (XLPE, documentación FDA-friendly) / Centro de control motores planta cementera (cable XLPE 6 kV + control Helukabel) / Reemplazo de red BT planta automotriz (Condumex NMX-J, entrega en 5 etapas semanales)
- **`lp-cables-especiales.html`:** Reemplazo de cables ESP en batería de pozos — Tabasco (8 pozos, Arteria 290 °F Round, stock disponible 72 h) / Reparación de emergencia pozo offshore — Campeche (Arteria 400 °F Flat, coordinación urgente desde Ciudad del Carmen) / Nuevo proyecto ESP con variador (Arteria 450 °F KEFLG, especificación coordinada con fabricante del sistema)
- **`lp-cables-extra-alta-tension.html`:** Línea 115 kV — interconexión parque solar utility scale (KEI XLPE 64/110 kV, 4.2 km, logística internacional en 2 embarques) / Subestación 230 kV planta industrial — Monterrey (Südkabel, especificación con estándar europeo requerido por socio tecnológico alemán)

---

## 7. Glosario técnico (nuevo archivo recomendado)

**Crear:** `glosario-cable-electrico.html` como nueva página en la sección VMShop/Blog.

**Términos mínimos a incluir:**

| Término | Definición breve |
|---|---|
| XLPE | Polietileno reticulado. Aislamiento de alta rigidez dieléctrica para cables de potencia. |
| EPR | Polímero de etileno-propileno. Aislamiento flexible y con mejor desempeño en ambientes húmedos. |
| LSZH | Low Smoke Zero Halogen. Cubierta retardante a la llama que no emite gases tóxicos al arder. Obligatoria en espacios confinados, túneles y edificios públicos. |
| ESP | Electric Submersible Pump. Sistema de bombeo sumergible para extracción de petróleo. |
| EHV | Extra High Voltage. Cables de tensión mayor a 66 kV. |
| HV | High Voltage. Cables entre 36 y 66 kV. |
| MV | Medium Voltage. Cables entre 1 kV y 36 kV. |
| U0/U | Tensión de diseño fase-tierra / fase-fase del cable (en kV). |
| Ampacidad | Corriente máxima admisible del cable en condiciones de instalación específicas. |
| Clase 2 | Conductor trenzado flexible (conductor estándar en cables de potencia fijos). |
| Clase 5 | Conductor muy flexible (cables móviles, trailing cables, cables para equipos). |
| Trailing cable | Cable diseñado para soportar enrollado/desenrollado continuo. Uso en equipos móviles. |
| BHT | Bottom Hole Temperature. Temperatura de fondo de pozo. Criterio de selección de cables ESP. |
| LAPEM | Laboratorio de Pruebas de Equipos y Materiales de CFE. Emite especificaciones técnicas de referencia para proyectos con CFE. |
| NMX-J | Norma mexicana para cables y conductores eléctricos (Condumex/Viakon). |
| MTO | Material Take-Off. Lista de materiales cuantificada para un proyecto de ingeniería. |

---

## 8. Notas de implementación para Claude Code

1. **No modificar** el CSS global ni los archivos de estilos compartidos.
2. **No modificar** la lógica JavaScript de los catálogos (filtros, búsqueda, renderizado de cards).
3. **Respetar la codificación HTML** de caracteres especiales del español (á = `&aacute;`, é = `&eacute;`, etc.) o usar UTF-8 directamente — mantener consistencia con el archivo existente.
4. **Insertar los Bloques A y B** (multi-proveedor y EPC integrado) en el mismo orden y posición en todas las LPs para mantener consistencia de experiencia.
5. **El estilo de las tablas** debe ser inline (como se muestra en los ejemplos) para no afectar estilos globales.
6. **Verificar** que las secciones nuevas sean responsivas revisando en móvil (breakpoint 768px). Para el grid de 3 columnas de casos de uso, agregar media query o usar `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))`.
7. **Prioridad de implementación:** Bloques A y B (compartidos) → Expansión de FAQs → Notas de ingeniería → Tabla XLPE/EPR → Casos de uso → Glosario.
