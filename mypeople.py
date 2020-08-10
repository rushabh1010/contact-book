from tkinter import *
import sqlite3
import datetime
from addpeople import addpeople
date=datetime.datetime.now().date()
date=str(date)
conn=sqlite3.connect('hii.db')
cur=conn.cursor()

class mypeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x500+600+200")
        self.title("my people")
        self.resizable(False,False)

        self.top = Frame(self, height=120, bg='blue')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=530, bg='white')
        self.bottom.pack(fill=X)
        # top frame
        self.top_image = PhotoImage(file="icons8-phone-contact-48.png")
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=120, y=30)
        self.heading = Label(self.top, text='my contact book', font='arial 15 bold', bg='blue', fg='orange')
        self.heading.place(x=180, y=40)
        self.date_lbl = Label(self.top, text="today's date: " +date, font="arial 10 bold", fg="orange", bg="blue")
        self.date_lbl.place(x=460, y=10)

        self.scroll=Scrollbar(self.bottom,orient=VERTICAL)

        self.listBox=Listbox(self.bottom,width=60,height=27)
        self.listBox.grid(row=0,column=0,padx=(40,0))
        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.listBox.yview)
        persons=cur.execute("select * from 'hello'").fetchall()
        count =0
        for person in persons:
            self.listBox.insert(count,str(person[0])+". "+person[1]+" "+person[2])
            count+=1
        self.scroll.grid(row=0,column=1,sticky=N+S)

def add_people(self):
    add_page=addpeople()
    self.destroy()