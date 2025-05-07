import os

filename = 'Zapis.txt'

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("Ovo je prvi red!\n")
    print(f"File '{filename}' napravljena je datoteka i ispisan prvi red!.")
else:
    with open(filename, 'a') as f:
        while True:
            line = input("Unesite redak (ili 'kraj' za završetak): ")
            if line.strip().lower() == 'kraj':
                break
            if line.count(',') != 2:
                print("Unesite redak u formatu: ime, prezime, ocjena")
                continue
            ime, prezime, ocijena = map(str.strip, line.split(','))
            if ocijena.isdigit() and 1 <= int(ocijena) <= 5:
                f.write(line + '\n')
                print(int(ocijena))
            else:
                print("Ocjena mora biti broj.")

with open(filename, 'r') as f:
    print("Sadržaj datoteke:")
    lines = f.readlines()
    for line in lines:
        print(line.strip())
