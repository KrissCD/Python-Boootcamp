brojevi[]

for i in range(7):
    x=int(input())
    brojevi.append(x)
broj=1
for i in range(13):
    for j in range(7):
        if broj in brojevi:
            print("X",end="")
        else:
            print("*",end="")
        broj=broj+1
    print()
