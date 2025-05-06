x=int(input())  #trajanje filma
n=int(input())  #koliko puta

odgledano=set()

for i in range(n):
    pfs,pfm=map(int,input().split())  #sat i minuta pocetka prikazivanja filma
    pgs,pgm=map(int,input().split())  #sat i minuta kada smo poceli gledat film
    kgs,kgm=map(int,input().split())  #sat i minuta kada smo prestali gledat film

    pocetak_prikazivanja=pfs * 60 + pfm
    kraj_filma=pocetak_prikazivanja + x

    pocetak_gledanja=pgs * 60 + pgm
    kraj_gledanja=kgs * 60 + kgm

    kraj_sata=kraj_filma // 60
    kraj_minuta=kraj_filma % 60

    if kraj_gledanja < pocetak_gledanja:
            kraj_gledanja += 24 * 60
    if kraj_filma < pocetak_prikazivanja:
            kraj_filma += 24 * 60

    kraj_sata=(kraj_filma % (24 * 60)) // 60
    kraj_minuta=kraj_filma % 60
    print(kraj_sata, kraj_minuta)

    if pocetak_gledanja<pocetak_prikazivanja:
        pocetak_gledanja=pocetak_gledanja+1440
    if kraj_gledanja<pocetak_gledanja:
        kraj_gledanja=kraj_gledanja+1440

    for i in range(pocetak_gledanja-pocetak_prikazivanja,kraj_gledanja-pocetak_prikazivanja):
        odgledano.add(i)

print(len(odgledano))
    
    
    
