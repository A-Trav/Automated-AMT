# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os, sys

print(sys.executable)
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../Src'))
sys.path.insert(0, os.path.abspath('../Src/Auth'))
sys.path.insert(0, os.path.abspath('../Src/Database'))
sys.path.insert(0, os.path.abspath('../Src/Handler'))
sys.path.insert(0, os.path.abspath('../Src/Model'))
sys.path.insert(0, os.path.abspath('../Src/Requests'))
sys.path.insert(0, os.path.abspath('../Src/ScheduledTask'))
sys.path.insert(0, os.path.abspath('../Src/Schema'))
sys.path.insert(0, os.path.abspath('../Src/Service'))
sys.path.insert(0, os.path.abspath('../Src/SMTP'))
sys.path.insert(0, os.path.abspath('../Src/Utils'))

project = 'Automated AMT'
copyright = '2023, Ashley Travaini'
author = 'Ashley Travaini'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = []
