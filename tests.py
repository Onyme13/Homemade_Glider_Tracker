import tkinter as tk
import threading
import time

class MapWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack()

    def update_map(self):
        # Simulate GPS positioning updates
        x = 400 + 100 * math.sin(time.time())
        y = 300 + 100 * math.cos(time.time())
        self.canvas.delete("position")
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red", tags="position")

def start_update_thread(map_window):
    while True:
        map_window.update_map()
        time.sleep(0.1)

if __name__ == "__main__":
    import math

    root = tk.Tk()
    root.title("GPS Positioning Map")

    map_window = MapWindow(master=root)

    update_thread = threading.Thread(target=start_update_thread, args=(map_window,))
    update_thread.daemon = True
    update_thread.start()

    map_window.mainloop()
