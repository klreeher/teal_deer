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
#DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives']

TIMEZONE = 'America/Chicago'

#THEME_STATIC_DIR = 'theme'
THEME = 'themes/mcss/pelican-theme' #
#THEME= 'pelican-themes/storm'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['index']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
               '/static/m-dark.css']
M_THEME_COLOR = '#22272e'

PLUGIN_PATHS = ['themes/mcss/plugins']
PLUGINS = ['m.htmlsanity']


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

FORMATTED_FIELDS = ['summary','landing', 'header', 'footer']


LANDING_PAGE_TITLE = 'tl;dr'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

M_SITE_LOGO_TEXT = 'Your Brand'

M_LINKS_NAVBAR1 = [('Features', 'features/', 'features', []),
                   ('Showcase', 'showcase/', 'showcase', []),
                   ('Download', 'download/', 'download', [])]

M_LINKS_NAVBAR2 = [('Blog', 'blog/', '[blog]', [
                        ('News', 'blog/news/', ''),
                        ('Archive', 'blog/archive/', '')]),
                   ('Contact', 'contact/', 'contact', [])]

M_LINKS_FOOTER1 = [('Your Brand', '/'),
                   ('Features', 'features/'),
                   ('Showcase', 'showcase/')]

M_LINKS_FOOTER2 = [('Download', 'download/'),
                   ('Packages', 'download/packages/'),
                   ('Source', 'download/source/')]

M_LINKS_FOOTER3 = [('Contact', ''),
                   ('E-mail', 'mailto:you@your.brand'),
                   ('GitHub', 'https://github.com/your-brand')]

M_FINE_PRINT = """
Your Brand. Copyright © `You <mailto:you@your.brand>`_, 2017. All rights
reserved.
"""