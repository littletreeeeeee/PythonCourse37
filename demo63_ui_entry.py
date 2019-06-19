# encoding=UTF-8
import tkinter
from tkinter import  font
top = tkinter.Tk()
myFont = font.Font(family='Verdana', size=30)
myCFont = font.Font(family='Microsoft YaHei UI', size=30)
label1 = tkinter.Label(top, text="input something", font=myCFont)
entry1 = tkinter.Entry(top, font=myCFont)
button1 = tkinter.Button(top, text='submit', font=myCFont)
label1.pack()
entry1.pack()
button1.pack()
top.minsize(400, 300)
top.mainloop()
