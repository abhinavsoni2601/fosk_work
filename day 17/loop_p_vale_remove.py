
# Importing the libraries
import pandas as pd
import numpy as np
# Importing the dataset
#dataset = pd.read_csv('Female_Stats.csv')
#
#labels = dataset.iloc[:, 0:1].values
#features = dataset.iloc[:, 1:].values
#featuresfather=dataset.iloc[:,[2]].values
#featuresmother=dataset.iloc[:,:[1]].values

# Importing the libraries

# Importing the dataset
dataset = pd.read_csv('iq_size.csv')

labels = dataset.iloc[:, 0:1].values
features = dataset.iloc[:, 1:].values


import statsmodels.api as sm
features = sm.add_constant(features)
list2=[]
list1=[0,1,2,3]
while True:
    features_opt = features[:,list1]
    regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
    list2=regressor_OLS.pvalues
    list2-=list2[0]
    temp=np.max(list2)
    temp2=np.argmax(list2)
    if temp>0.08:
        list1.pop(temp2)
        
        
    else:
        break
print(list1)