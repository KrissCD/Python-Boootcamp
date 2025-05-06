def unos():
    a=int(input("Unesi prvi broj: "))
    b=int(input("Unesi drugi broj: "))
    return a, b

def kvadrat(a, b):
    return a+b

def ispis(rezultat):
    print("Umnozak je: ",rezultat)


a, b=unos()
y=kvadrat(a,b)
ispis(y)


