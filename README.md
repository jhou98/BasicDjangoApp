# Basic Django App 
> A basic application in Django and Python that will connect to a local mySQL server to output data regarding electrical consumption for EV and Buildings at UBC. 

## Models 
- Assume you have your main project called __basic__ and you want to add a model to your app called __graphs__
### Creating a Model
- In the `graphs.models.py`, make sure to add `from django.db import models` so that models can be used 
- Create a model using `class %modelname%(models.Model):` and adding methods and variables to the model 
### Linking a Model to the Database
- In the `graphs.admin.py` file, add your newly created model with the following lines of code: <br>
<table>

    from .models import %modelname%`
    admin.site.register(%modelname%)`
</table>

- Make sure in your `graphs.apps.py` file you have everything configured like so: <br>
<table>

    from django.apps import AppConfig

    class GraphsConfig(AppConfig):
        name = 'graphs'
</table>

- In your `main.settings.py` file, check the `INSTALLED_APPS` to see if you have the graphs application path on the project.
> If not, add `'graphs.apps.GraphsConfig'` to the list 
- In the command shell, navigate to the top level project folder where __manage.py__ is and run the following commands to migrate the model changes into the server.
<table>

    python manage.py makemigrations
    python manage.py migrate
</table>

- Check your database to make sure a new table has been created named __graphs.%modelname%__

## Views 
### Creating a view 
- In `graphs.views.py` you can create a new view just like creating a new method in python. Have the following imports at the top of your file: 
<table>

    from django.shortcuts import render
    from django.http import HttpResponse, Http404
</table>

- Below, I have a view called index(request, **args) which returns a render
> render(request, HTML template that we are sending the render to, {reference name: python functions we want to use}) <br>
> this index function will store the sum of all the arguments into __'reference'__
<table>

    def index(request, **args):
       
        answ = args1 + args2 + ...
        return render(request, 'index.html', {'reference':answ})
</table>

### Adding the view to HTML template
- Using the example above, in `index.html`, if you wish to call upon the python function use `{{reference}}`
<table>

    <!DOCTYPE HTML>
    <html lang = "en">
    <head>
    <!-- index.html -->
    <title>index.html</title>
    <meta charset = "UTF-8" />
    </head>
    <body>
    <h1>Header: This is a addition function</h1>
    {{reference}} <!--Calls on our python variable (we can also have functions here)-->
    </body>
    </html>
</table>

### Creating a URL path 
- Now that your view and template pages are linked, you will need to setup a URL path to access this new view 
- In `graphs.urls.py` add the path to your `url patterns[]`
> The first argument will be the path you need to enter to get to your view from localhost <br>
> The second argument `views.index` tells you which view you are accessing <br>
> The last argument is a reference that you can call upon as a shortcut to the path 
<table>

     path('index/<args1>/<args2>/....',views.index, name='index')
</table>