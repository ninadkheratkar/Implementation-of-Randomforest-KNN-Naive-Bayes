# -*- coding: utf-8 -*-
"""ninad_kheratkar_finaltermproj.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ANtuosvE_s6c_rgKc72U4x616xVJgfnk
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb

"""Import dataset"""

mydata = pd.read_csv(r'/content/diabetes.csv')

mydata.sample(5)

mydata.shape

mydata.dtypes

"""Checking for null/missing data"""

nl = pd.concat([mydata.isnull().sum()], axis = 1, keys = ["Data"])
nl[nl.sum(axis=1) > 0]

"""Target variable"""

x = mydata.iloc[:,0:7]

y = mydata.iloc[:,8]

"""import libraries for all models"""

from sklearn.neighbors import KNeighborsClassifier 
from sklearn.ensemble import RandomForestClassifier 
from sklearn import tree 
from sklearn.naive_bayes import GaussianNB #Naive Bayes Classification Algo.
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report # To get models info.
from sklearn.model_selection import train_test_split # To split data
from sklearn.model_selection import cross_val_score

#random forest
def rnn(x,y):
  X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
  classifier = RandomForestClassifier(n_estimators=100)
  classifier.fit(X_train,y_train)
  y_pred = classifier.predict(X_test)
  a = np.array(confusion_matrix(y_test,y_pred))
  return a
pass

#KNeighborsClassifier
def knn(x,y):

  X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
  model1 = KNeighborsClassifier()
  learner = model1.fit(X_train,y_train)
  y_pred = learner.predict(X_test)
  a = np.array(confusion_matrix(y_test,y_pred))
  return a
pass

#Naive Bayes
def naive(x,y):
  X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
  gnb = GaussianNB() 
  gnb.fit(X_train, y_train)
  y_pred = gnb.predict(X_test)
  a = np.array(confusion_matrix(y_test,y_pred))
  return a
pass


#calculate funciton to calculate all metrics

def calculate(br):

  #true positive

  tp = br[1,1]

  #true negative
  tn = br[0,0]

  #false negative
  fn = br[1,0]

  #false positve
  fp = br[0,1]

  #True positive rate
  tpr = tp/(tp + fn)

  #True negative rate
  tnr = tn/(tn + fp)

  #False positive rate
  fpr = fp/(tn + fp)

  #False negative rate
  fnr = fn/(tp + fn)

  #Recall
  r = tp/(tp + fn)

  #precision
  p = tp/(tp + fp)

  #f1
  f1 = (2 * tp)/(2*(tp + fp + fn))

  #accuracy
  acc = (tp + tn)/(tp + fp + fn + tn)

  #error rate
  err = (fp + fn)/(tp + fp + fn + tn)
  

  df1 = pd.DataFrame({'Tp':[tp],'Tn':[tn],'Fp':[fp],'Fn':[fn],'Tpr':[tpr],'Tnr':[tnr],'Fpr':[fpr],'Fnr':[fnr],'Recall':[r],'Precision':[p],'F1':[f1],'Accuracy':[acc],'Error_rate':[err]})
  return df1
pass



def average(df,type):
  return pd.DataFrame({'Type':[type],'Tp':[df['Tp'].mean()],'Tn':[df['Tn'].mean()],'Fp':[df['Fp'].mean()],'Fn':[df['Fn'].mean()],'Tpr':[df['Tpr'].mean()],'Tnr':[df['Tnr'].mean()],'Fpr':[df['Fpr'].mean()],'Fnr':[df['Fnr'].mean()],'Recall':[df['Recall'].mean()],'Precision':[df['Precision'].mean()],'F1':[df['F1'].mean()],'Accuracy':[df['Accuracy'].mean()],'Error_rate':[df['Error_rate'].mean()]})
pass

df_random = pd.DataFrame({'Tp':[],'Tn':[],'Fp':[],'Fn':[],'Tpr':[],'Tnr':[],'Fpr':[],'Fnr':[],'Recall':[],'Precision':[],'F1':[],'Accuracy':[],'Error_rate':[]})

df_knn = pd.DataFrame({'Tp':[],'Tn':[],'Fp':[],'Fn':[],'Tpr':[],'Tnr':[],'Fpr':[],'Fnr':[],'Recall':[],'Precision':[],'F1':[],'Accuracy':[],'Error_rate':[]})

df_naive = pd.DataFrame({'Tp':[],'Tn':[],'Fp':[],'Fn':[],'Tpr':[],'Tnr':[],'Fpr':[],'Fnr':[],'Recall':[],'Precision':[],'F1':[],'Accuracy':[],'Error_rate':[]})

for i in range(1,10):

  a = rnn(x,y)
  df_random = df_random.append(calculate(a),ignore_index=True)
  b= knn(x,y)
  df_knn = df_knn.append(calculate(b),ignore_index=True)
  c = naive(x,y)
  df_naive= df_naive.append(calculate(c),ignore_index=True)
  


final = pd.DataFrame({'Type':[],'Tp':[],'Tn':[],'Fp':[],'Fn':[],'Tpr':[],'Tnr':[],'Fpr':[],'Fnr':[],'Recall':[],'Precision':[],'F1':[],'Accuracy':[],'Error_rate':[]})



final = final.append(average(df_knn,'Knn'),ignore_index=True)
final.set_index('Type')
final1 = final.append(average(df_random,'random'),ignore_index=True)
final1.set_index('Type')
final2 = final1.append(average(df_naive,'Naive'),ignore_index= True)
print('Random Forest \n',df_random)
print('\n\n')
print('Knn \n',df_knn)
print('\n Naive Bayes\n',df_naive)
print('\n\n',final2)