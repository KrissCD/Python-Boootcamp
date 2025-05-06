a=int(input())

if a>9 and a<100:
    b=a//10
    c=a%10
elif a>999 and a<10000:
    b=a//100
    c=a%100
else:
    b=a//1000
    c=a%1000

print(abs(b-c))
    
