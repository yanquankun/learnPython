from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.
def index(request):
    return HttpResponse("Hello, Django!")


def article_list(request):
    articles = Article.objects.all()  # 获取所有文章
    return render(request, 'article_list.html', {'articles': articles})  # 渲染文章列表模板


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)  # 根据文章ID获取文章
    return render(request, 'article_detail.html', {'article': article})
