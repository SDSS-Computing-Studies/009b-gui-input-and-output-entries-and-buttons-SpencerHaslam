"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""
import tkinter as tk 
from tkinter import *


win = tk.Tk()

eoutput = StringVar()
eoutput.set("Name")

varName = StringVar()
varName.set("hi")

"""
x = 10  regular python
x.set(10) tkinter python

regular python
data = input("Enter a number")
print(data)

tkinter
data = Entry1.get()
Entry2.set(data)

def updateA2():
    input = e1.get()
    varName.set(input)

def clickFunction():
    number = e1.get()
    number = float(number)



    answer = 2* number
    # Note...the insert method will insert output into the entry widget, with the
    # integer first parameter being the position in the Entry widget.  If there is
    # data already there, it'll confuse your output, so you need to delete the 
    # current contents
    # the Entry.delete() method takes 2 parameters, the start of the text you want
    # to delete, and the ending of the text you want to delete.  If you're not sure
    # of the length, you can delete using the special value END to go all the way
    # to the end of the entry widget
    a_entry.delete(0,END)
    a_entry.insert(0,answer)


l1 = Label(win, textvariable=eoutput)
e1 = Entry(win, width=20)
b1 = Button(win, text="Click to double", command=clickFunction)
a_label = Label(win, textvariable = varName)
a_entry = Entry(win, width=20)

l1.grid(row=1,column=1)
e1.grid(row=1,column=2)
b1.grid(row=2, column=1, columnspan=2)
a_label.grid(row=3,column=1)
a_entry.grid(row=3,column=2)



win.mainloop()