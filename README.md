# Django Girls Tutorial

チュートリアルの実践

Python  : 3.5.5 :: Anaconda custom (x86_64)
Django  : 1.11


# 以下、実践時のメモ

## 仮想環境の作成
```
python3 -m venv myvenv
```

## 仮想環境の使用
```
source myvenv/bin/activate
```

## Djangoのインストール
```
pip install django==1.11
```

## プロジェクトの作成
```
django-admin startproject mysite .


# 出来上がるディレクトリ構成
Django_Tutorial
├── manage.py         -- サイト管理用のスクリプト
└── mysite            -- サイトの設定ファイル
    ├── __init__.py
    ├── settings.py
    ├── urls.py       -- urlresolverをつかったURLのパターンのリストを含む
    └── wsgi.py
```

## データベースの作成
```
python manage.py migrate
```

## サーバーの起動
```
python manage.py runserver

# サイトの動作確認（Chromeでアクセス）
http://127.0.0.1:8000/
```

## ブログディレクトリの作成
```
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
```

## データベースにモデル用のテーブルを作る
```
python manage.py makemigrations blog
```

## データベースに格納されたモデルを確認する
```
python manage.py migrate blog
```

## サイト管理者の作成
```
python manage.py createsuperuser
```

## Herokuを使うために必要なパッケージのインストール
```
pip install dj-database-url gunicorn whitenoise
```

## requirements.txt（必要なPythonパッケージをHerokuに伝達する）の作成
```
pip freeze > requirements.txt


# requirements.txt の中身
dj-database-url==0.5.0
Django==1.11
gunicorn==19.8.1
pytz==2018.4
whitenoise==3.3.1
# Herokuで動かすのに必要なので追加
psycopg2==2.5.4
```

## Procfile（Herokuでどのコマンドを実行してウェブサイトをスタートするか指定する）
```
# 以下を記述
web: gunicorn mysite.wsgi
```

## runtime.txt (使っているPythonのバージョンを伝える)
```
python-3.5.5
```

## Herokuにログイン
```
heroku login
```

## アプリケーションの命名
```
heroku create selectfromwheres-blog

# 変更したい場合は
heroku apps:rename the-new-name
```

## herokuにプッシュ
```
git push heroku master
```

## herokuのウェブプロセスを起動
```
heroku ps:scale web=1
```

## ブラウザでアプリを開く
```
heroku open
```

## heroku上でのデータベースと管理者の作成
```
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

## Django shellの起動・終了
```
python manage.py shell
exit()
```
## postモデルのインポート
```
from blog.models import Post
# 全てのポストの表示
Post.objects.all()
```

## userモデルのインポート
```
from django.contrib.auth.models import User
# 登録されているユーザの確認
User.objects.all()
```

## コンソールからポストを作成
```
me = User.objects.get(username='select_from_where')
Post.objects.create(author = me, title = 'Sample title', text = 'Test')
# 全てのポストの表示
Post.objects.all()
```

## ポストのフィルタリング
```
# 作成者
Post.objects.filter(author=me)
# タイトル
Post.objects.filter(title__contains='title')
# 公開済みのポスト
from django.utils import timezone
Post.objects.filter(published_date__lte=timezone.now())
```

## ポストの公開
```
post = Post.objects.get(id=1)
post.publish()
```

## オブジェクトの並び替え
```
# 作成日による並び替え
Post.objects.order_by('created_date')
Post.objects.order_by('-created_date')    # 順序の入れ替え
```