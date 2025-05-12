def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib (n - 1) + fib (n - 2) # mozemo * + - ...
        
broj = int(input("Unesi Broj: "))
x = fib(broj)
print(x)




p = int(input("Unesi Broj: "))
a, b = 1, 1
for i in range(2, p):
    a, b = b, a + b

print(b)

