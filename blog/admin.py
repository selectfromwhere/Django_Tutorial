from django.contrib import admin
from .models import Post

admin.site.register(Post)    # adminページで見れるように、作成したモデルを登録する