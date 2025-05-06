n=str(input())

b=n[:len(n)//2]
c=n[len(n)//2:]

b=int(b)
c=int(c)

if b>c:
    print(b-c)
else:
    print(c-b)

