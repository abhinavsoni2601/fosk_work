import pandas as pd  
df=pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delimiter='\s+')

features = df.iloc[:, :-1].values  
labels = df.iloc[:, 1].values 


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

#train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test) 

from sklearn import metrics  
print('Mean Absolute Error:', metrics.mean_absolute_error(labels_test, labels_pred))  
 
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
lm = LinearRegression ()
lm_lasso = Lasso() 
lm_ridge =  Ridge() 
lm_elastic = ElasticNet() 


#Fit a model on the train data


lm.fit(features_train, labels_train)
lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)
lm_elastic.fit(features_train, labels_train)



predict_test_lm =	lm.predict(features_test ) 
predict_test_lasso = lm_lasso.predict (features_test) 
predict_test_ridge = lm_ridge.predict (features_test)
predict_test_elastic = lm_elastic.predict(features_test)

#Print the Loss Funtion - MSE & MAE

import numpy as np
from sklearn import metrics
print ("Simple Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lm),2) )

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2))

print ("ElasticNet Mean Square Error (MSE) for TEST data is")
print (np.round (metrics .mean_squared_error(labels_test, predict_test_elastic),2))

"""-------------------------------------"""
df1=df
lab=df1['lpsa']
m1=df1['lpsa'].mean()
def app(val):
    if val<m1:
        return 0
    else:
        return 1
    
lab=lab.apply(app).values
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, lab, test_size=0.2, random_state=0)  


from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  
