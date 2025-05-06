#ukupno zlicica ubacio u kavu
#ukupno zlicica ubacio u k kavu
#ukupno najvise zlicica u neku od pripremljenih kava


n=int(input())  #ukupan broj pripremljenih kava
s=input()        
k=int(input())  #broj poretka kave u koju je trebao ubacit zlicicu

zlicica=[]
zlicica_kava=0

for i in range(n):
    if s[i]=="0":
        zlicica.append(0)
        zlicica_kava+=1
    else:
        zlicica.append(zlicica_kava+1)
        zlicica_kava=0

print(sum(zlicica))
print(zlicica[k-1])
print(max(zlicica))




        
    


