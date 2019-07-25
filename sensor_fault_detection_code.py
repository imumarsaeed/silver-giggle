import serial
import time
import pickle
import numpy

arduino = serial.Serial('/dev/ttyACM0',9600) #Reading values from Arduino IDE code
time.sleep(1) #after each second

while True: #infinite loop until there is disconnectivity
    data = [] #values storing in this array
    for i in range (100): #this value can be changed according to need
        readTemperature = arduino.readline() #reading value from temp
        readTemp = float(readTemperature) #converting it to float to avoid any inconvenience
        print(readTemp) #priting the values in case if needed else comment it
        data.append(readTemp) #adding values to the list one by one
        time.sleep(1) #arduino needs to take rest

    Max = float(max(data)) #For feature extraction
    Mean = float(numpy.mean(data)) #For feature extraction

    with open('/home/pi/Desktop/Python_Codes/Pickle_SVM_model_Fault_Classification','rb') as f: #trained algorithm on PC then shifted here using sklearn Pickle because RP has low processing to do training each time
        svm_prediction = pickle.load(f) #0.21.2 version of sklearn needed on both training & testing systems

    X_test = [Max,Mean] #extracted features storing into the list or we can say variable
    print('Max/Mean: ', X_test) #printing the extracted features
    #[0] means faulty signal (Drift-Fault) \\ [1] means normal signal and sensor is OKAY!
    normal_label_one_faulty_label_zero = svm_prediction.predict([X_test]) #this line of code will be able to predict the sensor fault, because of trained SVM algorithm
    print(normal_label_one_faulty_label_zero) #Faulty-Signal [0] || Normal-Signal [1]
    
    time.sleep(3) #Pause loop for 3 seconds so RP can take rest
