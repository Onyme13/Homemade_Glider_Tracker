/*
Code du Arduino pression barométrique et localisation. Latitude, longitude, altitude.

Sortie: "latitude,longitude,vitesse,altitude,pression"
système métriques

TODO:
-peut-être changer la sortie baud de 9600 à 115200
-commenter le code
*/

#include <SPI.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BMP3XX.h"
#include <TinyGPSPlus.h>   
#include <SoftwareSerial.h>


SoftwareSerial ss(3, 2); 
TinyGPSPlus gps;
Adafruit_BMP3XX bmp;

#define BMP_SCK 13
#define BMP_MISO 12
#define BMP_MOSI 11 
#define BMP_CS 10



#define SEALEVELPRESSURE_HPA (1013.25)




void setup() {
  //Serial.begin(9600);
  //ss.begin(9600);
  Serial.begin(115200);
  ss.begin(115200);

  while(!Serial){
  }
    
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
  while (ss.available() > 0) // a modifier ?
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
