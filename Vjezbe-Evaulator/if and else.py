bodovi=int(input("Unesite broj bodova: "))
prisustvo=int(input("Unestite prisustvo: "))

if bodovi>=90 and prisustvo==100:
    print("Izvanredan rezultat")
elif bodovi>=90 and prisustvo==100:
    print("Student je položio")
elif bodovi>=60 and prisustvo<80:
    print("Uvjetna ocijena")
else:
    print("Student nije položio")


