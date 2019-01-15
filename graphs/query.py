import mysql 
import csv
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
    Uses Pandas to read a csv file to a dataframe object 
    :param str pathtofile: Path to file from our projects base directory
    :param str tablename: Name of the table we wish to input data into. \
    IF tablename exists, it will be replaced
    """
    df = pd.read_csv(__base+pathtofile)
    
    print("Finished reading csv")
    print(df)
    
    engine = create_engine('mysql+mysqlconnector://'+ __user + ':' + __passw + '@' + __host + ':' + __port + '/' + __schema, echo=False)
    print("Connected to mysql\n")

    df.to_sql(con=engine, name=tablename, if_exists='replace')

    

