# Django Girls Tutorial

チュートリアルの実践。  
ブログサイトを構築して、Herokuでデプロイする。

```
Python  : 3.5.5 :: Anaconda custom (x86_64)
Django  : 1.11
```

# 以下、実践時のメモ

## 仮想環境の作成とアクティベート
```
# "myvenv" という名称で、仮想環境を作成
python3 -m venv myvenv

# 仮想環境のアクティベート
source myvenv/bin/activate
```

## Djangoのインストール
```
# 最新バージョンのpipをインストール
pip install --upgrade pip

# Djangoのインストール
pip install django==1.11
```

## プロジェクトの作成
```
django-admin startproject mysite .


# 出来上がるディレクトリ構成
Django_Tutorial
├── manage.py         -- プロジェクト管理用のスクリプト
└── mysite            -- サイトの設定ファイル
    ├── __init__.py
    ├── settings.py   -- プロジェクトの設定ファイル
    ├── urls.py       -- URL宣言。サイトの目次
    └── wsgi.py       -- Webサーバーとのエントリーポイント

# WSGI(Web Server Gateway Interface)とは
PythonにおけるWebサーバーとWebアプリケーションを接続するための、標準化されたインターフェース定義
```

## プロジェクトの各種設定（settings.pyの編集）
```
# 該当の箇所を以下に修正する
LANGUAGE_CODE = 'ja-JP'   -- 言語
TIME_ZONE = 'Asia/Tokyo'  -- タイムゾーン
USE_TZ = False            -- タイムゾーンを固定する
```

## データベースの作成
```
# manage.pyと同じディレクトリで実行
python manage.py migrate
```

## サーバーの起動
```
# サーバの起動
python manage.py runserver

# サイトの動作確認（Chromeでアクセス）
http://127.0.0.1:8000/
```

## ブログアプリケーションの作成
```
# "blog"の名称でアプリケーションを作成
python manage.py startapp blog


# 出来上がるディレクトリ構成
djangogirls
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── mysite
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

# settings.pyのINSTALLED_APPSに'blog'を追加
INSTALLED_APPS = [
    'django.contrib.admin',
    # 略
    'blog'
]

# blog/models.py でモデルを作成
```

## データベースにモデルを認識させる
```
# blog/models.pyの変更を認識させる
python manage.py makemigrations blog

# データベースに格納されたモデルを確認する
python manage.py migrate blog
```

## サイト管理者の作成
```
# blog/admin.py を編集して、作成したPostモデルをadminページで見れるようにする
from django.contrib import admin
from .models import Post
admin.site.register(Post)

# スーパーユーザの作成
python manage.py createsuperuser
```

## Herokuにデプロイする
```
# Herokuを使うために必要なパッケージのインストール
pip install dj-database-url gunicorn whitenoise

# requirements.txt（必要なPythonパッケージをHerokuに伝達する）の作成
pip freeze > requirements.txt

# requirements.txt の中身
dj-database-url==0.5.0
Django==1.11
gunicorn==19.8.1
pytz==2018.4
whitenoise==3.3.1
# Herokuで動かすのに必要なので追加する
psycopg2==2.7.4

# Procfileの作成して以下を記述（Herokuでどのコマンドを実行してウェブサイトをスタートするか指定する）
web: gunicorn mysite.wsgi

# runtime.txt（Herokuに使っているPythonのバージョンを伝える）の作成
python-3.6.5

# ローカルとHerokuでデータベースの設定を分ける
# mysite/local_settings.py にローカルのデータベース設定を記述
# mysite/settings.py にHerokuのデータベース設定と、ローカルの設定を記述

# mysite/wsgi.py にDjangoWhiteNoiseを使うための設定を書き加える

# Herokuにログイン
heroku login

# アプリケーションの命名
heroku create selectfromwheres-blog

# 変更したい場合は
heroku apps:rename the-new-name

# herokuにプッシュ
git push heroku master

# herokuのウェブプロセスを起動
heroku ps:scale web=1

# ブラウザでアプリを開く
heroku open

# heroku上でのデータベースと管理者の作成
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

## Django shellの起動・終了
```
python manage.py shell
exit()
```

## Django shellから記事を投稿する
```
# postモデルのインポート
from blog.models import Post

# 全ての記事の表示
Post.objects.all()

# userモデルのインポート
from django.contrib.auth.models import User

# 登録されているユーザの確認
User.objects.all()

# コンソールから記事を作成
me = User.objects.get(username='select_from_where')
Post.objects.create(author = me, title = 'Sample title', text = 'Test')

# 作成者でフィルタリングした記事
Post.objects.filter(author=me)

# タイトルでフィルタリングした記事
Post.objects.filter(title__contains='title')

# 公開済みの記事
from django.utils import timezone
Post.objects.filter(published_date__lte=timezone.now())

# 記事の公開
post = Post.objects.get(id=1)
post.publish()

# 作成日による並び替え
Post.objects.order_by('created_date')
Post.objects.order_by('-created_date')    # 順序の入れ替え
```