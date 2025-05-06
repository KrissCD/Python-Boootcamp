n=int(input())

najveci=0
najmanji=101

for i in range(n):
    broj=int(input())
    if i==0:            #ako neznamo granicu najmanjeg i najveceg
        najveci=broj    #
        najmanji=broj   #
    if broj>najveci:    #ako trazimo najveci broj
        najveci=broj
    if broj<najmanji:   #ako trazimo najmanji broj
        najmanji=broj
        
print(najveci)
print(najmanji)
   
        
