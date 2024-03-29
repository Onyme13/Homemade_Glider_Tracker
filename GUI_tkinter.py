from tkinter import * 
from tkinter import ttk 
import datetime
from main import *
from positions_functions import *
import tkintermapviewglider as tkintermapview
from PIL import Image, ImageTk
from constants import *
from data_simulation import *




SPEED_THRESHOLD = 0 #km/h modify value for testing
REFRESH_RATE = 1000 #miliseconds
DISTANCE_THRESHOLD = 0.01 #If the distance between the two points is less than this, don't add the new point to the list. 0.01 is about 10m


position_list = []
mouvement = []
colors_list = ["#808080","#808080"]
kill_count = 0

# If the button is hit 3 times, the program will close
def kill():
    global kill_count
    kill_count += 1
    if kill_count == 3:
        window.destroy()
        exit()


window = Tk()

# Toggle full-screen mode
def toggle_fullscreen(event=None):
    state = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not state)

window.bind('<F11>', toggle_fullscreen)
window.bind('<Escape>', toggle_fullscreen)

# Start the application in full-screen mode
window.attributes('-fullscreen', True) # True for full-screen

window.title('GPS')
window.minsize(width=320,height=480)
#window.maxsize(width=320,height=480)

window.geometry("320x480")
window.config(background=BLACK)


#=== First row of the UI =======================================
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

#=== Second row of the UI =======================================

#Old code that used a local database instead of a tile server
#script_directory = os.path.dirname(os.path.abspath(__file__))
#database_path = os.path.join(script_directory, "data/MAP_GREY.db") 
#map_widget = tkintermapview.TkinterMapView(window, width=320, height=370,use_database_only=True, database_path=database_path)


# Create the map widget, and the tile server request
map_widget = tkintermapview.TkinterMapView(window, width=320, height=370,use_database_only=False, database_path=None)
map_widget.set_tile_server("http://127.0.0.1:5000/tiles/{z}/{x}/{y}.png", max_zoom=22)


map_widget.grid(row=2,rowspan=6,column=0,columnspan=9)
x, y = read_last_positon()
map_widget.set_position(x,y)  #  If no data is available, set the position to the last known position for preloading of the map. Optimisation for the map loading
map_widget.set_zoom(14) 
map_widget.max_zoom = 14 # Limit the zoom level to 14
map_widget.min_zoom = 9 # Limit the zoom level to 9



#=== Third row of the UI =======================================
label_alt_text = Label(window, text="ALT",fg=WHITE,background=BLACK,font=FONT)
label_alt_text.grid(row=8, column=0,columnspan=2)
label_alt = Label(window, text="0000 m",fg=WHITE,background=BLACK,font=FONT)
label_alt.grid(row=9, column=0,columnspan=2)


label_therm_text = Label(window, text="V/S.",fg=WHITE,background=BLACK,font=FONT)
label_therm_text.grid(row=8, column=3,columnspan=2)
label_therm = Label(window, text="00 m/s",fg=WHITE,background=BLACK,font=FONT)
label_therm.grid(row=9, column=3,columnspan=2)


label_speed_text = Label(window, text="SPEED",fg=WHITE,background=BLACK,font=FONT)
label_speed_text.grid(row=8, column=5,columnspan=2)
label_speed = Label(window, text="000 km/h",fg=WHITE,background=BLACK,font=FONT)
label_speed.grid(row=9, column=5,columnspan=2)

image_settings = PhotoImage(file="images/settings.png")
settings_button = Button(window,image=image_settings,bg=BLACK,command=kill)
settings_button.grid(row=8, rowspan=2 ,column=7,columnspan=1)

#================================================================================

#Initialisation of the path, make it as small as possible
x, y, = read_last_positon() 
x1, y1 = x+0.0001, y+0.0001
path = map_widget.set_path([(x, y),(x1,y1)],colors=colors_list, width=2)

# Function that updates the path drawing on the map
def update_path(mouvement):
    global path
    
    #Calculate the altitude difference between the last two points
    alt_diff = position_list[-1][0] - position_list[-2][0]
  
    #Change the color of the path depending on the altitude difference
    color = map_value_to_color(alt_diff)
    #Add the new point to the path
    path.add_position(mouvement[-1][0],mouvement[-1][1],color=color)

# Function that calculates the distance between two points, this will be used later to determine if the plane is moving or not
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

# Function that updates the position of the glider icon on the map
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
            
            # Udapte only if the distance between the two points is greater than the threshold value
            distance = calculate_distance(current_position, prevous_position)

            threshold = DISTANCE_THRESHOLD
            if distance > threshold:
                update_path(mouvement)
    ###

    #Change glider icon orientation 
    glider = Image.open('images/glider.png').resize((25,25)).rotate(orient(position_list))
    glider = ImageTk.PhotoImage(glider)

    map_widget.canvas_marker_list = map_widget.canvas_marker_list[:-2] #only keep the last two markers for clarity

    map_widget.set_position(lat, long, marker=True, icon=glider)


    

#Update the vertical speed color label
def map_value_to_color(value):

    color_scale = {
        -5: (0, 0, 1),   # Blue for null values
        0: (1, 1, 1),    # Gree for positive values
        5: (1, 0, 0)     # Red for negative values
    }

    closest_values = sorted(color_scale.keys(), key=lambda x: abs(x - value))[:2]

    color_ratio = (value - closest_values[0]) / (closest_values[1] - closest_values[0])

    color_start = color_scale[closest_values[0]]
    color_end = color_scale[closest_values[1]]

    r = int((1 - color_ratio) * color_start[0] + color_ratio * color_end[0])
    g = int((1 - color_ratio) * color_start[1] + color_ratio * color_end[1])
    b = int((1 - color_ratio) * color_start[2] + color_ratio * color_end[2])

    return f"#{r:02x}{g:02x}{b:02x}"

          

# Function that updates the data on the UI
def update_data():
    global init
    global latitude_old, longitude_old



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
    latitude = my_data['lat']
    longitude = my_data['long']
    satellites = my_data['sat']
    localQNH = my_data['localQNH']   

    
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
        write_mouvement(latitude,longitude,altitude,current_time) #write the last known position to a file 
    else:
        latitude, longitude = read_last_positon()
        update_position(altitude,latitude,longitude,speed)  # If no data is available, set the position to the last known position for preloading of the map
    window.after(REFRESH_RATE, update_data) #Initial value is 200

    #time.sleep(0.25) #Initial value is 0.25




def update_bat():
    #TODO
    pass


update_data()
window.mainloop()
