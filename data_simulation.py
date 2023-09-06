""" Function that simulates latitudes and longitudes position for demonstration only. The speed simulated is about 100km/h"""

import random
import time


def simulate_gps_position(latitude, longitude):
    
    # Simulate the movement of the plane by adding small random changes
    latitude += random.uniform(-0.001, 0.001)
    longitude += random.uniform(-0.001, 0.001)
    
    # Round the latitude and longitude values to 6 decimal places
    latitude = round(latitude, 6)
    longitude = round(longitude, 6)
    
    return latitude, longitude

