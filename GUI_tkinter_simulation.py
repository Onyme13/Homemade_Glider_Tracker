from tkinter import * 
from tkinter import ttk 
import datetime
from main import *
from positions_functions import *
import tkintermapviewglider as tkintermapview
from PIL import Image, ImageTk
import threading
import os
from constants import *
from data_simulation import *


#TODO: add position to a JSON file  
#TODO: find a way to put the path to global


####################3####FOR SIMULATIO####################

#min_latitude = 45.8177
#max_latitude = 47.8084
#min_longitude = 5.9559
#max_longitude = 10.4922
    
init = True

latitude_old = 0
longitude_old = 0

latitude_init,longitude_init = 46.600208, 6.376650


#####################################################################

##################### CPU uilization ##################################
import psutil

def write_cpu_utilization(file_path):
    cpu_percent = psutil.cpu_percent()
    localtime = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    
    with open(file_path, 'a') as file:
        file.write(str(localtime) + " - ")
        file.write(str(cpu_percent))
        file.write('%\n')

#####################################################################



SPEED_THRESHOLD = 0 #km/h modify value for testing
REFRESH_RATE = 2000 #miliseconds

position_list = []
mouvement = []
path_created = False


window = Tk()

window.title('GPS')
window.minsize(width=320,height=480)
#window.maxsize(width=320,height=480)

window.geometry("320x480")
window.config(background=BLACK)


#First row 
image_sats = Image.open('images/satellite.png')
image_sats = ImageTk.PhotoImage(image_sats)
label_image_sats = Label(window, image=image_sats,background=BLACK)
label_image_sats.grid(row=0, column=0)
label_sats_text = Label(window, text="00",fg=WHITE,background=BLACK,font=FONT)
label_sats_text.grid(row=0, column=1)

ttk.Separator(window, orient=VERTICAL).grid(column=2, row=0, rowspan=1, sticky='ns', padx=8)

label_pressure_text = Label(window, text="0000 hPa",fg=WHITE,background=BLACK,font=FONT)
label_pressure_text.grid(row=0, column=3)

ttk.Separator(window, orient=VERTICAL).grid(column=4, row=0, rowspan=1, sticky='ns', padx=8)

label_time_text = Label(window, text="00:00:00",fg=WHITE,background=BLACK,font=FONT)
label_time_text.grid(row=0, column=5)

ttk.Separator(window, orient=VERTICAL).grid(column=6, row=0, rowspan=1, sticky='ns', padx=8)

label_batterie_text= Label(window, text="00%",fg=WHITE,background=BLACK,font=FONT)
label_batterie_text.grid(row=0, column=7)
image_batterie = Image.open('images/batterie.png')
image_batterie = ImageTk.PhotoImage(image_batterie)
label_image_batterie = Label(window, image=image_batterie,background=BLACK)
label_image_batterie.grid(row=0, column=8)

#Second row

#script_directory = os.path.dirname(os.path.abspath(__file__))
#database_path = os.path.join(script_directory, "data/MAP_GREY.db") 

map_widget = tkintermapview.TkinterMapView(window, width=320, height=370,use_database_only=False, database_path=None)
map_widget.set_tile_server("http://127.0.0.1:5000/tiles/{z}/{x}/{y}.png", max_zoom=22)

#map_widget = tkintermapview.TkinterMapView(window, width=320, height=370,use_database_only=True, database_path=database_path)
map_widget.grid(row=2,rowspan=6,column=0,columnspan=9)
x, y = read_last_positon()
map_widget.set_position(x,y)  #  If no data is available, set the position to the last known position for preloading of the map
map_widget.set_zoom(14) 
map_widget.max_zoom = 14
map_widget.min_zoom = 9



#Third row
label_alt_text = Label(window, text="ALT",fg=WHITE,background=BLACK,font=FONT)
label_alt_text.grid(row=8, column=0,columnspan=3)
label_alt = Label(window, text="0000 m",fg=WHITE,background=BLACK,font=FONT)
label_alt.grid(row=9, column=0,columnspan=3)



label_therm_text = Label(window, text="THERM.",fg=WHITE,background=BLACK,font=FONT)
label_therm_text.grid(row=8, column=2,columnspan=3)
label_therm = Label(window, text="00 m/s",fg=WHITE,background=BLACK,font=FONT)
label_therm.grid(row=9, column=2,columnspan=3)



label_speed_text = Label(window, text="SPEED",fg=WHITE,background=BLACK,font=FONT)
label_speed_text.grid(row=8, column=4,columnspan=2)
label_speed = Label(window, text="000 km/h",fg=WHITE,background=BLACK,font=FONT)
label_speed.grid(row=9, column=4,columnspan=2)

image_settings = PhotoImage(file="images/settings.png")
settings_button = Button(window,image=image_settings,bg=BLACK)
settings_button.grid(row=8, rowspan=2 ,column=7,columnspan=1)


path = map_widget.set_path(mouvement, color="#F0F0F0", width=2)


def update_path(mouvement):
    global path_created
    global path
    
    alt_diff = mouvement[-1][0] - mouvement[-2][0]
    if not path_created :
        color = map_value_to_color(alt_diff)
        path = map_widget.set_path(mouvement, color=color, width=2)
        path_created = True
        print("path created")
    else:
        print("path modified")
        path.add_position(mouvement[-1][0],mouvement[-1][1])

def calculate_distance(current_position, prevous_position):
    lat1, lon1 = current_position
    lat2, lon2 = prevous_position
    earth_radius = 6371  # Earth's radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlong = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlong / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = earth_radius * c
    return distance


def update_position(alt,lat,long,speed):

    global position_list
    global mouvement
    

    
    #Only add the new position to the list if the plane is moving
    if speed >= SPEED_THRESHOLD:


        position_list.append([lat,long])
        mouvement.append([lat,long])


        if len(position_list) > 2:
            position_list.pop(0)
            mouvement.pop(0)


        if len(mouvement) >= 2:

            current_position = mouvement[-1]
            prevous_position = mouvement[-2]

            distance = calculate_distance(current_position, prevous_position)

            threshold = 0.01 #If the distance between the two points is less than this, don't add the new point to the list. 0.01 is about 10m

            if distance > threshold:
                update_path(mouvement)
    print(position_list)



    #Change glider icon orientation 
    glider = Image.open('images/glider.png').resize((25,25)).rotate(orient(position_list))
    glider = ImageTk.PhotoImage(glider)

    #map_widget.delete_all_marker()
    map_widget.canvas_marker_list = map_widget.canvas_marker_list[:-2] #only keep the last two markers for clarity

    map_widget.set_position(lat, long, marker=True, icon=glider)


    

#Update the vertical speed color label
def map_value_to_color(value):

    color_scale = {
        -5: (0, 0, 1),   # Blue
        0: (1, 1, 1),    # White
        5: (1, 0, 0)     # Red
    }

    closest_values = sorted(color_scale.keys(), key=lambda x: abs(x - value))[:2]

    color_ratio = (value - closest_values[0]) / (closest_values[1] - closest_values[0])

    color_start = color_scale[closest_values[0]]
    color_end = color_scale[closest_values[1]]

    r = int((1 - color_ratio) * color_start[0] + color_ratio * color_end[0])
    g = int((1 - color_ratio) * color_start[1] + color_ratio * color_end[1])
    b = int((1 - color_ratio) * color_start[2] + color_ratio * color_end[2])

    return f"#{r:02x}{g:02x}{b:02x}"



def update_data():
    global init
    global latitude_old, longitude_old


    write_cpu_utilization('cpu_utilization.txt')



    """ DATA DICT:

        "time": 0,
        "localQNH": 0,
        "lat" : 0,
        "long" : 0,
        "speed": 0,
        "altGPS": 0,
        "sat": 0,
        "vert": 0,
        "alt": 0
    """

    my_data = data()

    # Get the latest data values
    current_time = datetime.now()
    current_time = current_time.strftime("%H:%M:%S")

    altitude = my_data['alt']
    speed = my_data['speed']
    vert_speed = my_data['vert'] #vertical_speed(my_data['alt'])
    satellites = my_data['sat']
    localQNH = my_data['localQNH']   

    if init == True:
        latitude, longitude = simulate_gps_position(latitude_init,longitude_init)
        latitude_old = latitude
        longitude_old = longitude
        init = False
    else:
        latitude, longitude = simulate_gps_position(latitude_old,longitude_old)
        latitude_old = latitude
        longitude_old = longitude
    
    print(latitude, longitude)

    #Time text update
    label_time_text.config(text=str(current_time))
 
    #Speed text update
    label_speed.config(text=str(round(speed)) + ' km/h')

    #Satellites text update
    label_sats_text.config(text=str(round(satellites)))

    #Pressure (local QNH) text update
    label_pressure_text.config(text=str(round(localQNH)) + 'hPa')

    #Altitude text update
    label_alt.config(text=str(round(altitude)) + ' m')
    
    #Verical speed text update
    label_therm.config(text=str(vert_speed) + ' m/s')    


    #Location update
    if latitude!= 0 and longitude!= 0:
        update_position(altitude,latitude,longitude,speed) #update position for UI
        write_last_positon(latitude,longitude) #write the last known position to a file 
    else:
        latitude, longitude = read_last_positon()
        update_position(altitude,latitude,longitude,speed)  # If no data is available, set the position to the last known position for preloading of the map
    window.after(REFRESH_RATE, update_data) #Initial value is 200

    #time.sleep(0.25) #Initial value is 0.25




def update_bat():
    #TODO
    pass


#thread_update_data = threading.Thread(target=update_data)
#thread_update_data.start()

update_data()
window.mainloop()