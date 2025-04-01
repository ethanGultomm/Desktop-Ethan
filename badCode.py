# testing screen coordinates
# test results:
#   root window position coordinates are located at the top left of the window, not the middle

from tkinter import *
from tkinter import ttk


# global variables
fallSpeed = 3

root = Tk()
root.overrideredirect(True)
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.attributes("-topmost", True)
root.geometry('%dx%d' % (150, 150))
root.update_idletasks()

# get all the necessary variables
winWidth = root.winfo_width()
winHeight = root.winfo_height()
print(winWidth)
print(winHeight)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# the grip of '87
windowDragging = False
x, y = 0, 0
def mousePress(self, event):
    global x, y, windowDragging
    x, y = event.x , event.y
    windowDragging = True

def mouseMove(event):
    global x, y
    deltaX = event.x - x
    deltaY = event.y - y
    newX = root.winfo_x() + deltaX
    newY = root.winfo_y() + deltaY
    root.geometry('+%d+%d' % (newX, newY))

def mouseRelease(event):
    global x, y, windowDragging
    windowDragging = False
    if root.winfo_y() >= ((screenHeight - 48) - winHeight):
        goodY = (screenHeight - 48) - winHeight
        root.geometry('+%d+%d' % (root.winfo_x(), goodY))

def destroyPet(event):
    root.destroy()
        

root.bind("<Button-1>", lambda event, a = 1: mousePress(a,event))
root.bind("<Button-2>", destroyPet)
root.bind("<B1-Motion>", mouseMove)
root.bind("<ButtonRelease-1>", mouseRelease)

# make 'em FALLLL
def task():
    global fallSpeed
    setPos = False
    winPos_x = root.winfo_x()
    winPos_y = root.winfo_y()
    if not windowDragging :
        if winPos_y < ((screenHeight - 48) - winHeight):
            winPos_y += fallSpeed
            fallSpeed *= 1.1
            if fallSpeed > 25:
                fallSpeed = 25
            root.geometry('+%d+%d' % (winPos_x, winPos_y))
            setPos = True

        if winPos_y >= ((screenHeight - 48) - winHeight) and setPos:
            winPos_y = (screenHeight - 48) - winHeight
            fallSpeed = 3
            root.geometry('+%d+%d' % (winPos_x, winPos_y))
    else:
        fallSpeed = 3
    
    print(fallSpeed)
    root.after(10, task)

root.after(10, task)
root.mainloop()