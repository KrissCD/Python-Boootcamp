import time

def asc():
    with open('brojevi.txt', 'r') as f:
        lista = [int(line.strip()) for line in f if line.strip().isdigit()]
        c = 0
        start_time = time.time()  # Start t
        for i in range(1, len(lista)):
            kljuc = lista[i]
            j = i - 1
            while j >= 0 and lista[j] > kljuc:
                lista[j + 1] = lista[j]
                j -= 1
                c += 1
            lista[j + 1] = kljuc
        end_time = time.time()  # End 
        print(f'Nakon {c} koraka.')
        print(f"Vrijeme sortiranja (uzlazno): {end_time - start_time:.4f} sekundi")
    return lista

def dsc():
    with open('brojevi.txt', 'r') as f:
        lista = [int(line.strip()) for line in f if line.strip().isdigit()]
        c = 0
        start_time = time.time()  # Start 
        for i in range(1, len(lista)):
            kljuc = lista[i]
            j = i - 1
            while j >= 0 and lista[j] < kljuc:
                lista[j + 1] = lista[j]
                j -= 1
                c += 1
            lista[j + 1] = kljuc
        end_time = time.time()  # End 
        print(f'Nakon {c} koraka.')
        print(f"Vrijeme sortiranja (silazno): {end_time - start_time:.4f} sekundi")
    return lista

while True:
    print('\n-----Izbornik-----')
    print("Upisi 1 za Asc")
    print("Upisi 2 za Dsc")
    print("Upisi 0 za Izlaz iz programa")
    try:
        I = int(input("Unos: "))
        if I == 1:
            print("Sortirana lista (uzlazno):", asc())
        elif I == 2:
            print("Sortirana lista (silazno):", dsc())
        elif I == 0:
            print("Izlaz iz programa.")
            break
        else:
            print("Nevažeći unos. Pokušajte ponovno.")
    except ValueError:
        print("Molimo unesite broj.")

