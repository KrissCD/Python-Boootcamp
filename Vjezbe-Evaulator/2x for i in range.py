n=int(input())

djelitelj=0

for i in range (2,n):
    if n%i==0:
        #print(i)
        djelitelj=djelitelj+1
if djelitelj==0:
    print("Broj je prost")
else:
    print("Broj nije prost")

    
        
            
    
    
