n=int(input())

najveci=0
najmanji=101

for i in range(n):
    broj=int(input())
    if i==0:
        najveci=broj
        najmanji=broj
    if broj>najveci:
        najveci=broj
    if broj<najmanji:
        najmanji=broj
        
print(najveci)
print(najmanji)
   
        
