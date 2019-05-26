# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:15:36 2019

@author: mss2015
"""


import pandas as pd
df = pd.read_csv("Telecom_churn.csv")
df4=df[(df['international plan'] == 'yes') & \
 (df['voice mail plan'] == 'yes' )&(df['churn']==True)]
df2=df4['voice mail plan'].value_counts()
print("voice and international are {}".format(df2[0]))
df4=df[(df['churn']==True)].sum()
print("churn custumer total int charge {}".format(df4['total intl charge']))
chintlcharge=df4['total intl charge']
df4=df[(df['churn']==False)].sum()
print("non churn custumer total int charge {}".format(df4['total intl charge']))
nonchintlcharge=df4['total intl charge']
import matplotlib.pyplot as plt
vis1 = plt.pie([chintlcharge, nonchintlcharge], explode=[0, 0], labels=['churn','non churn'], autopct="%1.2f%%")
plt.axis('equal')
plt.show(vis1)
df4=df[(df['churn']==True)]
df5=df4['total night minutes'].max()
df6=df[(df['churn']==True)&(df4['total night minutes']==df5)]
print('state is '.format(df6['state']))
df4=df[(df['international plan'] == 'yes')&(df['churn']==True)]
df4=df4['churn'].value_counts()
intp=df4.values
df4=df[(df['voice mail plan'] == 'yes')&(df['churn']==True)]
df4=df4['churn'].value_counts()
voicep=df4.values
vis1 = plt.pie([intp, voicep], explode=[0, 0], labels=['interna','voice mail'], autopct="%1.2f%%")
plt.axis('equal')
plt.show(vis1)
df4=df[(df['churn']==True)]
df1=df4['total eve charge'].min()
df2=df4['total night charge'].min()
df3=df4['total intl charge'].min()
plt.bar(['total eve charge','total night charge','total intl charge'],[df1,df2,df3])

df4=df['account length'].max()
print(df4)
df4=df[(df['account length']==int(df4))]
df5=df4['churn'].values
if (df5==True):
    print('cata is churn')
else:
    print('cata is not churn')

df4=df[(df['churn']==True)]
df5= df4(df4['customer service calls']==1)
df6= df4(df4['customer service calls']==10)
    


