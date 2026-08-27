# PUBLICAR/ — qué es esta carpeta

Esta carpeta contiene **exactamente** los archivos que el sitio necesita y nada más.
Sale de la carpeta de trabajo (1.7 GB) filtrando lo que ninguna página, hoja de
estilo o JSON referencia de verdad. Se regenera con `_f3/publicar_github.py`; lo que
deja de usarse se aparta solo a `_basura/publicar-obsoleto/`.

**No edites archivos aquí.** Se sobrescriben en cada regeneración. Los originales
viven un nivel arriba.

---

## A · Publicar en GitHub Pages

El contenido de esta carpeta **es** la raíz del sitio. Se sube tal cual:

```bash
cd PUBLICAR
git init
git add -A
git commit -m "Sitio VMS Energy"
git branch -M main
git remote add origin https://github.com/<usuario>/<repo>.git
git push -u origin main
```

Después, en el repositorio: **Settings → Pages → Source: Deploy from a branch →
`main` / `(root)`**.

Tres archivos ya vienen puestos y conviene no quitarlos:

| Archivo | Para qué |
|---|---|
| `.nojekyll` | Sin él, GitHub procesa el sitio con Jekyll, que **ignora toda carpeta que empiece con `_`**. |
| `robots.txt` | `Disallow: /`. El espejo de GitHub no debe competir en Google con vmsenergy.com. Los `<link rel=canonical>` ya apuntan al dominio real; esto es el segundo cinturón. |
| `.gitattributes` | Fija finales de línea y marca los binarios, para que git no corrompa imágenes ni PDFs. |

---

## B · Publicar en WordPress

WordPress no consume la carpeta entera. Necesita tres cosas, en este orden.

### B.1 · El núcleo, al tema hijo

En `_nucleo-wordpress/` están aislados los cuatro archivos del sistema de diseño:

| Archivo | Qué contiene |
|---|---|
| `tokens.css` | **Sólo variables.** Colores, escalas, sombras, radios. No declara ni un componente. |
| `vms-core.css` | Los componentes compartidos: botones, tarjetas, rejillas, pie, bandas de cierre, proyectos de referencia. |
| `vms-header.css` | El encabezado y sus menús. |
| `vms-header.js` | La lógica de los menús (desplegables y menú móvil). |

Se encolan desde el `functions.php` del tema hijo, **en este orden**, porque
`vms-core.css` consume las variables de `tokens.css`:

```php
add_action( 'wp_enqueue_scripts', function () {
    $u = get_stylesheet_directory_uri();
    $v = '2026.08';                       // sube esto al cambiar un archivo
    wp_enqueue_style ( 'vms-tokens', "$u/css/tokens.css",     [],              $v );
    wp_enqueue_style ( 'vms-core',   "$u/css/vms-core.css",   ['vms-tokens'],  $v );
    wp_enqueue_style ( 'vms-header', "$u/css/vms-header.css", ['vms-core'],    $v );
    wp_enqueue_script( 'vms-header', "$u/js/vms-header.js",   [],              $v, true );
}, 20 );
```

El `$v` importa: sin él, los navegadores y el caché de WordPress siguen sirviendo
la versión vieja después de cada cambio.

`header.html` y `footer.html` son el encabezado y el pie canónicos, para reproducirlos
en la plantilla del tema. Son **fragmentos**, no páginas: sus enlaces relativos
(`index.html`, `assets/brand/...`) sólo resuelven desde la raíz del sitio, así que
al abrirlos sueltos se ven sin logo y con los enlaces rotos. Es lo esperado.

### B.2 · Las imágenes, a la biblioteca de medios

Todo `assets/` sube a la biblioteca. **Conserva la estructura de subcarpetas**:
las rutas dentro del HTML son relativas (`assets/img/...`) y si cambian hay que
reescribirlas página por página.

Un archivo merece atención: `assets/img/badge-experiencia-vms-epc.webp`. El nombre
es deliberadamente neutro para que, cuando cambie la cifra de años, baste con
sobrescribir el archivo sin tocar las 17 referencias que lo apuntan.

### B.3 · El contenido, página por página

Cada `.html` de esta carpeta es una página completa. Para WordPress se toma **sólo
lo que va entre `<main>` y `</main>`**: el encabezado y el pie los pone la plantilla
del tema, no el contenido.

Si se pega en un bloque HTML de Elementor, conviene revisar dos cosas:

1. Que Elementor no reescriba las rutas relativas de `assets/`.
2. Que la página no traiga su propio `<style>`: algunas cargan hojas adicionales
   (`corporativo-base.css`, `sectorial-base.css`, `servicios-base.css`,
   `equipamiento-base.css`, `blog-articulo.css`). Esas van al tema hijo igual que
   el núcleo, encoladas **después** de `vms-core.css`.

---

## C · Lo que esta carpeta **no** lleva

Y por qué, para que nadie lo busque:

- Los respaldos `_respaldo_*` de la carpeta de trabajo.
- `vms_web_backup/`, `actual/`, `assets - copia/` — copias del sitio anterior.
- Las imágenes que ninguna página referencia (unos 400 MB de los 567 MB de `assets/`).
- Las páginas de trabajo interno: `tabla-decision-conceptos.html`,
  `mapa-calibrador.html`, `FRAGMENTO-rim-zacatecas.html`, `especialidad_servicio.html`.
- Cuatro borradores de blog que no usan el núcleo y que nadie enlaza.

---

## D · Verificación antes de publicar

```bash
# ninguna referencia local rota
python3 - <<'EOF'
import os, re, glob, urllib.parse
pat = re.compile(r'(?:src|href)="([^"#?][^"]*?)"')
rotos = {}
for f in glob.glob('**/*.html', recursive=True):
    if f.startswith('_nucleo-wordpress'):   # fragmentos, no paginas servidas
        continue
    base = os.path.dirname(f)
    for m in pat.finditer(open(f, encoding='utf-8', errors='replace').read()):
        u = m.group(1)
        if re.match(r'^(https?:|mailto:|tel:|data:|javascript:|//|#)', u): continue
        p = urllib.parse.unquote(u.split('#')[0].split('?')[0])
        if p and not os.path.exists(os.path.normpath(os.path.join(base, p))):
            rotos.setdefault(p, []).append(f)
print('referencias locales rotas:', len(rotos))
for d, fs in sorted(rotos.items())[:20]:
    print(' ', d, '<-', fs[0])
EOF
```

Las rutas que empiezan con `' +` son plantillas de JavaScript, no referencias:
se pueden ignorar.
