"""
MkDocs hook: copy root assets/ into docs/assets/ before each build.

This allows site assets (logo, favicons, custom CSS/JS) to live outside the
docs/ content directory while remaining available to mkdocs at build time.
The docs/assets/ directory is gitignored — it's a build artifact.
"""

import os
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
