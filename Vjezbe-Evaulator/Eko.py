def drvosjeca(n, m, visine):
    dolje = 0
    gore = max(visine)
    rezultat = 0

    while dolje <= gore:
        sredina = (dolje + gore) // 2
        ukupno = sum((v - sredina) for v in visine if v > sredina)

        if ukupno >= m:
            rezultat = sredina  
            dolje = sredina + 1
        else:
            gore = sredina - 1  

    return rezultat


n, m = map(int, input().split())
visine = list(map(int, input().split()))
rezultat = drvosjeca(n, m, visine)
print(rezultat)

