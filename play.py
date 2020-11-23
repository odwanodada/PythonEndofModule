from tkinter import *
from tkinter import messagebox
from datetime import date
from datetime import time
w2 = Tk()
w2.title("Play Lotto")
w2.geometry("400x400")
w2.config(bg="pink")


# Create a frame
frame = LabelFrame(w2, bg="pink", text="LottoIthuba", font=("arial", 10, "bold"), pady=45, padx=45)
frame.grid(row=0, columnspan=2, padx=10, pady=10)

# pack label and Entry inside the frame
label1 = Label(frame, text="Enter Amount:", bg="pink", font=("arial", 10, "bold"))
label1.pack()

amount_input = Entry(frame)
amount_input.grid(row=4,column=5)


amount_input = Entry(frame)
amount_input.grid(row=4,column=7)








w2.mainloop()