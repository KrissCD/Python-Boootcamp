n = int(input())

natjecatelji = []
for _ in range(n):
    ime, prezime, bodovi = input().split()
    bodovi = int(bodovi)
    natjecatelji.append((ime, prezime, bodovi))

def kljuc_za_sortiranje(natjecatelj):
    ime = natjecatelj[0]
    prezime = natjecatelj[1]
    bodovi = natjecatelj[2]
    return (-bodovi, ime, prezime)

natjecatelji.sort(key=kljuc_za_sortiranje)

rang_lista = []
zadnji_bodovi = -1
mjesto = 0

for i in range(n):
    ime, prezime, bodovi = natjecatelji[i]
    if bodovi != zadnji_bodovi:
        mjesto = i + 1
        zadnji_bodovi = bodovi
    rang_lista.append((mjesto, ime, prezime, bodovi))

w1 = max(len(str(m)) for m, _, _, _ in rang_lista)
w2 = max(len(ime) + 1 + len(prezime) for _, ime, prezime, _ in rang_lista)
w3 = max(len(str(b)) for _, _, _, b in rang_lista) + len(" / 400")

sirina = 2 + w1 + 3 + w2 + 3 + w3 + 2
print("-" * sirina)

for red in rang_lista:
    mjesto = red[0]
    ime = red[1]
    prezime = red[2]
    bodovi = red[3]

    ime_prezime = ime + " " + prezime
    bodovi_tekst = str(bodovi) + " / 400"

    praznine_mjesto = " " * (w1 - len(str(mjesto)))
    praznine_ime = " " * (w2 - len(ime_prezime))
    praznine_bodovi = " " * (w3 - len(bodovi_tekst))

    print("| " + praznine_mjesto + str(mjesto) + " | " + ime_prezime + praznine_ime + " | " + praznine_bodovi + bodovi_tekst + " |")

# Ispis donje crte
print("-" * sirina)
