# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

import sphinx.application
from sphinx.locale import get_translation

import iati_sphinx_theme

MESSAGE_CATALOG_NAME = "iati-sphinx-theme"
_ = get_translation(MESSAGE_CATALOG_NAME)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# These are kept for compatibility but shouldn't appear anywhere on the final website.

project = "IATI Standard Gazette"
author = "IATI Secretariat"
language = "en"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinxcontrib.video",
    "sphinxcontrib.youtube",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "iati_sphinx_theme"
html_theme_options = {  # See https://iati-sphinx-theme.readthedocs-hosted.com/en/latest/#configuration for additional options and info
    "github_repository": "https://github.com/IATI/sphinx-theme",
    "header_title_text": _("IATI Standard Gazette"),
    "header_eyebrow_text": _("IATI Standard"),
    "languages": ["en"],
    "project_title": _("IATI Standard Gazette"),
    "show_download_links": True,
}

# Add any paths that contain custom static files (such as style sheets, videos,
# images) here, relative to this directory. They are copied after the builtin
# static files, so a file named "default.css" will overwrite the builtin
# "default.css".
html_static_path = ["_static"]

todo_include_todos = True

# -- Options for Texinfo output -------------------------------------------

locale_dirs = [
    "locale",
    os.path.join(os.path.dirname(iati_sphinx_theme.__file__), "locale"),
]


def setup(app: sphinx.application.Sphinx) -> None:
    locale_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "locale")
    app.add_message_catalog(MESSAGE_CATALOG_NAME, locale_path)
