#from sklearn.model_selection import train_test_split
#%matplotlib inline 
import pandas as pd
#import matplotlib.pyplot as plt

training_data = pd.read_excel ("/home/pi/Downloads/Training_Data_First.60(F)_Last.60(N).xlsx") #gets the data from PC

X_train = training_data[['Max','Mean']]
y_train = training_data[['Label']]

from sklearn.svm import SVC  
svclassifier = SVC(kernel='linear')  
svclassifier.fit(X_train, y_train.values.ravel()) #.ravel() func. accepts values as 2D as 1D was expected by the model


"""
while(1):
    X_test = []
    for i in range(0,100):
        X_test.append(readTemperature)

    X_test = features(X_test)
    result = svcclassifier.predict(X_test)
    print(result)
"""
   