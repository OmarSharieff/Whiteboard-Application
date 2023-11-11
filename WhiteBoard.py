import tkinter as tk
from tkinter.colorchooser import askcolor

# Function to start drawing on canvas
def start_drawing(event):
    # declaring global variables to be accessed from amywhere in the program
    global is_drawing, prev_x, prev_y
    # This variable is used to indicate whether a drawing action is in progress
    is_drawing = True
    # This captures the current coordinates of the mouse cursor whent the 'start_drawing' function is called
    prev_x, prev_y = event.x, event.y

# Function to actually from a line from starting point to end point
def draw(event):
    # global variables
    global is_drawing, prev_x, prev_y
    # truthy implementation
    if is_drawing:
        # This captures the coordinates of end points of line of the move cursor
        current_x, current_y = event.x, event.y
        # In Tkinter, Canvas.create_line() method is used to create lines in any canvas.
        # "capstyle=tk,ROUND" means endpoints of the line will have round edges
        # "smooth=True" helps in creating a smoother curve rather than a series of straight lines.
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill=drawing_color, width=line_width, capstyle=tk.ROUND, smooth=True)

# Function to stop drawing on canvas
def stop_drawing(event):
    global is_drawing
    is_drawing = False

# Building the Color Changing feature
def change_pen_color():
    global drawing_color
    # askcolor()[1] means that you are calling askcolor() function from 'tkinter.colorChooser' module to get the tuple,
    # and then accessing the second element of that tuple (index 1), which is the hexadecimal representation of the selected color.
    color = askcolor()[1]
    if color:
        drawing_color = color

# Function to adjuat line width
def change_line_width(value):
    global line_width
    line_width = int(value)

# Now, all the functionalties of Whiteboard are complete. Let's build our GUI
root = tk.Tk()
root.title("Whiteboard App")

# Creating canvas object
canvas = tk.Canvas(root, bg="white")

# Configuring canvas to fill up both the horizontal and vertical space of the application window,
# allowing the canvas to expand and occupy the entire window
canvas.pack(fill="both", expand=True)

# Inititalizing default values for pen color and line's width,
# since the App just opened, there wont be drawing taking place yet so 'is_drawing = False'
is_drawing = False
drawing_color = "black"
line_width = 2

# Size of Main Window
root.geometry("800x600")

# Building navbar and controls
controls_frame = tk.Frame(root)
controls_frame.pack(side="top", fill="x")

# Defining Buttons and their functions
color_button = tk.Button(controls_frame, text="Change Color", command=change_pen_color)
clear_button = tk.Button(controls_frame, text="Clear Canvas", command=lambda: canvas.delete("all"))

# Placing Buttons on bottom-left side of the window
color_button.pack(side="left", padx=5, pady=5)
clear_button.pack(side="left", padx=5, pady=5)

# Creating a Slider for the line width function
line_width_label = tk.Label(controls_frame, text="Line Width:")
# Configuring the label's placement within the 'control frame' widget
line_width_label.pack(side="left", padx=5, pady=5)

# Creating horizontal slider widget ranging from values 1 to 10,
# the 'command' option is set to call the 'change_line_width' function with the selected value whenever slider position changes
line_width_slider = tk.Scale(controls_frame, from_=1, to=10, orient="horizontal", command=lambda val: change_line_width(val))
# This sets the initial position of the slider to the value thats stored in 'line_width' variable
line_width_slider.set(line_width)
# Configuring the slider's placement within the 'controls_frame'
line_width_slider.pack(side="left", padx=5, pady=5)

# Binding or "Linking" the functions with the buttons we created so that the application actually works!
canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)

root.mainloop()