** Walkthrough of Project 

* Creating a Django Environment with mySQL  
- Make sure Python is installed 
- Create a new virtual environment ENV
- Activate the virtual environment through ENV/Scripts/activate 
- Install django in the virtual environment using pip install django
- Create a new project using django-admin startproject project name  
- Pip install pymysql 
- Add the following lines to the _init__.py file found in our original project directory 
 
    import pymysql

    pymysql.install_as_MySQLdb()
- start the server with python manage.py runserver 