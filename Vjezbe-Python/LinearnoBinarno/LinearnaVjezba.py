brojevi = list(map(str, input("Unesite rijeci odvojene razmakom: ").split()))
x = input("Unesite riječ koju želite da pretražite: ")

def linear_search(brojevi, x):
    for i in range(len(brojevi)):
        if brojevi[i] == x:
            return i
    return -1

result = linear_search(brojevi, x)
if result == -1:
    print("rijec nije pronađen")
else:
    print("rijec pronađen na indeksu: ", result)