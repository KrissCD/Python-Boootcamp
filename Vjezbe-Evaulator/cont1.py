n=int(input("upisi broj"))
k=int(input("preskoci"))
brojac=0

for i in range (1,n+1):
    if i%k==0:
       # print(i)
       brojac=brojac+1

print(brojac)
