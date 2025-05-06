n=int(input())

for i in range (2,n):
    if n%i==0:
        print("Broj nije prost")
        break
else:
    print("Broj je prost")

