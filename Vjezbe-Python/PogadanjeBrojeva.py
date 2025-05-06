import random
broj = random.randint(1, 10)
print("Pogodi broj od 1 do 10")

n = int(input("Unesite broj od 1 do 10: "))

while n != broj:  
    print("Niste pogodili broj.")
    n = int(input("Unesite broj: "))

print("Bravo pogodili ste!")
