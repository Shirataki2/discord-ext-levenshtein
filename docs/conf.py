# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import re

# -- Project information -----------------------------------------------------

project = 'discord-ext-levenshtein'
copyright = '2021, Tomoya Ishii'
author = 'Tomoya Ishii'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinxcontrib_trio',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

autodoc_typehints = 'none'
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

highlight_language = 'python3'
master_doc = 'index'
pygment_style = 'friendly'
source_suffix = '.rst'

with open('../discord/ext/levenshtein/__init__.py') as f:
    VERSION_MATCH = re.search(
        r'VersionInfo\(major=(\d+)?,\s*?minor=(\d+)?,\s*?micro=(\d+)?, .*',
        f.read(),
        re.MULTILINE
    )
if not VERSION_MATCH:
    raise RuntimeError('VersionInfo not found')

release = version = '.'.join([VERSION_MATCH.group(i) for i in range(1, 4)])
