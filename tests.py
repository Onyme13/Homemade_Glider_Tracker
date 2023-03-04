import tkinter as tk

class FlightDataGUI:
    def __init__(self, master):
        self.master = master
        master.title("Flight Data")
        
        # Create the labels for the data values
        self.altitude_label = tk.Label(master, text="Altitude: ")
        self.speed_label = tk.Label(master, text="Speed: ")
        self.vertical_speed_label = tk.Label(master, text="Vertical Speed: ")
        
        # Create the text widgets for the data values
        self.altitude_text = tk.Text(master, height=1, width=10)
        self.speed_text = tk.Text(master, height=1, width=10)
        self.vertical_speed_text = tk.Text(master, height=1, width=10)
        
        # Pack the labels and text widgets
        self.altitude_label.pack()
        self.altitude_text.pack()
        self.speed_label.pack()
        self.speed_text.pack()
        self.vertical_speed_label.pack()
        self.vertical_speed_text.pack()
        
        # Set initial data values
        self.altitude = 0
        self.speed = 0
        self.vertical_speed = 0
        
        # Update the data values every 100 ms
        self.update_data()
        self.master.after(100, self.update_data)
        
    def update_data(self):
        # Get the latest data values
        self.altitude = get_altitude()
        self.speed = get_speed()
        self.vertical_speed = get_vertical_speed()
        
        # Update the text widgets with the latest data values
        self.altitude_text.configure(state='normal')
        self.altitude_text.delete('1.0', 'end')
        self.altitude_text.insert('end', str(self.altitude))
        self.altitude_text.configure(state='disabled')
        
        self.speed_text.configure(state='normal')
        self.speed_text.delete('1.0', 'end')
        self.speed_text.insert('end', str(self.speed))
        self.speed_text.configure(state='disabled')
        
        self.vertical_speed_text.configure(state='normal')
        self.vertical_speed_text.delete('1.0', 'end')
        self.vertical_speed_text.insert('end', str(self.vertical_speed))
        self.vertical_speed_text.configure(state='disabled')
        
        # Schedule the next update
        self.master.after(100, self.update_data)
        
def get_altitude():
    # Replace with actual code to get altitude data
    return 30000
    
def get_speed():
    # Replace with actual code to get speed data
    return 500
    
def get_vertical_speed():
    # Replace with actual code to get vertical speed data
    return -100
    
# Create the main window and start the GUI
root = tk.Tk()
app = FlightDataGUI(root)
root.mainloop()
