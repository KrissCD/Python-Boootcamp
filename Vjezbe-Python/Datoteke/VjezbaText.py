f = open('file.txt', 'w')
f.write('Ovo je moj prvi tekst u datoteci.\n')
f.write('Ovo je moj drugi tekst u datoteci.\n')

f = open('file.txt', 'r')
print(f.readlines())
f.close()

#import os

#if os.path.exists('file.txt'):
#    os.remove('file.txt')
#else:
#    print("Datoteka ne postoji")    

f = open('file.txt', 'a')
f.write('Ovo je moj treci tekst u datoteci.\n')
f.close()


