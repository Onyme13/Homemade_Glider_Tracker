# Test file number one
from positions_functions import *
import random
import time

# Test 1

while True:
    #generate random latitude and longitude
    lat = random.uniform(0, 90)
    long = random.uniform(0, 90)
    write_mouvement(lat, long, 0, 0)

    time.sleep(1)
    print("Waiting...")