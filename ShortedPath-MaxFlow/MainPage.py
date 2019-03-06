from tkinter.ttk import Frame, Button, Style
import Handling.Graph as Gr

from tkinter import *


#Khoi tao Cua so tren mang hinh
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        def showdata():
            print(et_name.get())
            print(et_des.get())

        self.parent.title("My Window")
        self.style = Style()
        self.style.theme_use("alt")

        TopFrame = Frame(self, relief=RAISED)
        TopFrame.pack(fill=X, padx=5, pady=5, expand=True)
        BotFrame = Frame(self, relief=RAISED, borderwidth=1)
        BotFrame.pack(side=BOTTOM, fill=X)
        self.pack(fill=BOTH, expand=True)


        layout_name = Frame(TopFrame)
        layout_des = Frame(TopFrame)
        layout_max = Frame(TopFrame)
        layout_name.pack(fill=X)
        layout_des.pack(fill=X)
        layout_max.pack(fill=X)

        lbl_name = Label(layout_name, text="Enter the point:")
        lbl_des = Label(layout_des, text="Enter destination:")
        lbl_name.pack(side=LEFT)
        lbl_des.pack(side=LEFT)

        et_name = Entry(layout_name, width=20)
        et_des = Entry(layout_des, width=20)
        et_name.pack(side=RIGHT)
        et_des.pack(side=RIGHT)


        def _Click_Btn_Ok():
            X = et_name.get()
            Y = et_des.get()
            Gr.main(X, Y)

        #Bottom Button
        closeButton = Button(BotFrame, text="Close", command=self.quit)
        okButton = Button(BotFrame, text="OK", command = _Click_Btn_Ok)
        closeButton.pack(side=RIGHT, padx = 10, pady=10)
        okButton.pack(side=RIGHT)





root = Tk()
root.geometry("300x200+500+300")
app = Example(root)
root.mainloop()



#nhấn vào nút ok nhiều lần vẫn còn tạo ra nhiều đồ thị mới
