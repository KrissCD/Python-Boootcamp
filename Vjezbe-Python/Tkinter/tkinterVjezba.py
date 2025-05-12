from tkinter import *

root = Tk()
root.title("Kalkulator")

a = Entry(root, width = 20)
a.grid(row = 0,column=0)

b = Entry(root, width = 20)
b.grid(row = 0,column=1)

tipka = Button(root, text="Zbrajanje", command=lambda: Zbrajanje(int(a.get()), int(b.get())))
tipka.grid(row=1,column=0)
tipka = Button(root, text="Oduzimanje", command=lambda: Oduzimanje(int(a.get()), int(b.get())))
tipka.grid(row=1,column=1)
tipka = Button(root, text="Mnozenje", command=lambda: Mnozenje(int(a.get()), int(b.get())))
tipka.grid(row=2,column=0)
tipka = Button(root, text="Dijeljenje", command=lambda: Dijeljenje(int(a.get()), int(b.get())))
tipka.grid(row=2,column=1)

labela = Label(root,text="Ovdje se prikazuje rezultat")
labela.grid(row=3,column=0)

def Zbrajanje(a,b):
    rezultat = a + b
    labela.config(text="Zbroj je: " + str(rezultat))
    return
def Oduzimanje(a,b):
    rezultat = a - b
    labela.config(text="Razlika je: " + str(rezultat))
    return
def Mnozenje(a,b):
    rezultat = a * b
    labela.config(text="Umnozak je: " + str(rezultat))
    return
def Dijeljenje(a,b):    
    if b != 0:
        rezultat = a / b
        labela.config(text="Kolicnik je: " + str(rezultat))
    else:
        labela.config(text="Dijeljenje s nulom nije dozvoljeno")
    return
root.mainloop()
