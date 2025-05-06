    # Ispis rezultata nakon svakog gola
for minuta, ime, tim in golovi:
    if tim == 'Hrvatska':
        rezultat_hrvatske += 1
    else:
        rezultat_brazila += 1
    print(f"{rezultat_hrvatske}:{rezultat_brazila} {ime}")

