#include<DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);


void setup() {
  // put your setup code here, to run once:
  Serial.begin(230400);
  dht.begin();
}

void loop() {
  
  float count=0;
  float b=0.5;
  float y=0;

  for (float count=0; count<100; count++) {
    float t = dht.readTemperature();
    if (count<=50) {
      y = float(t);
    }
    else {
      y = float(t + b);
      b = float(b + 0.5); 
    }
    delay(20); //here 1=1ms --- 10ms ---  1000ms=1sec
    Serial.println(y);
    Serial.println(dht.readTemperature());  
   }
}
