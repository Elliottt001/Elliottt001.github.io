"""Run after building: python3 tests/site-content.test.py /path/to/built/site."""
import hashlib
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
SITE = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / 'site'
assert (SITE / 'index.html').is_file(), 'Build the site first'


class Page(HTMLParser):
    def __init__(self, article_only=True):
        super().__init__()
        self.article_only = article_only
        self.in_article = False
        self.ids = set()
        self.references = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'article':
            self.in_article = True
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if self.in_article or not self.article_only:
            for name in ('href', 'src'):
                if name in attrs:
                    self.references.append(attrs[name])

    def handle_endtag(self, tag):
        if tag == 'article':
            self.in_article = False


# Use inventories rather than exists(): macOS can accept incorrectly cased URLs.
files = {p.resolve() for p in SITE.rglob('*') if p.is_file()}
pages = {}
for path in sorted(p for p in files if p.suffix == '.html'):
    page = Page()
    page.feed(path.read_text())
    pages[path] = page

errors = []
count = 0
for path, page in pages.items():
    for ref in page.references:
        parts = urlsplit(ref)
        if parts.scheme or parts.netloc:
            if parts.hostname != 'note.elliotttzhang.cn':
                continue
            target = SITE / unquote(parts.path).lstrip('/')
        else:
            target = (SITE / unquote(parts.path).lstrip('/') if parts.path.startswith('/')
                      else path.parent / unquote(parts.path))
        target = target.resolve()
        if not parts.path:
            target = path
        elif target not in files and target / 'index.html' in files:
            target /= 'index.html'
        count += 1
        if target not in files:
            errors.append(f'{path.relative_to(SITE)}: missing {ref}')
        elif parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:
            errors.append(f'{path.relative_to(SITE)}: missing anchor {ref}')
assert not errors, '\n'.join(sorted(set(errors)))

assert not (ROOT / 'auto_nav.py').exists()
assert not list(DOCS.rglob('dir-of-res.py'))
assert not (DOCS / 'CS/ctf/youku.md').exists()
assert not (DOCS / 'CS/ctf/lab0.html').exists()
assert (ROOT / 'archive/requests/youku.md').is_file()
export = ROOT / 'archive/exports/lab0.html'
page = Page(article_only=False)
page.feed(export.read_text())
for ref in page.references:
    parts = urlsplit(ref)
    if parts.scheme or parts.netloc or not parts.path:
        continue
    assert (export.parent / unquote(parts.path)).resolve().is_file(), ref

seen = {}
for path in DOCS.rglob('*'):
    if (not path.is_file() or path.suffix.lower() not in ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg')
            or path.relative_to(DOCS).parts[0] in ('CS', 'assets')):
        continue
    digest = hashlib.sha256(path.read_bytes()).digest()
    assert digest not in seen, (seen.get(digest), path)
    seen[digest] = path

assert not list(SITE.rglob('youku/index.html'))
assert not (SITE / 'CS/ctf/lab0.html').exists()
print(f'{len(pages)} generated pages and {count} internal references passed; archives and image duplicates passed.')
