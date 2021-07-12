"""Sphinx configuration."""
from datetime import datetime

import changelog_binder

project = "changelog-binder"
author = "Scality"
copyright = f"{datetime.now().year}, {author}"  # noqa: A001

version = changelog_binder.__version__
release = version

html_theme = "furo"

extensions = [
    "sphinx.ext.autodoc",
    "sphinxarg.ext",
]
