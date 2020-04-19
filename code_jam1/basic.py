from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import sqlite3
import time
import datetime
import random
import smtplib

conn = sqlite3.connect('students.db')
c = conn.cursor()

def mail(usr_name):
    # creates SMTP session 
    s = smtplib.SMTP('smtp.cc.iitk.ac.in', 25) 
  

    s.starttls() 
  
# Authentication 
    s.login("abcd@iitk.ac.in", "********") 
  
# message to be sent 
    message = "There is an emergency. We need the supply of"+cmb.get()+" .Please help by donating it."
  
# sending the mail 
    s.sendmail("abc@iitk.ac.in", usr_name+"@iitk.ac.in", message) 
  
# terminating the session 
    s.quit() 


def checkcmbo():

    if cmb.get() == "A+":
        c.execute('SELECT * FROM students WHERE blood_group == "A+"')
        data1 = c.fetchall()
        for row in data1:
            mail(row[1])

        c.execute('SELECT * FROM students WHERE blood_group == "A-"')
        data2 = c.fetchall()
        for row in data2:
            mail(row[1])
        c.execute('SELECT * FROM students WHERE blood_group == "O+"')
        data3 = c.fetchall()
        for row in data3:
            mail(row[1])
        c.execute('SELECT * FROM students WHERE blood_group == "O-"')
        data4 = c.fetchall()
        for row in data4:
            mail(row[1])
        messagebox.showinfo('STUDENT LIST', 'mails have been sent successfully')    




    elif cmb.get() == "A-":
        c.execute('SELECT * FROM students WHERE blood_group == "A-"')
        data1 = c.fetchall()
        for row in data1:
            mail(row[1])
        c.execute('SELECT * FROM students WHERE blood_group == "O-"')
        data2 = c.fetchall()
        for row in data2:
            mail(row[1])
        messagebox.showinfo('STUDENT LIST', 'mails have been sent successfully')

    elif cmb.get() == "B+":
        c.execute('SELECT * FROM students WHERE blood_group == "B+"')
        data1 = c.fetchall()
        for row in data1:
            mail(row[1])
        c.execute('SELECT * FROM students WHERE blood_group == "B-"')
        data2 = c.fetchall()
        for row in data2:
            mail(row[1])
        c.execute('SELECT * FROM students WHERE blood_group == "O+"')
        data3 = c.fetchall()
        for row in data3:
            mail(row[1])
        c.execute('SELECT * FROM students WHERE blood_group == "O-"')
        data4 = c.fetchall()
        for row in data4:
            mail(row[1])
        messagebox.showinfo('STUDENT LIST', 'mails have been sent successfully')



    elif cmb.get() == "B-":
        c.execute('SELECT * FROM students WHERE blood_group == "B-"')
        data = c.fetchall()
        for row in data:
            mail(row[1])
        c.execute('SELECT * FROM students WHERE blood_group == "O-"')
        data1 = c.fetchall()
        for row in data1:
            mail(row[1])
        messagebox.showinfo('STUDENT LIST', 'mails have been sent successfully')


    elif cmb.get() == "O+":
        c.execute('SELECT * FROM students WHERE blood_group == "O+"')
        data = c.fetchall()
        for row in data:
            mail(row[1])
        c.execute('SELECT * FROM students WHERE blood_group == "O-"')
        data1 = c.fetchall()
        for row in data1:
            mail(row[1])
        messagebox.showinfo('STUDENT LIST', 'mails have been sent successfully')

    elif cmb.get() == "O-":
        c.execute('SELECT * FROM students WHERE blood_group == "0-"')
        data = c.fetchall()
        for row in data:
            mail(row[1])
        messagebox.showinfo('STUDENT LIST', 'mails have been sent successfully')

    elif cmb.get() == "AB+":
        for row in students:
            mail(row[1])
        messagebox.showinfo('STUDENT LIST', 'mails have been sent successfully')

        
    else:
        c.execute('SELECT * FROM students WHERE blood_group == "AB-"')
        data = c.fetchall()
        for row in data:
            mail(row[1])
        c.execute('SELECT * FROM students WHERE blood_group == "B-"')
        data1 = c.fetchall()
        for row in data1:
            mail(row[1])
        c.execute('SELECT * FROM students WHERE blood_group == "A-"')
        data2 = c.fetchall()
        for row in data2:
            mail(row[1])
        c.execute('SELECT * FROM students WHERE blood_group == "O-"')
        data3 = c.fetchall()
        for row in data3:
            mail(row[1])   
        messagebox.showinfo('STUDENT LIST', 'mails have been sent successfully')            



window = Tk()

window.title("Welcome To BLOOD-MAILING!xD")
window.geometry( '400x400')

lbl = Label(window, text="Select the required Blood Group")
lbl.grid(column=0, row=0)
cmb = Combobox(window)

cmb['values']= ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
btn = Button(window, text="Get Value",command=checkcmbo)
btn.grid(column=1,row=2)



cmb.grid(column=0, row=2)

window.mainloop()
