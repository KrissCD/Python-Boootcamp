from tkinter import *
from tkinter import messagebox
import os

NOTES_DIR = r"C:\Users\CTK\Documents\GitHub\Python-Boootcamp"

root = Tk()
root.title("Biljeske")

label_naziv = Label(root, text="Naziv Biljeske")
label_naziv.grid(row=0, column=0)

entry_naziv = Entry(root, width=30)
entry_naziv.grid(row=1, column=0)

label_sadrzaj = Label(root, text="Sadrzaj")
label_sadrzaj.grid(row=2, column=0)

text_sadrzaj = Text(root, width=60, height=10)  
text_sadrzaj.grid(row=3, column=0)

def spremi():
    naziv = entry_naziv.get().strip()
    sadrzaj = text_sadrzaj.get("1.0", "end-1c")
    if not naziv:
        messagebox.showwarning("Upozorenje", "Unesite naziv bilješke!")
        return
    try:
        with open(os.path.join(NOTES_DIR, f"{naziv}.txt"), "w", encoding="utf-8") as f:
            f.write(sadrzaj)
        messagebox.showinfo("Uspjeh", f"Bilješka '{naziv}.txt' je spremljena.")
        osvjezi_listu()
        entry_naziv.delete(0, END)           
        text_sadrzaj.delete("1.0", END)      
    except Exception as e:
        messagebox.showerror("Greška", f"Dogodila se greška pri spremanju: {e}")
def osvjezi_listu():
    listbox_biljeske.delete(0, END)
    for fname in os.listdir(NOTES_DIR):
        if fname.endswith(".txt"):
            listbox_biljeske.insert(END, fname)

def ucitaj_biljesku(event):
    odabrano = listbox_biljeske.curselection()
    if not odabrano:
        return
    fname = listbox_biljeske.get(odabrano[0])
    try:
        with open(os.path.join(NOTES_DIR, fname), "r", encoding="utf-8") as f:
            sadrzaj = f.read()
        entry_naziv.delete(0, END)
        entry_naziv.insert(0, fname[:-4])  
        text_sadrzaj.delete("1.0", END)
        text_sadrzaj.insert("1.0", sadrzaj)
    except Exception as e:
        messagebox.showerror("Greška", f"Dogodila se greška pri učitavanju: {e}")

tipka = Button(root, text="Spremi Biljeske", command=spremi)
tipka.grid(row=4, column=0, pady=(5, 0), sticky="w")

label_lista = Label(root, text="Pohranjene bilješke:")
label_lista.grid(row=5, column=0, sticky="w")

listbox_biljeske = Listbox(root, width=60, height=8)
listbox_biljeske.grid(row=6, column=0, pady=(5,0), sticky="w")
listbox_biljeske.bind("<<ListboxSelect>>", ucitaj_biljesku)

osvjezi_listu()

root.mainloop()