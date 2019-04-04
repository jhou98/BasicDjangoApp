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
__user = 'root'
__passw = 'Cerc2019'
__schema= 'basic'
__host = 'localhost'
__port = '3306'

def createNewTable(pathtofile, tablename): 
    """
    Uses Pandas to read a csv file to a dataframe object and stores it into our database \n
    :param str pathtofile: Path to file from our projects base directory \n
    :param str tablename: Name of the table we wish to input data into. \n
    IF tablename exists, it will fail
    """
    df = pd.read_csv(__base+pathtofile)
    
    print("Finished reading csv")
    print(df)
    
    engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)
    print("Connected to mysql\n")

    # set index_label to timestamp since this is the AutoField generated by django.models 
    df.to_sql(con=engine, name=tablename, if_exists='fail', index=False, index_label = 'timestamp')

def createSubTable(pathtofile, tablename, cols):
    """
    Uses Pandas to read a csv file to a dataframe object and stores it into our database \n
    :param str pathtofile: Path to file from our projects base directory \n
    :param str tablename: Name of the table we wish to input data into. \n
    :param list cols: List of columns to specifically use ie. ['Timestamp', 'Power'] \n
    IF tablename exists, it will fail
    """
    df = pd.read_csv(__base+pathtofile, usecols=cols)
    
    print("Finished reading csv")
    print(df)
    
    engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)
    print("Connected to mysql\n")

    # set index_label to timestamp since this is the AutoField generated by django.models 
    df.to_sql(con=engine, name=tablename, if_exists='fail', index=False, index_label = 'timestamp')        
    

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

    df.to_sql(con=engine, name=tablename, if_exists='append', index=False, index_label = 'timestamp')

def replaceTable(pathtofile, tablename): 
    """
    Uses Pandas to read a csv file to a dataframe object and stores it into our database \n
    :param str pathtofile: Path to file from our projects base directory \n
    :param str tablename: Name of the table we wish to input data into. \n
    IF tablename exists, it will be replaced with the new data
    """
    df = pd.read_csv(__base+pathtofile)
    
    print("Finished reading csv")
    print(df)
    
    engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)
    print("Connected to mysql\n")

    df.to_sql(con=engine, name=tablename, if_exists='replace', index=False, index_label = 'timestamp')


def getBaseData(tablename):
    """
    Reads the raw data and returns it \n
    :param str tablename: Name of table to be opened in our basic db \n
    Returns the dataframe created by pandas of our table    
    """
    engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)

    df = pd.read_sql_table(con=engine, table_name=tablename)
    return df

def getDateData(tablename, timecol, startdate, enddate):
    """
    Reads raw data according to the date and returns it \n
    :param str tablename: Name of table to be opened \n
    :param str timecol: Name of the Date column \n
    :param DateTime startdate: Start date we want to select data from \n
    :param DateTime enddate: End date we want to select data from \n
    Returns a dataframe of our table 
    """
    engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)

    #sql query to select specific dates 
    my_query = "SELECT * FROM " + \
                tablename + \
                " WHERE " + timecol + " >= " + "'" + startdate + "'" + \
                " AND " + timecol + " <= "+ "'" + enddate + "'"

    df = pd.read_sql_query(sql = my_query, con=engine)
    return df

def getSingleDateData(tablename, timecol, dateval):
    """
    Reads and returns all the data for a single date 
    :param str tablename: Name of table to be opened \n
    :param str timecol: Name of Date column \n
    :param Datetime dateval: Date to extract data from \n
    Returns a dataframe of our data 
    """
    
    start_date = dateval+' 00:00:00'
    end_date = dateval+' 23:45:00'
    
    # Call the dateData method to create a dataframe for our specified date
    df = getDateData(tablename,timecol,start_date,end_date)
    return df

def getCurrentPower(tablename, timecol, powercol):
    """
    Reads and returns the most recent power reading
    :param str tablename: Name of table to be opened \n
    :param str timecol: Name of time column \n
    :param str powercol: Name of the power column \n
    Returns a decimal power value 
    """
    df = getRecentData(tablename, 1, timecol)
    if df.empty:
        return 0
    return df.at[0, 'value']

def getDailyPeak(tablename, timecol):
    """
    Reads and returns the peak power for yesterday
    :param str tablename: Name of table to be opened \n
    :param str timecol: Name of time column \n
    Returns a decimal power value 
    """
    # Only need the most recent point since we will sample the data we need with another query 
    df = getRecentData(tablename, 1, timecol)

    if df.empty: 
        return 0

    #Calculating the current day 
    curr_year = df.iloc[0].timestamp.year 
    curr_month = df.iloc[0].timestamp.month 
    curr_day = df.iloc[0].timestamp.day 
    prev_day = curr_day-1
    #Calculate the previous day is the end of the previous month
    if curr_day == 1: 
        if (curr_month == 4 or curr_month == 6 or curr_month == 9 or curr_month == 11): 
            #31st is the previous day 
            prev_day = 31
        else: 
            if curr_month == 3: 
                #28th or 29th is the previous day
                if curr_year % 4 == 0: 
                    #Leap Year
                    prev_day = 29
                else: 
                    prev_day = 28
            else: 
                #30th is the previous day
                prev_day = 30
        if curr_month == 1: 
            curr_month = 12
            curr_year = curr_year-1
        else: 
            curr_month = curr_month - 1
    
    date = str(curr_year)+'-'+str(curr_month)+'-'+str(prev_day)
    my_df = getSingleDateData(tablename, timecol, date )
    return my_df.max().value

def getMonthlyPeak(tablename):
    """
    Reads and returns the peak power for the previous month
    :param str tablename: Name of table to be opened \n
    Assumes Timestamp is the name of our date column \n
    Returns a decimal power value 
    """
     # Only need the most recent point since we will sample the data we need with another query 
    df = getRecentData(tablename, 1, 'timestamp')

    if df.empty: 
        return 0 
        
    #Calculating the current month
    curr_year = df.iloc[0].timestamp.year 
    curr_month = df.iloc[0].timestamp.month 

    if curr_month == 1: 
        month = 12
        year = curr_year-1
    else: 
        month = curr_month-1
        year = curr_year
    
    if (month == 4 or month == 6 or month == 9 or month == 11):
        day = 30
    else: 
        if month==2: 
            if year%4==0: 
                day = 29
            else: 
                day = 28 
        else: 
            day = 31 
    
    start = str(year)+'-'+str(month)+'-'+str(1)
    end = str(year)+'-'+str(month)+'-'+str(day)
    my_df = getDateData(tablename, 'timestamp', start, end)
    return my_df.max().value

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

def pandasToJSON(df):
    """
    Converts a dataframe into a JSON string 
    """
    return df.to_json(date_format='iso', orient='split')

def getRecentDataList(num_req):
    """
    Reads and returns a Query list of data from powerdata \n 
    :param int num_req: Number of datapoints to retrieve
    """
    from .models import WestEV
    latest_data_list = WestEV.objects.order_by('-timestamp')[:num_req]
    return latest_data_list

def getMaxData(num_req):
    """
    Gets a list of data points ordered by power consumption \n
    :param int num_req: Number of data points to be extracted \n
    """
    from .models import WestEV 
    latest_data_list = WestEV.objects.order_by('-value')[:num_req]
    return latest_data_list

