#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
import os as _os
import yaml
_HERE = _os.path.dirname(_os.path.abspath(__file__))

AUTHOR = 'JAWS-UG 長崎'
SITENAME = 'JAWS-UG 長崎'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

# 今日の日付
today = date.today()

DEFAULT_LANG = 'ja'

# Feed生成
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Markdown拡張
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
}

# ページ設定
PAGE_URLS = {
    'about': 'about.html',
    'join': 'join.html',
}

# ナビゲーションメニュー
MENUITEMS = [
    ('ホーム', '/'),
    ('JAWS-UGとは', '/about.html'),
    ('参加方法', '/join.html'),
    ('行動規範', '/code-of-conduct.html'),
    ('メンバー', '/members.html'),
    ('イベント一覧', '/events.html'),
]

# テーマ設定
THEME = 'simple'

# テンプレートディレクトリ（カスタムテーマでsimpleをオーバーライド）
THEME_TEMPLATES_OVERRIDES = [_os.path.join(_HERE, 'theme', 'templates')]

# 直接生成するテンプレート
DIRECT_TEMPLATES = ['index', 'events']

# 静的ファイル
STATIC_PATHS = ['images', 'static']

# 静的ファイルのパス設定
EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'},
    'static/custom.css': {'path': 'custom.css'},
}

# カスタムCSS
STYLESHEET_URL = '/custom.css'

# 追加のヘッダー（faviconの読み込み）
EXTRA_HEAD = """
<link rel="icon" type="image/x-icon" href="/favicon.ico">
"""

# Favicon
FAVICON = 'favicon.ico'

# 日付フォーマット
DEFAULT_DATE = (2026, 4, 1)
DATE_FORMATS = {
    'ja': '%Y年%m月%d日',
}

# イベントカテゴリ設定
DEFAULT_CATEGORY = 'events'
CATEGORY_URL = 'events/{slug}.html'
CATEGORY_SAVE_AS = 'events/{slug}.html'

# 記事URL設定
ARTICLE_URL = 'events/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'events/{date:%Y}/{date:%m}/{slug}.html'

# ページURL設定
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# テンプレートファイルを無視
IGNORE_FILES = ['_template.md']

# メンバーYAMLファイルを読み込み
def load_members():
    members_file = _os.path.join(_HERE, 'content', 'members.yaml')
    if _os.path.exists(members_file):
        with open(members_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return {'members': []}

JINJA_GLOBALS = {
    'site_members': load_members()['members']
}
