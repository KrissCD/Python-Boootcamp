
zivotinje=["lav","macka","pas","slon","zamorac","lav"]


for i in range(len(zivotinje)):
    print(zivotinje[i])

zivotinje[2]=("tigar")

zivotinje.append("hrcak")
zivotinje.insert(0,"zmija")

zivotinje.remove("slon")
zivotinje.pop(2)

    
for i in range(len(zivotinje)):
    print("Zivotinja: ",i, zivotinje[i])

ziv2=zivotinje.copy()

print(zivotinje.index("lav"))


