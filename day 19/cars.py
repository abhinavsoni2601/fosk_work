import pandas as pd  
import matplotlib.pyplot as plt  

with open('Auto_mpg.txt', mode='rt') as file :
   file_contents = file.read()
file = open('new.csv', mode='wt')
file.write(file_contents)




database=pd.read_csv("new.csv",delimiter = '\s+',header=None)
database.columns=[ "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]
maxmpg=database['car name'][database['mpg']==database['mpg'].max()]
print(maxmpg)
database['horsepower']=database['horsepower'].replace('?', database['horsepower'].mode()[0]).astype('float64')
database['cylinders']=database['cylinders'].astype('float64')
database['model year']=database['model year'].astype('float64')
database['origin']=database['origin'].astype('float64')
features = database.drop('mpg', axis=1) 
features = features.drop('car name', axis=1)
labels = database['mpg'] 




from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  

from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)  


labels_pred = regressor.predict(features_test)

df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  

plt.plot(labels_test,labels_pred)

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test)  

df1=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  

plt.plot(labels_test,labels_pred)

