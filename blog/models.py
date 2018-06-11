from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')    # 外部キー
    title = models.CharField(max_length=200)   # 文字数制限ありのテキストフィールド
    text = models.TextField()                  # 制限なしのテキストフィールド
    created_date = models.DateTimeField(default=timezone.now)     # 日付と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True)  # 日付と時間のフィールド

    def publish(self):                         # ブログを公開するメソッド
        self.published_date = timezone.now()
        self.save()                            # オブジェクトをデータベースに保存

    def __str__(self):
        return self.title