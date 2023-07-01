import tkinter
import tkintermapviewglider as tkintermapview

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1000}x{700}")
root_tk.title("map_view_simple_example.py")

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