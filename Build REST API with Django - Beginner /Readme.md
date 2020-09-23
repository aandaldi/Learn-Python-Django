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
1. 
 