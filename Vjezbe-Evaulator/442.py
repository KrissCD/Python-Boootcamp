n=str(input())

for i in range(len(n)-2):
    if int(n[i])+int(n[i+1])+int(n[i+2])==10:
        a=n[i]
        b=n[i+1]
        c=n[i+2]
print(a,b,c)
    
        
        
