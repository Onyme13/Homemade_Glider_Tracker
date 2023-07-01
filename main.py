import serial
from datetime import datetime
import itertools
import time
from constants import SEALEVELPRESSURE, METERSOFAIRHETCOPASCAL, HETCOPASCALMETERSOFAIR

arduinoSerial = serial.Serial('COM4', 9600)


previous_altitude = 0
previous_time = 0
altitudeBucket = []
altGPSArray = []
localQNH = 0
heightCalibrated = 0
calibrated = False  

def adapt_local_pressure(altGPS, alt):
    global localQNH
    global heightCalibrated
    global calibrated


    altGPSArray.append(altGPS)

    if len(altGPSArray) > 20:
        altGPSArray.pop(0)
        if all(abs(x - y) < 3.5 for x, y in itertools.combinations(altGPSArray, 2) if x != 0.0):
            localQNH = SEALEVELPRESSURE + ((sum(altGPSArray) / len(altGPSArray)) - alt) * METERSOFAIRHETCOPASCAL
            heightCalibrated = round((localQNH - SEALEVELPRESSURE) * HETCOPASCALMETERSOFAIR, 1)
            calibrated = True  

def vertical_speed(alt):
    global previous_altitude, previous_time
    current_time = time.time()
    delta_time = current_time - previous_time
    altitude_difference = alt - previous_altitude
    vertical_speed = altitude_difference / delta_time
    
    # Update previous values for the next iteration
    previous_altitude = alt
    previous_time = current_time
    
    vertical_speed = round(vertical_speed, 1)
    return vertical_speed

def data():
    #time.sleep(1)
    #while arduinoSerial.inWaiting() == 0:
    #    pass
    dataString = arduinoSerial.readline().decode('utf-8')
    dataArray = dataString.replace('\r\n', '').split(',')

    localtime = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    returnDict = {
        "time": localtime,
        "localQNH": 0,
        "lat": 0,
        "long": 0,
        "speed": 0,
        "altGPS": 0,
        "sat": 0,
        "vert": 0,
        "alt": 0
    }

    if len(dataArray) == 1:
        altitude = float(dataArray[0])
        vert_speed = vertical_speed(altitude)
        if calibrated:
            altitude += heightCalibrated
        returnDict.update({"vert": vert_speed, "alt": altitude})
    elif len(dataArray) >= 5:
        latitude = float(dataArray[0]) 
        longitude = float(dataArray[1])
        speed = float(dataArray[2])
        altitudeGPS = float(dataArray[3])
        satellites = float(dataArray[4])
        altitude = float(dataArray[-1])

        vert_speed = vertical_speed(altitude)

        if not calibrated:
            adapt_local_pressure(altitudeGPS, altitude)

        if calibrated:
            altitude += heightCalibrated

        returnDict.update({
            "lat": latitude,
            "long": longitude,
            "speed": speed,
            "altGPS": altitudeGPS,
            "sat": satellites,
            "vert": vert_speed,
            "alt": altitude
        })

    print(returnDict)
    return returnDict

#while True:
#    data()
