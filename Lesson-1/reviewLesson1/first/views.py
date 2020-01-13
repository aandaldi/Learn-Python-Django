from django.shortcuts import render

from .models import Post
# Create your views here.
def index(request):

    Posts = Post.objects.all()
    print(Posts)

    context = {
        'title':'this is title',
        'body': ' This is Body',
        'Posts': Posts
    }

    return render(request, 'first/index.html', context=context)
