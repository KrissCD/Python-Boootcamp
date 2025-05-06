def unesi_broj():
    return int(input("Unesi broj: "))

def je_paran(n):
    return n%2==0

def ispisi_poruka(paran):
    if paran:
        print("Broj je paran")
    else:
        print("Broj nije paran")

broj=unesi_broj()
rez=je_paran(broj)
ispisi_poruka(rez)
