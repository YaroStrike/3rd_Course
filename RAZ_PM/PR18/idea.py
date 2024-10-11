import tkinter as tk
import math

def animate_last_shape():
    global angle
    angle += 5  # Increment the angle for rotation
    x_offset = 5 * math.cos(math.radians(angle))  # Calculate x offset for rotation
    y_offset = 5 * math.sin(math.radians(angle))  # Calculate y offset for rotation
    
    # Move the last shape (the trunk) to the right and rotate
    canvas.move(shapes[-1], 5 + x_offset, y_offset)
    
    # Keep the top-left corner of the last shape relative to another shape
    canvas.move(shapes[-1], 5, 0)  # Move right
    canvas.after(100, animate_last_shape)

root = tk.Tk()
root.title("variant11")
root.geometry("1366x768")
canvas = tk.Canvas(root, width=1366, height=768)
canvas.pack()

shapes = []
# (left, top, right, bottom)
# Adding shapes as before...

# Initialize angle for rotation
angle = 0

# Start the animation for the last shape
animate_last_shape()
root.mainloop()