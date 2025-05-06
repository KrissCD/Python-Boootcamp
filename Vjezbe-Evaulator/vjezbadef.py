def pozdrav(ime,spol):
    if spol=="M":
        print("Dobrodosao,",ime)
    else:
        print("Dobrodosla,",ime)

pozdrav("Lana","Z")
pozdrav("Luka","M")

def pozdrav(ime):
    print("Bok,sta ima", ime)

pozdrav("Lana")
pozdrav("Ivan")


def zbroji(a,b):
    print("Zbroj je:",a+b)

zbroji(4,6)
zbroji(20,30)

def pomnozi(c,d):
    print("Umnozak je:",c*d)

pomnozi(10,5)
pomnozi(2,10)

def kvadrat(x):
    return x * x

rezultat=kvadrat(5)
print("Kvadrat je:",rezultat)


def maksimum(a,b):
    if a>b:
        return a
    else:
        return b

veci=maksimum(10,30)
print(veci)

def je_paran(n):
    return n%2==0

print(je_paran(4))
print(je_paran(7))

if je_paran(4)==True:
    print("Broj je paran")
if je_paran(15)==False:
    print("Broj nije paran")





