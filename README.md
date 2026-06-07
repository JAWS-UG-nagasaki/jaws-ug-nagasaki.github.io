# JAWS-UG 長崎 Webサイト

JAWS-UG長崎のWebサイトを構築・管理するためのリポジトリです。

## 技術スタック

- **Pelican**: Pythonベースの静的サイトジェネレーター
- **uv**: 高速なPythonパッケージマネージャー
- **pyproject.toml**: 依存パッケージ管理
- **uv.lock**: 依存パッケージのロックファイル
- **Markdown**: コンテンツ記述
- **GitHub Actions**: 自動デプロイ

## ディレクトリ構成

```
.
├── content/              # コンテンツ（Markdown）
│   ├── events/          # イベント記事
│   ├── pages/           # 静的ページ
│   └── index.md         # トップページ
├── output/              # 生成されたHTML（.gitignore）
├── static/              # 静的ファイル（CSS,画像など）
├── pelicanconf.py       # Pelican設定（開発用）
├── publishconf.py       # Pelican設定（本番用）
├── Makefile             # ビルドコマンド
└── .github/workflows/   # GitHub Actions
```

## 開発環境セットアップ

### 前提条件

- Python 3.10+
- uv

### インストール

```bash
# シェルスクリプトを使用してセットアップ（推奨）
./serve.sh setup
```

または手動で：

```bash
# uvで仮想環境を作成
uv venv

# pyproject.tomlとuv.lockから依存パッケージをインストール
uv sync
```

## ローカル開発

### 方法1: シェルスクリプトを使用（推奨）

```bash
# 初回のみ: セットアップ、ビルド、サーバー起動をまとめて実行
./serve.sh setup-serve

# セットアップのみ
./serve.sh setup

# ビルドとサーバー起動（デフォルトポート8000）
./serve.sh

# ポートを指定して実行
./serve.sh serve 8001

# ビルドのみ
./serve.sh build
```

### 方法2: Makefileを使用

```bash
# サイトをビルド
make html

# ローカルサーバーを起動（http://localhost:8000）
make serve

# ポートを指定して起動（例: 8001番ポート）
make serve PORT=8001
```

または：

```bash
# ビルドとサーバー起動をまとめて実行
make devserver

# ポートを指定して実行
make devserver PORT=8001
```

## コンテンツの追加

### イベントを追加する

`content/events/`ディレクトリに新しいMarkdownファイルを作成します。テンプレートは`content/events/_template.md`を参照してください。

```bash
cp content/events/_template.md content/events/2026-06-01-event-name.md
```

### ページを追加する

`content/pages/`ディレクトリにMarkdownファイルを追加します。

## デプロイ

mainブランチにプッシュすると、GitHub Actionsが自動的にGitHub Pagesにデプロイします。

### 初期設定

1. GitHubリポジトリのSettings > PagesでSourceを「GitHub Actions」に設定
2. Settings > Actions > General > Workflow permissionsで「Read and write permissions」に設定

### ドメイン設定

サイトのドメインは `publishconf.py` で環境変数 `SITEURL` から読み込むように設定されています。

- **GitHub Actionsでのデプロイ時**: `.github/workflows/deploy.yml` で `SITEURL` 環境変数を設定します（現在は `https://jaws-ug-nagasaki.github.io/website`）
- **ローカルでのビルド時**: 環境変数を設定してビルドします

```bash
# ドメインを指定してビルド
SITEURL=https://jaws-ug-nagasaki.github.io/website pelican -s publishconf.py
```

ドメインを変更する場合は、`.github/workflows/deploy.yml` の `SITEURL` 環境変数の値を変更してください。

## 運用フロー

イベント後に以下の手順でサイトを更新：

1. `content/events/`にイベント記事を追加
2. 必要に応じてトップページを更新
3. `git commit` & `git push`
4. GitHub Actionsが自動デプロイ

## ライセンス

本リポジトリのコンテンツは、特記のない限りCC BY-NC 4.0（表示 - 非営利 4.0 国際）で公開されます。

## Webサイト

- **[JAWS-UG長崎 Webサイト](https://jaws-ug-nagasaki.github.io/)**
- **[connpass](https://jawsug-nagasaki.connpass.com/)**
