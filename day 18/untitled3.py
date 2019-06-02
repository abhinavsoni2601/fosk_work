# -*- coding: utf-8 -*-
"""
Created on Wed May 29 18:37:19 2019

@author: User
"""


import pandas as pd
import numpy as np
database = pd.read_csv('tree_addhealth.csv', sep=',', header=0)  
database.isnull().any()
database.dropna()
labels = database.iloc[:,7].values 
features = database.iloc[:,[0,1,2,3]].values
#gender, age, (race/ethnicity) Hispanic, White, Black, Native American and Asian, alcohol use,
# alcohol problems, marijuana use
#, cocaine use, inhalant use, availability of cigarettes in the home, depression, and self-esteem