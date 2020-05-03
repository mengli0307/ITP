#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Policygenius'
SITENAME = u'PolicyGenius_content'
SITEURL = 'https://mengli0307.github.io'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

STATIC_PATHS = ['images']

SITELOGO = 'logo.png'
FAVICON = 'logo.png'
SITELOGO_SIZE = 14

# SITE THEME
#THEME = "./themes/notmyidea-ah21"

# Markdown PLUGIN
#MARKDOWN = {
    #'extension_configs': {
        #'markdown.extensions.codehilite': {'css_class': 'highlight'},
        #'markdown.extensions.extra': {},
        #'markdown.extensions.meta': {},
        #'markdown.extensions.tables': {  # TABLE
        #}
        #'markdown.extensions.toc': {     # CATALOG，REFERENCES: https://python-markdown.github.io/extensions/toc/
        #    'title': 'TOC:',      # TITLE OF CATALOG
        #    'toc_depth': 3,
        #},
        #'output_format': 'html5',
    #},
#}

#SET THE MAXIMUM LENGTH OF SUMMARY
SUMMARY_MAX_LENGTH = 50

# TRACKED BY GOOGLE_ANALYTICS ACCOUNT
GOOGLE_ANALYTICS = 'UA-xxxxxxxxx-x'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Policygenius', 'https://www.policygenius.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/Policygenius'),
          ('Twitter', 'https://twitter.com/policygenius'),
          ('LinkedIn', 'https://www.linkedin.com/company/policygenius'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

