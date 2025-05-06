N = int(input())
X = int(input())
Z = int(input())

zapisi = []

for _ in range(Z):
    stanica, kartica, senzor = map(int, input().split())
    zapisi.append((kartica, stanica, senzor))

zarada = 0
putnici = {}

def tip(s):
    return "ULAZ" if s % 2 == 0 else "IZLAZ"

# Tablica faktora prema kombinaciji ulaz/izlaz
faktor = {
    ("ULAZ", "IZLAZ"): 1,
    ("ULAZ", "ULAZ"): 2,
    ("IZLAZ", "IZLAZ"): 3,
    ("IZLAZ", "ULAZ"): 4
}

for kartica, stanica, senzor in zapisi:
    if kartica in putnici:
        ulazna_stanica, ulazni_senzor = putnici.pop(kartica)
        udaljenost = abs(stanica - ulazna_stanica)
        zarada += udaljenost * X * faktor[(tip(ulazni_senzor), tip(senzor))]
    else:
        putnici[kartica] = (stanica, senzor)

print(zarada)
