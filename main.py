#!/usr/bin/python3
import serial
from datetime import datetime

#TODO transmit local QNH, transmit local time

arduinoSerial = serial.Serial('COM4',9600)

SEALEVELPRESSURE = 1013.25 
METERSOFAIRHETCOPASCAL = 0.12677457000000025
HETCOPASCALMETERSOFAIR = 7.8880172892718
FEETSPERMETER = 3.28084

returnDict = {
        "time": 0,
        "localQNH": 0,
        "lat" : 0,
        "long" : 0,
        "speed": 0,
        "altGPS": 0,
        "sat":0,
        "alt": 0
    }    

verticalSpeed = 0
altitudeBucket = [] #Bucket for the altitude data of the barometric sensor
oldAlt = 0 #Old altitude data for measuring vertical speed
altGPSArray = [] #Array of the altitude data from the GPS
localQNH = 0 #local QNH difference with the sea level pressure
heightCalibrated = 0
calibrated = False #boolean for the calibration of the local QNH



def adapt_local_pressure(altGPS,alt):
    global calibrated
    global localQNH
    global heightCalibrated

    altitude_proximity_counter=0
    
    altGPSArray.append(altGPS)
    
    if len(altGPSArray) > 20:
        altGPSArray.pop(0)
        for x in range (len(altGPSArray)):
            for y in range (len(altGPSArray)):
                if altGPSArray[x] < altGPSArray[y] + 3.5 and altGPSArray[x] > altGPSArray[y] - 3.5 and altGPSArray[x]!=0.0:
                    altitude_proximity_counter+=1
                else:
                    break

    if altitude_proximity_counter == 400:
        localQNH = SEALEVELPRESSURE + ((sum(altGPSArray)/20)-alt) * METERSOFAIRHETCOPASCAL
        heightCalibrated = round((localQNH - SEALEVELPRESSURE) * HETCOPASCALMETERSOFAIR,1)
        calibrated=True

def vertical_speed(alt):
    global verticalSpeed
    global newAlt
    global oldAlt

    newAlt = alt
    altitudeBucket.append(alt)
    if len(altitudeBucket) > 4: #data is received every 0.25 every 4*0.25=1sec calculate vertical speed in m/s  
        altitudeBucket.pop(0)
    newAlt = sum(altitudeBucket)/4

    verticalSpeed = round(newAlt-oldAlt,1) 

    if verticalSpeed == -0.0:
        verticalSpeed = 0.0

    oldAlt=newAlt

    return verticalSpeed #TODO Return something else 


#main function that processes data
def data():
    while(arduinoSerial.inWaiting()==0):
        pass
    dataString = arduinoSerial.readline().decode('utf-8')
    dataArray = dataString.replace('\r\n','').split(',')

    localtime = datetime.now()
    localtime = localtime.strftime("%H:%M:%S.%f")[:-3]
    returnDict.update({
        'time':localtime
    })
    
    #If lenght of dataArray is only one, this means the only output is barometric height
    if len(dataArray) == 1:
        altitude = float(dataArray[0])
        #altitude = float(dataArray[0])
        if calibrated: #If QNH is calibrated, adjust the height.
            altitude += heightCalibrated
        
        returnDict.update({"alt":altitude})
        
    #dataArray[latitude, longitude, speed, altitude of GPS, altitude barometric] (metric system)
    if len(dataArray) >= 5:

        latitude = float(dataArray[0]) 
        longitude = float(dataArray[1])
        speed = float(dataArray[2])
        altitudeGPS = float(dataArray[3])
        satellites = float(dataArray[4])
        altitude = float(dataArray[-1])
        
        if calibrated: #If QNH is calibrated, adjust the height.
            altitude += heightCalibrated

        #If QNH is not calibrated, calibrate the local QNH with GPS data
        if not calibrated:
            adapt_local_pressure(altitudeGPS,altitude)
        
        returnDict.update({
            "lat" : latitude,
            "long" : longitude,
            "speed": speed,
            "altGPS": altitudeGPS,
            "sat":satellites,
            "alt": altitude
        })
    #print serial data from Arduino
    #print(dataArray)
    print(returnDict)
    return returnDict

#testing output data
while True:
    #pass
    data()
