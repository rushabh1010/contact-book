from tkinter import *
import sqlite3
import datetime
from tkinter import messagebox
conn=sqlite3.connect('hii.db')
cur=conn.cursor()

date=datetime.datetime.now().date()
date=str(date)


class addpeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x500+600+200")
        self.title("add people")
        self.resizable(False,False)

        self.top = Frame(self, height=120, bg='blue')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=530, bg='white')
        self.bottom.pack(fill=X)
        # top frame
        self.top_image = PhotoImage(file="icons8-phone-contact-48.png")
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=120, y=30)
        self.heading = Label(self.top, text='add new person', font='arial 15 bold', bg='blue', fg='orange')
        self.heading.place(x=180, y=40)
        self.date_lbl = Label(self.top, text="today's date: " +date, font="arial 10 bold", fg="orange", bg="blue")
        self.date_lbl.place(x=460, y=10)

        #name
        self.label_name=Label(self.bottom,text="name",font="arial 15 bold",fg="black")
        self.label_name.place(x=40,y=40)
        self.entry_name=Entry(self.bottom,width=30,bd=4)
        self.entry_name.insert(0,"enter name")
        self.entry_name.place(x=150,y=40)
        #surname
        self.label_lastname = Label(self.bottom, text="last  name", font="arial 15 bold", fg="black")
        self.label_lastname.place(x=40, y=80)
        self.entry_lastname = Entry(self.bottom, width=30, bd=4)
        self.entry_lastname.insert(0, "enter surname")
        self.entry_lastname.place(x=150, y=80)
        #contact
        self.label_number = Label(self.bottom, text="number", font="arial 15 bold", fg="black")
        self.label_number.place(x=40,y=120)
        self.entry_number = Entry(self.bottom, width=10, bd=4)
        self.entry_number.insert(0, "enter number")
        self.entry_number.place(x=150, y=120)
        #submit button
        button=Button(self.bottom,text="add person",bg="blue",command=self.add_people)
        button.place(x=100,y=160)

    def add_people(self):
        name = self.entry_name.get()
        surname = self.entry_lastname.get()
        number = self.entry_number.get()

        if name and surname and number !="":
           try:
               '''database'''
               query="INSERT INTO 'hello'(name,surname,number) VALUES(?,?,?)"
               cur.execute(query,(name, surname, number))
               conn.commit()
               messagebox.showinfo("success","contact added")


           except EXCEPTION as e:
               messagebox.showerror("error",str(e))
        else:
            messagebox.showerror("Error", "fill all THE fields", icon='warning')