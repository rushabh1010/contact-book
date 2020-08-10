from tkinter import *
import datetime
from mypeople import *
from addpeople import *

date=datetime.datetime.now().date()
date=str(date)
class application(object):
    def __init__(self,master):
        self.master = master
#frame
        self.top=Frame(master, height=120,bg='blue')
        self.top.pack(fill=X)
        self.bottom=Frame(master, height=530,bg='white')
        self.bottom.pack(fill=X)
      #top frame
        self.top_image=PhotoImage(file="icons8-phone-contact-48.png")
        self.top_image_label=Label(self.top,image=self.top_image)
        self.top_image_label.place(x=120,y=30)
        self.heading=Label(self.top, text = 'my contact book',font='arial 15 bold',bg = 'blue',fg='orange')
        self.heading.place(x=180,y=40)
        self.date_lbl=Label(self.top,text="today's date: "+date,font="arial 10 bold",fg="orange",bg="blue")
        self.date_lbl.place(x=460,y=10)
        #BUTTON 1
        self.viewButton = Button(self.bottom,text="view people",fg="red",font="arial 12 bold",command=self.my_people)
        self.viewButton.place(x=250,y=30)
        #button 2
        self.addButton = Button(self.bottom, text="add people", font="arial 12 bold",command=self.add_people)
        self.addButton.place(x=250, y=90)
        #button 3
        self.aboutusButton = Button(self.bottom, text="about us", font="arial 12 bold")
        self.aboutusButton.place(x=250, y=150)

    def my_people(self):
        people=mypeople()

    def add_people(self):
        add_page=addpeople()
def main():
    root = Tk()
    app = application(root)
    root.title("contact app")
    root.geometry("650x550+350+200")
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()