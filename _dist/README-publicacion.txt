PAQUETE DE PUBLICACION — Blog "Mantenimiento de subestaciones AT, MT y BT"
Generado: 2026-04-27
Dominio destino: vmsenergy.com

CONTENIDO DEL ZIP
-----------------
/blog-mantenimiento-reparacion-subestaciones-at-mt-bt.html
    Articulo principal (~2,800 palabras, JSON-LD BlogPosting/Breadcrumb/FAQ).
    Reemplaza la version anterior en stub.

/checklist-anual-subestaciones-at-mt-bt.html
    Lead magnet imprimible vinculado desde el articulo (boton "Descargar checklist").
    noindex,follow — NO agregar al sitemap.

/blog-subestacion-electrica-industrial.html
    Editado: bloque "Lecturas relacionadas" con 3 cross-links activados.
    Republicar para conservar la red de enlaces internos.

/sitemap.xml
    lastmod actualizado a 2026-04-27 para los blogs afectados.
    Resubir a Google Search Console tras desplegar.

/assets/img/blog/mantenimiento-subestaciones/
    hero-mantenimiento-subestaciones.webp     (190 KB) — hero del articulo
    og-mantenimiento-subestaciones.webp       (190 KB) — preview Open Graph (idealmente 1200x630)
    tipos-mantenimiento-subestaciones.svg     (5.9 KB) — infografia tipos de mantenimiento
    pruebas-electricas-subestaciones.svg      (6.6 KB) — infografia pruebas electricas
    caso-cementera-jalisco-69kv.webp          (309 KB) — foto caso real
    prompts.md                                — prompts AI usados para generar las imagenes

/HANDOFF-blog-mantenimiento-subestaciones.md
    Documento completo de handoff con pendientes, validacion editorial,
    301 desde URL del WP, y metricas a monitorear.


DEPENDENCIAS QUE DEBEN EXISTIR YA EN PRODUCCION
------------------------------------------------
- /assets/brand/vms_logo_blue.png   (header)
- /assets/brand/vms_logo_white.png  (footer)
- /assets/img/Especialidades_servicios.png  (fallback hero — no se usa, pero esta en el CSS)
- contacto_cta.html  (form de captura, expande a 7 campos con ?producto=mantenimiento-subestaciones)
- especialidad_mantenimiento.html, soluciones_*.html, lp-*.html  (nav y footer)
- aviso-privacidad.html, codigo-conducta.html, politica-*.html, directorio.html, buzon-sugerencias.html
- index.html, nosotros.html, soluciones.html, procura.html, VMShop.html, carreras.html, contacto.html
- blog-importancia-tableros-distribucion.html, blog-caso-exito-embotelladora-colima-2022.html  (sidebar)


PASOS DE DESPLIEGUE
-------------------
1. Subir los HTML al root del dominio (mantener nombre exacto).
2. Subir la carpeta /assets/img/blog/mantenimiento-subestaciones/ respetando ruta.
3. Reemplazar sitemap.xml.
4. Configurar 301 desde la URL del WP:
     https://vmsenergy.com/mantenimiento-y-reparacion-de-subestaciones-electricas-at-mt-y-bt-en-mexico/
   hacia:
     https://vmsenergy.com/blog-mantenimiento-reparacion-subestaciones-at-mt-bt.html
5. Despublicar la entrada antigua del WordPress.
6. Resubir sitemap.xml en Google Search Console y solicitar indexacion del articulo.
7. Validar JSON-LD en https://search.google.com/test/rich-results
8. Probar el form en contacto_cta.html?producto=mantenimiento-subestaciones (debe expandir a 7 campos
   y etiquetar la lead como "mantenimiento-subestaciones" en CRM/email a comercial).
