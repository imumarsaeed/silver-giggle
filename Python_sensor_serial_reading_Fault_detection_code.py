import serial
import time
import pickle
import numpy
import csv

arduino = serial.Serial('/dev/ttyACM0', 9600) #Reading values from Arduino IDE code

while True: #infinite loop until there is disconnectivity

    readTemp = float(arduino.readline().strip().decode('utf-8')) #reading value from temp
    
    if readTemp ==1.0 or readTemp ==0.0:
        print('Actual Value = ',readTemp)
        signal = []
        for i in range (100): #this value can be changed according to need
            point = float(arduino.readline().strip().decode('utf-8'))
            signal.append(point) #reading value from temp
            #print(point) #printing all values coming from Arduino
                  
        Max = float(max(signal)) #For feature extraction
        Mean = float(numpy.mean(signal)) #For feature extraction
        
        #Paste your Joblib or Pickle file path here of trained data
        with open('/home/pi/Downloads/Sensor_Fault_Detection_Code_and_Pickle_Files/0.1/0.1_Trained_Algorithm_Pickle_Files/DT_Pi_Trained_Code_FaultDetection_PICKLE','rb') as f: #trained algorithm on PC then shifted here using sklearn Pickle because RP has low processing to do training each time
            prediction = pickle.load(f) #0.21.2 version of sklearn needed on both training & testing systems

        X_test = [Max,Mean] #extracted features storing into the list or we can say variable
        print('Max/Mean: ', X_test) #printing the extracted features
        predicted_value = prediction.predict([X_test]) #this line of code will be able to predict the sensor fault, because of trained model
        print('Predicted = ',predicted_value) #Faulty-Signal [0] || Normal-Signal [1]

        csvData = [readTemp, predicted_value]
        #Paste link of csv file here for storing the results
        with open('/home/pi/Desktop/Results.csv','a') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows([csvData])
    else:
        print('Wait')

#time.sleep 20 ms --- END!
    
