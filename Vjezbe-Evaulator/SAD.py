ag=int(input()) #donald
bg=int(input()) #kamala
c=int(input()) #pobjednik
cg=int(input()) #zadani kandidat pobjednik glasovi

if c==1:
    print("DONALD")
    ag=ag+cg
else:
    print("KAMALA")
    bg=bg+cg

if ag>bg:
    print("DONALD")
else:
    print("KAMALA")








        






















