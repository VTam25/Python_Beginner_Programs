from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)

window = Tk()
window.title("Clock GUI")

date_label = Label(window, font=("Ink Free", 20), fg="#C8A2C8")
date_label.pack()

time_label = Label(window, font=("Arial", 40), fg="white", bg="#C8A2C8")
time_label.pack()

day_label = Label(window, font=("Ink Free", 20), fg="#C8A2C8")
day_label.pack()


update()
window.mainloop()