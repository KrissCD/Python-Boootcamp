s=str(input())
m=str(input())

sati=0
minute=0


if int(s[0])==1:
    sati=sati+8
if int(s[1])==1:
    sati=sati+4
if int(s[2])==1:
    sati=sati+2
if int(s[3])==1:
    sati=sati+1


if int(m[0])==1:
    minute=minute+32
if int(m[1])==1:
    minute=minute+16
if int(m[2])==1:
    minute=minute+8
if int(m[3])==1:
    minute=minute+4
if int(m[4])==1:
    minute=minute+2
if int(m[5])==1:
    minute=minute+1

print(sati,minute)



        
        
    
        
    
    
