/*
Code du Arduino pression barométrique et localisation. Latitude, longitude, altitude.

Sortie: "latitude,longitude,vitesse,altitude,pression"
système métriques

Testé avec Arduino Uno et Arduino Micro

*/

#include <SPI.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BMP3XX.h"
#include <TinyGPSPlus.h>   
#include <SoftwareSerial.h>


//SoftwareSerial ss(3, 2); // TX, RX, for Arduino Uno ONLY !
SoftwareSerial ss(9, 8); // RXD, TXD --> for Arduino Micro
TinyGPSPlus gps;
Adafruit_BMP3XX bmp;

#define BMP_SCK 13 // SCK
#define BMP_MISO 6 // SDO
#define BMP_MOSI 11 // SDI
#define BMP_CS 10 // CSB



#define SEALEVELPRESSURE_HPA (1013.25)




void setup() {
  Serial.begin(9600);
  ss.begin(9600);

  while(!Serial){
  }
  
  //commencer le setup pour le baromètre    
  if (! bmp.begin_SPI(BMP_CS, BMP_SCK, BMP_MISO, BMP_MOSI)) {  
     Serial.println("Could not find a valid BMP3 sensor, check wiring!");
    while (1);
  }

  bmp.setTemperatureOversampling(BMP3_OVERSAMPLING_8X);
  bmp.setPressureOversampling(BMP3_OVERSAMPLING_4X);
  bmp.setIIRFilterCoeff(BMP3_IIR_FILTER_COEFF_3);
  bmp.setOutputDataRate(BMP3_ODR_50_HZ);


}
void loop() {
  while (ss.available() > 0) 
    if (gps.encode(ss.read())){
      gps_loc();
    }
  //gps_location();
  vert_speed();
  Serial.println();
  delay(250);
}

//-----------------------------------------------------------------------------------------------//

void vert_speed(){
  if (! bmp.performReading()) {
  Serial.println("Failed to perform reading :(");
  return;
  }
  Serial.print(bmp.readAltitude(SEALEVELPRESSURE_HPA));

}

void gps_loc(){
    if (gps.location.isValid()){
      Serial.print(gps.location.lat(), 8);
      Serial.print(","); 
      Serial.print(gps.location.lng(), 8);
      Serial.print(",");
      Serial.print(gps.speed.kmph());
      Serial.print(",");
      Serial.print(gps.altitude.meters());  
      Serial.print(",");
      Serial.print(gps.satellites.value());  
      Serial.print(","); 
  }

}
