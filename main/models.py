from django.db import models

class Blogpost(models.Model):
    CATEGORY = (
        ("science", "学科のこと"),
    )

    title = models.CharField(
        verbose_name="タイトル",
        max_length=200
    )


    content = models.TextField(
    verbose_name="本文"
)

    #投稿日時フィールド
    posted_at= models.DateTimeField(
        verbose_name="投稿日時",
        auto_now_add=True
    )
    category=models.CharField(
        verbose_name="カテゴリー",
        max_length=50,
        choices=CATEGORY
    )

    def __str__(self):
        return self.title