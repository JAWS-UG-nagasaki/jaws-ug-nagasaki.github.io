#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# 本番環境用設定
SITEURL = 'https://jaws-ug-nagasaki.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# SEO対策
GOOGLE_ANALYTICS = ''  # 必要に応じて追加
