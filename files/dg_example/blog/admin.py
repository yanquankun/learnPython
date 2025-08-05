from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)  # 注册博客模型到Django管理后台
