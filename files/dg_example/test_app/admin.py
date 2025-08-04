from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)  # 注册文章模型到Django管理后台
