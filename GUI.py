import PySimpleGUI as sg
from PIL import Image
from datetime import datetime



#data() ==> Dict[time,lat,lon,speed,altGPS,sat,alt]
#320x480
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H:%M:%S")
image_setting = './images/settings.png'



first_column = [[sg.T('ALT',text_color='#FFFFFF',background_color='#000000',font=('Regular',13))],
                [sg.T('0000 m',text_color='#FFFFFF',background_color='#000000',font=('Regular',13),key='-ALT-')]]

second_column = [[sg.T('THERM.',text_color='#FFFFFF',background_color='#000000',font=('Regular',13))],
                [sg.T('10 m/s',text_color='#FFFFFF',background_color='#000000',font=('Regular',13),key='-THERM-')]]

third_column =[[sg.T('SPEED',text_color='#FFFFFF',background_color='#000000',font=('Regular',13))],
                [sg.T('000 km/h',text_color='#FFFFFF',background_color='#000000',font=('Regular',13),key='-SPEED-')]]

fourth_column = [[sg.B('',image_filename='images/settings.png',button_color='#000000',border_width=1)]]

layout = [
    [sg.Image('images/satellite.png',background_color='#000000',pad=(0,0)),
     sg.T('00',text_color='#FFFFFF',background_color='#000000',font=('Regular',13),pad=(0,0),justification='l',key='-SATS-'),
     sg.VerticalSeparator(),
     sg.T("0000 hPa",text_color='#FFFFFF',background_color='#000000',font=('Regular',13),key='-PRESS-'),
     sg.VerticalSeparator(),
     sg.T('00:00:00',text_color='#FFFFFF',background_color='#000000',font=('Regular',13),key='-TIMEUTC-'),
     sg.VerticalSeparator(),
     sg.Stretch(background_color="#000000"),
     sg.T('00%',text_color='#FFFFFF',background_color='#000000',font=('Regular',11
     ),pad=(0,0),key='-BATT-'),
     sg.Image('images/batterie.png',background_color='#000000',pad=(0,0))],

    [sg.Image('images/map.png',pad=(0,5))],

    [sg.Column(first_column,background_color='#000000',pad=(0,0)),
     sg.VSeperator(),
     sg.Column(second_column,background_color='#000000',pad=(0,0)),
     sg.VSeperator(),
     sg.Column(third_column,background_color='#000000',pad=(0,0)),
     sg.VSeperator(),
     sg.Column(fourth_column,background_color='#000000',pad=(0,0))
    ] 
]

window = sg.Window("Demo",layout,  background_color='#000000',margins=(0,5))

#TODO put data() into a dict insteed of calling the function each time..
while True:
    event, values = window.read(timeout=0)
    
    """    #data() ==> Dict[lat,lon,speed,altGPS,sat,alt]
    satellites = str((data()['sat']))    
    window['-SATS-'].update(satellites)

    pressure = str((data()['---']))    
    window['-PRESS-'].update(pressure)

    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    window['-TIMEUTC-'].update(currentTime)

    #TODO create function for battery
    #window['-BATT-'].update(currentTime)
        
    alt = str((data()['alt']))    
    window['-ALT-'].update(alt)

    verticalSpeed = str(vertical_speed(data()['alt']))
    window['THERM-'].update(currentTime)

    speed = str(str((data()['speed'])))
    window['-SPEED-'].update(currentTime)

    #verticalSpeed = str(vertical_speed(data()['alt']))
    #window['-TEXT-'].update(verticalSpeed)
    """

#    if event == sg.WIN_CLOSED or event == 'Exit':
#        break
#    window.close()

