from tkinter import *

mycolor = "blue"

def press(event):
    global px, py
    px= event.x
    py= event.y
   
def paint(event):
    global px, py
    canvas.create_line(px, py, event.x, event.y, fill=mycolor, width=3)
    px, py= event.x, event.y
    
def change_color():
    global mycolor
    mycolor="red"

window = Tk()
canvas = Canvas(window)
canvas.pack()
canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonPress-1>", press)
button = Button(window, text="빨강색", command=change_color)
button.pack()
window.mainloop()
