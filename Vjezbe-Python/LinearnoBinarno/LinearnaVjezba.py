brojevi = list(map(int, input("Unesite brojeve odvojene razmakom: ").split()))
x = input("Unesite riječ koju želite da pretražite: ")

def linear_search(brojevi, x):
    for i in range(len(brojevi)):
        if brojevi[i] == x:
            return i
    return -1

result = linear_search(brojevi, x)
if result == -1:
    print("Element nije pronađen")
else:
    print("Element pronađen na indeksu: ", result)