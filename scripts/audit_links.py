"""Audit internal href targets and image src across all root .html files.

Reports:
  - broken local href targets (href="page.html..." where page does not exist)
  - broken local image references (src="assets/..." not on disk)
Skips: external (http(s)://), mailto:, tel:, anchors-only (#...), javascript:.
"""
import glob
import os
import re
from collections import defaultdict
from urllib.parse import unquote

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

HREF_RE = re.compile(r'(?:href|src)\s*=\s*"([^"]+)"', re.I)
SKIP_SCHEMES = ('http://', 'https://', 'mailto:', 'tel:', 'javascript:', 'data:')
# Ignore values that are clearly JS-template runtime concatenations
# (e.g.  '" + item.link + "'  appearing inside ' + foo + ').
JS_TEMPLATE_RE = re.compile(r"'\s*\+|\+\s*'|^[\s+]|\$\{")


def existing_files(root: str) -> set[str]:
    out = set()
    for dirpath, _dirnames, filenames in os.walk(root):
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root).replace('\\', '/')
            out.add(rel)
            out.add(rel.lower())
    return out


def audit():
    existing = existing_files(ROOT)
    broken_href = defaultdict(list)
    broken_src = defaultdict(list)
    confiab_refs = []

    pages = sorted(glob.glob(os.path.join(ROOT, '*.html')))
    for path in pages:
        rel_page = os.path.relpath(path, ROOT).replace('\\', '/')
        with open(path, encoding='utf-8') as fp:
            html = fp.read()

        for raw in HREF_RE.findall(html):
            href = raw.strip()
            if not href or href.startswith('#'):
                continue
            if any(href.startswith(s) for s in SKIP_SCHEMES):
                continue
            if JS_TEMPLATE_RE.search(href):
                continue
            target = unquote(href.split('#')[0].split('?')[0])
            if not target:
                continue
            target_norm = target.lstrip('./').replace('\\', '/')
            if target_norm in existing or target_norm.lower() in existing:
                pass
            else:
                # classify
                if re.search(r'\.(png|jpe?g|webp|svg|gif|ico)$', target_norm, re.I):
                    broken_src[rel_page].append(target_norm)
                else:
                    broken_href[rel_page].append(target_norm)

            if 'confiabilidad-electrica-industrial' in target_norm:
                confiab_refs.append((rel_page, target_norm))

    print('=' * 70)
    print('BROKEN HREF (links to pages/files that do NOT exist on disk)')
    print('=' * 70)
    if not broken_href:
        print('  (none)')
    else:
        # group: target -> list of pages
        by_target = defaultdict(set)
        for page, targets in broken_href.items():
            for t in targets:
                by_target[t].add(page)
        for t in sorted(by_target):
            pages_with = sorted(by_target[t])
            sample = ', '.join(pages_with[:3])
            extra = f' (+{len(pages_with)-3} more)' if len(pages_with) > 3 else ''
            print(f'  MISSING TARGET: {t}')
            print(f'    referenced by: {sample}{extra}')

    print()
    print('=' * 70)
    print('BROKEN IMAGE SRC (local image refs not on disk)')
    print('=' * 70)
    if not broken_src:
        print('  (none)')
    else:
        by_target = defaultdict(set)
        for page, targets in broken_src.items():
            for t in targets:
                by_target[t].add(page)
        for t in sorted(by_target):
            pages_with = sorted(by_target[t])
            sample = ', '.join(pages_with[:3])
            extra = f' (+{len(pages_with)-3} more)' if len(pages_with) > 3 else ''
            print(f'  MISSING ASSET: {t}')
            print(f'    referenced by: {sample}{extra}')

    print()
    print('=' * 70)
    print(f"REFERENCES TO 'confiabilidad-electrica-industrial' across all pages: {len(confiab_refs)}")
    print('=' * 70)
    by_page = defaultdict(int)
    for page, _ in confiab_refs:
        by_page[page] += 1
    for page, n in sorted(by_page.items()):
        print(f'  {page}: {n}')


if __name__ == '__main__':
    audit()
