#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = 'Sivasubramaniam Arunachalam'
SITENAME = 'Sivasubramaniam Arunachalam'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


STATIC_PATHS = [
    'images',
    'extra/CNAME',

    'images/favicon/favicon.ico',
    'images/favicon/android-chrome-144x144.png',
    'images/favicon/apple-touch-icon.png',
    'images/favicon/browserconfig.xml',
    'images/favicon/favicon-16x16.png',
    'images/favicon/favicon-32x32.png',
    'images/favicon/mstile-150x150.png',
    'images/favicon/safari-pinned-tab.svg',
    'images/favicon/site.webmanifest',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},

    'images/favicon/favicon.ico': {'path': 'favicon.ico'},
    'images/favicon/android-chrome-144x144.png': {'path': 'android-chrome-144x144.png'},
    'images/favicon/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'images/favicon/browserconfig.xml': {'path': 'browserconfig.xml'},
    'images/favicon/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'images/favicon/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'images/favicon/mstile-150x150.png': {'path': 'mstile-150x150.png'},
    'images/favicon/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},
    'images/favicon/site.webmanifest': {'path': 'site.webmanifest'},
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.join(BASE_DIR, 'theme')
