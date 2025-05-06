t=int(input())
s=int(input())
d=int(input())
j=int(input())
k=int(input())


n=1000*t+100*s+10*d+j

def o1(n):
    if str(n).count("8")==3:
        novi=n//2
        if novi<10000:
            return novi
    return none

def o2(n):
    if n>=1000:
        novi=n-500
        return novi
    return none

def o3(n):
    proste=[2, 3, 5, 7]
    zbroj=0
    broj=0

    for slovo in str(N):
        znamenka=int(slovo)
        if znamenka in proste:
            zbroj+=znamenka
            broj+=1
    if broj>=2:
        novi=N+zbroj
        if novi<10000:
            return novi
    return None
    
    
    
