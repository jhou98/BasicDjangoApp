# Walkthrough of Project 

## Setup a Django Project with mySQL  
- Make sure Python is installed, you can check through the `python -V` command
- Create a new virtual environment ENV, [walkthrough for virtual environment](https://virtualenv.pypa.io/en/latest/)
- Activate the virtual environment through `ENV/Scripts/activate` or `source ENV/bin/activate`  
- Install django in the virtual environment using `pip install django`
- Create a new project using `django-admin startproject project *name of project`
- Install mysql to django `pip install pymysql` 
- Add the following lines to the [\_\_init\_\_.py](/basic/__init__.py) file found in our original project directory:
    `import pymysql` <br>
    `pymysql.install_as_MySQLdb()` 
- In the [settings.py](/basic/settings.py) file, change the database settings to the following: 
<table>

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'name of database',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': 'PORT CONNECTED',
        }
    }

</table>

- Start the server with `python manage.py runserver` while in the main directory where __manage.py__ is found
- Ensure your server is running by navigating to localhost:8000 in a browser 

## Setup App 
- Use `python manage.py startapp graphs` to create a new app in our project called graphs 
    > We will use this to create our graphs app for our project 
- In [graphs/models](/graphs/models.py), create a new class model called __EVData__ and add any fields needed to it 
- Create a new file called _urls.py_ in the graphs folder and add the following: 
<table>

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]

</table>

- In the INSTALLED_APPS setting found in our [settings.py](/basic/settings.py), add `graphs.apps.GraphsConfig` so our project knows our graphs app is installed
- In the command shell, run `python manage.py makemigrations graphs` to store our changes into a migration and then call `python manage.py sqlmigrate graphs 0001` and `python manage.py migrate` to create these model tables into our mySQL database 
    > The migrate command takes all migrations that have not been applied and runs them against your database 
    > In the future, for changes in models.py, call `python manage.py makemigrations` and `python manage.py migrate` to make the changes 
- To add or modify the database, you can either run a python shell using `python manage.py shell` and creating and saving objects __OR__ creating and logging into the admin page at <u>localhost:8000/admin</u> and adding the following to the [admin.py in graphs](/graphs/admin.py)
<table>

    from django.contrib import admin
    from .models import EVData

    admin.site.register(EVData)

</table>

## Setting up mySQL Queries 
- To create a new table in our database, use the following code in python: 
<table>

    import mysql 
    from mysql import connector 

    # Establish a connection to our mySQL db at localhost:3306 (add host and port if this changes)
    # Assumes you have already created a database
    myconnection = connector.MySQLConnection(user='username',password='password',database='name of database')
    mycursor = myconnection.cursor()

    # Creates a new table if there isn't already a table with the same name
    mycursor.execute("CREATE TABLE IF NOT EXISTS tablename (id INT AUTO_INCREMENT PRIMARY KEY, namevars VARTYPE, ...")

</table>

- After creating a table, add sample data either through a csv or xlsx file, which can be achieved through queries and pandas. 


## Creating a CSS Template page 
- To setup a template, you need to first create a new file called __views.py__ to store your different views: 
<table>

    def nameofview(request):
    return render(request, "corresponding html file", {python files})

</table>

- In your __urls.py__ file, you will need to add the following code to link the view to your webpage: 
<table>

    from . import views

    urlpatterns = [
        path('path desired for url', views.nameofview, name='name for referencing'),
    ]

</table>

- Finally, in your main [urls.py](/basic/urls.py) file, you will need to modify and add the following: 
<table>

    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('path desired for url', include('foldername.urls')),
    ]
    
</table>

- In the future, you will only need to do parts 1 and 2 as the path in our main __urls.py__ will already be setup. 
- For creating the CSS template, we will be using [bootstrap](https://getbootstrap.com/) as a template 
### Adding python functions to your page 
- To add a python function to our page, modify our __views.py__ in a similar fashion as below: 
<table>

    def index(request):
        from folder.pythonfile import pythonfunction
        return render(request, "html file", {"reference": pythonfunction})

</table>

- In our __html file__ add `{{reference}}` where you wish to put the python function 

