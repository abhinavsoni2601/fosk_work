
# Importing the libraries
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('Female_Stats.csv')

labels = dataset.iloc[:, 0:1].values
features = dataset.iloc[:, 1:].values
#featuresfather=dataset.iloc[:,[2]].values
#featuresmother=dataset.iloc[:,:[1]].values

import statsmodels.api as sm
features = sm.add_constant(features)
features_opt = features[:,[0,1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.pvalues
regressor_OLS.summary()
features=features[:,[1,2]]

from sklearn.linear_model import LinearRegression
reg_1 = LinearRegression()
reg_1.fit(features, labels)
reg_1.coef_