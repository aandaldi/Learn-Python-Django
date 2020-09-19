# Simple Django Rest Framework

## Steps:
1. Add Dependencies:
    - `pip install djangorestframework`

2. Start Project and Create App
    - `django-admin startproject rest_api`
    - `cd rest_api`
    - `django-admin startapp posts`
    - add app and restframewok on `rest_api/settings.py`
    ~~~
        # Application definition
        
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'rest_framework',                    #add restframework 
            'posts',                            #add apps
        ]
    ~~~

3. Create app model
4. Migrate the app, you will migrate the app after any update/add app model. for migrate,  run this command:
    - `./manage.py makemigration`
    - `.manage.py migrate`
5. Register app in admin template. use this when you want to manage from admin page. register in `posts/admin.py`
    ~~~
    from django.contrib import admin
    from .models import Post
    
    admin.site.register(Post)
    ~~~
    
    for login in admin page, you must to use admin account. create super admin with: `./manage.py createsuperadmin` and follow the instruction.

6. Create `serializers.py` file on app directory
    ~~~
    # posts/serializers.py
    from rest_framework import serializers
    from . import models
    
    
    class PostSerializer(serializers.ModelSerializer):
    
        class Meta:
            fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
            model = models.Post
    ~~~

7. update the `views.py` on app
    ~~~
    # posts/views.py
    from rest_framework import generics
    
    from .models import Post
    from .serializers import PostSerializer
    
    class PostList(generics.ListCreateAPIView):
        queryset = Post.objects.all()
        serializer_class = PostSerializer
    
        def get_read_serializer_class(self):
            if self.request.method == 'POST':
                return PostSerializer
    
            return PostSerializer
    
    
    class PostDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Post.objects.all()
        serializer_class = PostSerializer
    ~~~

8. Routing:
    - from project url add app in `rest_api/urls.py`:
        ~~~
            from django.contrib import admin
            from django.urls import include, path
            
            urlpatterns = [
                path('admin/', admin.site.urls),
                path('api/', include('posts.urls')),
            ]
        ~~~
    - in `posts/urls.py`:
        ~~~
            # posts/urls.py
            from django.urls import path
            
            from . import views
            
            urlpatterns = [
                path('', views.PostList.as_view()),
                path('<int:pk>/', views.PostDetail.as_view()),
            ]
        ~~~

9. run server `./manage.py runserve`
    access the app in `localhost:8000`.
    - admin page (`localhost:8000/admin`)
    - posts page (`localhost:8000/admin`)