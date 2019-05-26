# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:03:09 2019

@author: mss2015
"""

import numpy as np
import pandas as pd
df = pd.read_csv("Automobile.csv")
df['price'] = df['price'].fillna(df['price'].mean())
df1=df['price']
nparrary=np.array(df1)
print("min is {}".format(np.min(nparrary)))
print("max is {}".format(np.max(nparrary)))
print("std is {}".format(np.std(nparrary)))