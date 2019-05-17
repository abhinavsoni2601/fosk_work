# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:17:00 2019

@author: DELL
"""
str2=''
var=0
str1=input('enter the name of txt file')
str1=str1+'.txt'
with open(str1,'rt')as file1:
    while True:
        str2=file1.readline()
        if not str2:
            break
        str3=str2
print(str3)
#    file1.seek(0,2)
#    print(file1.read())