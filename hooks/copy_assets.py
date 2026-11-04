"""
MkDocs hook: copy root assets/ into docs/assets/ before each build.

This allows site assets (logo, favicons, custom CSS/JS) to live outside the
docs/ content directory while remaining available to mkdocs at build time.
The docs/assets/ directory is gitignored — it's a build artifact.
"""

import os
from pathlib import Path
import re
import shutil


def on_pre_build(config):
    """Copy root assets/ into docs/assets/ before building."""
    config_dir = os.path.dirname(config.config_file_path)
    src = os.path.join(config_dir, "assets")
    dst = os.path.join(config.docs_dir, "assets")

    if not os.path.isdir(src):
        return

    # Remove any stale copy
    if os.path.islink(dst):
        os.unlink(dst)
    elif os.path.isdir(dst):
        shutil.rmtree(dst)

    shutil.copytree(src, dst)


def on_serve(server, config, **kwargs):
    """Watch root assets/ for changes so live-reload picks them up."""
    config_dir = os.path.dirname(config.config_file_path)
    assets_dir = os.path.join(config_dir, "assets")
    if os.path.isdir(assets_dir):
        server.watch(assets_dir)


def on_page_content(html, page, config, **kwargs):
    """Inline homepage SVGs so manual theme changes reach their palette."""
    if page.file.src_uri != "index.md":
        return html

    def illustration(match):
        svg = (Path(config.docs_dir) / match[1]).read_text(encoding="utf-8")
        css_class = re.search(r'\bclass="([^"]+)"', match[0])
        classes = "nh-illustration" + (" " + css_class[1] if css_class else "")
        # Every occurrence needs its own accessible title, including reused art.
        title_id = f"nh-art-{match.start()}"
        svg = svg.replace('id="title"', f'id="{title_id}"')
        svg = svg.replace('aria-labelledby="title"', f'aria-labelledby="{title_id}"')
        return svg.replace("<svg ", f'<svg class="{classes}" ', 1)

    return re.sub(
        r'<img\b[^>]*\bsrc="(assets/mkdocs/images/notes/[a-z]+\.svg)"[^>]*>',
        illustration, html,
    )
