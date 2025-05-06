n=int(input())
hikari=90*60
hikaruj=90*60

for i in range(n):
    mm, ss=map(int, input().split(":"))
    trajanje=mm*60+ss
    if i%2==0:
        hikari-=trajanje
        hikari+=30
    else:
        hikaruj-=trajanje
        hikaruj+=30

#hikari//60,hikari%60
#hikaruj//60,hikaruj%60

hm=str(hikari//60)
hs=str(hikari%60)

hjm=str(hikaruj//60)
hjs=str(hikaruj%60)

if len(hm)==1:
    hm="0"+str(hm)
if len(hs)==1:
    hs="0"+str(hs)
if len(hjm)==1:
    hjm="0"+str(hjm)
if len(hjs)==1:
    hjs="0"+str(hjs)

print(hm,hs,sep=":")
print(hjm,hjs,sep=":")
