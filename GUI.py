import PySimpleGUI as sg
from main import *


#data() ==> Dict[lat,lon,speed,altGPS,alt]
#320x480


layout = [
    [sg.Text("Vertical speed")],
    [sg.Text(key='-TEXT-'),sg.Text('m/s')]
] 

window = sg.Window("Demo",layout, size=(320,480))


while True:
    event, values = window.read(timeout=0)

    verticalSpeed = str(vertical_speed(data()['alt']))
    window['-TEXT-'].update(verticalSpeed)

    #if event == sg.WIN_CLOSED or event == 'Exit':
    #    break
    #window.close()

