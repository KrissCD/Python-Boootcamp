def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        minimalni_index = i
        for j in range(i + 1, n):
            if lista[j] > lista(minimalni_index):
                minimalni_index = j
            lista[i], lista[minimalni_index] = lista[minimalni_index], lista[i]


          
