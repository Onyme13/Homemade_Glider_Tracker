from tkinter import * 
from tkinter import ttk 
import datetime
from main import *
import tkintermapview
from PIL import Image, ImageTk

BLACK = '#000000'
WHITE = '#FFFFFF'
FONT = ('Regular',13)


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

map_widget = tkintermapview.TkinterMapView(window, width=320, height=370)
map_widget.grid(row=2,rowspan=6,column=0,columnspan=9)
map_widget.set_position(46.818188, 8.227512)  # Switzerland Center
map_widget.set_zoom(15)



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


def update_position(lat,long):
    marker = map_widget.set_position(lat, long, marker=True,)





def update_data():

    """ DATA DICT:

        "time": 0,
        "localQNH": 0,
        "lat" : 0,
        "long" : 0,
        "speed": 0,
        "altGPS": 0,
        "sat":0,
        "alt": 0
    """

    my_data = data()

    # Get the latest data values
    current_time = datetime.now()
    current_time = current_time.strftime("%H:%M:%S")

    altitude = my_data['alt']
    speed = my_data['speed']
    vert_speed = vertical_speed(my_data['alt'])
    latitude = my_data['lat']
    longitude = my_data['long']
    satellites = my_data['sat']
    localQNH = my_data['localQNH']   

    #Time text update
    label_time_text.configure(text=str(current_time))
 
    #Speed text update
    label_speed.configure(text=str(round(speed)) + ' km/h')

    #Satellites text update
    label_sats_text.configure(text=str(round(satellites)))

    #Pressure (local QNH) text update
    label_pressure_text.configure(text=str(round(localQNH)) + ' hPa')

    #Altitude text update
    label_alt.configure(text=str(round(altitude)) + ' m')
    
    #Verical speed text update
    label_therm.configure(text=str(vert_speed) + ' m/s')    


    #Location update


    window.after(200, update_data) #Initial value is 200




def update_bat():
    #TODO
    pass

#thread_update_data = threading.Thread(target=update_data)
#thread_update_data.start()


update_data()
window.mainloop()