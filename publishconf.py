#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# 本番環境用設定
# 環境変数 SITEURL が設定されている場合はそれを使用し、
# 設定されていない場合はデフォルト値を使用
SITEURL = os.environ.get('SITEURL', 'https://jaws-ug-nagasaki.github.io/website')
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# SEO対策
GOOGLE_ANALYTICS = ''  # 必要に応じて追加

# Sitemapプラグイン設定（本番環境用）
PLUGINS = ['sitemap']
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
