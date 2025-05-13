
import os
import tkinter as tk
from tkinter import ttk, messagebox

NOTES_DIR = r"C:\Users\CTK\Documents\GitHub\Python-Boootcamp"

def center_window(win, width=600, height=400):
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.title("Bilješke")
center_window(root, 700, 500)
root.minsize(600, 400)

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(row=0, column=0, sticky="NSEW")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=3)
mainframe.columnconfigure(1, weight=2)
mainframe.rowconfigure(3, weight=1)

# Naziv
label_naziv = ttk.Label(mainframe, text="Naziv bilješke:")
label_naziv.grid(row=0, column=0, sticky="W", padx=(0, 5), pady=(0, 2))

entry_naziv = ttk.Entry(mainframe, width=40)
entry_naziv.grid(row=0, column=1, sticky="EW", pady=(0, 2))

# Sadržaj
label_sadrzaj = ttk.Label(mainframe, text="Sadržaj:")
label_sadrzaj.grid(row=1, column=0, sticky="NW", padx=(0, 5), pady=(0, 2))

text_frame = ttk.Frame(mainframe)
text_frame.grid(row=1, column=1, sticky="NSEW", pady=(0, 2))
text_frame.rowconfigure(0, weight=1)
text_frame.columnconfigure(0, weight=1)

text_sadrzaj = tk.Text(text_frame, width=50, height=12, wrap="word", font=("Segoe UI", 11))
text_sadrzaj.grid(row=0, column=0, sticky="NSEW")

scroll_text = ttk.Scrollbar(text_frame, orient="vertical", command=text_sadrzaj.yview)
scroll_text.grid(row=0, column=1, sticky="NS")
text_sadrzaj.config(yscrollcommand=scroll_text.set)

# Listbox for notes
label_lista = ttk.Label(mainframe, text="Pohranjene bilješke:")
label_lista.grid(row=2, column=0, sticky="W", padx=(0, 5), pady=(10, 2))

listbox_frame = ttk.Frame(mainframe)
listbox_frame.grid(row=3, column=0, sticky="NSEW", padx=(0, 5))
listbox_frame.rowconfigure(0, weight=1)
listbox_frame.columnconfigure(0, weight=1)

listbox_biljeske = tk.Listbox(listbox_frame, width=30, height=12, font=("Segoe UI", 10))
listbox_biljeske.grid(row=0, column=0, sticky="NSEW")

scroll_list = ttk.Scrollbar(listbox_frame, orient="vertical", command=listbox_biljeske.yview)
scroll_list.grid(row=0, column=1, sticky="NS")
listbox_biljeske.config(yscrollcommand=scroll_list.set)

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
    except Exception as e:
        messagebox.showerror("Greška", f"Dogodila se greška pri spremanju: {e}")

def osvjezi_listu():
    listbox_biljeske.delete(0, tk.END)
    try:
        files = sorted(fname for fname in os.listdir(NOTES_DIR) if fname.endswith(".txt"))
        for fname in files:
            listbox_biljeske.insert(tk.END, fname)
    except Exception as e:
        messagebox.showerror("Greška", f"Ne mogu učitati bilješke: {e}")

def ucitaj_biljesku(event):
    odabrano = listbox_biljeske.curselection()
    if not odabrano:
        return
    fname = listbox_biljeske.get(odabrano[0])
    try:
        with open(os.path.join(NOTES_DIR, fname), "r", encoding="utf-8") as f:
            sadrzaj = f.read()
        entry_naziv.delete(0, tk.END)
        entry_naziv.insert(0, fname[:-4])  # remove .txt
        text_sadrzaj.delete("1.0", tk.END)
        text_sadrzaj.insert("1.0", sadrzaj)
    except Exception as e:
        messagebox.showerror("Greška", f"Dogodila se greška pri učitavanju: {e}")

def clear_fields():
    entry_naziv.delete(0, tk.END)
    text_sadrzaj.delete("1.0", tk.END)
    listbox_biljeske.selection_clear(0, tk.END)

# Buttons
button_frame = ttk.Frame(mainframe)
button_frame.grid(row=4, column=0, columnspan=2, pady=(15, 0), sticky="EW")
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

btn_spremi = ttk.Button(button_frame, text="Spremi bilješku", command=spremi)
btn_spremi.grid(row=0, column=0, padx=5, sticky="EW")

btn_clear = ttk.Button(button_frame, text="Očisti polja", command=clear_fields)
btn_clear.grid(row=0, column=1, padx=5, sticky="EW")

btn_refresh = ttk.Button(button_frame, text="Osvježi listu", command=osvjezi_listu)
btn_refresh.grid(row=0, column=2, padx=5, sticky="EW")

listbox_biljeske.bind("<<ListboxSelect>>", ucitaj_biljesku)

osvjezi_listu()
root.mainloop()