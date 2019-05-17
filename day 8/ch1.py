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
    
    
 

import pandas as pd
from collections import OrderedDict
list7=['Team','Weighted Matches','Points' ,'Rating']
data=OrderedDict(zip(list7,[list2,list3,list4,list5]))
df = pd.DataFrame(data) 
df.to_csv("icc.csv")



