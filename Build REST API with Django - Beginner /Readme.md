# Learn To build rest api with django for beginner

## Create Projects
1. install djangorestframework
1. add app on projects settings include rest_framewok
2. start create first project with `django-admin startproject profiles_project .` dot(".") to create project on root file
1. start create profiles app with `django-admin startapp profiles_api`.
1. add app on `INSTALLED_APPS` in projects settings. we add `rest_framework` and `rest_framework.authtoken` for dependencies app and `profiles_projects` for projects app


## MODELS
1. add attribute for model
1. create objects variable
1. create modelManager, the model manager will be manage for creating the object from that model
1. set our custom user model for defaul user model on django
1. create migrations and sync DB


## MIGRATIONS
1. make migrations. For create script to migrate the model on db, use `./manage.py makemigrations`
1. apply for migrations file `./manage.py migrate`

## DJANGO ADMIN
1. create super user on db `./manage.py createsuperuser` and follow the instruction for create new super user
1. run the server and can access the Django Admin Page on `<host>:<port>/admin` with the superuser
1. allow to manage the objects from model with register the model on admin site with `admin.site.register(<model>)` on admin.py in app directory


## API VIEWS
In the Above sample api view:
~~~
    from rest_framework.views import APIView
    from rest_framework.response import Response
    
    
    class HelloAPIView(APIView):
        """ Test API View """
    
        def get(self, request, format=None):
            """Returns a list of APIView features"""
            an_apiview = [
                'Uses HTTP mehtods as function (get, post, patch, put, delete)',
                'Is similar to a tradition Django View',
                'Give otu the most control over you application logic',
                'Is mapped manually to URLs',
            ]
    
            return Response({
                'message': 'Hello!',
                'an_apiview': an_apiview
            })
~~~

- To see my views, we need to register the views on url.
    1. Include app urls in project urls,
    1. register the endpoint of views on app urls.

*you can see this ***views*** code on `views.py` profile_api directory, and you try to get on browser `<host>:<port>/api/hello-view/` to see the view response


### SERIALIZERS AND VIEWS

1. First we create serializers for `hello-view` on `serializers.py`
    - you can see the `serializers.py` for see how to create simple serializer and `views.py` post for the implement serializer for response view
2. Create simple http method on `view.py` and give the response of helloview

### VIEWSET
1. import package viewset from rest_framework
1. create new class with viewset as parent.
1. import DefaultRouter from rest_fromework
1. create router variable with the value is Instance of DefaultRoter
1. add path in `urlpatterns` with the value is include of router.urls
1. test with `<host>:<port>/api`
1. create http method for viewset


### DESAIN YOUR API
1. desain url path

steps:
- create serializer for validate model api.
    - create Meta class with value (model, fields)
    - you using another rule in Meta class
- create viewset for access serializer in endpoint
- register the viewset in router on `urls.py` file and test your app.

2. create persmission class
    - create permission class on new file, call with `permissions.py`, you can see the code on the file

3. add authentication and permissions to ViewSet
    - import `TokenAuthentication` from `rest_framework` abd file `permissions` on views
    - create authentication_classes variable
    - dont forget, the authentication must be tuple value 