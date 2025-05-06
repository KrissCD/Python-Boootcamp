n=int(input("Koliko brojeva zelite upisati"))
brojevi=[]


for i in range(n):
    x=int(input())
    brojevi.append(x)
        
print(brojevi)

for i in range(len(brojevi)):
    print(brojevi[i])
    
broj2=brojevi.copy()
    
