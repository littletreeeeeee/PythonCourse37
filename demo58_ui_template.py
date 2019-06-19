# File/Settings
# Editor/Live Template
# main ==> tkmain (複製main)
# Description: a simpleUI
# encoding=UTF-8


import tkinter
from tkinter import  font


def callback1(ev):
    label.config(text="enter event:", bg='#F00')


def callback2(ev):
    label.config(text="leave event:", bg='#0F0')


def callback3():
    label.config(text='clicked', bg='#FFF')


top = tkinter.Tk()
myFont = font.Font(family='Verdana', size=30)
myCFont = font.Font(family='Microsoft YaHei UI', size=30)
label = tkinter.Label(top, text='display callback', bg='#FFF', font=myFont)
button = tkinter.Button(top, text='click me', font=myCFont, command=callback3)
label.pack()
button.pack()
button.bind('<Enter>', callback1)
button.bind('<Leave>', callback2)

top.minsize(400, 300)
top.mainloop()