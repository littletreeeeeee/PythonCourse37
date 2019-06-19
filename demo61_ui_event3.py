# encoding=UTF-8
import tkinter
from tkinter import  font

def callback1():
    label1.config(text='buy iphonexs max')
def callback2():
    label1.config(text='buy pixel4')

#合併為如下 可以只Call callback 或分開
def callback():
    if var1.get()==1:
        label1.config(text='buy iphonexs max')
    elif var1.get()==2:
        label1.config(text='buy pixel4')

top = tkinter.Tk()
var1 = tkinter.IntVar()
var1.set(1) # option initial value
myFont = font.Font(family='Verdana', size=30)
myCFont = font.Font(family='Microsoft YaHei UI', size=30)
label1 = tkinter.Label(top, text="label1", font=myFont)
rb1 = tkinter.Radiobutton(top, text='iOS', font=myCFont, value=1, variable=var1, command=callback1)
rb2 = tkinter.Radiobutton(top, text='android', font=myCFont, value=2, variable=var1, command=callback2)
label1.pack()
rb1.pack()
rb2.pack()
top.minsize(400, 300)
top.mainloop()