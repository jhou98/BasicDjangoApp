# Walkthrough of Project 
- A rough walkthrough of the project. Important parts are revised and shown in [README file](README.md)
- This walkthrough DOES NOT cover all of the project and is a rough draft of the overall thought process. 

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
    ```python
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
    ```


- Start the server with `python manage.py runserver` while in the main directory where __manage.py__ is found
- Ensure your server is running by navigating to localhost:8000 in a browser 

## Setup App 
- Use `python manage.py startapp graphs` to create a new app in our project called graphs 
    > We will use this to create our graphs app for our project 
- In [graphs/models](/graphs/models.py), create a new class model called __EVData__ and add any fields needed to it 
- Create a new file called _urls.py_ in the graphs folder and add the following: 
    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```

- In the INSTALLED_APPS setting found in our [settings.py](/basic/settings.py), add `graphs.apps.GraphsConfig` so our project knows our graphs app is installed
- In the command shell, run `python manage.py makemigrations graphs` to store our changes into a migration and then call `python manage.py sqlmigrate graphs 0001` and `python manage.py migrate` to create these model tables into our mySQL database 
    > The migrate command takes all migrations that have not been applied and runs them against your database 
    > In the future, for changes in models.py, call `python manage.py makemigrations` and `python manage.py migrate` to make the changes 
- To add or modify the database, you can either run a python shell using `python manage.py shell` and creating and saving objects __OR__ creating and logging into the admin page at <u>localhost:8000/admin</u> and adding the following to the [admin.py in graphs](/graphs/admin.py)
    ```python
    from django.contrib import admin
    from .models import EVData

    admin.site.register(EVData)
    ```

## Setting up mySQL Queries 
- To create a new table in our database, use the following snippet of code found in [controller.py](/graphs/controller.py): 
    ```python
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
    ```
- To update or replace a table, you can change the `if_exists` to either `'replace'` or `'update'`


## Creating a CSS Template page 
1. To setup a template, you need to first create a new file called __views.py__ to store your different views: 
    ```python
    def nameofview(request):
    return render(request, "corresponding html file", {python files})
    ```

2. In your __urls.py__ file, you will need to add the following code to link the view to your webpage: 
    ```python
    from . import views

    urlpatterns = [
        path('path desired for url', views.nameofview, name='name for referencing'),
    ]
    ```

3. Finally, in your main [urls.py](/basic/urls.py) file, you will need to modify and add the following: 
    ```python
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('path desired for url', include('foldername.urls')),
    ]
    ```
- In the future, you will only need to do parts 1 and 2 as the path in our main __urls.py__ will already be setup. 
- For creating the CSS template, we will be using [bootstrap](https://getbootstrap.com/) as a template 
### Adding python functions to your page 
- To add a python function to our page, modify our __views.py__ in a similar fashion as below: 
    ```python
    def index(request):
        from folder.pythonfile import pythonfunction
        return render(request, "html file", {"reference": pythonfunction})
    ```
- In our __html file__ add `{{reference}}` where you wish to put the python function 
### Creating a List View 
- This subsection will walk through how to create a simple list of datapoints in our web app
    > [Creating a __powerData model__](#Power-Data-Model) <br>
    > [Creating and linking the view to our url](#Updating-views.py-and-urls.py) <br>
    > [Creating a basic unordered list in our HTML template](#HTML-Template) <br>
#### Power Data Model
- In our [models.py](/graphs/models.py) create a class called `powerData`: 
    ```python
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
    ```

- Run the migrations into our database 
- Add data values into our new powerData model by running the following code: 
    ```python
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
    ```

#### Updating views.py and urls.py
- In [urls.py](/graphs/urls.py) add `path('max/<int:num_req>/',views.peakData, name='max')` as a new path 
- In [views.py](/graphs/views.py) create a new view called `peakData` and add the following code: 
    ```python
    def peakData(request, num_req):
        """
        Gets a list of data points ordered by power consumption \n
        :param int num_req: Number of data points to be extracted
        """
        from .models import powerData 
        # Creates an ordered list of [num_req] from Max->Min power
        latest_data_list = powerData.objects.order_by('-Power')[:num_req]
        return render(request, 'max_val.html', {'max_power':latest_data_list})
    ```

#### HTML Template
- Create a new html template called max_val.html (or whichever name you put in peakData.render()) and add the following block: 
    ```html
    <h1>Maximum Power Consumption</h1>
    <br>
    <!--Unordered list of the Power Consumption listed from Greatest to Least-->
    <ul>
    {% for x in max_power %} 
        <li><b>Date: </b>{{x.Timestamp}} <b>Power: </b>{{x.Power}}</li>
        {% endfor %}
    </ul>
    ```
- Now you should be able go to localhost:8000/max/INSERT_NUMBER_HERE and get an unordered list similar to below:
![Basic Power List](/static/images/basiclistview.JPG)


## Adding a graph using MatPlotLib
- Now that our database is setup and connected to the django application, and we have practice working with queries, we will try creating a basic graph using the MatPlotLib library 
- The goal of this part is to create something similar to the example shown below: 
![Basic Graph](/static/images/matplotlib_fig2.png)
- We will adding and playing with this first in our [controller.py](/graphs/controller.py) to access our database
- Add a method that will allow us to extract the most recent data into a pandas dataframe like so: 
    ```python
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
    ```
- Next, we will add the method that creates a pyplot like seen above by adding another method to our controller.py file 
    ```python
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
    ```
- To view your graph, you can use `plt.show()` method 

## Adding a graph to the Web App using Chart.js 
- Now that we have some experience working with graphs, we will be using [chart.js](https://www.chartjs.org/) to display charts onto our web application 
- You will need to add [the latest script](https://cdnjs.com/libraries/Chart.js) into your __base.html__ file before beginning, and add [django rest framework](https://www.django-rest-framework.org/) to your project 
- In your __base.html__ file, also add the following block: 
    ```html
    <script> 
      $(document).ready(function(){
        {% block jquery %}{% endblock %}
      })
    </script>
    ```

- Follow the [tutorial video](https://www.youtube.com/watch?v=B4Vmm3yZPgc) so that you will have a better understanding of Chart.js and how to set everything up 
- We will be using the __getRecentData__ function in our [controller.py](/graphs/controller.py) file, as well as a new function: 
    ```python
    def pandasToJSON(df):
    """
    Converts a dataframe into a JSON string 
    """
    return df.to_json(date_format='iso', orient='split')
    ```

- In our views.py, we will create a class similar to the tutorial in our __views.py__ file 
> It will be using our __getRecentData__ and __pandasToJSON__ controller functions to obtain and format the data 
    ```python
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
    ```

- And in our [urls.py](/graphs/urls.py) add a new path for this class `path(r'api/data',views.ChartData.as_view(), name='chart' ),`
> Now if we go to our http://localhost:8000/api/data we should be able to see our latest data values in a JSON string 
- In a html file called __graphs.html__, add the following code and make sure the template is linked to your http://localhost:8000 
    ```html
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
    ```

- in v0.4, we have a similar example with 2 graphs instead of 1 as shown: 
![chart.js_ex1](/static/images/chartjs_fig1.png)

## Creating Gauges 
- To look at a bit more static data, we will be using gauges from [svg-gauges](https://github.com/naikus/svg-gauge)
- For our case, we will generate gauges that will look like the image below:

![Basic Gauge](/static/images/gauge_basic.JPG)

- In order to use the svg-gauges library, you will need to download and host the source code remotely. Fortunately Github allows you to do this pretty easily. 

> Navigate to your Github Project __Settings__ Page (or create a new github project if you have not done so already)
> Scroll down the __Github Pages__ section where you have the option to host project pages on Github repository
> Choose __master branch /docs folder__ as your source to build from and publish your page 
> In your Github Project, create a new folder called docs and add the code from svg-gauges into that folder, and then push the changes to your Github Repository
> If setup correctly, you should be able to navigate according to the URL to something similar to https://username.github.io/#PROJECTNAME/svg-gauge/dist/gauges.js 

- In your __base.html__ file, add your new URL as a javascript source 

- In addition, in your base.html file, modify the style of the gauge with the following code:

    ```html
    <style>
    /** 
      * Gauge Styling
      * Check out https://codepen.io/anon/pen/WPEbGe and https://github.com/naikus/svg-gauge for more info
      */
    .gauge-container>.gauge>.dial {
      stroke: #ABB2AC;
      stroke-width: 10;
    }

    .gauge-container>.gauge>.value {
      stroke: #73C2E5;
      stroke-dasharray: none;
      stroke-width: 10;
    }

    .gauge-container>.gauge>.value-text {
      fill: #D78730;
      transform: translate3d(20%, 23%, 0);
      display: inline-block;
    }

    .gauge-container>.value-text {
      color: #D78730;
      font-weight: 100;
      font-size: 1.5em;
      position: absolute;
      bottom: 10%;
      right: 15%;
      display: inline-block;
      font-family: Arial, Helvetica, sans-serif;
    }

    .gauge-container>.label {
      position: absolute;
      right: 0%;
      top: 0%;
      display: inline-block;
      background: rgba(255, 255, 255, 0);
      font-family: Arial, Helvetica, sans-serif;
      font-size: 0.7em;
      color: #0C5784; 
    }
    </style>
    ```

- The _gauge dial_ refers to the background dial
- The _gauge value_ refers to the colored value fill for the dial 
- The _gauge value-text_ refers to the displayed number corresponding to the colored value fill for the dial 
- The _value-text_ refers to the text beneath the value, in our example kWh
- The _label_ refers to the label on the upper right hand corner 

## Connecting to an Azure SQL server 

- To being migrating the project from a localhost to the cloud, we need to first set up and connect to a Cloud Database, which we chose to be __Azure SQL__
- This section will walk through the following steps: 
    1. Creating a SQL Server
    2. Setting up Firewall 
    3. Testing Connection

### Creating a SQL Server 

- Follow the instructions in the __Create a single database section__ found on [the following tutorial by Microsoft](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-single-database-get-started) as a guide for creating a single database 
- Make sure to keep note of the server name, admin login and password
- Use __Canada Central__ for location and __Basic__ for pricing tier

### Setting up a Firewall

- Once your database is created, follow [these instructions](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-server-level-firewall-rule) to setup a firewall to enable connections 

### Testing Connection

- To start off, we will use the Azure portal to create a table and input a datapoint 
- In your Azure Portal, navigate to your Database's Query Editor and login according to your username and password set when you created the database

![Query Editor](/static/images/azurefig1.png)

- In the Query, add the following code and run it, making sure you get a table returned successfully with the values inserted

<table>
    CREATE TABLE testtable(
        "timestamp" datetime, 
        "value" float
    );

    INSERT INTO testtable(
        "timestamp",
        "value"
    ) VALUES (
        '2019-01-30 12:00:00',
        1.01
    );

    SELECT * FROM testtable; 
</table>

- Now we will try creating a python file to try connecting. We will assume you have a method that returns to you a dataframe with the following 2 columns: timestamp and value
- Make sure you have pandas and pyodbc installed. If not, use `pip install` to add them to your virtual environment

    ```python  
        import pandas as pd 
        import pyodbc 

        # Note that these are all strings
        server = <servername> 
        database =  <databasename>
        username = <username>
        password = <password>
        driver = '{ODBC Driver 13 for SQL Server}' # Depends, check your server information 

        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        cursor = cnxn.cursor()

        cursor.execute('select * from testtable;')
        print(cursor.fetchone())
    ```

![ODBC Driver](/static/images/azurefig2.png)

- You should be able to get the same information as you had from your previous Query in the Azure portal 

- To create a connection with pandas, create a file with the following code

    ```python
        from sqlalchemy import create_engine

        ### Azure SQL Setup (all strings)
        __server = <servername>
        __db = <databasename>
        __uid = <username>
        __pwd = <password>
        __drv = 'ODBC Driver 17 for SQL Server' #note that the { } are dropped 
        __tbl = <tablename> #testtable in our previous example
        __idx = <indexname> #timestamp in our previous example 

        ## Connection Engine
        connectionstring = 'mssql+pyodbc://{uid}:{password}@{server}:1433/{database}?driver={driver}'.format(
            uid=__uid,
            password=__pwd,        
            server=__server,
            database=__db,
            driver=__drv.replace(' ', '+'))    
        cxn = create_engine(connectionstring)
        print("Connected to sql\n")

        df = getDf() #assume you have are returned dataframe with 2 columns: timestamp and value 
        print(df)
        df.to_sql(name = __tbl, con=cxn, if_exists='append', index=False, index_label=__idx)
    ```

- Once you run the file, you should be able to see the df rows appended to your table that you created already in your Azure portal

- To add the cloud server onto your Django Web Platform, you will need to modify the default Database settings in the __settings.py__ file

    ```python 
         'default': {
           'ENGINE': 'sql_server.pyodbc',
           'NAME': '<databasename>',
           'USER': '<username>@myserver', 
           'PASSWORD': '<password>', 
           'HOST': '<servername>', #ie. powertest.database.windows.net
           'PORT': '',
        }
    ```

## Creating a 2 Part Chart 
- This section will walkthrough how to create a chart with both historic/realtime data as well as predicted future + max/min error 
- We will be using Chart.js to implement our chart 
- The main issue with creating these sets of data is the difference in the timestamps (x-axis) and the difference in the number of points. 
    > In order to solve this, we need to create 4 seperate datasets 

        1. Historic/Realtime Data
        2. Predicted Data 
        3. Max error for Predicted Data 
        4. Min error for Predicted Data 

    > Each of these datasets must be the same size and have the same timestamps (x-axis), so we must fill in any missing points with null values 
- The functions below walk through how it was done for the first iteration of the project: 

    ```javascript 
        /**
         * Function updates a Chart without gauges. 
         * @note THIS IS FUNCTION THAT WE WOULD CALL TO RUN THE WHOLE THING
         * @param {Chart} chart Chart object. 
         * @param {string} _url string for URL to obtain historical data in JSON format. 
         * @param {string} pred_url string for URL to obtain predicted data in JSON format. 
         */
        function updateData(chart, _url, pred_url) {
            $.ajax({
                url: _url,
                type: "GET",
                success: function (data) {
                    console.log("polling next point")
                    var result = JSON.parse(data)
                    var date = []
                    var val = []
                    parsedata(date, val, result.data)
                    //Update our EV gauge and Charts
                    updateChart(chart, date, val, pred_url)
                },
                error: function (err_data) {
                    console.log("error", err_data)
                }
            });
        }
        /*--------- The following are all helper functions for updateData() ----------*/
        /**
        * Function that helps us parse our current data. 
        * @note Assumes that the data array is a 2d array where the second dimension corresponds
        * as follows: 
        *  - [0]: date
        *  - [1]: value
        * 
        * @param {Array} date Array of dates
        * @param {Array} val Array of values 
        * @param {Array} data Array of data to be parsed 
        */
        function parsedata(date, val, data) {
            var length = data.length - 1
            for (var x in data) {
                date.push((data[length - x][0]).slice(0, 16))
                val.push(data[length - x][1])
            }
        }
        /**
         * Updates our Chart that has predicted and historic power values. 
         * 
         * @param {Chart} chart Chart object. 
         * @param {Array} timestamps Array of date values.  
         * @param {Array} pwr Array of float values corresponding to power.  
         * @param {string} _url URL to obtain predicted JSON data from.  
         */
        function updateChart(chart, timestamps, pwr, _url) {
            $.ajax({
                url: _url,
                type: "GET",
                success: function (data) {
                    var result = JSON.parse(data)
                    var predicted_date = []
                    var predicted_val = []
                    var predicted_max = []
                    var predicted_min = []
                    parsepredicted(predicted_date, predicted_val, predicted_max, predicted_min, result.data)
                    //Add most recent datapoint into our chart
                    addDataChart(chart, timestamps, pwr, predicted_date, predicted_val, predicted_max, predicted_min)
                },
                error: function (err_data) {
                    console.log("error", err_data)
                }
            });
        }
        /**
        * Function that helps us parse our predicted data 
        * @note Assumes that the data array is a 2d array where the second dimension corresponds
        * as follows: 
        *  - [0]: date
        *  - [1]: value
        *  - [2]: max 
        *  - [3]: min 
        * 
        * @param {Array} date array of dates 
        * @param {Array} val array of values 
        * @param {Array} max array of max error 
        * @param {Array} min array of min error 
        * @param {Array} data Data array to parse 
        */
        function parsepredicted(date, val, max, min, data) {
            var length = data.length - 1
            for (var x in data) {
                date.push((data[length - x][0]).slice(0, 16))
                val.push(data[length - x][1])
                max.push(data[length - x][2])
                min.push(data[length - x][3])
            }
        }
        /**
        * Helper function to update our chart. 
        * 
        * @param {Chart} chart Chart object.
        * @param {Array} curr_x Current/Historical timestamps. 
        * @param {Array} curr_y Current/Historical power values.
        * @param {Array} pred_x Predicted timestamps. 
        * @param {Array} pred_y Predicted power values.
        * @param {Array} pred_max Predicted maximum error value. 
        * @param {Array} pred_min Predicted minimum error value. 
        * 
        */
        function addDataChart(chart, curr_x, curr_y, pred_x, pred_y, pred_max, pred_min) {
        
            //create the new arrays that will have null values so that total sizes are equal to the label size 
            var timestamp = curr_x.slice(0)
            var val = curr_y.slice(0)
            var predictedval = []
            var predictedmax = []
            var predictedmin = []
            formatpredicted(curr_x, pred_x, pred_y, pred_max, pred_min, timestamp, val, predictedval, predictedmax, predictedmin)

            chart.data.datasets[0].data = val
            chart.data.datasets[1].data = predictedval
            chart.data.datasets[2].data = predictedmax
            chart.data.datasets[3].data = predictedmin
            chart.data.labels = timestamp
            chart.update();
        }
    ```

- What is done in the code is essentially going through and creating datasets of the same size, and filling out the missing datapoints with the correct timestamp and a null value. The data is pulled from 2 different URL's which are sent the data in a JSON string format. 
- The chart is created by just using 4 datasets when creating it, and setting different color, fill and styling values: 

    ```javascript 
        /**
        * Creates a chart for either building or ev along with predicted values. 
        * 
        * @param {Array} dates Array of dates for our chart. 
        * @param {Array} pwr_vals Array of power for our chart.
        * @param {Array} future_pwr Array of future values for our chart. 
        * @param {Array} maxerr_pwr Array of max error for future values.
        * @param {Array} minerr_pwr Array of min error for future values.
        * @param {string} id HTML element id. 
        * @param {string} lbl_title Title of the chart.
        * @param {string} x_axis Title for x-axis of the chart.
        * @param {string} y_axis Title for y-axis of the chart. 
        * @param {string} _lbl Label for our main data series. 
        * 
        * @returns {Chart} Chart object. 
        */
        function createChart(dates, pwr_vals, future_pwr, maxerr_pwr, minerr_pwr, id, _title, x_axis, y_axis, _lbl) {
            var ctx = document.getElementById(id).getContext('2d');


            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: dates,
                    datasets: [{
                        label: _lbl,
                        data: pwr_vals,
                        spanGaps: false,
                        backgroundColor: 'rgba(155, 194, 229, 0.4)',
                        borderColor: '#73C2E5',
                        fill: false,
                    }, {
                        label: 'Predicted Values',
                        data: future_pwr,
                        spanGaps: false,
                        backgroundColor: 'rgba(155, 194, 229, 0.4)', // rgba(215, 135, 48, 0.4)'
                        borderColor: '#73C2E5',
                        fill: false,
                        borderDash: [10, 10]
                    }, {
                        label: 'Max Error',
                        data: maxerr_pwr,
                        spanGaps: false,
                        backgroundColor: 'rgba(155, 194, 229, 0.4)',
                        borderColor: '#D78730',
                        borderWidth: 1,
                        fill: '-1',
                        pointRadius: 0,
                    }, {
                        label: 'Min Error',
                        data: minerr_pwr,
                        spanGaps: false,
                        backgroundColor: 'rgba(155, 194, 229, 0.4)',
                        borderColor: '#D78730',
                        borderWidth: 1,
                        fill: '-2',
                        pointRadius: 0,
                    }]
                },
                options: {
                    title: {
                        display: true,
                        text: _title,
                        fontColor: '#0C5784',
                        fontSize: 25,
                    },
                    scales: {
                        xAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: x_axis,
                                fontColor: '#0C5784',
                                fontSize: 20
                            },
                            ticks: {
                                fontColor: '#0C5784'
                            },
                            gridLines: {
                                color: '#0C5784',
                                display: true
                            }
                        }],
                        yAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: y_axis,
                                fontColor: '#0C5784',
                                fontSize: 20,
                            },
                            ticks: {
                                beginAtZero: true,
                                fontColor: '#0C5784'
                            },
                            gridLines: {
                                color: '#0C5784',
                                display: true
                            }
                        }],
                    },
                    legend: {
                        labels: {
                            fontColor: '#0C5784'
                        }
                    },
                }
            });
            return myChart
        }
    ```