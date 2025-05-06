#pozitivna nula ako je prije broj negativan a poslije pozitivan
# - 0 + pozitivna nula
# + 0 - negativna nula

n=int(input())
brojevi=[]

for i in range (n):
    x=int(input())
    brojevi.append(x)

pozitivni=0
negativni=0
nula=0

for i in range(1,n-1):
    if brojevi[i]==0:
        if brojevi[i-1]>0 and brojevi[i+1]<0:
            negativni=negativni+1
        elif brojevi[i-1]<0 and brojevi[i+1]>0:
            pozitivni=pozitivni+1
else:
    nula=nula+1

print(pozitivni, negativni)


negativni=negativni+1
        
        
        
        
        




        
       
        
    
    
        


