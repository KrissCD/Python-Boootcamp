n = str(input("Unesite rijec: "))

def palidrom(rijec):
    if len(rijec) <= 1:
        print("Rijec je palindrom")
        return True
    if rijec[0] == rijec[-1]:
        return palidrom(rijec[1:-1])
    else:
        print("Rijec nije palindrom")
        return False

palidrom(n)
