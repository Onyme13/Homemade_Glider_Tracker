from tkinter import *

root = Tk()

# Create Canvas widget
canvas = Canvas(root, width=200, height=200)
canvas.pack()

# Draw a red vertical line
canvas.create_line(100, 0, 100, 200, fill="red")

root.mainloop()