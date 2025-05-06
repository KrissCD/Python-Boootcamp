import random  

number = random.randint(1, 100)

while number % 5 != 0:
    print(f"{number} nije djeljiv sa 5")
    number = random.randint(1, 100)

print(f"{number} je djeljiv sa 5")