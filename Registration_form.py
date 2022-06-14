from cgitb import text
from inspect import getargvalues
from tkinter  import *
from tkinter import font

from click import command

root= Tk()

#for frame
root.geometry("400x400")

#Title for frame
root.title("Registration") 

def getvals():
    print("accepted")

#form labeling with packing
Label(root,text="Registration Form", font="arial 16 bold").grid(row=0,column=3)

#field name with packing
name=Label(root, text="Name",font="arial 10 bold").grid(row=3,column=2)
phone=Label(root, text="Phone",font="arial 10 bold").grid(row=4,column=2)
gender=Label(root, text="Gender",font="arial 10 bold").grid(row=5,column=2)
email=Label(root, text="Email",font="arial 10 bold").grid(row=6,column=2)

#variable for storing Data
name_value=StringVar
phone_value=StringVar
gender_value=StringVar
email_value=StringVar
check_value=IntVar

#entry fields and packing
entry_name=Entry(root, textvariable=name_value).grid(row=3, column=3)
entry_phone=Entry(root, textvariable=phone_value).grid(row=4, column=3)
entry_gender=Entry(root, textvariable=gender_value).grid(row=5, column=3)
entry_email=Entry(root, textvariable=email_value).grid(row=6, column=3)

#creating check Button
checkbtn= Checkbutton(text="Remember me?", variable=check_value).grid(row=7, column=3)

#submit button and pack

Button(text="Submit", command=getvals).grid(row=8, column=3)


root.mainloop()