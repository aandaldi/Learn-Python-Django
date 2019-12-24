from django.shortcuts import render

from .models import Post


# Create your views here.
def index(request):
    # query get posts
    posts = Post.objects.all()
    print(posts)

    context = {
        'Title': 'Blog',
        'Heading': 'Test Heading di blog',
        'Posts': posts,
    }
    return render(request, 'blog/index.html', context)
