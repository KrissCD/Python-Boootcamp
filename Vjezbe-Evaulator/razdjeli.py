n=int(input())


#A + B + C = N
#A ≤ B ≤ C
#Svaki bar jedan bod

kombinacije=0

for i in range(1,n//3+1):
    for j in range(i,(n//2)+1):
        k=n-i-j
        if k>=j:
            
            kombinacije+=1
                
print(kombinacije)
            
            
            
    
    
            


