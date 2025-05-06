
n=int(input())

brojac=0

for i in range(n):
    for j in range(i):
        brojac+=1
        print(brojac+1, end=" ")
    print()




