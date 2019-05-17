import requests
from bs4 import BeautifulSoup  as bs
url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
str1=requests.get(url).text
str2=bs(str1,'lxml')
table=str2.find('table',class_='table')
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]

for x in table.findAll('tr') :
    cell=x.findAll('td')
    if (len(cell) == 5):
        list2.append(cell[1].text.strip())
        list3.append(cell[2].text.strip())
        list4.append(cell[3].text.strip())
        list5.append(cell[4].text.strip())
    
    
 
list9=list(zip(list2,list3,list4,list5))

import sqlite3
from pandas import DataFrame
coonect1=sqlite3.connect("icc.db")
#curser1.execute("DROP Table icc;")
curser1=coonect1.cursor()
curser1.execute ("""CREATE TABLE icc(
          list2 TEXT,
          list3 TEXT, 
          list4 TEXT,
          list5 TEXT
          )""")
for i in list9:
    curser1.execute("INSERT INTO icc VALUES {}".format(i))

curser1.execute("SELECT * FROM icc")
df = DataFrame(curser1.fetchall())
coonect1.commit()
coonect1.close()
