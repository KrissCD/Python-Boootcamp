import os

filename = 'Evidencija.txt'

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("Ime, Prezime, Ocjena\n")
    print(f"File '{filename}' created with a header row.")

def izbornik():
    with open(filename, 'a') as f:
        while True:
            line = input("Unesite redak (ime, prezime, ocjena) ili 'kraj' za povratak: ")
            if line.strip().lower() == 'kraj':
                break
            if line.count(',') != 2:
                print("Unesite redak u formatu: ime, prezime, ocjena")
                continue
            ime, prezime, ocjena = map(str.strip, line.split(','))
            if ocjena.isdigit() and 1 <= int(ocjena) <= 5:
                f.write(f"{ime}, {prezime}, {ocjena}\n")
                print("Unos dodan.")
            else:
                print("Ocjena mora biti broj između 1 i 5.")

def prikaz():
    with open(filename, 'r') as f:
        print("Sadržaj datoteke:")
        lines = f.readlines()
        for line in lines:
            print(line.strip())

def pretraga_po_prezimenu():
    prezime = input("Unesite prezime za pretragu: ").strip()
    with open(filename, 'r') as f:
        found = False
        for line in f:
            if prezime.lower() in line.lower().split(',')[1].strip():
                print(line.strip())
                found = True
        if not found:
            print("Nema zapisa s tim prezimenom.")

def obrisi_file():
    os.remove(filename)
    print(f"File '{filename}' obrisan.")
    with open(filename, 'w') as f:
        f.write("Ime, Prezime, Ocjena\n")
    print(f"File '{filename}' ponovno kreiran s početnim redom.")

def zamijeni():
    prikaz()
    redak_za_brisanje = input("Unesite točan redak koji želite zamijeniti: ").strip()
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        found = False
        for line in lines:
            if line.strip() == redak_za_brisanje:
                novi_redak = input("Unesite novi redak (ime, prezime, ocjena): ").strip()
                if novi_redak.count(',') == 2:
                    ime, prezime, ocjena = map(str.strip, novi_redak.split(','))
                    if ocjena.isdigit() and 1 <= int(ocjena) <= 5:
                        f.write(f"{ime}, {prezime}, {ocjena}\n")
                        print("Redak zamijenjen.")
                        found = True
                    else:
                        print("Ocjena mora biti broj između 1 i 5.")
                        f.write(line)  # Write the original line back
                else:
                    print("Unesite redak u formatu: ime, prezime, ocjena")
                    f.write(line) 
            else:
                f.write(line)
        if not found:
            print("Redak nije pronađen.")

while True:
    print("\nInteraktivni izbornik:")
    print("1. Dodaj novi unos")
    print("2. Prikaži sve unose")
    print("3. Pretraži po prezimenu")
    print("4. Obriši cijelu datoteku")
    print("5. Zamijeni redak")
    print("0. Izlaz")
    choice = input("Odaberite opciju: ").strip()

    if choice == '1':
        izbornik()
    elif choice == '2':
        prikaz()
    elif choice == '3':
        pretraga_po_prezimenu()
    elif choice == '4':
        obrisi_file()
    elif choice == '5':
        zamijeni()
    elif choice == '0':
        print("Izlaz iz programa.")
        break
    else:
        print("Nevažeća opcija. Pokušajte ponovno.")