import serial
import time
import pickle
import numpy
import csv

arduino = serial.Serial('/dev/ttyACM0', 9600) #Reading values from Arduino IDE code

while True: #infinite loop until there is disconnectivity
    data = [] #values storing in this array
    for i in range (100): #this value can be changed according to need
        readTemp = float(arduino.readline().strip().decode('utf-8')) #reading value from temp
        #readTemp = float(readTemperature) #converting it to float to avoid any inconvenience
        #print(readTemp) #priting the values in case if needed else comment it
        data.append(readTemp) #adding values to the list one by one
        #time.sleep(0.5) # 0.01=10ms, 0.1=100ms, 0.01=10ms

    for values in data:
        if values == 1.0:
            generated_signal = values
            #print(generated_signal)
        elif values == 0.0:
            generated_signal = values
            #print(generated_signal)

    random_fault_generation = [generated_signal]
    print(random_fault_generation)
    
    Max = float(max(data)) #For feature extraction
    Mean = float(numpy.mean(data)) #For feature extraction
    
    #Paste your Joblib or Pickle file path here of trained data
    with open('/home/pi/Downloads/Sensor_Fault_Detection_Code_and_Pickle_Files/0.1/0.1_Trained_Algorithm_Pickle_Files/DT_Trained_Code_FaultDetection_PICKLE','rb') as f: #trained algorithm on PC then shifted here using sklearn Pickle because RP has low processing to do training each time
        prediction = pickle.load(f) #0.21.2 version of sklearn needed on both training & testing systems

    X_test = [Max,Mean] #extracted features storing into the list or we can say variable
    print('Max/Mean: ', X_test) #printing the extracted features
    #[0] means faulty signal (Drift-Fault) \\ [1] means normal signal and sensor is OKAY!
    normal_label_one_faulty_label_zero = prediction.predict([X_test]) #this line of code will be able to predict the sensor fault, because of trained SVM algorithm
    print(normal_label_one_faulty_label_zero) #Faulty-Signal [0] || Normal-Signal [1]

    csvData = [random_fault_generation, normal_label_one_faulty_label_zero]

    #Paste link of csv file here for storing the results
    with open('/home/pi/Desktop/Results/0.1/DT_0.1_detection_results.csv','a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows([csvData])

#time.sleep 50 ms --- END!
        
