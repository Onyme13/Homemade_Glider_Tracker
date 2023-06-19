import math




#Function that define the oritentation of the glider (360°)
def def_orient(list_position):

    if len(list_position) > 2:
        old_lat = list_position[-2][0]
        old_long = list_position[-2][1]

        new_lat = list_position[-1][0]
        new_long = list_position[-1][1]

        if new_long-old_long != 0:
            tan_calc = (new_lat-old_lat)/(new_long-old_long)
            if tan_calc < 0:
                tan_calc *= -1
        else:
            tan_calc= 0
        
        orientation = math.tan((tan_calc))
        
        return orientation
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
    

