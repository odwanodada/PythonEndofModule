from tkinter import *
from tkinter import messagebox
import random
from datetime import date
from datetime import time
import random
from random import seed
from random import randint
w2 = Tk()
w2.title("Play Lotto")
w2.geometry("400x400")
w2.config(bg="yellow")



def play():
    a = int(num1.get())
    b = int(num2.get())
    c = int(num3.get())
    d = int(num4.get())
    e = int(num5.get())
    f = int(num6.get())

    mynumbers = [a,b,c,d,e,f]
    return mynumbers


def random_num():
    Lottonumbers = []
    for x in range(6):
        newrandom = random.randint(1,49)
        if newrandom not in Lottonumbers:
            Lottonumbers.append(newrandom)
            num1_text.insert("1.0", str(Lottonumbers[0]))
            num2_text.insert("1.0", str(Lottonumbers[1]))

        return Lottonumbers


def compare():
    mynumbers = play()
    Lottonumbers= random_num()

    result = [y for y in mynumbers if y in Lottonumbers]

    # if (mynumbers) < 0 or (mynumbers) > 49:
    #     messagebox.showinfo("Get Ready", "Get ready to play")
    # if len(Lottonumbers) == len(mynumbers):
    #     if len(mynumbers) == 6:
    #         messagebox.showinfo("winer", "You won")
    if len(result) == 6:
        messagebox.showinfo("lotto", "You Won R10, 000 000.00")
    elif len(result) == 5:
        messagebox.showinfo("lotto", "You Won R8,584.00")

    elif len(result) == 4:
        messagebox.showinfo("lotto", "You Won R2,384.00")

    elif len(result) == 3:
        messagebox.showinfo("lotto", "You Won R100.50")

    elif len(result) == 2:
        messagebox.showinfo("lotto", "You Won R20.00")

    elif len(result) == 1:
        messagebox.showinfo("lotto", "You Won R0.00")



num1 = Entry(w2, width=5)
num1.place(x=30, y=100)

num2 = Entry(w2, width=5)
num2.place(x=80, y=100)

num3 = Entry(w2, width=5)
num3.place(x=130, y=100)

num4 = Entry(w2, width=5)
num4.place(x=180, y=100)

num5= Entry(w2, width=5)
num5.place(x=230, y=100)

num6= Entry(w2, width=5)
num6.place(x=280, y=100)


play_button = Button(w2, text="PlAY ", bg="magenta", command=compare)
play_button.place(x=80, y=150)

num1_text = Text(w2,width=7,height=3,bg="blue")
num1_text.place(x=30, y=190)

num2_text = Text(w2,width=7,height=3,bg="red")
num2_text.place(x=120, y=190)



w2.mainloop()
