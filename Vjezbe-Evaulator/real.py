n=int(input()) #broj utakmica

prosuti_brojevi = 0

for i in range(n):
    rp,pp,rk,pk=map(int, input().split())
    if rp>pp:
        if rk<pk:
            prosuti_brojevi=+3
    elif rk==pk:
        prosuti_brojevi=+2
    elif rp==pp:
        if rk<pk:
            prosuti_brojevi=+1
print(prosuti_brojevi)
            
                
    
    
   
        
       
    
