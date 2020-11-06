"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""
#! python3

import tkinter as tk 
from tkinter import *

win = tk.Tk()
myLabel = StringVar()
myLabel2 = StringVar()
myLabel3 = StringVar()

def click():
    input1 = eName.get()
    input2 = eAdjective.get()
    input3 = eNoun.get()
    eIduhno.delete(0,END)
    eIduhno.insert(0,input1)
    myLabel.set(input1)
    myLabel2.set(input2)
    myLabel3.set(input3)
    Pls.grid(row=5,column=3,sticky=W)
    Who.grid(row=5,column=5,sticky=W)
    To.grid(row=5,column=7,sticky=W)
    cless.grid(row=5,column=9,sticky=W)

eName = Entry(win)
eAdjective = Entry(win)
eIduhno = Entry(win)
b1 = Button(win,text='Place words',command=click)
l1 = Label(win, textvariable=myLabel)
lName = Label(win, text= 'Enter a Name')
lAdjective = Label(win, text= 'Enter an Adjective')
l2 = Label(win, textvariable=myLabel2)
eNoun = Entry(win)
lNoun = Label(win, text= 'Enter a Noun')
l3 = Label(win, textvariable=myLabel3)
Pls = Label(win, text="Please excuse")
Who = Label(win, text="who is far too")
To = Label(win,text="to attend")
cless = Label(win,text="class.")
lab = Label(win,text = "      ")

lName.grid(row=1,column=1)
eName.grid(row=1,column=2)
b1.grid(row=4,column=1)
lAdjective.grid(row=2,column=1)
eAdjective.grid(row=2, column=2)
lNoun.grid(row=3,column=1)
eNoun.grid(row=3, column=2)
l1.grid(row=5,column=4,sticky=W)
l2.grid(row=5,column=6,sticky=W)
l3.grid(row=5,column=8,sticky=W)
lab.grid(row=5, column=1,columnspan=2)

win.mainloop()