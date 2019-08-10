#include<DHT.h>
#define DHTPIN 13 //Pin attached for sensor reading
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();
}

void loop() {

  int randomNumber;
  randomNumber = random(0,2); //Random 1 and 0 generation
  Serial.println(randomNumber);
  
//For normal sample 100 values

  if (randomNumber == 1) {
    
      float count=0;
      float b=0;
      float y=0;
      
      for (float count=0; count<100; count++) {
      float t = dht.readTemperature();
      if (count<=50) {
        y = float(t);
      }
      else {
        y = float(t + b);
        b = float(b + 0); 
      }
      Serial.println(y);
      //Serial.println(dht.readTemperature()); 
      delay(50); //here 1=1ms --- 100=100ms --- 1000=1sec
      }
  }

//For faulty sample 100 values
  
  else if (randomNumber == 0) { 
      
      float count=0;
      float b=0.1;
      float y=0;

      for (float count=0; count<100; count++) {
      float t = dht.readTemperature();
      if (count<=50) {
        y = float(t);
      }
      else {
        y = float(t + b);
        b = float(b + 0.1); 
      }
      Serial.println(y);
      //Serial.println(dht.readTemperature()); 
      delay(50); //here 1=1ms --- 100=100ms --- 1000=1sec
      }
   }
}

//Change Drift fault value according. i.e. 0.5, 0.1, 0.3 etc --- END!
