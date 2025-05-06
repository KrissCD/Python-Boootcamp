import math 
import statistics

ocjene = []
for i in range(5):
    ocjene = int(input("Unesite ocjenu: "))
    ocjene.append(ocjene)

print("prosjek: ", sum(ocjene) / len(ocjene))
print("medijan: ", sorted(ocjene)[len(ocjene) // 2])


