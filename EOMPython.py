from tkinter import *
from tkinter import messagebox


w = Tk()
w.title("Lotto")
w.geometry("400x400")
w.config(bg="pink")

user_lbl=Label(w, text="Username")
user_lbl.pack()

user_entry=Entry(w, textvariable="username")
user_entry.pack()

age_lbl=Label(w, text="Age:")
age_lbl.pack()

age_entry=Entry(w, textvariable="Age")
age_entry.pack()

check_button= Button(w, text="Check ", bg="magenta").pack()


w.mainloop()