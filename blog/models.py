from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')    # 他のモデルへのリンク
    title = models.CharField(max_length=200)   # テキスト数の定義
    text = models.TextField()                  # 制限なしのテキストフィールド
    created_date = models.DateTimeField(
            default=timezone.now)              # 日付と時間のフィールド
    published_date = models.DateTimeField(
            blank=True, null=True)             # 日付と時間のフィールド

    def publish(self):                         # ブログを公開するメソッド
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title