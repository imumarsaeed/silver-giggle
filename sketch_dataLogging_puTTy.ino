#include<DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();
  //Serial.println("Clear Data!");
  //Serial.println("Temperature");
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.print("DATA,Date,Time,Temp,Humid");
  Serial.println(dht.readTemperature());
  //Serial.println("");
  //Serial.print(dht.readHumidity());
  //Serial.println(",");

  delay(1000);
}
