
H = int(input())  
golovi = []

for _ in range(H):
    ime, minuta = input().split()
    golovi.append((int(minuta), ime, "HRVATSKA"))

B = int(input())  

for _ in range(B):
    ime, minuta = input().split()
    golovi.append((int(minuta), ime, "BRAZIL"))

golovi.sort()

rezultat_hrvatske = 0
rezultat_brazila = 0

for minuta, ime, tim in golovi:
    if tim == "HRVATSKA":
        rezultat_hrvatske += 1
    else:
        rezultat_brazila += 1
    print(f"{rezultat_hrvatske}:{rezultat_brazila} {ime}")



    





