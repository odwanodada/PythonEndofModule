from tkinter import *
from tkinter import messagebox
import random
from datetime import date
from datetime import time
w2 = Tk()
w2.title("Play Lotto")
w2.geometry("400x400")
w2.config(bg="yellow")


def verify():
    messagebox.showinfo("you guys are crazy")
    mycheck=Button(w2, text="check status", command=verify)
    mycheck.pack()

def play():
    Lottonumbers = []
    a = int(num1.get())
    b = int(num2.get())
    c = int(num3.get())
    d = int(num4.get())
    e = int(num5.get())
    f = int(num6.get())

    mynumbers= sorted([a, b, c, d, e, f])


    for x in range(6):
        newrandom=random.randint(1,49)
        Lottonumbers.append(newrandom)
    print(Lottonumbers)



    result=[y for y in mynumbers if y in Lottonumbers]
    print(result)




num1 = Entry(w2, width=3)
num1.place(x=30, y=100)

num2 = Entry(w2, width=3)
num2.place(x=80, y=100)

num3 = Entry(w2, width=3)
num3.place(x=130, y=100)

num4 = Entry(w2, width=3)
num4.place(x=180, y=100)

num5= Entry(w2, width=3)
num5.place(x=230, y=100)

num6= Entry(w2, width=3)
num6.place(x=280, y=100)


play_button = Button(w2, text="PlAY ", bg="magenta", command=play)
play_button.place(x=320, y=120)


w2.mainloop()