n=int(input())

zbroj=0
max_z=0

for i in range(n):
    h=str(input())
    if len(h)==2 or len(h)==4:
        max_z=0
        for i in range(1, len(h)):
            z=int(h[:i])+int(h[i:])
            if z>max_z:
                max_z=z
        zbroj+=max_z
    else:
        zbroj+=int(h)

print(zbroj)
        
        
    
