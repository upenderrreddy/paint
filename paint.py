import tkinter.ttk as ttk  # widgets
from os import getcwd
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog  # for saving as image
from tkinter import messagebox  # widget for saved message
from PIL import ImageGrab

root = Tk()
root.title('Paint')
root.geometry('800x800')

brush_color = 'black'


def paint(e):
    # e=event moving of mouse
    # changing background color of canvas when we click on canvas area
    # my_canvas.config(bg='black')

    # Brush Parameters
    brush_width = '%.0f' % float(my_slider.get())
    # brush_color = 'green'
    brush_type2 = brush_type.get()  # capstyle is brushtypes: BUTT, ROUND, PROJECTING
    # PROJECTING is Diamond shape

    # starting position
    x1, y1 = e.x - 1, e.y - 1
    # ending position
    x2, y2 = e.x + 1, e.y + 1

    # draw on canvas
    my_canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=brush_width, capstyle=brush_type2, smooth=True)


# change size of brush
def change_brush_size(thing):
    slider_label.config(text='%.0f' % float(my_slider.get()))


# change brush color
def change_brush_color():
    global brush_color
    # brush_color = colorchooser.askcolor(color=brush_color)
    # color=Label(root,text=brush_color)
    # color.pack(pady=10)
    # colorchooser.askcolor(color=brush_color) returns list and index 1 contains #ffff00

    brush_color = colorchooser.askcolor(color=brush_color)[1]


# change canvas color
def change_canvas_color():
    global bg_color
    bg_color = colorchooser.askcolor(color=brush_color)[1]
    my_canvas.config(bg=bg_color)


# clear screen
def clear_screen():
    my_canvas.delete(ALL)
    my_canvas.config(bg='white')


# save image
def save_as_png():
    # returns location with name example D:/UR/paint/im.png
    filetypes = [('png files', '*.png'), ('All Files', '*.*')]
    result = filedialog.asksaveasfilename(initialdir=getcwd(), filetypes=filetypes)
    if result.endswith('.png'):
        pass
    else:
        result += '.png'
    # print(result)
    if result:
        x = root.winfo_x() + my_canvas.winfo_x()
        y = root.winfo_y() + my_canvas.winfo_y()
        x1 = x + my_canvas.winfo_width()
        y1 = y + my_canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(result)

        # pop up success message
        messagebox.showinfo("Image Saved", "Your Image has been saved!")


# create canvas
w = 600
h = 400

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

# creating lines
# x1,y1=0,100
# x2,y2=300,100
# my_canvas.create_line(x1,y1,x2,y2,fill='red')
# my_canvas.create_line(150,0,150,200,fill='red')
# y coordinate starts at top unlike normal 2-d plane

# bind mouse to canvas
# B1-Button-1 of mouse
my_canvas.bind('<B1-Motion>', paint)
# B1 is left click
# B3 is right click
# Motion-just rolling on area makes an event

# create brush options frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20)

# brush size
brush_size_frame = LabelFrame(brush_options_frame, text="Brush Size")
brush_size_frame.grid(row=0, column=0, padx=50)
# Brush Slider
# value is default size
my_slider = ttk.Scale(brush_size_frame, from_=1, to=100, command=change_brush_size, orient=VERTICAL, value=10)
my_slider.pack(padx=10, pady=10)

# Brush slider label
slider_label = Label(brush_size_frame, text=my_slider.get())
slider_label.pack(pady=5)

# Brush Type
brush_type_frame = LabelFrame(brush_options_frame, text='Brush Type', height=400)
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type = StringVar()
# setting default to round
brush_type.set('round')

# create radio buttons for brush type
brush_type_radio1 = Radiobutton(brush_type_frame, text='round', variable=brush_type, value='round')
brush_type_radio2 = Radiobutton(brush_type_frame, text='slash', variable=brush_type, value='butt')
brush_type_radio3 = Radiobutton(brush_type_frame, text='diamond', variable=brush_type, value='projecting')

brush_type_radio1.pack(anchor=W)  # aligning radio buttons to left w=west
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# change colors
change_color_frame = LabelFrame(brush_options_frame, text="Change Colors")
change_color_frame.grid(row=0, column=2)

# change brush color button
brush_color_button = Button(change_color_frame, text='Brush color', command=change_brush_color)
brush_color_button.pack(padx=10, pady=10)

# change canvas background color
canvas_color_button = Button(change_color_frame, text='Canvas color', command=change_canvas_color)
canvas_color_button.pack(padx=10, pady=10)

# program options frame :clear_screen,save
options_frame = LabelFrame(brush_options_frame, text='Program options')
options_frame.grid(row=0, column=3, padx=50)

# clear screen button
clear_botton = Button(options_frame, text='clear screen', command=clear_screen)
clear_botton.pack(padx=10, pady=10)

# save image
save_image_button = Button(options_frame, text='save to PNG', command=save_as_png)
save_image_button.pack(padx=10, pady=10)

root.mainloop()

# pyinstaller --onefile -w 'filename.py'
# to convert .py to .exe
