import pandas as pd  
df=pd.read_csv("kc_house_data.csv",delimiter=',')
df['sqft_above']=df['sqft_above'].fillna(df['sqft_above'].mode()[0])
df['date']=df['date'].str.split("T",expand=True)


features = df.drop(['id','price',],axis = 1)
labels = df['price']

features.isnull().any()
labels.isnull().any()


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

#train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test) 

#Model accuracy
print('accuracy')
print (regressor.score(features_test, labels_test))
print (regressor.score(features_train, labels_train))

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
lm_lasso = Lasso() 
lm_ridge =  Ridge() 
lm_elastic = ElasticNet() 


#Fit a model on the train data


lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)
lm_elastic.fit(features_train, labels_train)



predict_test_lasso = lm_lasso.predict (features_test) 
predict_test_ridge = lm_ridge.predict (features_test)
predict_test_elastic = lm_elastic.predict(features_test)

#Print the Loss Funtion - MSE & MAE

import numpy as np
from sklearn import metrics

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2))

print ("ElasticNet Mean Square Error (MSE) for TEST data is")
print (np.round (metrics .mean_squared_error(labels_test, predict_test_elastic),2))
