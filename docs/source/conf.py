"""\
NASA Open Science at NLU Configuration
======================================

Author: Akshay Mestry <xa@mes3.dev>
Created on: 22 April, 2026
Last updated on: 29 April, 2026

This file contains the configuration settings for building NLU's NASA
Open Science 2026 website using Sphinx, a popular Python documentation
tool.
"""

from __future__ import annotations

import typing as t
from datetime import datetime as dt

from markupsafe import Markup

from kaamiki import version as theme_version

if t.TYPE_CHECKING:
    from collections.abc import Sequence

project: t.Final[str] = "Open Science 2026 at NLU"
author: t.Final[str] = "National Louis University"
project_copyright: str = f"© {dt.now().year} {author}."
source: t.Final[str] = "https://github.com/xames3/nlu-oss"
email: t.Final[str] = "tholden1@nl.edu"
version: str = theme_version

extensions: list[str] = []

exclude_patterns: Sequence[str] = ["_build"]
smartquotes: bool = False

html_theme: t.Final[str] = "kaamiki"
html_title: str = ""
html_baseurl: t.Final[str] = "https://nasa.csisnlu.com/"
html_context: dict[str, t.Any] = {
    "add_copy_to_headerlinks": True,
    "fa_icons": {
        "dark_mode": "fa-solid fa-moon-star",
        "light_mode": "fa-solid fa-sun-bright",
    },
    "favicons": {
        "manifest": "favicons/site.webmanifest",
        "size_16": "favicons/favicon-16x16.png",
        "size_32": "favicons/favicon-32x32.png",
        "size_180": "favicons/apple-touch-icon.png",
    },
    "header_buttons": {},
    "logo_url": "https://nl.edu/media/nledu/site-assets/images/logo.svg",
    "open_links_in_new_tab": True,
    "project": {
        "author": author,
        "source": source,
        "email": email,
    },
    "secondary_toctree_title": "On this page",
    "show_breadcrumbs": False,
    "show_feedback": True,
    "show_last_updated_on": True,
    "show_previous_next_pages": False,
    "show_scrolltop": False,
    "show_searchbox": False,
    "show_sphinx": True,
    "show_toctree": True,
    "sidebar_buttons": {},
}
html_favicon: t.Final[str] = "_static/favicons/favicon.ico"
html_static_path: list[str] = ["_static"]
html_permalinks_icon: t.Final[str] = ""
html_use_index = True
html_search = True
templates_path: list[str] = ["_templates"]


def setup(app):
    app.add_css_file("override.css")


ogp_site_name: str = project
ogp_site_url: t.Final[str] = html_baseurl
ogp_social_cards: dict[str, str | bool] = {
    "site_url": html_baseurl,
    "enable": True,
}
ogp_type: t.Final[str] = "website"
ogp_enable_meta_description: bool = True
