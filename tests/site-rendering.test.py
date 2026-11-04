"""Regression checks for rendered notes: python tests/site-rendering.test.py [site] [build.log]."""

import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, Comment

ROOT = Path(__file__).resolve().parents[1]
SITE = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "site"
errors = []
pages = 0
for path in sorted(SITE.rglob("*.html")):
    soup = BeautifulSoup(path.read_text(), "html.parser")
    article = soup.select_one("article.md-content__inner")
    if article is None:
        continue
    pages += 1
    if path.relative_to(SITE).as_posix() not in ("index.html", "404.html"):
        if len(article.select(".ns-statistics")) != 1:
            errors.append(f"{path}: missing or duplicate statistics")
    for code in article.select("pre code"):
        if path.relative_to(SITE).as_posix().startswith("MATH/") and re.search(r"\\(?:frac|begin|sum|int|mathbf)\b", code.get_text()):
            errors.append(f"{path}: mathematical prose was rendered as a code block")
        if "ns-statistics" in code.get_text() or "margin-top: -30px" in code.get_text():
            errors.append(f"{path}: statistics contaminated a code example")
    for frame in article.select("iframe[src], audio[src], video[src], source[src]"):
        if frame["src"].startswith("http:"):
            errors.append(f"{path}: insecure embedded resource {frame['src']}")
    # Syntax lessons intentionally show raw source; prose in normal notes must not.
    for code in article.select("pre, code, .arithmatex"):
        code.decompose()
    if not path.relative_to(SITE).as_posix().startswith("CS/tools/markdown-"):
        for node in article.find_all(string=True):
            if isinstance(node, Comment):
                continue
            if re.search(r"!\[\[|\[\[(?:Python|Summary Of Calculus|Knowledge Frame)|"
                         r"\\(?:frac|begin|sum|int|mathbf|left|right)\b", node):
                errors.append(f"{path}: unparsed note syntax: {node[:100]}")

footnotes = BeautifulSoup((SITE / "CS/tools/markdown-advanced/index.html").read_text(), "html.parser")
assert footnotes.select_one("#fn\\:1") and footnotes.select_one("a.footnote-ref"), "Footnotes must link to their text"

if len(sys.argv) > 2:
    warnings = [line for line in Path(sys.argv[2]).read_text().splitlines() if line.startswith("WARNING")]
    allowed = {
        "A reference to 'none.md' is included in the 'nav' configuration, which is not found in the documentation files.",
        "A reference to '1.md' is included in the 'nav' configuration, which is not found in the documentation files.",
    }
    errors.extend(line for line in warnings if line.split(" -  ", 1)[-1] not in allowed)

assert not errors, "\n".join(errors)
print(f"Rendering regressions passed on {pages} pages; code, formulas, footnotes and embeds passed.")
