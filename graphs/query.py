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
    :param str tablename: Name of the table we wish to input data into. \
    IF tablename exists, it will fail
    """
    df = pd.read_csv(__base+pathtofile)
    
    print("Finished reading csv")
    print(df)
    
    engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)
    print("Connected to mysql\n")

    df.to_sql(con=engine, name=tablename, if_exists='fail')

def updateTable(pathtofile, tablename):
    """
    Updates a table in our database by appending the new data into the table \n
    :param str pathtofile: Path to file from our projects base directory \n
    :param str tablename: name of table to input data. \
    IF tablename exists, we will append the data to the bottom \
    OTHERWISE it will create a new table 
    """
    df = pd.read_csv(__base+pathtofile)
    
    print("Finished reading csv")
    print(df)
    
    engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)
    print("Connected to mysql\n")

    df.to_sql(con=engine, name=tablename, if_exists='append')

def replaceTable(pathtofile, tablename): 
    """
    Uses Pandas to read a csv file to a dataframe object and stores it into our database \n
    :param str pathtofile: Path to file from our projects base directory \n
    :param str tablename: Name of the table we wish to input data into. \
    IF tablename exists, it will be replaced with the new data
    """
    df = pd.read_csv(__base+pathtofile)
    
    print("Finished reading csv")
    print(df)
    
    engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)
    print("Connected to mysql\n")

    df.to_sql(con=engine, name=tablename, if_exists='replace')
    
def baseData(tablename):
    """
    Reads the raw data and returns it \n
    :param str tablename: Name of table to be opened in our basic db \n
    Returns the dataframe created by pandas of our table    
    """
    engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)

    df = pd.read_sql_table(con=engine, table_name=tablename)
    print(df)
    return df
    

