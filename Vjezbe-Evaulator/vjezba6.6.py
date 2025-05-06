n=int(input())


#A + B + C = N
#A ≤ B ≤ C
#Svaki bar jedan bod

kombinacije=0

for i in range(1,n):
    for j in range(i,n):
        for k in range(j,n):
            if i+j+k==n and i<=j and j<=k:
                kombinacije+=1
                
print(kombinacije)
            
            
            
    
    
            


