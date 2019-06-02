import pandas as pd
import numpy as np
database = pd.read_csv('affairs.csv', sep=',', header=0)  
labels = database.iloc[:,-1].values 
features = database.iloc[:,:-1].values
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [6,7])
features = onehotencoder.fit_transform(features).toarray()


#for finding thr drop value
unique = database["occupation_husb"].value_counts()
variable=len(unique)

#deleteing the not reqwuired value
features = np.delete(features, [0,6], 1)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)
#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)


var1=probability[:,1].size
var2=np.sum(probability[:,1])
result=var2/var1
print(result)

list1=[3,25,3,1,3,16,3,5]
list1=np.array(list1)
list1=list1.reshape(1,-1)
list1 = onehotencoder.transform(list1).toarray()
list1 = np.delete(list1, [0,6], 1)

pred_w1 = classifier.predict(list1)
print(pred_w1)