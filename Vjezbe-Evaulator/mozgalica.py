def prirodan_broj():
    n=int(input())
    return n

def povecaj(n):
    return n+1

def paran(n):
    if n%2==0:
        return n+1
    else:
        return n-1
    
def jedinica(n):
    return n+(n%10)

def znamenka(n):
    n_str = str(n)
    if len(n_str) < 2:
        return n  
    n_str = n_str[:-2] + n_str[-1] + n_str[-2]
    return int(n_str)

n = int(input())
k = int(input())

#obrada broja

for i in range(k):
    a = int(input())
    if a == 1:
        n = povecaj(n)
    elif a == 2:
        n = paran(n)
    elif a == 3:
        n = jedinica(n)
    elif a == 4:
        n = znamenka(n)

print(n)
    
