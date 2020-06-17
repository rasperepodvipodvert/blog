#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = 'ifilatov'
SITENAME = 'blog.filatovz.ru'
SITEURL = 'https://rasperepodvipodvert.github.io/pub_blog/'
USE_FOLDER_AS_CATEGORY = True

PATH = 'content'

TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = 'ru'
ARCHIVES_TEXT = u'Архив'
ARTICLESCATEGORY_TEXT = u'Статьи в категории'
ARTICLESTAG_TEXT = u'Статьи с тегом'
AUTHOR_TEXT = u'Автор'
AUTHORS_TEXT = u'Авторы'
CATEGORIES_TEXT = u'Категории'
CATEGORY_TEXT = u'Категория'
TAGS_TEXT = u'Теги'
COMMENTS_TEXT = u'Комментарии'
CONTENT_TEXT = u'Содержимое'
FIRST_TEXT = u'первая'
LAST_TEXT = u'последняя'
READMORE_TEXT = u'далее...'
LINKS_TEXT = u'Ссылки'
SOCIALLINKS_TEXT = u'Социал'

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('home', '/'),
    ('best', '/tag/best/')
)
HIDE_CATEGORIES_FROM_MENU = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('<i class="fa-li fa fa-vk"></i> ВКонтакте', 'https://vk.com/filatovzru'),
          ('<i class="fa-li fa fa-twitter"></i> Twitter', 'https://twitter.com/ia_filatov'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'neighbors', 'related_posts', 'assets', 'tipue_search']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

# отображение тегов
DISPLAY_TAGS_ON_SIDEBAR = True
# показывать в облаке или списком
DISPLAY_TAGS_INLINE = False

THEME = "themes"
DISPLAY_PAGES_ON_MENU = True

# url and path settings
RELATIVE_URLS = True
CACHE_CONTENT = False
STATIC_PATHS = ['icons', 'media', 'extra', 'emojify', 'stuff','robots.txt', 'CNAME' ]
EXTRA_PATH_METADATA = {
    'robots.txt': {'path': 'robots.txt'},
    'CNAME': {'path': 'CNAME'},
}
# article
ARTICLE_URL = u'articles/{category}/{slug}/'
ARTICLE_SAVE_AS = u'articles/{category}/{slug}/index.html'
# page
PAGE_URL = u'{slug}/'
PAGE_SAVE_AS = u'{slug}/index.html'
# author
AUTHOR_URL = u'author/{slug}/'
AUTHOR_SAVE_AS = u'author/{slug}/index.html'
# authors
AUTHORS_URL = u'authors/'
AUTHORS_SAVE_AS = u'authors/index.html'
# category
CATEGORY_URL = u'category/{slug}'
CATEGORY_SAVE_AS = u'category/{slug}.html'
# tag
TAG_URL = u'tag/{slug}/'
TAG_SAVE_AS = u'tag/{slug}/index.html'
TAG_CLOUD_STEPS = True

CURRENT_YEAR = datetime.date.today().year
