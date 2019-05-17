# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:43:43 2019

@author: abhin
"""

import pymongo
client=pymongo.MongoClient("mongodb://abhinav123:abhinav123@cluster0-shard-00-00-a8btm.mongodb.net:27017,cluster0-shard-00-01-a8btm.mongodb.net:27017,cluster0-shard-00-02-a8btm.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
mydb = client.univercity
def add_stu(name,age,roll,branch):
    
    mydb.univercity.insert_one(
            {
           'Student_Name': name,
          'Student_Age': age, 
          'Student_Roll_no': roll,
          'Student_Branch': branch})
    return "Employee added successfully"
add_stu('abhi',20,1,'cse')
add_stu('abhi2',21,2,'cse')
add_stu('abhi3',23,3,'cse')
add_stu('abhi4',25,1,'it')
user = mydb.univercity.find()
for i in user:
    print (i)
