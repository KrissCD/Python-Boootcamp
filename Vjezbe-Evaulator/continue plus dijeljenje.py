n=int(input("unesi broj"))
k=int(input("preskaci"))

for i in range (1,n+1):
    if i%k==0:
        continue
    print(i)
