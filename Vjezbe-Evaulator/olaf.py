n,x=map(int,input().split())
pozicija=x
put=0
for i in range (n):
    s=input()
    d=int(input())
    put=put+d
    if s=="L":
        pozicija=pozicija-d
    elif s=="D":
        pozicija=pozicija+d
print(pozicija-x+(put))
            
            
            

                  
            

    
        
        
      
    
        
                

        
    
