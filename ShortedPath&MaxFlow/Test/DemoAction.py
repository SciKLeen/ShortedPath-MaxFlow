from tkinter import *

class buckysButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text='Print Message', command=self.printMessage())
        self.printButton.pack(side = LEFT)

    def printMessage(self):
        print("ahihi");

root = Tk()
b = buckysButtons(root)
root.mainloop()