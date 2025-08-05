from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)  # 博客标题
    content = models.TextField()  # 博客内容
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间
    updated_at = models.DateTimeField(auto_now=True)  # 更新时间

    def __str__(self):
        return self.title  # 返回博客标题
