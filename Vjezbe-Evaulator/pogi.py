#n ulaznica, od 1 do n
#k osoba pokusalo uci
#x serijeski broj
#ui serijiski brojevi na njihovim ulaznicama

n=int(input())
k=int(input())
x=int(input())

serijski_brojevi=[]


for i in range(k):
    ui=int(input())
    if ui not in serijski_brojevi:
        serijski_brojevi.append(ui)
    
if x in serijski_brojevi:
    print("DA")
else:
    print("NE")
    
if x in serijski_brojevi:
    print(serijski_brojevi.index(x)+1)
else:
    print("0")
    
print(len(serijski_brojevi))
print(*serijski_brojevi)


