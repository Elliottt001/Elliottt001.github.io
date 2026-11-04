"""Count rendered content; never insert statistics into Markdown or code."""

import re
from html.parser import HTMLParser

from mkdocs.plugins import event_priority


class Statistics(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.code = None
        self.code_lines = 0
        self.images = 0

    def handle_starttag(self, tag, attrs):
        if tag == "pre":
            self.code = []
        elif tag == "img":
            self.images += 1

    def handle_data(self, data):
        if self.code is not None:
            self.code.append(data)
        else:
            self.text.append(data)

    def handle_endtag(self, tag):
        if tag == "pre" and self.code is not None:
            self.code_lines += len("".join(self.code).rstrip("\n").splitlines())
            self.code = None


@event_priority(50)
def on_page_content(html, page, config, **kwargs):
    if not page.markdown.strip():
        page.meta.setdefault("description", config.site_description)
    if (page.file.src_uri == "index.md" or page.meta.get("nostatistics")
            or "statistics" in page.meta.get("hide", [])):
        return html
    counts = Statistics()
    # Formula source is neither prose nor executable code.
    counts.feed(re.sub(r'<(span|div) class="arithmatex">.*?</\1>', "", html, flags=re.S))
    text = " ".join(counts.text)
    words = len(re.findall(r"[\u4e00-\u9fff]|[A-Za-z0-9]+", text))
    statistics = config.theme.get_env().get_template("partials/statistics.html").render(
        words=words,
        code_lines=counts.code_lines,
        images=counts.images,
        read_time=round(words / 300 + counts.code_lines / 80),
    )
    # At this stage h1 is an actual HTML heading, not a comment in a code fence.
    heading = re.search(r"<h1\b[^>]*>.*?</h1>", html, re.S)
    if heading:
        return html[:heading.end()] + statistics + html[heading.end():]
    page.meta["page_statistics"] = statistics
    return html
