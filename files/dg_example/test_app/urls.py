from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Map the root URL to the index view
    path('articles/', views.article_list, name='article_list'),  # 文章
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),  # 文章详情
]
