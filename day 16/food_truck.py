import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
dataset = pd.read_csv('Foodtruck.csv')  
print(dataset.info())
# not use scince profit and etc can have -ve value 
#plt.boxplot(dataset.values)
dataset.plot(x='Population', y='Profit', style='o')  
plt.xlabel('population')  
plt.ylabel('profit')  
plt.show()
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values 
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 
x=[3.7]
x = np.array(x)
print(regressor.predict(x.reshape(1,1)))
plt.scatter(features, labels, color = 'red')
plt.plot(features, regressor.predict(features), color = 'blue')
#from sklearn.model_selection import train_test_split  
#features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=0) 
#from sklearn.linear_model import LinearRegression  
#regressor = LinearRegression()  
#regressor.fit(features_train, labels_train) 
