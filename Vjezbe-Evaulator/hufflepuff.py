n=int(input())

Gryffindor_C=0 #lana crvena
Slytherin_Z=0 #lara zelena
Ravenclaw_P=0 #masa plava
Hufflepuff_Y=0 # zuta


for i in range (n):
    boja=str(input())
    if boja=="C":
        Gryffindor_C +=1
    elif boja=="Z":
        Slytherin_Z +=1
    elif boja=="P":
        Ravenclaw_P +=1
    elif boja=="Y":
        Hufflepuff_Y +=1

if Gryffindor_C>Slytherin_Z and Gryffindor_C>Hufflepuff_Y and Gryffindor_C>Ravenclaw_P:
    print("LANA")
elif Slytherin_Z>Gryffindor_C and Slytherin_Z>Hufflepuff_Y and Slytherin_Z>Ravenclaw_P:
    print("LARA")
elif Ravenclaw_P>Gryffindor_C and Ravenclaw_P>Hufflepuff_Y and Ravenclaw_P>Slytherin_Z:
    print("MASA")
else:
    print("EXPELLIARMUS")





    












                
            
        
    






