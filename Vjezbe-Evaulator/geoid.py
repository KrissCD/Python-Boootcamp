n=int(input())
a, b=map(int,input().split())

prava_formula=a*a+2*a*b+b*b
kriva_formula=a*a+b*b

pravi_rezultati=0
krivi_rezultati=0
netocni_rezultati=0

for _ in range(n):
        r=int(input())
        if r==prava_formula:
            pravi_rezultati +=1
        elif r==kriva_formula:
            krivi_rezultati +=1
        else:
            netocni_rezultati +=1

print(pravi_rezultati)
print(krivi_rezultati)
print(netocni_rezultati)
        
