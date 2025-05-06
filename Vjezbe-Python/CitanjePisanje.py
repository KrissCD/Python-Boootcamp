with open ('moj_tekst.txt', 'r+') as f:
    sadrzaj = f.read()
    f.seek(0)  # Vracamo se na pocetak datoteke
    f.write("Novi uvod.\n" + sadrzaj)
    

with open ('moj_tekst.txt', 'a+') as f:
    f.seek(0)
    sadrzaj = f.read()
    f.write("Dodatni tekst.\n")
    print(sadrzaj)

try:
    with open("novi_izvjestaj", "x") as f:
        f.write("kreirano samo ako je datoteka ne postoji")
except FileExistsError:
    print("datoteka vec postoji")