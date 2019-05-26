# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:09:10 2019

@author: mss2015
"""

import pandas as pd
df = pd.read_csv("training_titanic.csv")
df.info()
df2=df['Survived'].value_counts()
print("servived are {}".format(df2[1]))
print("dead count is are {}".format(df2[0]))
df3=df['Survived'].value_counts(normalize = True)
print("servived % are {}".format(df3[1]))
print("dead % is are {}".format(df3[0]))
#df4=df[(df['Survived'] == 1) & \
# (df['Sex'] == 'female' )]
df4=df[(df['Sex']=='female')]
df2=df4['Survived'].value_counts()
print("servived female are {}".format(df2[1]))
print("dead count female is are {}".format(df2[0]))
df4=df[(df['Sex']=='male')]
df2=df4['Survived'].value_counts()
print("servived male are {}".format(df2[1]))
print("dead count male is are {}".format(df2[0]))
df['Age'] = df['Age'].fillna(df['Age'].mean())
df["child"] = df["Age"].map(lambda x: 0 if x >=18 else 1 )
df4=df[(df['child']==1)]
df2=df4['Survived'].value_counts()
print("servived child are {}".format(df2[1]))
print("dead count child is are {}".format(df2[0]))