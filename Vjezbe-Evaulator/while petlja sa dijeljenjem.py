n=int(input())

brojac=0
zbroj=0

while n>0:
    print(n%10)
    zbroj=zbroj+n%10
    n=n//10
    print("broj n je sada:",n)
    brojac=brojac+1
