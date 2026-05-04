"""Bulk-propagate the new 'Confiabilidad Eléctrica (UPS/BESS)' entry to every
page that already lists 'Infraestructura Energética' in:
  - header submenu 'Soluciones EPC'
  - footer 'Servicios EPC' column

Idempotent: skips files where the link already exists.
"""
import glob
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TARGET_HREF = 'confiabilidad-electrica-industrial.html#inicio'

HEADER_BADGE = (
    '<li><a href="confiabilidad-electrica-industrial.html#inicio" '
    'style="background:#0f4c81;color:#fff;border-radius:999px;padding:.2rem .6rem;display:inline-block">'
    'Confiabilidad El&eacute;ctrica (UPS/BESS)</a></li>'
)

# Both `Energ&eacute;tica` (HTML entity) and `Energética` (raw UTF-8 é) are in
# use across the codebase, so accept both.
ENERG = r'Energ(?:&eacute;|é)tica'

HEADER_RE = re.compile(
    r'(?P<indent>[ \t]*)<li><a href="soluciones_infraestructura_energetica\.html#inicio">'
    r'Infraestructura ' + ENERG + r'</a></li>'
)

FOOTER_RE = re.compile(
    r'(?P<indent>[ \t]*)<li><a href="soluciones_infraestructura_energetica\.html#inicio" '
    r'style="color:#cbd5e1;text-decoration:none">Infraestructura ' + ENERG + r'</a></li>'
)

# Idempotency check: did we already add the header badge / footer entry?
HEADER_DONE_RE = re.compile(
    r'<li><a href="confiabilidad-electrica-industrial\.html#inicio" '
    r'style="background:#0f4c81;color:#fff;border-radius:999px'
)
FOOTER_DONE_RE = re.compile(
    r'<li><a href="confiabilidad-electrica-industrial\.html#inicio" '
    r'style="color:#cbd5e1;text-decoration:none">'
)


def patch(html: str) -> tuple[str, bool, bool]:
    header_added = False
    footer_added = False

    if not HEADER_DONE_RE.search(html):
        new_html, n = HEADER_RE.subn(
            lambda m: m.group(0) + '\n' + m.group('indent') + HEADER_BADGE,
            html, count=1)
        if n:
            html = new_html
            header_added = True

    if not FOOTER_DONE_RE.search(html):
        footer_li = (
            '<li><a href="confiabilidad-electrica-industrial.html#inicio" '
            'style="color:#cbd5e1;text-decoration:none">'
            'Confiabilidad El&eacute;ctrica (UPS/BESS)</a></li>'
        )
        new_html, n = FOOTER_RE.subn(
            lambda m: m.group(0) + '\n' + m.group('indent') + footer_li,
            html, count=1)
        if n:
            html = new_html
            footer_added = True

    return html, header_added, footer_added


def main():
    files = sorted(glob.glob(os.path.join(ROOT, '*.html')))
    files += sorted(glob.glob(os.path.join(ROOT, 'partials', '*.html')))
    summary = {'changed': [], 'skipped_already_done': [], 'no_anchor': []}
    for path in files:
        with open(path, encoding='utf-8') as fp:
            original = fp.read()
        if 'soluciones_infraestructura_energetica.html#inicio' not in original:
            summary['no_anchor'].append(os.path.basename(path))
            continue
        new_html, h, f = patch(original)
        if new_html != original:
            with open(path, 'w', encoding='utf-8') as fp:
                fp.write(new_html)
            summary['changed'].append((os.path.basename(path), h, f))
        else:
            summary['skipped_already_done'].append(os.path.basename(path))

    print(f"Files changed: {len(summary['changed'])}")
    for name, h, f in summary['changed']:
        marks = ('h' if h else '-') + ('f' if f else '-')
        print(f'  [{marks}] {name}')
    print(f"\nFiles already up-to-date: {len(summary['skipped_already_done'])}")
    for name in summary['skipped_already_done']:
        print(f'  -- {name}')
    print(f"\nFiles without anchor: {len(summary['no_anchor'])}")
    for name in summary['no_anchor']:
        print(f'  ?? {name}')


if __name__ == '__main__':
    main()
