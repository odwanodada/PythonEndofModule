from tkinter import *
from tkinter import messagebox
from datetime import *


w = Tk()
w.title("Lotto")
w.geometry("400x400")
w.config(bg="yellow")


def check():
    age = int(age_entry.get())
    name = user_entry.get()
    if (age>=18):
        messagebox.showinfo("INFO", "You qualify to play")
        f = open("results.txt", "a+")
        f.write("name:" + name +"\n")
        f.write("age:" + str(age) + "\n")
        f.close()
        w.withdraw()
        import play
        play.verify()
    else:
        messagebox.showinfo("INFO", "Under age to play")
        user_entry.delete(0, END)
        age_entry.delete(0, END)




date = datetime.now()
date_lbl= Label(w)
date_lbl.pack()
date_lbl.config(text="date" + date.strftime(" %d/ %m/ %y "))

time = datetime.now()
time_lbl= Label(w)
time_lbl.pack()
time_lbl.config(text="time" + time.strftime(" %H: %M"))


user_lbl=Label(w, text="Username:")
user_lbl.pack()

user_entry=Entry(w, textvariable="username")
user_entry.pack()

age_lbl=Label(w, text="Age:")
age_lbl.pack()

age_entry=Entry(w, textvariable="Age")
age_entry.pack()

check_button= Button(w, text="Check ", bg="magenta",command=check).pack()


w.mainloop()