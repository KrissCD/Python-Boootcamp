def binarno(lista, trazena_rijec):
    lijevo = 0
    desno = len(lista) - 1
    koraci = 0  

    while lijevo <= desno:
        sredina = (lijevo + desno) // 2
        koraci += 1
        if lista[sredina] == trazena_rijec:
            return sredina, koraci  
        elif lista[sredina] < trazena_rijec:
            lijevo = sredina + 1
        else:
            desno = sredina - 1

    return -1, koraci  

rijeci = map(str, input("Unesite brojeve odvojene razmakom: ").split())
rijeci = sorted(rijeci)
print("Sortirana lista:", rijeci)
trazena_rijec = input("Unesite broj koji želite pronaći: ")
rezultat, koraci = binarno(rijeci, trazena_rijec)

if rezultat != -1:
    print(f"Riječ '{trazena_rijec}' je pronađena na indeksu {rezultat} nakon {koraci} koraka.")
else:
    print(f"Riječ '{trazena_rijec}' nije pronađena u listi nakon {koraci} koraka.")