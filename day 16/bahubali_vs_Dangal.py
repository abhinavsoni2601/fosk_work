import pandas as pd  
import numpy as np  
dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')  
print(dataset.info())
features = dataset.iloc[:, :1].values  
labels = dataset.iloc[:, 1:].values 
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels)
x=[10]
x = np.array(x)
print(regressor.predict(x.reshape(1,1)))
