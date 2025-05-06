a=int(input()) #dugina prve grancice
b=int(input()) #dugina druge grancice
c=int(input()) #dugina trece grancice

#zbroj dugina bilo kojih dviju stranica UVIJEK je veca ne duljine trece


if a+b>c and c+b>a and a+c>b:
    print("DA")
else:
    print("NE")



    



