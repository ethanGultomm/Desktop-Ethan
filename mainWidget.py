from tkinter import *
from tkinter import ttk
from Ethan import *

# global variables
listOfEthans = []

root = Tk()
root.title("what python does to a man")
# root.overrideredirect(True)
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="--- The Ethan Machine ---").grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)
root.attributes("-topmost", True)
root.geometry('%dx%d' % (370, 150))
root.update_idletasks()
# functions for the buttons
def addOneEthan():
    # constructor for the Ethan class goes here, add it to the list of Ethans to kill later PogU
    global listOfEthans
    listOfEthans.append(Ethan(root.winfo_x(), root.winfo_y()))
    print(len(listOfEthans))

def destroyOneEthan():
    # destroy 1 Ethan from the list in a queue fashion
    global listOfEthans
    ethanToBeKilled = listOfEthans.pop(0)
    ethanToBeKilled.murder()
    del ethanToBeKilled

def destroyAllEthan():
    # destroy all instances of Ethan in the list
    global listOfEthans
    for x in range(len(listOfEthans)):
        ethanToBeKilled = listOfEthans.pop(0)
        ethanToBeKilled.murder()
        del ethanToBeKilled

ttk.Button(frm, text="Create 1 Ethan", command=addOneEthan).grid(column=0, row=1)
ttk.Button(frm, text="Destroy 1 Ethan", command=destroyOneEthan).grid(column=1, row=1)
ttk.Button(frm, text="Destroy ALL Ethan >:)", command=destroyAllEthan).grid(column=2, row=1)

root.mainloop()

# NOTED BUGS 23/12/2022:
#   - addOneEthan function stops after creating the Ethan object, possibly from the looping code of the Ethan. Try putting the loop code of the class on a thread.
#   - turns out it was the mainloop function of the Ethan widget i fucking hate everything