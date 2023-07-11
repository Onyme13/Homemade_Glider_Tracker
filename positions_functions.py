import math




#Function that define the oritentation of the glider (360°)
def orient(position_list):

    if len(position_list) >= 2:

        old_latitude = position_list[-2][0]
        old_longitude = position_list[-2][1]
        new_latitude = position_list[-1][0]
        new_longitude = position_list[-1][1]


        old_latitude = math.radians(old_latitude)
        old_longitude = math.radians(old_longitude)
        new_latitude = math.radians(new_latitude)
        new_longitude = math.radians(new_longitude)

        delta_latitude = new_latitude - old_latitude
        delta_longitude = new_longitude - old_longitude

        direction = math.degrees(math.atan2(delta_longitude, delta_latitude))

        direction = (direction + 360) % 360

        return direction
    else:
        return 0




#function that stores the last known postion in CSV file
def write_last_positon(lat,long):
    with open("data/last_pos.csv", "w") as f:
        f.write(str(lat)+","+str(long))

#function that reads the last known postion from the CSV file from the write_last_positon function
def read_last_positon():
    with open("data/last_pos.csv", "r") as f:
        lat,long = f.readline().split(",")
        return float(lat),float(long)
    
def write_mouvement(alt,lat,long):
    with open("data/mouvement.csv", "a") as f:
        f.write(str(lat)+","+str(lat)+","+str(long))


def read_mouvement():
    with open("data/mouvement.csv", "r") as f:
        alt,lat,long = f.readline().split(",")
        return float(alt), float(lat),float(long)

