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
- To create a new table in our database, use the following snippet of code found in [controller.py](/graphs/controller.py): 
<table>

    def createNewTable(pathtofile, tablename): 
        """
        Uses Pandas to read a csv file to a dataframe object and stores it into our database
        :param str pathtofile: Path to file from our projects base directory
        :param str tablename: Name of the table we wish to input data into. \
        IF tablename exists, it will fail
        """
        df = pd.read_csv(__base+pathtofile)
    
        print("Finished reading csv")
        print(df)
    
        engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)
        print("Connected to mysql\n")

        df.to_sql(con=engine, name=tablename, if_exists='fail')

</table>

- To update or replace a table, you can change the `if_exists` to either `'replace'` or `'update'`


## Creating a CSS Template page 
1. To setup a template, you need to first create a new file called __views.py__ to store your different views: 
<table>

    def nameofview(request):
    return render(request, "corresponding html file", {python files})

</table>

2. In your __urls.py__ file, you will need to add the following code to link the view to your webpage: 
<table>

    from . import views

    urlpatterns = [
        path('path desired for url', views.nameofview, name='name for referencing'),
    ]

</table>

3. Finally, in your main [urls.py](/basic/urls.py) file, you will need to modify and add the following: 
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
### Creating a List View 
- This subsection will walk through how to create a simple list of datapoints in our web app
    > [Creating a __powerData model__](#Power-Data-Model) <br>
    > [Creating and linking the view to our url](#Updating-views.py-and-urls.py) <br>
    > [Creating a basic unordered list in our HTML template](#HTML-Template) <br>
#### Power Data Model
- In our [models.py](/graphs/models.py) create a class called `powerData`: 
<table>

    class powerData(models.Model):
        """
        Class that holds 3 variables
            1. index 
            2. Timestamp: DateTime
            3. Power: Decimal(max digits = 8, decimal places = 3)
        """
        index = models.AutoField(primary_key=True)
        Timestamp = models.DateTimeField()
        Power = models.DecimalField(max_digits = 8, decimal_places = 3)

        def __str__(self):
            return "The date is: " + self.Timestamp.strftime("%m/%d/%y %H:%M:%S") + " and The power is: " + str(self.Power)
</table>

- Run the migrations into our database 
- Add data values into our new powerData model by running the following code: 
<table>

    def updateTable(pathtofile, tablename):
        """
        Updates a table in our database by appending the new data into the table \n
        :param str pathtofile: Path to file from our projects base directory \n
        :param str tablename: name of table to input data. \
        IF tablename exists, we will append the data to the bottom \
        OTHERWISE it will create a new table 
        """
        # Add the corresponding path, a sample that works is //static//data//2018services.csv
        df = pd.read_csv(__base+pathtofile)
        
        print("Finished reading csv")
        print(df)
        
        # Add the corresponding authentication and database information
        engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)
        print("Connected to mysql\n")

        # Modify if_exists to replace or fail to replace existing table or fail if table exists
        df.to_sql(con=engine, name=tablename, if_exists='append', index=False, index_label = 'index')

</table>

#### Updating views.py and urls.py
- In [urls.py](/graphs/urls.py) add `path('max/<int:num_req>/',views.peakData, name='max')` as a new path 
- In [views.py](/graphs/views.py) create a new view called `peakData` and add the following code: 
<table>

    def peakData(request, num_req):
        """
        Gets a list of data points ordered by power consumption \n
        :param int num_req: Number of data points to be extracted
        """
        from .models import powerData 
        # Creates an ordered list of [num_req] from Max->Min power
        latest_data_list = powerData.objects.order_by('-Power')[:num_req]
        return render(request, 'max_val.html', {'max_power':latest_data_list})

</table>

#### HTML Template
- Create a new html template called max_val.html (or whichever name you put in peakData.render()) and add the following block: 
<table>

    <h1>Maximum Power Consumption</h1>
    <br>
    <!--Unordered list of the Power Consumption listed from Greatest to Least-->
    <ul>
    {% for x in max_power %} 
        <li><b>Date: </b>{{x.Timestamp}} <b>Power: </b>{{x.Power}}</li>
        {% endfor %}
    </ul>

</table>

- Now you should be able go to localhost:8000/max/INSERT_NUMBER_HERE and get an unordered list similar to below:
![Basic Power List](/static/images/basiclistview.JPG)


## Adding a graph using MatPlotLib
- Now that our database is setup and connected to the django application, and we have practice working with queries, we will try creating a basic graph using the MatPlotLib library 
- The goal of this part is to create something similar to the example shown below: 
![Basic Graph](/static/images/matplotlib_fig2.png)
- We will adding and playing with this first in our [controller.py](/graphs/controller.py) to access our database
- Add a method that will allow us to extract the most recent data into a pandas dataframe like so: 
<table>

    def getRecentData(tablename, num_req, col):
    """
    Reads and returns the recent data \n
    :param str tablename: Name of table to be opened \n
    :param int num_req: Number of datapoints to be limited to \n
    :param str col: Name of column in database to be ordered by \n
    Returns a dataframe of our data
    """ 
    engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)

     #sql query to select specific dates 
    my_query = "SELECT * FROM " + \
                tablename + \
                " ORDER BY " + col + " DESC" + \
                " LIMIT " + str(num_req)
    df = pd.read_sql_query(sql = my_query, con=engine)
    return df
</table>

- Next, we will add the method that creates a pyplot like seen above by adding another method to our controller.py file 
<table>

    def graphData(x,y):
    """
    Graphs and shows data 
    :param dataframe column x: values in x column (date)  
    :param dataframe column y: values in y column (power)
    Returns pyplot plt 
    """
    from matplotlib import pyplot as plt
    from matplotlib import dates as mdates

    yearsFmt = mdates.DateFormatter('%Y-%m-%d %H:%M')
    fig, ax = plt.subplots()
    line, = ax.plot(x,y,'b-') #solid line  
    
    line.set_antialiased(False)
    
    # format the ticks
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.grid(True)

    fig.autofmt_xdate()

    plt.xlabel("Date")
    plt.ylabel("Power")
    plt.title("EV Power Data")
    return plt
</table>

- To view your graph, you can use `plt.show()` method 


