#include <SPI.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BMP3XX.h"
#include <SoftwareSerial.h>
#include <math.h>
#include <LiquidCrystal.h>


Adafruit_BMP3XX bmp;

#define BMP_SCK 13
#define BMP_MISO 12
#define BMP_MOSI 11 
#define BMP_CS 10

#define SEALEVELPRESSURE_HPA (1013.25)
#define FEETSPERMETER 3.28084

LiquidCrystal lcd(12,11,5,4,3,2);


float altArray[4] = {0,0,0,0};
float  newAlt, alt;
float oldAlt = 0;
int i;
float verticalSpeed;

void setup() {
  lcd.begin(16,2);
  lcd.print("Feet/Min. ");
  //Serial.begin(9600);
  
  while(!Serial){
  }
  if (!bmp.begin_I2C()) { 
    Serial.println("Could not find a valid BMP3 sensor, check wiring!");
    while (1);
  }
    
  //if (! bmp.begin_SPI(BMP_CS, BMP_SCK, BMP_MISO, BMP_MOSI)) {  
  //  Serial.println("Could not find a valid BMP3 sensor, check wiring!");
  //  while (1);
  //}

  bmp.setTemperatureOversampling(BMP3_OVERSAMPLING_8X);
  bmp.setPressureOversampling(BMP3_OVERSAMPLING_4X);
  bmp.setIIRFilterCoeff(BMP3_IIR_FILTER_COEFF_3);
  bmp.setOutputDataRate(BMP3_ODR_50_HZ);

}

void vert_speed(){
  if (! bmp.performReading()) {
  Serial.println("Failed to perform reading :(");
  return;
  }

  alt = bmp.readAltitude(SEALEVELPRESSURE_HPA);
  alt = alt * FEETSPERMETER;
  

  float sum = 0;

  altArray[0] = alt;
  altArray[1] = altArray[0];
  altArray[2] = altArray[1];
  altArray[3] = altArray[2];


  for(i=0; i<4;i++){
    sum += altArray[i];
  }

  newAlt = sum/4;

  verticalSpeed = newAlt - oldAlt;
  //verticalSpeed = verticalSpeed * 100;
  verticalSpeed = round(verticalSpeed);
  //verticalSpeed = verticalSpeed/100;

  Serial.print(verticalSpeed);
  Serial.print(" ft/min ");

  lcd.setCursor(5, 1);
  lcd.print(verticalSpeed);
  lcd.print("    ");




    
  //Serial.print(verticalSpeed * FEETSPERMETER * 60 );
  //Serial.print(" ft/min ");  


  oldAlt=newAlt;  

}

void loop() {
  vert_speed();
  //Serial.println();
  delay(250);


}
