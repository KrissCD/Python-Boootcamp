from tkinter import *
import datetime

def update_clock():
    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    digital_clock.config(text=current_time)  
    root.after(1000, update_clock)

root = Tk()
root.title("Digital Clock")

digital_clock = Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
digital_clock.pack(pady=20)

update_clock()  

root.mainloop()