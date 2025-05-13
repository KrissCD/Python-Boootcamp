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

print(rang_lista)