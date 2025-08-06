from django.shortcuts import render
from .models import Post


# Create your views here.
def post_blog(request):
    blog_list = Post.objects.order_by('updated_at')
    print(blog_list)
    return render(request, 'blog.html', {'blog_list': blog_list})
