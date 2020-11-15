extensions = [
    ...,
    "myst_nb"
]

extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
]



# inside conf.py
latex_elements = {
    'preamble': r'''
\usepackage{cancel}
'''
}

latex_show_urls = 'footnote'

panels_css_variables = {
    "tabs-color-label-active": "hsla(231, 99%, 66%, 1)",
    "tabs-color-label-inactive": "rgba(178, 206, 245, 0.62)",
    "tabs-color-overline": "rgb(207, 236, 238)",
    "tabs-color-underline": "rgb(207, 236, 238)",
    "tabs-size-label": "1rem",
}


