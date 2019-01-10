### Walkthrough of Project 

## Setup a Django Project with mySQL  
- Make sure Python is installed 
- Create a new virtual environment ENV
- Activate the virtual environment through ENV/Scripts/activate 
- Install django in the virtual environment using `pip install django`
- Create a new project using `django-admin startproject project *name of project`
- Install mysql to django `pip install pymysql` 
- Add the following lines to the [\_\_init\_\_.py](/basic/__init__.py) file found in our original project directory   
    `import pymysql` <br>
    `pymysql.install_as_MySQLdb()` 
- In the [settings.py](/basic/settings.py) file, change the database settings to the following: 
<table>

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NAME OF DB',
        'USER': 'root',
        'PASSWORD': 'PASSWORD OF ROOT',
        'HOST': '127.0.0.1',
        'PORT': 'PORT CONNECTED',
        }
    }

</table>
- Start the server with `python manage.py runserver` while in the main directory where __manage.py__ is found
- Ensure your server is running by navigating to localhost:8000 in a browser 