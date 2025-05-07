def binarno(lista, trazeni_broj):
    lijevo = 0
    desno = len(lista) - 1
    koraci = 0  

    while lijevo <= desno:
        sredina = (lijevo + desno) // 2
        koraci += 1
        if lista[sredina] == trazeni_broj:
            return sredina, koraci  
        elif lista[sredina] < trazeni_broj:
            lijevo = sredina + 1
        else:
            desno = sredina - 1

    return -1, koraci  

brojevi = map(int, input("Unesite brojeve odvojene razmakom: ").split())
brojevi = sorted(brojevi)
print("Sortirana lista:", brojevi)
trazeni_broj = int(input("Unesite broj koji želite pronaći: "))
rezultat, koraci = binarno(brojevi, trazeni_broj)

if rezultat != -1:
    print(f"Broj {trazeni_broj} pronađen na indeksu {rezultat} nakon {koraci} koraka.")
else:
    print(f"Broj {trazeni_broj} nije pronađen u listi nakon {koraci} koraka.")