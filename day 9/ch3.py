# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:14:01 2019

@author: abhin
"""
from pandas import DataFrame

import mysql.connector 
connection = mysql.connector.connect(user='a9462567025', password='abhinav@123', host='db4free.net', database = 'databasename1')
curser1 = connection.cursor()

curser1.execute ("""CREATE TABLE calen3(
        BID_NO INTEGER, 
        items INTEGER,
        Quantity_Required TEXT,
        Department_Name_And_Address TEXT,
        Start INTEGER,
        End INTEGER
          )""")
curser1.execute("INSERT INTO calen3 VALUES (12,32,'qw','sdf',234,345)")
curser1.execute("INSERT INTO calen3 VALUES (132,322,'qw','sdf',2334,3453)")

curser1.execute("SELECT * FROM calen3")
df = DataFrame(curser1.fetchall())
df.columns=[' BID NO',
           'items',
          ' Quantity Required',
          ' Department Name And Address',
          ' Start Date/Time(Enter date and time in different columns)',
          ' End Date/Time(Enter date and time in different columns)']
connection.commit()