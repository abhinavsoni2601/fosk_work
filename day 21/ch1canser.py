import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

dataset = pd.read_csv("breast_cancer.csv")
dataset.isnull().any()
dataset['G']=dataset['G'].fillna(dataset['G'].mode()[0])
dataset.isnull().any()
dataset["K"]=np.where(dataset["K"]==4,1,0)

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()


data1=dataset.iloc[:,1:].values

from sklearn.model_selection import train_test_split
features_train, features_test = train_test_split(data1, test_size=0.5, random_state=0)

gnb.fit(
    features_train[:,:-1],
    features_train[:,-1]
)
labels_pred = gnb.predict(features_test[:,:-1])

from sklearn.metrics import confusion_matrix
cm_mnb = confusion_matrix(features_test[:,-1], labels_pred)


score = gnb.score(features_train[:,:-1],features_train[:,-1])
score = gnb.score(features_test[:,:-1],labels_pred)

x=np.array([[6,2,5,3,9,4,7,2,2]])
labels_pred1 = gnb.predict(x)
if labels_pred1 ==1:
    print('you may have cancer')
else:
    print('you dont have canser')


"""--------------------------------"""

