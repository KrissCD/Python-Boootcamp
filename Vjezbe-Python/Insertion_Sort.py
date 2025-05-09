def insertion_sort(lista):
    for i in range(1, len(lista)):
        kljuc = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > kljuc:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = kljuc

import math
import random

brojevi = set()

while len(brojevi) <= 999:
    x = random.randint(1,10000)
    brojevi.add(x)

print(brojevi)
print(len(brojevi))

with open ("brojevi.txt", "w") as f:
    for broj in brojevi:
        f.write(str(broj) + "\n")






        



