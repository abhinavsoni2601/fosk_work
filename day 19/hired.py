
import pandas as pd  
import numpy as np  

dataset = pd.read_csv("PastHires.csv")  
features = dataset.iloc[:,0:-1].values 
labels = dataset.iloc[:,-1].values 


le_objs = []

from sklearn.preprocessing import LabelEncoder

for i in [1,3,4,5]:
    labelencoder = LabelEncoder()
    features[:,i] = labelencoder.fit_transform(features[:,i])
    le_objs.append(labelencoder)

labelencoder = LabelEncoder()
labels = labelencoder.fit_transform(labels)
le_objs.append(labelencoder)

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  

#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

#Evaluating score
#For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  


from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred)) 


#    Predict employment of a currently employed 10-year veteran, previous employers 4
#, went to top-tire school, having Bachelor's Degree without Internship.


x = np.array([[10,'Y',4,'BS','Y','Y']])
x[:,1 ] = le_objs[0].transform(x[:,1 ])
x[:,3 ] = le_objs[1].transform(x[:,3 ])
x[:,4 ] = le_objs[2].transform(x[:,4 ])
x[:,5 ] = le_objs[3].transform(x[:,5 ])

pred = classifier.predict(x)

print(pred)

