import tkinter

from time import strftime

root = tkinter.Tk()

root.title("Digital Clock")

myClock = tkinter.Label()

myClock.pack()

myClock["font"] = "Algerian 80 bold"

myClock["fg"] = "yellow"

myClock["bg"] = "black"

def run():

    myClock["text"] = strftime("%H:%M:%S")
 
    myClock.after(1000, run)

run()
