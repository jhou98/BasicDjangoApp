import mysql 
import csv
from mysql import connector 
import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# Base directory of our project, used to get files 
__base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def createNewTable( name ):
    """
    newMonthlyTable will connect to our basic database and create a new table, if table already exists nothing is modified. \n
    :param str name: The name of the table we wish to create \n
    The Structure of the table will have the following columns: 
        id - INT, will be automatically generated 
        date - DATE in YYYY-MM-DD format 
        96 timestamps at increments of 15 minutes - kW or kWh in Decimal values, up to 99999.999
    """

    # Establishes a new connection to our mySQL db located at localhost:3306 
    # Update this method according to the database setup 
    myconnection = connector.MySQLConnection(user='root',password='Cerc@2019',database='basic')
    mycursor = myconnection.cursor()

    # Executes a new CREATE TABLE 
    mycursor.execute(__createTable(name))


def __createTable( name ):
    """
    Hidden helper function that will return the Script in a string for creating a table
    :param str name: Name of the table we wish to create 
    """

    return "CREATE TABLE IF NOT EXISTS " + name + " (id INT AUTO_INCREMENT PRIMARY KEY, date DATE,\
            `00:00` DECIMAL(8,3), `00:15` DECIMAL(8,3), `00:30` DECIMAL(8,3), `00:45` DECIMAL(8,3),\
            `01:00` DECIMAL(8,3), `01:15` DECIMAL(8,3), `01:30` DECIMAL(8,3), `01:45` DECIMAL(8,3),\
            `02:00` DECIMAL(8,3), `02:15` DECIMAL(8,3), `02:30` DECIMAL(8,3), `02:45` DECIMAL(8,3),\
            `03:00` DECIMAL(8,3), `03:15` DECIMAL(8,3), `03:30` DECIMAL(8,3), `03:45` DECIMAL(8,3),\
            `04:00` DECIMAL(8,3), `04:15` DECIMAL(8,3), `04:30` DECIMAL(8,3), `04:45` DECIMAL(8,3),\
            `05:00` DECIMAL(8,3), `05:15` DECIMAL(8,3), `05:30` DECIMAL(8,3), `05:45` DECIMAL(8,3),\
            `06:00` DECIMAL(8,3), `06:15` DECIMAL(8,3), `06:30` DECIMAL(8,3), `06:45` DECIMAL(8,3),\
            `07:00` DECIMAL(8,3), `07:15` DECIMAL(8,3), `07:30` DECIMAL(8,3), `07:45` DECIMAL(8,3),\
            `08:00` DECIMAL(8,3), `08:15` DECIMAL(8,3), `08:30` DECIMAL(8,3), `08:45` DECIMAL(8,3),\
            `09:00` DECIMAL(8,3), `09:15` DECIMAL(8,3), `09:30` DECIMAL(8,3), `09:45` DECIMAL(8,3),\
            `10:00` DECIMAL(8,3), `10:15` DECIMAL(8,3), `10:30` DECIMAL(8,3), `10:45` DECIMAL(8,3),\
            `11:00` DECIMAL(8,3), `11:15` DECIMAL(8,3), `11:30` DECIMAL(8,3), `11:45` DECIMAL(8,3),\
            `12:00` DECIMAL(8,3), `12:15` DECIMAL(8,3), `12:30` DECIMAL(8,3), `12:45` DECIMAL(8,3),\
            `13:00` DECIMAL(8,3), `13:15` DECIMAL(8,3), `13:30` DECIMAL(8,3), `13:45` DECIMAL(8,3),\
            `14:00` DECIMAL(8,3), `14:15` DECIMAL(8,3), `14:30` DECIMAL(8,3), `14:45` DECIMAL(8,3),\
            `15:00` DECIMAL(8,3), `15:15` DECIMAL(8,3), `15:30` DECIMAL(8,3), `15:45` DECIMAL(8,3),\
            `16:00` DECIMAL(8,3), `16:15` DECIMAL(8,3), `16:30` DECIMAL(8,3), `16:45` DECIMAL(8,3),\
            `17:00` DECIMAL(8,3), `17:15` DECIMAL(8,3), `17:30` DECIMAL(8,3), `17:45` DECIMAL(8,3),\
            `18:00` DECIMAL(8,3), `18:15` DECIMAL(8,3), `18:30` DECIMAL(8,3), `18:45` DECIMAL(8,3),\
            `19:00` DECIMAL(8,3), `19:15` DECIMAL(8,3), `19:30` DECIMAL(8,3), `19:45` DECIMAL(8,3),\
            `20:00` DECIMAL(8,3), `20:15` DECIMAL(8,3), `20:30` DECIMAL(8,3), `20:45` DECIMAL(8,3),\
            `21:00` DECIMAL(8,3), `21:15` DECIMAL(8,3), `21:30` DECIMAL(8,3), `21:45` DECIMAL(8,3),\
            `22:00` DECIMAL(8,3), `22:15` DECIMAL(8,3), `22:30` DECIMAL(8,3), `22:45` DECIMAL(8,3),\
            `23:00` DECIMAL(8,3), `23:15` DECIMAL(8,3), `23:30` DECIMAL(8,3), `23:45` DECIMAL(8,3))"

'''
def __insertMany(name):
    """
    Hidden helper function that will insert multiple rows into our main table format 
    :param str name: Name of table to insert data 
    """

    sqlquery = "INSERT INTO " + name + " (date, `00:00`, `00:15`, `00:30`, `00:45`,\
                `01:00`, `01:15`, `01:30`, `01:45`,\
                `02:00`, `02:15`, `02:30`, `02:45`,\
                `03:00`, `03:15`, `03:30`, `03:45`,\
                `04:00`, `04:15`, `04:30`, `04:45`,\
                `05:00`, `05:15`, `05:30`, `05:45`,\
                `06:00`, `06:15`, `06:30`, `06:45`,\
                `07:00`, `07:15`, `07:30`, `07:45`,\
                `08:00`, `08:15`, `08:30`, `08:45`,\
                `09:00`, `09:15`, `09:30`, `09:45`,\
                `10:00`, `10:15`, `10:30`, `10:45`,\
                `11:00`, `11:15`, `11:30`, `11:45`,\
                `12:00`, `12:15`, `12:30`, `12:45`,\
                `13:00`, `13:15`, `13:30`, `13:45`,\
                `14:00`, `14:15`, `14:30`, `14:45`,\
                `15:00`, `15:15`, `15:30`, `15:45`,\
                `16:00`, `16:15`, `16:30`, `16:45`,\
                `17:00`, `17:15`, `17:30`, `17:45`,\
                `18:00`, `18:15`, `18:30`, `18:45`,\
                `19:00`, `19:15`, `19:30`, `19:45`,\
                `20:00`, `20:15`, `20:30`, `20:45`,\
                `21:00`, `21:15`, `21:30`, `21:45`,\
                `22:00`, `22:15`, `22:30`, `22:45`,\
                `23:00`, `23:15`, `23:30`, `23:45`) \
                VALUES ()"  
'''

def readCSV(pathtofile):
    """
    Read and prints our csv file using csv reader 
    """
    with open(__base+pathtofile) as csvfile: 
        readCSV = csv.reader(csvfile, delimiter=',')
        print(readCSV)

        for row in readCSV:
            print(row)

def readToDataframe(pathtofile, sheetval, opt): 
    """
    Uses Pandas to read a xlsx file to a dataframe object 
    :param str pathtofile: Path to file from our projects base directory
    :param boolean opt: If TRUE, we have a 2d matrix, \
    OTHERWISE we have a 2 column list. 
    """
    df = pd.read_excel(__base+pathtofile, sheetname=sheetval)
    print("Finished reading excel")

    # If/Else loop 
    if opt == True:
        print("Column Headings: ")
        print(df.columns)
    else: 
        date_column = df['Timestamp']
        power_column = df['Power Demand EV parkade (kW)']
        print(date_column)
        print(power_column)

