from tkinter import * 
from tkinter import ttk 
import time

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
label_sats = Label(window, text="00",fg=WHITE,background=BLACK,font=FONT)
label_sats.grid(row=0, column=1)

ttk.Separator(window, orient=VERTICAL).grid(column=2, row=0, rowspan=1, sticky='ns', padx=8)

label_pressure = Label(window, text="0000 hPa",fg=WHITE,background=BLACK,font=FONT)
label_pressure.grid(row=0, column=3)

ttk.Separator(window, orient=VERTICAL).grid(column=4, row=0, rowspan=1, sticky='ns', padx=8)

label_time = Label(window, text="00:00:00",fg=WHITE,background=BLACK,font=FONT)
label_time.grid(row=0, column=5)

ttk.Separator(window, orient=VERTICAL).grid(column=6, row=0, rowspan=1, sticky='ns', padx=8)

label_batterie= Label(window, text="00%",fg=WHITE,background=BLACK,font=FONT)
label_batterie.grid(row=0, column=8)
image_batterie = Image.open('images/batterie.png')
image_batterie = ImageTk.PhotoImage(image_batterie)
label_image_batterie = Label(window, image=image_batterie,background=BLACK)
label_image_batterie.grid(row=0, column=9)

#Second row




window.mainloop()
