# Walkthrough of Project 
- A rough walkthrough of the project. Important parts are revised and shown in [README file](README.md)

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

## Adding a graph to the Web App using Chart.js 
- Now that we have some experience working with graphs, we will be using [chart.js](https://www.chartjs.org/) to display charts onto our web application 
- You will need to add [the latest script](https://cdnjs.com/libraries/Chart.js) into your __base.html__ file before beginning, and add [django rest framework](https://www.django-rest-framework.org/) to your project 
- In your __base.html__ file, also add the following block: 
<table>

    <script> 
      $(document).ready(function(){
        {% block jquery %}{% endblock %}
      })
    </script>
</table>

- Follow the [tutorial video](https://www.youtube.com/watch?v=B4Vmm3yZPgc) so that you will have a better understanding of Chart.js and how to set everything up 
- We will be using the __getRecentData__ function in our [controller.py](/graphs/controller.py) file, as well as a new function: 
<table>

    def pandasToJSON(df):
    """
    Converts a dataframe into a JSON string 
    """
    return df.to_json(date_format='iso', orient='split')
</table>

- In our views.py, we will create a class similar to the tutorial in our __views.py__ file 
> It will be using our __getRecentData__ and __pandasToJSON__ controller functions to obtain and format the data 
<table>

    from django.http import HttpResponse, Http404, JsonResponse
    import pandas as pd 
    from rest_framework.views import APIView
    from rest_framework.response import Response

    class ChartData(APIView):
    """
    This method is used to send 100 most recent data points as a JSON string\n
    Has built in support for authentication and permissions \n 
    See https://www.django-rest-framework.org/api-guide/views/ for more details 
    """ 
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_powerdata',100,'Timestamp')
        data = pandasToJSON(my_df)
        return Response(data)
</table>

- And in our [urls.py](/graphs/urls.py) add a new path for this class `path(r'api/data',views.ChartData.as_view(), name='chart' ),`
> Now if we go to our http://localhost:8000/api/data we should be able to see our latest data values in a JSON string 
- In a html file called __graphs.html__, add the following code and make sure the template is linked to your http://localhost:8000 
<table>

    {% extends 'base.html' %}
    {% block title%}Title{% endblock %}

    {% block header %} <h1>Home</h1> {% endblock %}

    {% block content %}
    <!--Content Here-->
    <div class='row'>
        <canvas id="myChartEV" width="400" height="400"></canvas>
    </div>

    {% endblock %}
    <!--Script for our Charts-->
    <script>
    {% block jquery %}
        var endpoint = '/api/data'
        
        $.ajax({
            method:"GET",
            url: endpoint,
            success: function(data){
                console.log(data)
                //convert our values from JSON string to JSON object
                var result = JSON.parse(data) 
                //Empty arrays to store our values 
                var date = []
                var power = []
                //length (as our objects are in Most recent->least recent)
                var length = result.data.length-1
                for (var x in result.data){
                    //slice the ISO-Format String 
                    //YYYY-mm-ddTHH:MM:SS.DDDZ -> YYYY-mm-ddTHH:MM
                    date.push(result.data[length-x][1].slice(0,16))
                    power.push(result.data[length-x][2])
                }
                console.log(date)
                console.log(power)
                //calls our function on success 
                createEVChart(date,power)  
            },
            error: function(err_data){
                console.log("error")
                console.log(err_data)
            }
        });

        /**
        * @param Array x_axis: Array of dates for our chart  
        * @param Array y_axis: Array of power for our chart
        * Returns a chart corresponding to our EV data
        */
        function createEVChart(x_axis,y_axis){
            
            var ctx_ev = document.getElementById("myChartEV").getContext('2d');

            var myChartEV = new Chart(ctx_ev, {
                type: 'line',
                data: {
                    labels: x_axis,
                    datasets: [{
                        label: 'Power Consumption',
                        data: y_axis,
                        backgroundColor: 'rgba(255, 99, 132, 0)',
                        borderColor: 'rgba(255,99,132,1)',
                    }]
                },
                options: {
                    title:{
                        display: true,
                        text: 'EV Charging Stations'
                    },
                    scales: {
                        xAxes:[{
                            display: true,
                            scaleLabel:{
                                display:true,
                                labelString:'Time'
                            }
                        }],
                        yAxes: [{
                            display: true,
                            scaleLabel:{
                                display: true,
                                labelString: 'Power'
                            },
                            ticks: {
                                beginAtZero:true
                            }
                        }]
                    }
                }
            });
        }
    {% endblock %}
    </script>

</table>

- in v0.4, we have a similar example with 2 graphs instead of 1 as shown
![chart.js_ex1](/static/images/chartjs_fig1.png)






