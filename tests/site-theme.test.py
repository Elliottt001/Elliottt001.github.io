"""Run after mkdocs build: python3 tests/site-theme.test.py."""
from html.parser import HTMLParser
from pathlib import Path


class Styles(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.links.append(attrs.get('href', ''))


root = Path(__file__).resolve().parents[1]
site = root / 'site'
assert (site / 'index.html').exists(), 'Build the site first'
pages = list(site.rglob('*.html'))
for page in pages:
    parser = Styles()
    parser.feed(page.read_text())
    theme = [href for href in parser.links if href.endswith('assets/mkdocs/css/custom.css')]
    assert theme, f'{page.relative_to(site)} does not load the shared theme'
    target = site / theme[0].lstrip('/') if theme[0].startswith('/') else page.parent / theme[0]
    assert target.resolve().is_file(), f'{page}: broken theme URL'
    assert not any('lxgw-wenkai' in href for href in parser.links), f'{page}: remote font dependency'

for subject in ['AI', 'CS', 'MATH', 'FINANCE', 'ROBOTICS', 'PROJECT', 'INTERN', 'WORK', 'BOOK']:
    content = (root / 'docs' / subject / 'index.md').read_text()
    assert 'class="ns-cover"' in content, f'{subject}: missing shared cover'
    assert 'style=' not in content, f'{subject}: conflicting inline styles'

print(f'Shared theme and local stylesheet URLs verified on all {len(pages)} HTML pages.')
