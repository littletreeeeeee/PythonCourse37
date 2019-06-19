# encoding=UTF-8
import tkinter
from tkinter import  font


def callback1(ev):
    message1.config(text='move to[%d,%d]' % (ev.x, ev.y))


top = tkinter.Tk()
myFont = font.Font(family='Verdana', size=30)
myCFont = font.Font(family='Microsoft YaHei UI', size=30)
message1 = tkinter.Message(top, text="display coordinate", font=myCFont, bg='#C0FFEE')
message1.pack()
message1.bind('<Motion>', callback1)
top.minsize(400, 300)
top.mainloop()