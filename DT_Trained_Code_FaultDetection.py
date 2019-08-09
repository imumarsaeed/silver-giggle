#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd


# In[17]:


training_data = pd.read_excel (r"C:\Users\MCSL-user\OneDrive\Data Sets for Machine Learning\Data Acquired - Sensor\0.1_Change_Drift_Fault_Samples\Training_Data_First.60(F)_Last.60(N).xlsx") #gets the data from PC
training_data.describe() #Displays data - First 60% Drift fault - Last 60% Normal Data 


# In[3]:


X_train = training_data[['Max','Mean']]
y_train = training_data[['Label']]


# In[4]:


from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=0, max_depth=2)
clf.fit(X_train, y_train.values.ravel()) #.ravel() func. accepts values as 2D as 1D was expected by the model


# In[16]:


testing_data = pd.read_excel (r"C:\Users\MCSL-user\OneDrive\Data Sets for Machine Learning\Data Acquired - Sensor\0.1_Change_Drift_Fault_Samples\Testing_Data_First.40(F)_Last.40(N).xlsx")
testing_data.describe()


# In[6]:


X_test = testing_data[['Max','Mean']]
y_test = testing_data[['Label']]


# In[7]:


clf.predict(X_test)


# In[8]:


clf.score(X_test, y_test)


# In[9]:


y_pred = clf.predict(X_test)


# In[10]:


from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))


# In[11]:


# Now we are gonna use Pickle or Joblib API which actually helps in not training the model each time we run the program.
import pickle

with open('DT_Trained_Code_FaultDetection_PICKLE','wb') as f: #wb=write binary
    pickle.dump(clf,f)


# In[12]:


with open('DT_Trained_Code_FaultDetection_PICKLE','rb') as f:
    DT_prediction = pickle.load(f)


# In[13]:


DT_prediction.predict(X_test)


# In[14]:


DT_prediction.score(X_test, y_test)


# In[ ]:




