from tkinter import *
from tkinter import messagebox
import random

w2 = Tk()
w2.title("Play Lotto")
w2.geometry("700x700")
w2.config(bg="yellow")


def savetofile():
    x = result ="\n "+ namestudent.get() + "  " + fscore.get()+"/4"
    messagebox.showinfo("results", "your results been saved successfuly")
    if int(enter_num4.get())==1:
        f = open('results C1.txt', 'a')
        f.write(result)
        f.close()
    if int(year.get())==2:
        f = open('results C2.txt', 'a')
        f.write(result)
        f.close()
    if int(year.get())==3:
        f = open('results C3.txt', 'a')
        f.write(result)
        f.close()

def play():
    a = int(enter_num1.get("1.0", END))
    b = int(enter_num2.get("1.0", END))
    c = int(enter_num3.get("1.0", END))
    d = int(enter_num4.get("1.0", END))
    e = int(enter_num5.get("1.0", END))
    f = int(enter_num6.get("1.0", END))

    mynumbers = [a,b,c,d,e,f]
    return mynumbers


def random_num():
    num1_text.delete("1.0", END)
    num2_text.delete("1.0", END)
    num3_text.delete("1.0", END)
    num4_text.delete("1.0", END)
    num5_text.delete("1.0", END)
    num6_text.delete("1.0", END)

    Lottonumbers = []
    for x in range(6):
        newrandom = random.randint(1,49)
        if newrandom not in Lottonumbers:
            Lottonumbers.append(newrandom)


    num1_text.insert("1.0", str(Lottonumbers[0]))
    num2_text.insert("1.0", str(Lottonumbers[1]))
    num3_text.insert("1.0", str(Lottonumbers[2]))
    num4_text.insert("1.0", str(Lottonumbers[3]))
    num5_text.insert("1.0", str(Lottonumbers[4]))
    num6_text.insert("1.0", str(Lottonumbers[5]))
    return Lottonumbers


def compare():
    mynumbers = play()
    Lottonumbers= random_num()

    result = [y for y in mynumbers if y in Lottonumbers]

    if len(result) == 6:
        messagebox.showinfo("lotto", "You Won R10, 000 000.00")
        enter_num1.delete('1.0', END)
        enter_num2.delete('1.0', END)
        enter_num3.delete('1.0', END)
        enter_num4.delete('1.0', END)
        enter_num5.delete('1.0', END)
        enter_num6.delete('1.0', END)

    elif len(result) == 5:
        messagebox.showinfo("lotto", "You Won R8,584.00")
        enter_num1.delete('1.0', END)
        enter_num2.delete('1.0', END)
        enter_num3.delete('1.0', END)
        enter_num4.delete('1.0', END)
        enter_num5.delete('1.0', END)
        enter_num6.delete('1.0', END)

    elif len(result) == 4:
        messagebox.showinfo("lotto", "You Won R2,384.00")
        enter_num1.delete('1.0', END)
        enter_num2.delete('1.0', END)
        enter_num3.delete('1.0', END)
        enter_num4.delete('1.0', END)
        enter_num5.delete('1.0', END)
        enter_num6.delete('1.0', END)

    elif len(result) == 3:
        messagebox.showinfo("lotto", "You Won R100.50")
        enter_num1.delete('1.0', END)
        enter_num2.delete('1.0', END)
        enter_num3.delete('1.0', END)
        enter_num4.delete('1.0', END)
        enter_num5.delete('1.0', END)
        enter_num6.delete('1.0', END)


    elif len(result) == 2:
        messagebox.showinfo("lotto", "You Won R20.00")


    elif len(result) == 1:
        messagebox.showinfo("lotto", "You Won R0.00")


def reset_all():
    num1_text.delete("1.0", END)
    num2_text.delete("1.0", END)
    num3_text.delete("1.0", END)
    num4_text.delete("1.0", END)
    num5_text.delete("1.0", END)
    num6_text.delete("1.0", END)

    enter_num1.delete('1.0', END)
    enter_num2.delete('1.0', END)
    enter_num3.delete('1.0', END)
    enter_num4.delete('1.0', END)
    enter_num5.delete('1.0', END)
    enter_num6.delete('1.0', END)

def exit_window():
    message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application')
    if message_box == 'yes':
        w2.destroy()
    else:
        pass






enter_num1 = Text(w2,width=7,height=3,bg="pink",font=("arial", 20, "bold"))
enter_num1.place(x=30, y=100)


enter_num2 = Text(w2,width=7,height=3,bg="pink",font=("arial", 20, "bold"))
enter_num2.place(x=120, y=100)

enter_num3 = Text(w2,width=7,height=3,bg="pink",font=("arial", 20, "bold"))
enter_num3.place(x=220, y=100)


enter_num4 = Text(w2,width=7,height=3,bg="pink",font=("arial", 20, "bold"))
enter_num4.place(x=320, y=100)


enter_num5 = Text(w2,width=7,height=3,bg="pink",font=("arial", 20, "bold"))
enter_num5.place(x=420, y=100)

enter_num6 = Text(w2,width=7,height=3,bg="pink",font=("arial", 20, "bold"))
enter_num6.place(x=520, y=100)







play_button = Button(w2, text="PLAY ", bg="magenta", command=compare)
play_button.place(x=80, y=280)

reset_button = Button(w2, text="RESET ", bg="magenta",command=reset_all)
reset_button.place(x=200, y=280)

exit_button = Button(w2, text="EXIT ", bg="magenta",command=exit_window)
exit_button.place(x=320, y=280)

num1_text = Text(w2,width=7,height=3,bg="green",font=("arial", 20, "bold"))
num1_text.place(x=30, y=350)

num2_text = Text(w2,width=7,height=3,bg="green",font=("arial", 20, "bold"))
num2_text.place(x=120, y=350)

num3_text = Text(w2,width=7,height=3,bg="green",font=("arial", 20, "bold"))
num3_text.place(x=220, y=350)

num4_text = Text(w2,width=7,height=3,bg="orange",font=("arial", 20, "bold"))
num4_text.place(x=320, y=350)

num5_text = Text(w2,width=7,height=3,bg="orange",font=("arial", 20, "bold"))
num5_text.place(x=420, y=350)

num6_text = Text(w2,width=7,height=3,bg="orange",font=("arial", 20, "bold"))
num6_text.place(x=520, y=350)



w2.mainloop()
