from tkinter import *
from tkinter import ttk
from queue import Queue
import random

walkingRightPath = "D:\Ethan\PersonalProject\Dekstop 'goddayz'\walking(250x250).gif"
walkingLeftPath = "D:\Ethan\PersonalProject\Dekstop 'goddayz'\walking_facing_left(250x250).gif"
idleRightPath = "D:\Ethan\PersonalProject\Dekstop 'goddayz'\idle(250x250).png"
idleLeftPath = "D:\Ethan\PersonalProject\Dekstop 'goddayz'\idle_facing_left(250x250).png"

class Ethan:
    # Variables
    fallSpeed = 3
    root = None
    winWidth = None
    winHeight = None
    screenWidth = None
    screenHeight = None
    windowDragging = False
    x, y = 0, 0
    stopLoop = Queue()
    changeFrame = 0
    changeState = 0
    state = "IDLE"      # im to lazy to make a enum
    imageLable = None
    frameCountWalk = 0
    frm = None

    # frames
    walkingRightFrame2 = []
    walkingLeftFrame = []
    idleRightFrame = None
    idleLeftFrame = None

    # Constructor
    def __init__(self, xPos, yPos) :
        self.root = Toplevel()
        self.root.overrideredirect(True)
        self.frm = ttk.Label(self.root)
        defaultBgColor = self.root.cget('bg')
        self.root.wm_attributes('-transparentcolor', defaultBgColor)
        self.frm.grid()
        self.root.attributes("-topmost", True)
        self.root.geometry('%dx%d' % (262, 262))
        self.root.geometry('+%d+%d' % (xPos, yPos))
        self.root.update_idletasks()

        # bind the grip functions
        self.root.bind("<B1-Motion>", self.mouseMove)
        self.root.bind("<ButtonRelease-1>", self.mouseRelease)
        self.root.bind("<Button-1>", self.mousePress)

        # import idle picture
        idle = PhotoImage(file=idleRightPath)
        self.imageLable = Label(self.frm, image = idle)
        self.imageLable.grid(column=0, row=0)
        self.imageLable.image = idle

        # load animations
        self.loadWalkAnimation()

        # get widget dimensions
        self.winWidth = self.root.winfo_width()
        self.winHeight = self.root.winfo_height()
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()

        # do the deed
        self.root.update_idletasks()
        self.startEthan()
    

    # the grip of '87
    def mousePress(self, event):
        self.x, self.y = event.x , event.y
        self.windowDragging = True
    
    def mouseMove(self, event):
        deltaX = event.x - self.x
        deltaY = event.y - self.y
        newX = self.root.winfo_x() + deltaX
        newY = self.root.winfo_y() + deltaY
        self.root.geometry('+%d+%d' % (newX, newY))
    
    def mouseRelease(self, event):
        self.windowDragging = False
        if self.root.winfo_y() >= ((self.screenHeight - 48) - self.winHeight):
            goodY = (self.screenHeight - 48) - self.winHeight
            self.root.geometry('+%d+%d' % (self.root.winfo_x(), goodY))
    
    # load all animation frames
    def loadWalkAnimation(self):
        # <right walk>
        self.walkingRightFrame2.append(PhotoImage(file=walkingRightPath, format="gif -index 0"))
        self.walkingRightFrame2.append(PhotoImage(file=walkingRightPath, format="gif -index 1"))
        self.walkingRightFrame2.append(PhotoImage(file=walkingRightPath, format="gif -index 2"))
        self.walkingRightFrame2.append(PhotoImage(file=walkingRightPath, format="gif -index 3"))
        self.walkingRightFrame2.append(PhotoImage(file=walkingRightPath, format="gif -index 4"))
        self.walkingRightFrame2.append(PhotoImage(file=walkingRightPath, format="gif -index 5"))
        self.walkingRightFrame2.append(PhotoImage(file=walkingRightPath, format="gif -index 6"))
        self.walkingRightFrame2.append(PhotoImage(file=walkingRightPath, format="gif -index 7"))
        self.walkingRightFrame2.append(PhotoImage(file=walkingRightPath, format="gif -index 8"))
        self.walkingRightFrame2.append(PhotoImage(file=walkingRightPath, format="gif -index 9"))
        self.walkingRightFrame2.append(PhotoImage(file=walkingRightPath, format="gif -index 10"))
        self.walkingRightFrame2.append(PhotoImage(file=walkingRightPath, format="gif -index 11"))
        self.walkingRightFrame2.append(PhotoImage(file=walkingRightPath, format="gif -index 12"))
        self.walkingRightFrame2.append(PhotoImage(file=walkingRightPath, format="gif -index 13"))
        # </right walk>

        # <left walk>
        self.walkingLeftFrame.append(PhotoImage(file=walkingLeftPath, format="gif -index 0"))
        self.walkingLeftFrame.append(PhotoImage(file=walkingLeftPath, format="gif -index 1"))
        self.walkingLeftFrame.append(PhotoImage(file=walkingLeftPath, format="gif -index 2"))
        self.walkingLeftFrame.append(PhotoImage(file=walkingLeftPath, format="gif -index 3"))
        self.walkingLeftFrame.append(PhotoImage(file=walkingLeftPath, format="gif -index 4"))
        self.walkingLeftFrame.append(PhotoImage(file=walkingLeftPath, format="gif -index 5"))
        self.walkingLeftFrame.append(PhotoImage(file=walkingLeftPath, format="gif -index 6"))
        self.walkingLeftFrame.append(PhotoImage(file=walkingLeftPath, format="gif -index 7"))
        self.walkingLeftFrame.append(PhotoImage(file=walkingLeftPath, format="gif -index 8"))
        self.walkingLeftFrame.append(PhotoImage(file=walkingLeftPath, format="gif -index 9"))
        self.walkingLeftFrame.append(PhotoImage(file=walkingLeftPath, format="gif -index 10"))
        self.walkingLeftFrame.append(PhotoImage(file=walkingLeftPath, format="gif -index 11"))
        self.walkingLeftFrame.append(PhotoImage(file=walkingLeftPath, format="gif -index 12"))
        self.walkingLeftFrame.append(PhotoImage(file=walkingLeftPath, format="gif -index 13"))
        # </left walk>

        self.idleRightFrame = PhotoImage(file=idleRightPath)
        self.idleLeftFrame = PhotoImage(file=idleLeftPath)

    # main loop
    def task(self):
        setPos = False
        winPos_x = self.root.winfo_x()
        winPos_y = self.root.winfo_y()
        
        # <animation code>
        if self.state == "IDLE":
            self.state == "IDLE"
        elif self.state == "WALK LEFT":
            if self.changeFrame == 0:   # change to the next frame
                self.imageLable.configure(image=self.walkingLeftFrame[self.frameCountWalk])
                
                self.frameCountWalk += 1
                if self.frameCountWalk > 13:
                    self.frameCountWalk = 0
            
            if not self.windowDragging :
                winPos_x -= 3

            self.state == "WALK LEFT"
        elif self.state == "WALK RIGHT":
            if self.changeFrame == 0:   # change to the next frame
                self.imageLable.configure(image=self.walkingRightFrame2[self.frameCountWalk])
                
                self.frameCountWalk += 1
                if self.frameCountWalk > 13:
                    self.frameCountWalk = 0
            
            if not self.windowDragging :
                winPos_x += 3

            self.state == "WALK RIGHT"
        
        self.changeFrame += 1           # each frame took 40 milliseconds each
        if self.changeFrame == 3:       # if changeFrame goes to 0, then we change frame
            self.changeFrame = 0
        # </animation code>

        # <state movement code>
        self.changeState += 1
        if self.changeState == 200:
            self.changeState = 0
            randomPicks = [True, False]
            # 50/50 whether to change state or not.
            if random.choice(randomPicks):
                if random.choice(randomPicks):
                    self.state = "WALK LEFT"
                    self.changeFrame = 0
                else:
                    self.state = "WALK RIGHT"
                    self.changeFrame = 0
            else:
                if self.state == "WALK LEFT":
                    self.imageLable.configure(image=self.idleLeftFrame)
                elif self.state == "WALK RIGHT":
                    self.imageLable.configure(image=self.idleRightFrame)
                self.state = "IDLE"
        # </state movement code>

        # <falling and movement code>
        if not self.windowDragging :

            if winPos_x < 0:
                winPos_x = 0
            elif winPos_x > (self.screenWidth - self.winWidth):
                winPos_x = self.screenWidth - self.winWidth

            if winPos_y < ((self.screenHeight - 48) - self.winHeight):
                winPos_y += self.fallSpeed
                self.fallSpeed *= 1.1
                if self.fallSpeed > 25:
                    self.fallSpeed = 25
                setPos = True

            if winPos_y >= ((self.screenHeight - 48) - self.winHeight) and setPos:
                winPos_y = (self.screenHeight - 48) - self.winHeight
                self.fallSpeed = 3
            self.root.geometry('+%d+%d' % (winPos_x, winPos_y))
            

        else:
            self.fallSpeed = 3
        # </falling and movement code>

        self.root.after(10, self.task)
    
    def murder(self):
        self.stopLoop.put(1)
        self.root.destroy()
        return

    def startEthan(self):
        self.root.after(10, self.task)