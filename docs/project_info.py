# Project-specific configuration for Sphinx documentation.
# This file contains settings that vary per repository.
# The main conf.py imports these values and can be synced across all repos.

from urllib.parse import urlparse

# Project name (used for titles, headers, and Sphinx internals)
project = "IATI Standard Gazette"

# URL of the live tool this repo documents. Set this for repos that
# document a deployed tool (Validator, Datastore, Publisher, ...).
# Leave as None for repos where the docs themselves are the deliverable
# (legal terms, handbooks, the docs base itself).
#
# When set, the page header gets a two-item nav: a link to the tool, and
# a self-link labelled "<name>: Documentation". When unset, the header
# shows a single self-link labelled with the project name.
#
# Use the URL without "www." - the hostname is reused as the Plausible
# analytics domain (see plausible_domain below), so check it matches the
# site URL registered in Plausible.
tool_url = None

# Short label used in the nav. Defaults to ``project``. Override only
# when the project name is long and the nav needs a tighter label (e.g.
# project = "Country Development Finance Data", nav_label = "CDFD").
nav_label = None

# Eyebrow text: the smaller text that appears directly above the website title
eyebrow_text = "IATI Standard"

# GitHub repository URL (used by the theme for the "Source code at GitHub" footer link)
github_repository = "https://github.com/IATI/iati-standard-gazette"

# Plausible analytics domain, derived from tool_url so docs are tracked
# under the tool's site. Set to None to disable, or a string to override.
plausible_domain = urlparse(tool_url).hostname if tool_url else None

# Supported languages for the documentation
languages = ["en"]

redoc = []
