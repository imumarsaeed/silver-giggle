import serial
import pickle
with open('/home/pi/Desktop/Python_Codes/Pickle_SVM_model_Fault_Classification','rb') as f:
    svm_prediction = pickle.load(f)

arduino = serial.Serial('/dev/ttyACM0',9600)

while (True):
    if(arduino.inWaiting()>0):
        readTemperature = arduino.readline()
        readTemp = float(readTemperature)
        #print (readTemp)
        X_test = []
        for i in range(0,100): #Store temp values in list, extract features max/min then predict N/F
            X_test.append(readTemp)
            
        classifier = max,min(X_test)
        result = svm_prediction.predict(classifier)
        print(result)
        
        
"""
while(True):
    X_test = []
    for i in range(0,100): #Store temp values in list, extract features max/min then predict N/F
        X_test.append(readTemp)

    classifier = max,min(X_test)
    result = svm_prediction.predict(classifier)
    print(result)
"""