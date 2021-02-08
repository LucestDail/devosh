from django.shortcuts import render
from .models import Post

# Create your views here.


def blog_main(request):
    return render(request, 'blog_main.html')


def blog_post(request):
    print(request.path.split("/")[3])
    postlist = Post.objects.all()
    return render(request, 'blog_post.html', {'postlist': postlist})


def blog_post_category(request, category):
    print(category)
    postlist = Post.objects.filter(categorys=category)
    return render(request, 'blog_category_post.html', {'postlist': postlist})