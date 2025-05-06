def O1(N):
    if str(N).count('8') == 3:
        novi = N // 2
        if novi < 10000:
            return novi
    return None

def O2(N):
    if N >= 1000:
        novi = N - 500
        if novi < 10000:
            return novi
    return None

def O3(N):
    proste = [2, 3, 5, 7]
    zbroj = 0
    broj = 0

    for slovo in str(N):
        znamenka = int(slovo)
        if znamenka in proste:
            zbroj += znamenka
            broj += 1
    if broj >= 2:
        novi = N + zbroj
        if novi < 10000:
            return novi
    return None

def O4(N):
    broj = str(N)
    znamenke = []
    for i in range(len(broj)):
        znamenke.append(int(broj[i]))
    for i in range(len(broj)):
        for j in range(i + 1, len(broj)):
            if znamenke[i] + znamenke[j] == 11:
                suma = sum(znamenke)
                novi = N * suma
                if novi < 10000:
                    return novi
    return None

def O5(N):
    novi = N + 1
    if novi < 10000:
        return novi
    return None

def prolazak_dolinom(T, S, D, J, K):
    N = 1000 * T + 100 * S + 10 * D + J
    for _ in range(K):
        original = N

        rezultat = O1(N)
        if rezultat is not None:
            N = rezultat
            continue

        rezultat = O2(N)
        if rezultat is not None:
            N = rezultat
            continue

        rezultat = O3(N)
        if rezultat is not None:
            N = rezultat
            continue

        rezultat = O4(N)
        if rezultat is not None:
            N = rezultat
            continue

        rezultat = O5(N)
        if rezultat is not None:
            N = rezultat
            continue

    return N


T=int(input())  # tisucu
S=int(input())  # sto
D=int(input())  # deset
J=int(input())  # jedan
K=int(input())  # prolazak

print(prolazak_dolinom(T,S,D,J,K))
