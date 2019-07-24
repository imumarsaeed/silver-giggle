#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import os
#import pylab as pl
#import numpy as np
#import tensorflow as tf
#import scipy.optimize as opt
#from sklearn import preprocessing
#from sklearn.cross_validation import train_test_split - Not used anymore thats why causes an error
#from sklearn.model_selection import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


training_data = pd.read_excel (r"C:\Users\MCSL-user\OneDrive\Data Sets for Machine Learning\Data Acquired - Sensor\Training_Data_First.60(F)_Last.60(N).xlsx") #gets the data from PC
training_data.head() #Displays data - First 60% Drift fault - Last 60% Normal Data 


# In[3]:


training_data.describe() #Returns the statistical summary of Numerical Data


# In[4]:


training_data.plot(kind='line')
plt.show() # First 60% Drift fault - Last 60% Normal Data - Total=120 Rows


# In[5]:


ax = training_data[training_data['Label'] == 0][0:100].plot(kind='scatter', x='Max', y='Mean', color='DarkBlue', label='Faulty');
training_data[training_data['Label'] == 1][0:100].plot(kind='scatter', x='Max', y='Mean', color='Red', label='Normal', ax=ax);
plt.show()


# In[6]:


#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4) #40% of data for test

X_train = training_data[['Max','Mean']]
y_train = training_data[['Label']]


# In[7]:


from sklearn.svm import SVC  
svclassifier = SVC(kernel='linear')  
svclassifier.fit(X_train, y_train.values.ravel()) #.ravel() func. accepts values as 2D as 1D was expected by the model


# In[8]:


testing_data = pd.read_excel (r"C:\Users\MCSL-user\OneDrive\Data Sets for Machine Learning\Data Acquired - Sensor\Testing_Data_First.40(F)_Last.40(N).xlsx")
testing_data.describe()


# In[9]:


X_test = testing_data[['Max','Mean']]
y_test = testing_data[['Label']]


# In[10]:


svclassifier.predict(X_test)


# In[11]:


y_pred = svclassifier.predict(X_test)


# In[12]:


svclassifier.score(X_test, y_test) #Accuracy score 100%


# In[13]:


from sklearn.metrics import classification_report, confusion_matrix  
print(confusion_matrix(y_test,y_pred))  
#print(classification_report(y_test,y_pred))


# In[14]:


print(classification_report(y_test,y_pred)) 


# In[16]:


# Now we are gonna use Pickle or Joblib API which actually helps in not training the model each time we run the program.
import pickle

with open('SVM_model_Fault_Classification','wb') as f: #wb=write binary
    pickle.dump(svclassifier,f)


# In[17]:


with open('SVM_model_Fault_Classification','rb') as f:
    SVM_prediction = pickle.load(f)


# In[18]:


SVM_prediction.predict(X_test)


# In[20]:


SVM_prediction.score(X_test, y_test)#We got same accuracy asw above, but using not training.Yahooo! :D


# In[ ]:




