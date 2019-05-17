# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:03:57 2019

@author: abhin
"""



import sqlite3
from pandas import DataFrame
coonect1=sqlite3.connect("univercity.db")
curser1=coonect1.cursor()
curser1.execute ("""CREATE TABLE univercity(
          Student_Name TEXT,
          Student_Age INTEGER, 
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )""")
curser1.execute("INSERT INTO univercity VALUES ('abhi',20,1,'cse')")
curser1.execute("INSERT INTO univercity VALUES ('abhi2',21,2,'cse')")
curser1.execute("INSERT INTO univercity VALUES ('abhi3',23,3,'cse')")
curser1.execute("INSERT INTO univercity VALUES ('abhi4',25,1,'it')")
curser1.execute("SELECT * FROM univercity")
df = DataFrame(curser1.fetchall())
df.columns=["Student_Name", "Student_Age", "Student_Roll_no", "Student_Branch"]
coonect1.commit()
coonect1.close()

