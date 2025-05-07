try: 
    f = open('nepostoji.txt', 'r')
    print(f.read())
    f.close()
except:
    print("Datoteka ne postoji")
finally:
    print("Kraj programa")


