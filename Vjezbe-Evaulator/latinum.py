
#1 poluga 20 traka
#1 traka 100 listica

p=int(input()) #poluga 1=20 traka
t=int(input()) #traka 1=100 listica
l=int(input()) #listica

rp=int(input()) #rom poluga
rt=int(input()) #rom traka
rl=int(input()) #rom listica

zp=int(input()) #zek poluga
zt=int(input()) #tek traka
zl=int(input()) #tek listica

p1=p*20
t1=(p1+t)*100
l1=l+t1

print(l1)

if rp>zp or rt>zt or rl>zl:
    print("ROM")
else:
    print("ZEK")

