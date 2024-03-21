def beolvasas(file_nev):
    jaratok = []

    with open(file_nev, 'r') as file:
        while True:
            sor = file.readline().strip()
            if not sor:
                break
            sor = sor.split(',')
            jaratszam = sor[0]
            indulasi_ido = sor[1]
            utasok_info = sor[2].split('|')  # utasok 

            utasok = []
            for utas_info in utasok_info:
                utas_info = utas_info.split(';')
                nev = utas_info[0]
                utlevel = utas_info[1]
                ules = utas_info[2]
                utasok.append([nev, utlevel, ules])

            jaratok.append([jaratszam, indulasi_ido, utasok])

    return jaratok

def aFeladat(jaratok, keresett_jaratszam):
    for jarat in jaratok:
        if jarat[0] == keresett_jaratszam:
            return len(jarat[2])
    return 0

def bFeladat(jaratok, keresett_jaratszam):
    talalatok_szama = 0
    ules_elso_karakterek = set()
    ules_elofordulasok = {}

    for jarat in jaratok:
        if jarat[0] == keresett_jaratszam:
            for utasok in jarat[2]:
                ules_szam_elso_karakter = utasok[2][0]  #char
                if ules_szam_elso_karakter in ules_elso_karakterek:
                    if ules_szam_elso_karakter in ules_elofordulasok:
                        ules_elofordulasok[ules_szam_elso_karakter] += 1
                    else:
                        ules_elofordulasok[ules_szam_elso_karakter] = 2
                else:
                    ules_elso_karakterek.add(ules_szam_elso_karakter)

    for elofordulas in ules_elofordulasok.values():
        if elofordulas >= 2:  
            talalatok_szama += 1

    return talalatok_szama

def cFeladat(adatok):
    utlevel_szamok = set()
    tobbszor_utazo_utasok = set()

    for jarat in adatok:
        for utas in jarat[2]:
            nev = utas[0]  
            utlevel_szam = utas[1]  
            if utlevel_szam in utlevel_szamok:
                tobbszor_utazo_utasok.add((nev, utlevel_szam))
            else:
                utlevel_szamok.add(utlevel_szam)

    return tobbszor_utazo_utasok

def main():
    adatok = beolvasas('adatok.txt')
    while True:
        keresett_jaratszam = input("Add meg a keresett járatszámot: ").strip().upper()
        if keresett_jaratszam:
            break
        else:
            print("Hibás a formátum.")

    # A feladat
    utasok_szama = aFeladat(adatok, keresett_jaratszam)
    print(f"A {keresett_jaratszam} járaton {utasok_szama} utas vett jegyet.")

    # B feladat
    talalatok_szama = bFeladat(adatok, keresett_jaratszam)
    print(f"A {keresett_jaratszam} járaton {talalatok_szama} olyan sor van, ahol legfeljebb 2 ember ül.")

    # C feladat
    tobbszor_utazo_utasok = cFeladat(adatok)

    if tobbszor_utazo_utasok:
        print("Vannak olyan utasok, akik többször is utaztak.\nAzok az utasok, akik többször utaztak:")
        for nev, utlevel_szam in tobbszor_utazo_utasok:
            print(f"Név: {nev}, Útlevélszám: {utlevel_szam}")
    else:
        print("Nincsenek olyan utasok, akik többször is utaztak.")

main()
