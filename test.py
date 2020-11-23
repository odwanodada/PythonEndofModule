from tkinter import *

def calculatemoney():
    done = float(Lines1.get())
    salary3 = done * 0.08
    salary4 = done * 1


    labelresult = Label(root, text='%.0f' % salary4).grid(row=3, column=2)
    labelresult = Label(root, text=' £ %.2f' % salary3).grid(row=4, column=2)

root = Tk()


root.title('Dict8 Calc')
root.geometry('250x200+800+100')
Lines1 = StringVar()
var1 = Label(root, text='Enter Lines').grid(row=0, column=1)
var2 = Label(root, text='Lines Today').grid(row=3, column=1)
var3 = Label(root, text='Money Today').grid(row=4, column=1)
var4 = Label(root, text='Lines Total').grid(row=6, column=1)
var5 = Label(root, text='Money Total').grid(row=7, column=1)
myLines = Entry(root, textvariable=Lines1).grid(row=0, column=2)

button1 = Button(root, text='  Calculate  ', command=calculatemoney).grid(row=8, column=2)


root.mainloop()
