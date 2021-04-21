#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kate'
SITENAME = u'Teal Deer'
SITEURL = ''
SITE_DESCRIPTION = 'everything that\'s unfit to print'

DEFAULT_DATE = 'fs' 

PATH = 'content'

PLUGINS= None
# tipue doesn't work with pip install for plugins ;_;
#PLUGIN_PATHS = ["plugins"]
#PLUGINS = ['tipue_search']

SEARCH_ON = False

# these are required for tipue
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', '404']

TIMEZONE = 'America/Chicago'

#THEME_STATIC_DIR = 'theme'
THEME = 'themes/elegant' #
#THEME= 'pelican-themes/storm'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
        # ('Python.org', 'http://python.org/'),
        # ('Jinja2', 'http://jinja.pocoo.org/'),
        # ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL_PROFILE_LABEL = u'find me @'

SOCIAL = (
    ('Twitter', 'https://twitter.com/krp_mpls', 'Twitter'),
    ("Github", "https://github.com/klreeher/", 'Github'),
    ("RSS", SITEURL + "/feeds/all.atom.xml", 'RSS Feeds'),
)

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True

FORMATTED_FIELDS = ['summary']


LANDING_PAGE_TITLE = 'tl;dr'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
