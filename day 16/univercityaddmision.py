# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:38:50 2019

@author: User
"""

import numpy as np
import pandas as pd
dataset = pd.read_csv('University_data.csv')  
print(dataset.info())
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, -1:].values 
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels)



x = ["Cabrini",337,1.5,2.3,9.0,0]
x = np.array(x).reshape(1,-1)
x[:,0] = labelencoder.transform(x[:,0])
x = onehotencoder.transform(x).toarray()
x = x[:,1:]
regressor.predict(x)