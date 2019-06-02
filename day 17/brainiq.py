# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:59:10 2019

@author: User
"""

# Importing the libraries
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('iq_size.csv')

labels = dataset.iloc[:, 0:1].values
features = dataset.iloc[:, 1:].values

from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)

x=[90,70,150]
import numpy as np
x=np.array(x, dtype=np.float64)
x=x.reshape(1,-1)
lin_reg_1.predict(x)

import statsmodels.api as sm
features = sm.add_constant(features)


features_opt = features[:, [0, 1, 2, 3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.pvalues


features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.pvalues
regressor_OLS.summary()

features_opt = features[:, [1, 2]]
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features_opt, labels)

x=[90,70]
import numpy as np
x=np.array(x, dtype=np.float64)
x=x.reshape(1,-1)
lin_reg_1.predict(x)