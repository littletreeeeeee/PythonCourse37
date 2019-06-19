# encoding=UTF-8
import tkinter
from tkinter import  font
def callback1(ev):
    label1.config(text=message % int(ev))


message = 'value=%d'
top = tkinter.Tk()
var1 = tkinter.IntVar()
myFont = font.Font(family='Verdana', size=30)
myCFont = font.Font(family='Microsoft YaHei UI', size=30)
label1 = tkinter.Label(top, text=message % 0, font=myFont)
scale1 = tkinter.Scale(top, font=myCFont, orient='h', from_=0, to=100,
                       showvalue=False, variable=var1, command=callback1)
label1.pack()
scale1.pack()
top.minsize(400, 300)
top.mainloop()