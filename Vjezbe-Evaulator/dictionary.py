ucenik={
    "ime": "Ana",
    "razred": 6,
    "ocjena": 5,
}

print(ucenik["ime"])
print(ucenik["razred"])
print(ucenik["ocjena"])
print(ucenik.get("prezime", "Nema prezime"))

ucenik["prezime"]="Lesic"    

print(ucenik.get("prezime", "Nema prezime"))

ucenik.pop("prezime")

ucenik["prezime"]="Lesic"

for kljuc in ucenik:
    print(kljuc, ucenik[kljuc])

for k, v in ucenik.items():
    print(k,":",v)

for v in ucenik.values():
    print(v)

ucenik.keys()
ucenik.items()


