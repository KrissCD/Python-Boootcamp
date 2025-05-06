def unesi_brojeve():
    a=float(input())
    b=float(input())
    return a,b

def zbroji(a,b):
    return a+b

def oduzmi(a,b):
    return a-b

def pomnozi(a,b):
    return a*b

def podijeli(a,b):
    if b==0:
        return "Greska"
    return a/b

a,b=unesi_brojeve()
print(zbroji(a,b))
print(oduzmi(a,b))
print(pomnozi(a,b))
print(podijeli(a,b))
