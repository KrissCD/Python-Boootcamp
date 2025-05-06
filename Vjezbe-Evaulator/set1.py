def teniski_meč(ishod):
    setovi = ishod.split("/")
    
    setovi_ime1 = 0
    setovi_ime2 = 0
    
    for i in range(len(setovi)):
        gemovi = setovi[i].split(":")
        gem1 = int(gemovi[0])  
        gem2 = int(gemovi[1])
        
        if gem1 > gem2:
            setovi_ime1 += 1
        else:
            setovi_ime2 += 1
    
    if setovi_ime1 == 3:
        print("ime1")
    else:
        print("ime2")
    
    print(setovi_ime1, setovi_ime2)

ishod = input()

teniski_meč(ishod)
