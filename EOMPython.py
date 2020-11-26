from tkinter import *
from tkinter import messagebox


w = Tk()
w.title("Lotto")
w.geometry("400x400")
w.config(bg="yellow")


def check():
    age = int(age_entry.get())
    if (age>=18):
        messagebox.showinfo("INFO", "You qualify to play")
        w.withdraw()
        import play
        play.verify()
    else:
        messagebox.showinfo("INFO", "Under age to play")
        user_entry.delete(0, END)
        age_entry.delete(0, END)






user_lbl=Label(w, text="Username")
user_lbl.pack()

user_entry=Entry(w, textvariable="username")
user_entry.pack()

age_lbl=Label(w, text="Age:")
age_lbl.pack()

age_entry=Entry(w, textvariable="Age")
age_entry.pack()

check_button= Button(w, text="Check ", bg="magenta",command=check).pack()


w.mainloop()