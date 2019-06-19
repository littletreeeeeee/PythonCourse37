#encoding=UTF-8
import tkinter
from tkinter import font
top = tkinter.Tk()
#print( tkFont.families())
for f in font.families():
    print( f)
print()
myFont = font.Font(family='Verdana', size=30)
myCFont = font(family='Microsoft YaHei UI', size=30)
label1 = tkinter.Label(top, text="Hello world1", pady=30, bg='#C0FFEE', font=myFont)
label2 = tkinter.Label(top, text="welcome", padx=30, bg='#FFEEC0', font=myFont)
label3 = tkinter.Label(top, text='橫逸資訊', font=myCFont, fg='#990000', bg='#EEFFC0',
                       padx=20, pady=40)
label2.pack()
label1.pack()
label3.pack()
top.mainloop()