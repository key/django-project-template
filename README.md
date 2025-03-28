# Django 4.2+ プロジェクトテンプレート

これはモダンな設定を備えたシンプルな Django 4.2+ プロジェクトテンプレートです。多くの Django プロジェクトテンプレートは過度に多くの前提を置いていたり、複雑すぎたりします。このテンプレートは最小限の前提で、新しいプロジェクトのための有用な基盤を提供します。

## 特徴

- Django 4.2+ と Python 3.12 のサポート
- 依存関係管理に [Pipenv](https://github.com/pypa/pipenv) を使用
- [Django REST Framework](https://www.django-rest-framework.org/) による REST API サポート
- 開発ツール:
  - [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org) によるデバッグとパフォーマンス分析
  - [django-extensions](http://django-extensions.readthedocs.org) による便利な開発コマンド
  - コード品質のための [pre-commit](https://pre-commit.com/) フック
- PostgreSQL と Redis のための Docker Compose 設定
- CI/CD のための GitHub Actions ワークフロー
- ステージングと本番環境のための HTTPS とセキュリティ設定
- psycopg2-binary による PostgreSQL データベースサポート
- django-redis による Redis キャッシュ統合
- エラー追跡のための Sentry 統合
- 高性能リクエスト処理のための Bjoern WSGI サーバー
- 静的ファイル配信のための WhiteNoise

## インストール方法

### 前提条件

システム要件をインストールします:

```bash
brew bundle  # macOS の場合
# Ubuntu/Debian の場合: sudo apt-get install -y libev-dev direnv
```

### 新しいプロジェクトの作成

このテンプレートから Django プロジェクトを作成します:

```bash
django-admin startproject \
  --template=https://github.com/key/django-project-template/archive/master.zip \
  --name=env.example \
  --extension=py,md,yml \
  project_name
```

### 環境設定

`env.example` から `.env` を作成し、direnv を許可します:

```bash
mv env.example .env
direnv allow .
```

### 依存関係のインストール

Python モジュールをインストールします:

```bash
# macOS と Homebrew の場合
C_INCLUDE_PATH=/usr/local/include LD_LIBRARY_PATH=/usr/local/lib pipenv install --dev

# Ubuntu/Debian の場合
pipenv install --dev
```

### 開発サービスの起動

Docker を使用して PostgreSQL と Redis を起動します:

```bash
docker compose up -d
```

## 環境変数

このテンプレートはクラスベースの設定のために [django-configurations](https://django-configurations.readthedocs.io/) を使用しています。`DJANGO_CONFIGURATION` 環境変数によって使用する設定クラスが決まります。

### 共通環境変数

これらの変数はすべての環境で使用されます:

```
DJANGO_CONFIGURATION=Dev  # オプション: Dev, Test, Prod
DJANGO_SECRET_KEY='your-secret-key'
DATABASE_URL='postgresql://postgres:password@localhost:15432/project_name'
CACHE_URL='redis://localhost:16379/1'
```

### 本番環境変数

これらの設定はステージングと本番環境で使用されます:

```
DJANGO_SESSION_COOKIE_SECURE='yes'
DJANGO_SECURE_BROWSER_XSS_FILTER='yes'
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF='yes'
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS='yes'
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_REDIRECT_EXEMPT=''
DJANGO_SECURE_SSL_HOST=''
DJANGO_SECURE_SSL_REDIRECT='yes'
DJANGO_SECURE_PROXY_SSL_HEADER='HTTP_X_FORWARDED_PROTO,https'
SENTRY_DSN='your-sentry-dsn'  # エラー追跡用
```

## 開発

### サーバーの実行

Django 開発サーバーを起動します:

```bash
python manage.py runserver
```

### テストの実行

テストを実行します:

```bash
python manage.py test --configuration=Test
```

## デプロイメント

このテンプレートは様々なプラットフォームにデプロイできます:

1. **自己ホスト型サーバー**: 高性能のための内蔵 Bjoern WSGI サーバーを使用
2. **Docker**: 同梱の compose.yaml で Docker 対応済み
3. **クラウドプラットフォーム**: Django をサポートするほとんどのクラウドプラットフォームと互換性あり

## ライセンス

The MIT License (MIT)

Copyright (c) 2012-2025 José Padilla, Mitsukuni Sato

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
