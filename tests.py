# Test file number one

import tkinter
import tkintermapview
from tkinter import messagebox

def show_warning_page():
    warning_window = root_tk.Toplevel(root_tk)
    warning_window.title("Warning")
    warning_window.geometry("300x150")

    warning_label = root_tk.Label(warning_window, text="This is a warning message!\nProceed at your own risk.")
    warning_label.pack(pady=20)

    ok_button = root_tk.Button(warning_window, text="OK", command=lambda: on_ok(warning_window))
    ok_button.pack(pady=10)

def on_ok(window):
    window.destroy()  # Close the warning window
    # Proceed to the main application or open the main window here

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1000}x{700}")
root_tk.title("map_view_simple_example.py")
messagebox.showinfo("Main Application", "Welcome to the main application!")

# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=1000, height=700, corner_radius=0)
map_widget.pack(fill="both", expand=True)

map_widget.set_tile_server("http://127.0.0.1:5000/tiles/{z}/{x}/{y}.png", max_zoom=22)

# create map widget and only use the tiles from the database, not the online server (use_database_only=True)
#map_widget = TkinterMapView(root_tk, width=1000, height=700, corner_radius=0, use_database_only=True,
#                            max_zoom=15, database_path=database_path)
map_widget.pack(fill="both", expand=True)
map_widget.set_position(46.818188, 8.227512)  # Switzerland Center
map_widget.set_zoom(15)
    


root_tk.mainloop()