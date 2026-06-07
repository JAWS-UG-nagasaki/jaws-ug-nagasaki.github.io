#!/bin/bash

# JAWS-UG 長崎 Webサイト ローカル開発サーバー起動スクリプト

set -e

ACTION=${1:-serve}
PORT=${2:-8000}

setup() {
    echo "🔧 仮想環境を作成中..."
    if [ ! -d ".venv" ]; then
        uv venv
    else
        echo "✅ 仮想環境は既に存在します"
    fi

    echo "📦 依存パッケージをインストール中..."
    uv sync
}

build() {
    echo "📦 サイトをビルド中..."
    uv run pelican content -s pelicanconf.py
    echo "📁 静的ファイルをコピー中..."
    cp static/favicon.ico output/favicon.ico
    cp static/custom.css output/custom.css
}

serve() {
    echo "🚀 ローカルサーバーを起動中... (http://localhost:$PORT)"
    cd output && python3 -m http.server $PORT
}

case $ACTION in
    setup)
        setup
        ;;
    build)
        build
        ;;
    serve)
        build
        serve
        ;;
    setup-serve)
        setup
        build
        serve
        ;;
    *)
        echo "使い方: ./serve.sh [command] [port]"
        echo ""
        echo "コマンド:"
        echo "  setup         仮想環境の作成とパッケージインストール"
        echo "  build         サイトのビルドのみ"
        echo "  serve         ビルドとサーバー起動（デフォルト）"
        echo "  setup-serve   セットアップ、ビルド、サーバー起動をまとめて実行"
        echo ""
        echo "例:"
        echo "  ./serve.sh              # ビルド+サーバー起動（ポート8000）"
        echo "  ./serve.sh serve 8001   # ビルド+サーバー起動（ポート8001）"
        echo "  ./serve.sh setup        # セットアップのみ"
        echo "  ./serve.sh setup-serve  # セットアップ+ビルド+サーバー起動"
        exit 1
        ;;
esac
