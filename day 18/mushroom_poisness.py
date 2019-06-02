
import pandas as pd
import numpy as np
database = pd.read_csv('mushrooms.csv', sep=',', header=0)  
database.info()
labels = database.iloc[:,0].values 
features = database.iloc[:,[5,21,22]].values


le_objs = []

from sklearn.preprocessing import LabelEncoder

for i in range(3):
    labelencoder = LabelEncoder()
    features[:,i] = labelencoder.fit_transform(features[:,i])
    le_objs.append(labelencoder)

labelencoder = LabelEncoder()
labels = labelencoder.fit_transform(labels)
le_objs.append(labelencoder)

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0,1,2])
features = onehotencoder.fit_transform(features).toarray()

unique = database["odor"].value_counts()
variable1=len(unique)
unique = database["population"].value_counts()
variable2=len(unique)
unique = database["habitat"].value_counts()
variable3=len(unique)
features = np.delete(features, [0,variable2,variable3], 1)



from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features, labels)

x = np.array([['p','s','u']])
x[:,0 ] = le_objs[0].transform(x[:,0 ])
x[:,1 ] = le_objs[1].transform(x[:,1 ])
x[:,2 ] = le_objs[2].transform(x[:,2 ])
x = onehotencoder.transform(x).toarray()
x = np.delete(x, [0,variable2,variable3], 1)


# Predicting the class labels
labels_pred = classifier.predict(x)


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
