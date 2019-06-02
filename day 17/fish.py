
# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Importing the dataset
dataset = pd.read_csv('bluegills.csv')
labels = dataset.iloc[:, 1:].values
features = dataset.iloc[:, 0:-1].values
plt.scatter(features, labels)
# not liner so use polly
from sklearn.linear_model import LinearRegression
#lin_reg_1 = LinearRegression()
#lin_reg_1.fit(features, labels)
#plt.scatter(features, labels, color = 'red')
#plt.plot(features, lin_reg_1.predict(features), color = 'blue')

from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)


lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)

# Visualising the Polynomial Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')

x=np.array(5).reshape(1,-1)
x=poly_object.transform(x)
lin_reg_2.predict(x)