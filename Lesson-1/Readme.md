### Learn First Project

step:
    - install django on venv
    ` 1. django-admin startproject <namaproject> `
    ` 2. django-admin startapp <namaapp> `
    ` 3. buat urls.py untuk masing masing app `
    ` 4. arahkan url project ke masing masing url app,`
    ` 5. create masing masing template(jangan lupa ganti setting directory template
        dan add di installed app untuk masing masing app)`
    `
    
    
    
    
###  Learn Model
add step:
    - install mysql server
    - install libmysqlclient - > pip install mysqlclient
    - setting database in settings
    - migrate database
    - create app.
    - create model -> register to admin
    - mikemigration -> migrate
    - runserver
    
    
    

*note : if you wan't to manage your model from admin, register app to admin.py


### Learn ORM
 default ORM in django include:
   ``` 
    - create(),
    - getall(),
    - get(), => option-using(__iexact,)
    - filter(),
    - delete(),
    - save(),
    - exclude(),
    - orderby(),
    - values/values_list => convert result to dict/list 
   ```
    more on django-query set in:
    [a link] (https://docs.djangoproject.com/en/3.0/ref/models/querysets/)
   
   
 
### url pattern
