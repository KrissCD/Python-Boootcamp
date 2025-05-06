a,b,c,d=map(int,input().split())
p,q=map(int,input().split())


if a>c and a>d and b>c and b>d:
    if p>q:
        print("A")
    else:
        print("B")

if a>b and a>d and c>b and c>d:
    if p>q:
        print("A")
    else:
        print("C")

if a>b and a>c and d>b and d>c:
    if p>q:
        print("A")
    else:
        print("D")

if b>a and b>c and c>a and c>d:
    if p>q:
        print("B")
    else:
        print("C")

if b>a and b>c and d>a and d>c:
    if p>q:
        print("B")
    else:
        print("D")

if c>a and c>b and d>a and d>b:
    if p>q:
        print("C")
    else:
        print("D")
    
    
    
