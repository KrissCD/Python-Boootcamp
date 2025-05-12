import os

def pretrazi_ucenike():
    folder = os.path.dirname(os.path.abspath(__file__))

    ucenici_path = os.path.join(folder, "Ucenici.txt")
    pretraga_path = os.path.join(folder, "ZaPretragu.txt")

    with open(ucenici_path, 'r') as f:
        ucenici = set(line.strip() for line in f if line.strip())

    with open(pretraga_path, 'r') as f:
        za_pretragu = [line.strip() for line in f if line.strip()]

    for ime in za_pretragu:
        if ime in ucenici:
            print(ime,"- DA")
        else:
            print(ime,"- NE")

pretrazi_ucenike()

