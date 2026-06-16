#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
import os as _os
import yaml
import base64
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

# Author, Tags, Categoriesページを無効化
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
TAG_URL = ''
TAG_SAVE_AS = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''

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
STATIC_EXCLUDES = ['googled0690c3ab706fd43.html']

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

# 記事URL設定
ARTICLE_URL = 'events/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'events/{date:%Y}/{date:%m}/{slug}.html'

# ページURL設定
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# テンプレートファイルを無視
IGNORE_FILES = ['_template.md', 'googled0690c3ab706fd43.html']

# Sitemapプラグイン設定
PLUGINS = ['sitemap', 'tailwindcss']

# Tailwind CSS設定
TAILWIND = {
    "version": "3.0.24",
}
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
    },
    'exclude': [
        '/tag/.*',
        '/category/.*',
        '/author/.*',
        '/archive/.*',
        '/events/events.html',
        '/members.html'
    ]
}

# メンバーYAMLファイルを読み込み
def load_members():
    members_file = _os.path.join(_HERE, 'content', 'members.yaml')
    if _os.path.exists(members_file):
        with open(members_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return {'members': []}

# Discord URL設定（環境変数から読み込み、デフォルトはダミー値）
# スパム対策のためBase64エンコード
_raw_discord_url = _os.environ.get('DISCORD_URL', 'https://discord.gg/')
DISCORD_URL = base64.b64encode(_raw_discord_url.encode('utf-8')).decode('utf-8')

JINJA_GLOBALS = {
    'site_members': load_members()['members'],
    'discord_url': DISCORD_URL
}
