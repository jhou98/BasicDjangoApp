"""
    Test file for connecting to Microsoft Azure 
"""

import pandas as pd 
import pyodbc 

server = 'powertest.database.windows.net'
database = 'myTestDatabase'
username = 'azureuser'
password = 'Cerc2019'
driver = '{ODBC Driver 17 for SQL Server}'

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()

cursor.execute('select * from testtable;')
print(cursor.fetchone())

# 'default': {
#   'ENGINE': 'sql_server.pyodbc',
#   'NAME': 'myTestDatabase',
#   'USER': 'azureuser@myserver',
#   'PASSWORD': 'Cerc2019', 
#   'HOST': 'powertest.database.windows.net,
#   'PORT': '',
# }