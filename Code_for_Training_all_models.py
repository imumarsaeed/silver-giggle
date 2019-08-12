#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


training_data = pd.read_excel (r" ----- Put link of training data here ---- ") #gets the data from PC
training_data.describe() #Displays data - First 60% Drift fault - Last 60% Normal Data


# In[3]:


X_train = training_data[['Max','Mean']]
y_train = training_data[['Label']]


# In[4]:


#Code to train all models --- Not changing any Parameters --- Same for all faults considered

#1 SVM Classifier --- kernal=linear
from sklearn.svm import SVC  
clf = SVC(kernel='linear')  
clf.fit(X_train, y_train.values.ravel()) #.ravel() func. accepts values as 2D as 1D was expected by the model

#2 Neural Network  --- hidden layers=3
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(2))
clf.fit(X_train, y_train.values.ravel())

#3 Naive Bayes Classifer --- GaussianNB
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X_train, y_train.values.ravel())

#4 K-Nearest Neighbour Classifier --- Neighbors=2
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=2)
clf.fit(X_train, y_train.values.ravel())

#5 Decision Tree Classifer --- 
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth=2)
clf.fit(X_train, y_train.values.ravel()) 


# In[5]:


testing_data = pd.read_excel (r" ----- Put link of testing data here ---- ")
testing_data.describe()


# In[6]:


X_test = testing_data[['Max','Mean']]
y_test = testing_data[['Label']]

clf.predict(X_test)


# In[7]:


y_pred = clf.predict(X_test)

clf.score(X_test, y_test) #Accuracy score 100%


# In[8]:


from sklearn.metrics import classification_report, confusion_matrix  
print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))


# In[ ]:


# --- Now we are gonna use Pickle or also can use Joblib API which helps in generating specific parameters from trained model to be deployed without training each time ---

import pickle
with open(' --- Paste link here where file can be write and saved --- ','wb') as f: #wb=write binary
    pickle.dump(clf,f)
with open(' --- Paste link here from where file can be read --- ','rb') as f: #rb=read binary
    prediction = pickle.load(f)
 
# --- For Testing

prediction.predict(X_test)
prediction.score(X_test, y_test) #God bless the Accuracy!

