#f = open('moj_tekst.txt', 'r')
#sadrzaj = f.read()
#print(sadrzaj)
#f.close()

#f = open('moj_tekst.txt', 'r')
#print(f.readline())
#f.close()

f = open('moj_tekst.txt', 'a')  # 'a' za append
f.write("\nOvo je moj cetvrti tekst u datoteci.")
f.close()