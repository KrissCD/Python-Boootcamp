def pretvori_temperaturu(vrijednost, skala):
    if skala == "C":
        return (vrijednost * 9/5) + 32  # Celzijus u Farenhajt
    elif skala == "F":
        return (vrijednost - 32) * 5/9  # Farenhajt u Celzijus
    else:
        return "Nevažeća skala!"

# Unos od korisnika
vrijednost = float(input())
skala = input()

rezultat = pretvori_temperaturu(vrijednost, skala)
print(rezultat)

