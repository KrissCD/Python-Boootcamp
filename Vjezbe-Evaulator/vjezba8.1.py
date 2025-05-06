def zbroji(a,b):
    return a+b

def oduzmi(a,b):
    return a-b

def pomnozi(a,b):
    return a*b

def podijeli(a,b):
    return a/b

def izbornik():
    print("kalkulator")
    print("1-zbroji")
    print("2-oduzmi")
    print("3-pomnozi")
    print("4-podijeli")
    print("0-izlaz")

def unesi_brojeve():
    a=float(input("unesi prvi"))
    b=float(input("unesi drugi"))
    return a,b

while True:
    izbornik()
    izbor=int(input("odaberi broj"))

    if izbor==0:
        print("kraj")
        break
    if izbor in [1,2,3,4]:
        a,b=unesi_brojeve()
    
if broj==1:
   print(zbroji(a,b))
elif broj==2:
    print(oduzmi(a,b))
elif broj==3:
    print(pomnozi(a,b))
elif broj==4:
    print(podijeli(a,b))

