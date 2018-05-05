#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys

import os

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.
sys.path.append(os.curdir)

SITEURL = 'https://sivaa.in'
SITENAME = 'Sivasubramaniam Arunachalam'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""

TIMEZONE = 'Europe/Berlin'

STATIC_PATHS = [
    'images',
    'extra/CNAME',
    'extra/robots.txt',

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
    'extra/robots.txt': {'path': 'robots.txt'},

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
