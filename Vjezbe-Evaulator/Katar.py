#N klima uredaja od 1 do N
#P = Pali klimu 
#G = Gasi klimu
#Sve klime ugasene 
#X = poslani signali 

N = int(input())  # broj klima
X = int(input())  # broj signala
klime = [0] * N  # 0 = ugašena, 1 = upaljena

for i in range(X):
    k = int(input())
    if i % 2 == 0:
        klime[k-1] = 1
    else:
        klime[k-1] = 0

# Broj upaljenih klima
upaljene = sum(klime)
print(upaljene)

minimalni_signali = N - upaljene

if X%2 == 0:
    print(minimalni_signali * 2 - 1)
else:
    print(minimalni_signali * 2)

