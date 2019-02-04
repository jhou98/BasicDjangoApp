# Basic Django App 
- A basic application in Django and Python that will connect to a local mySQL server to output data regarding electrical consumption for EV and Buildings at UBC. 
- This file will go over the essentials of application. For more details and django setup, check out [Walkthrough](Walkthrough.md) and [Django Documentation](https://docs.djangoproject.com/en/2.1/)
- Our project follows the Model View Controller Structure(MVC), where there are three main components: Model, View, and Controller. 
    > __Model__: The Model component defines the data objects and its fields and behaviour <br>
    > __View__: View component is used for UI logic and whatever the user interacts with <br>
    > __Controller__: The Controller component acts as an interface between the Model and View to process all logic and requests, manipulate the data from the Model and interact with our View to render the final results. <br>

[Part 1 - Models](#Models) 
------
[Part 2 - Views](#Views) 
------
[Part 3 - Controller](#Controller)
------
[Part 3 - Database](#Database) 
------
[Part 4 - Graphs](#Graphs) 
------


## Models 
- Assume you have your main project called __basic__ and you want to add a model to your app called __graphs__
### Creating a Model
- In the `graphs.models.py`, make sure to add `from django.db import models` so that models can be used 
- Create a model using `class %modelname%(models.Model):` and adding methods and variables to the model 
### Linking a Model to the Database
- In the `graphs.admin.py` file, add your newly created model with the following lines of code: <br>
    ```python
    from .models import %modelname%`
    admin.site.register(%modelname%)`
    ```
- Make sure in your `graphs.apps.py` file you have everything configured like so: <br>
    ```python
    from django.apps import AppConfig

    class GraphsConfig(AppConfig):
        name = 'graphs'
    ```

- In your `main.settings.py` file, check the `INSTALLED_APPS` to see if you have the graphs application path on the project.
> If not, add `'graphs.apps.GraphsConfig'` to the list 
- In the command shell, navigate to the top level project folder where __manage.py__ is and run the following commands to migrate the model changes into the server.
    <table>

        python manage.py makemigrations
        python manage.py migrate
    </table>

- Check your database to make sure a new table has been created named __graphs.%modelname%__
<br> [Back to Top](#Basic-Django-App)
## Views 
### Creating a view 
- In `graphs.views.py` you can create a new view just like creating a new method in python. Have the following imports at the top of your file: 
    ```python
    from django.shortcuts import render
    from django.http import HttpResponse, Http404
    ```

- Below, I have a view called index(request, **args) which returns a render
    > render(request, HTML template that we are sending the render to, {reference name: python functions we want to use}) <br>
    > this index function will store the sum of all the arguments into __'reference'__
    ```python
    def index(request, **args):
       
        answ = args1 + args2 + ...
        return render(request, 'index.html', {'reference':answ})
    ```

### Adding the view to HTML template
- Using the example above, in `index.html`, if you wish to call upon the python function use `{{reference}}`
    ```HTML
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
    ```

### Creating a URL path 
- Now that your view and template pages are linked, you will need to setup a URL path to access this new view 
- In `graphs.urls.py` add the path to your `url patterns[]`
    > The first argument will be the path you need to enter to get to your view from localhost <br>
    > The second argument `views.index` tells you which view you are accessing <br>
    > The last argument is a reference that you can call upon as a shortcut to the path 
    ```python
     path('index/<args1>/<args2>/....',views.index, name='index')
    ```

<br>[Back to Top](#Basic-Django-App)
## Controller
- In your __graphs__ folder, you will create a new python file called __controller.py__, where it will store the communication and queries for the database and model to our views 
### Accessing Models
- Django models provides a easy way to access our database without queries
> Assume we have a created and migrated a model named __powerdata__ for our project
> Our model has a datetime field called _Timestamp_ and we wish to generate a list ordered by this field 
    ```python
        def getDateList():
            from .models import powerdata
            data_list = powerData.objects.order_by('-Timestamp')
            return data_list
    ```

- By importing our powerdata model, we are able to access our data directly 
- However, there are limitations for this method including how you can structure the data being returned and how you can query the data, hence you may need to access the database directly instead

### Accessing Database 
- To access the database, we will be using the __pandas__ package for dataframes and __sqlalchemy__ package for creating an connection engine, which you will need to `pip install` 
- Let us use the same example as before, ordering the powerdata model by date
    ```python
        from sqlalchemy import create_engine
        import pandas as pd
        def getDateData(tablename, col):
            """
            Reads and returns the recent data \n
            :param str tablename: Name of table to be opened \n
            :param str col: Name of column in database to be ordered by \n
            Returns a dataframe of our data
            """ 
            engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)

            #sql query to select specific dates 
            my_query = "SELECT * FROM " + \
                        tablename + \
                        " ORDER BY " + col + " DESC"
            df = pd.read_sql_query(sql = my_query, con=engine)
            return df
    ```

- In the code block above, when we call the function in our __views.py__ file we would have `'graphs_powerdata'` in our _tablename_ and `'Timestamp'` in our _col_
> __user, __passw, __host, __port, __schema are all database variables that you will need to define in your controller
- As you can see in the above example, there is more code required for accessing the database, as well as more dependencies. However, it does allow for more flexibility with your queries, since you can basically do any SQL query as long as you input it into the my_query variable  

<br>[Back to Top](#Basic-Django-App)

## Database 
### Creating a new table 
- Walkthrough of setting up a MySQL database and adding data to the table 
- To start off, create a new MySQL server and save the settings into the DATABASES in __settings.py__ 
- To create a table, we simply need to create a new model class and migrate the class to our database. Create the following model and follow the steps in Part 1 to link it to our database. 
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
        return "Date: " + self.Timestamp.strftime("%m/%d/%y %H:%M:%S") + "  Power: " + str(self.Power)
    ```

- In your database, you should now be able to see a new empty table along the names of __graphs_powerdata__ with 3 fields: 
    1. index 
    2. Timestamp
    3. Power

### Using Pandas to add data to your table 
- There are multiple different ways to update the new table in your MySQL database. However, the way we will be doing it will be using the pandas package to read a CSV file and inserting the values into our table. The advantage of this is pandas makes it easy and fast to update and insert large amounts of data into our database. 
- Therefore, in our `controller.py` file, add the following function for pandas 
    ```python
    import mysql 
    from mysql import connector
    from sqlalchemy import create_engine
    import os
    import pandas as pd
    from pandas import ExcelWriter
    from pandas import ExcelFile

    # Base directory of our project, used to get files 
    __base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Database variables
    __user = ##username 
    __passw = ##password
    __schema= ##server
    __host = ##host
    __port = ##port

    def updateTable(pathtofile, tablename):
        """
        Updates a table in our database by appending the new data into the table \n
        :param str pathtofile: Path to file from our projects base directory \n
        :param str tablename: name of table to input data. \n
        IF tablename exists, we will append the data to the bottom \
        OTHERWISE it will create a new table 
        """
        df = pd.read_csv(__base+pathtofile)
        
        print("Finished reading csv")
        print(df)
        
        engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)
        print("Connected to mysql\n")

        df.to_sql(con=engine, name=tablename, if_exists='append', index=False, index_label = 'index')
    ```

- The `updateTable` function will add new points to the table corresponding to the _tablename_ and will not modify any previous values already in the table 
    > We can also change the functionality by modifying the `if_exists` parameter to either _'fail'_ or _'replace'_ if we wish to have our function fail if the table already exists (creating a new table) or replace the old table data with our new data 
- Now we can run a python shell and call this command to insert data into our table. Make sure to store the csv file somewhere within project folder so you can navigate to it, and that the column names correspond to the fields we created in our models class. 
    <table>

        python manage.py shell 
        >>>from graphs import controller as c 
        >>>c.updateTable(//pathtofile, 'graphs_powerdata')
    </table>

- Afterwards, if you connected everything correctly, you should be able to see the new data in both your MySQL connector and your Django admin page on localhost:8000/admin
<br>[Back to Top](#Basic-Django-App)

## Graphs 
- This section will go over how to create a graph using Chart.js 
- This section assumes you have a base template called `base.html` which your other HTML templates extend using `{% extends 'base.html' %}` and `controller.py` file for working with the data 
- For this section, we will be using the the __powerData__ model that we went over in part 3 under the __graphs app__
### Getting Data in JSON format 
- In order for Chart.js to work, we need to have our data formatted into a JSON object 
    > Have [django rest framework](https://www.django-rest-framework.org/) installed and added to the INSTALLED_APPS in __settings.py__ <br>
    > Add [the script for chart.js](https://cdnjs.com/libraries/Chart.js) to your template 
- In __controller.py__, create a python function that gets a number of the latest data from the powerData model in the database 
    ```python
    import pandas as pd

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

- Since the function above only returns a dataframe and not a JSON, we need to add another functon in __controller.py__ 
    ```python
    def pandasToJSON(df):
    """
    Converts a dataframe into a JSON string 
    """
    return df.to_json(date_format='iso', orient='split')
    ```

- Now that you have created 2 functions that will help query data from our MySQL database and convert it into a JSON string, we can create a class in __views.py__ that will use the JSON framework and send 100 data points to our HTML template page 
    ```python
    from django.http import HttpResponse, Http404, JsonResponse
    import pandas as pd 
    from rest_framework.views import APIView
    from rest_framework.response import Response

    # Rest Framework 
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

- Create a new page that uses the django-rest-framework in __urls.py__ 
    ```python
    urlpatterns = [
        path(r'api/data',views.ChartData.as_view(), name='chart' ),
    ]
    ```

- Once saved, run your server and go to http://localhost:8000/api/data and you will be able to view the JSON string that we will work with in our javascript 
### Converting JSON data into a Graph
- At this point, you should be able to view data in a JSON string format at http://localhost:8000/api/data 
- In this section, you will convert that JSON string into a JSON object and graph the object using chart.js into the HTML template 
- In __base.html__ add the following script, which tells us when the page is "ready" to be manipulated safely
    ```HTML
     <!--Custom Scripts-->
    <script> 
      $(document).ready(function(){
        {% block jquery %}{% endblock %}
      })
    ```

- In a new file called __graphs.html__, we will extend our __base.html__ template and run some javascript functions in our jquery block to generate our charts. Make sure to also link the template to a view and url
    ```HTML
    {% extends 'base.html' %}

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
            },
            error: function(err_data){
                console.log("error")
                console.log(err_data)
            }
        });
    {% endblock %}
    </script>
    ```

- Run the code on localhost and navigate to the url corresponding to this view. In the console, you should be able to see the data being printed out in 3 formats: 
    1. A JSON string of all the data 
    2. JSON object of dates 
    3. JSON object of power 
- We will be using the two JSON objects - date and power, for our graph, and passing it through a function that uses chart.js. Add the following function right below our `$.ajax` call within the jquery block. 
    ```javascript
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
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
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
    ```

- Add the following line of code to the success function(data) in our `$.ajax` call so that we use our newly created function `createEVChart`
    ```javascript
    //calls our function on success 
    createEVChart(date,power) 
    ```
- In addition, in our HTML body, we need to create the element and format it so that it will display onto the web page. 
    ```HTML
    <div class='container'>
            <canvas id="myChartEV" width="400" height="400"></canvas>
    </div>
    ```
<br> [Back to Top](#Basic-Django-App)
