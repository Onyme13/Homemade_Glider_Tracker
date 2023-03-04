from tkinter import * 
from tkinter import ttk 
import datetime
from main import *

from PIL import Image, ImageTk

BLACK = '#000000'
WHITE = '#FFFFFF'
FONT = ('Regular',13)


window = Tk()

window.title('GPS')
window.minsize(width=320,height=480)
window.maxsize(width=320,height=480)

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
label_batterie_text.grid(row=0, column=8)
image_batterie = Image.open('images/batterie.png')
image_batterie = ImageTk.PhotoImage(image_batterie)
label_image_batterie = Label(window, image=image_batterie,background=BLACK)
label_image_batterie.grid(row=0, column=9)

#Second row







#Third row
label_alt_text = Label(window, text="ALT",fg=WHITE,background=BLACK,font=FONT)
label_alt_text.grid(row=1, column=0,columnspan=3)
label_alt = Label(window, text="0000 m",fg=WHITE,background=BLACK,font=FONT)
label_alt.grid(row=2, column=0,columnspan=3)



label_therm_text = Label(window, text="THERM.",fg=WHITE,background=BLACK,font=FONT)
label_therm_text.grid(row=1, column=2,columnspan=3)
label_therm = Label(window, text="00 m/s",fg=WHITE,background=BLACK,font=FONT)
label_therm.grid(row=2, column=2,columnspan=3)



label_speed_text = Label(window, text="SPEED",fg=WHITE,background=BLACK,font=FONT)
label_speed_text.grid(row=1, column=4,columnspan=2)
label_speed = Label(window, text="000 km/h",fg=WHITE,background=BLACK,font=FONT)
label_speed.grid(row=2, column=4,columnspan=2)

image_settings = PhotoImage(file="images/settings.png")
settings_button = Button(window,image=image_settings,bg=BLACK)
settings_button.grid(row=2, column=7,columnspan=2)





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
    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%H:%M:%S")

    altitude = my_data['alt']
    speed = my_data['speed']
    vertical_speed = vertical_speed(my_data['alt'])
    latitude = my_data['lat']
    longitude = my_data['lon']
    satellites = my_data['sat']
    localQNH = my_data['localQNH']


    

    #Time text update
    label_time_text.configure(state='normal')
    label_time_text.delete('1.0', 'end')
    label_time_text.insert('end', str(current_time))
    label_time_text.configure(state='disabled')

    #Speed text update
    label_speed_text.configure(state='normal')
    label_speed_text.delete('1.0', 'end')
    label_speed_text.insert('end', str(speed))
    label_speed_text.configure(state='disabled')

    #Satellites text update
    label_sats_text.configure(state='normal')
    label_sats_text.delete('1.0', 'end')
    label_sats_text.insert('end', str(satellites))
    label_sats_text.configure(state='disabled')


    #Pressure (local QNH) text update
    label_pressure_text.configure(state='normal')
    label_pressure_text.delete('1.0', 'end')
    label_pressure_text.insert('end', str(localQNH))
    label_pressure_text.configure(state='disabled')

    #Altitude text update
    label_alt_text.configure(state='normal')
    label_alt_text.delete('1.0', 'end')
    label_alt_text.insert('end', str(altitude))
    label_alt_text.configure(state='disabled')
    
    
    #Schedule the next update
    window.after(100, update_data)




def update_bat():
    #TODO
    pass


window.mainloop()