import random as r

def shrekdob(db):
    lista = []
    for i in range(db*2):
        kocka = r.randint(1,18)
        lista.append(kocka)
    return lista

def fionadob(db):
    lista = []
    for i in range(db*2):
        kocka = r.randint(1,18)
        lista.append(kocka)
    return lista

def shrekosszegzes(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i]
    return osszeg

def fionaosszegzes(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i]
    return osszeg

def shrekmin(lista):
    mine = lista[0]
    for i in range(1,len(lista),1):
        if lista[i] < mine:
            mine = lista[i]
    return mine

def fionamin(lista):
    mine = lista[0]
    for i in range(1,len(lista),1):
        if lista[i] < mine:
            mine = lista[i]
    return mine

def kinyert(egy, ketto):
    if egy > ketto:
        return("Shrek nyert!")
    elif egy == ketto:
        return("Döntetlen!")
    else:
        return("Fiona nyert!")

def main():
    fiona = fionadob(7)
    print("Fiona: ",fiona)
    fossz = fionaosszegzes(fiona)
    print("Fiona értékeinek összesen: ",fossz)
    shrek = shrekdob(7)
    print("Shrek: ",shrek)
    sossz = shrekosszegzes(shrek)
    print("Shrek értékeinek összesen: ",sossz)
    fmin = fionamin(fiona)
    print("Fiona legkisebb értéke: ",fmin)
    smin = shrekmin(shrek)
    print("Shrek legkisebb értéke: ",smin)
    if smin < fmin:
        print("Shrek dobta a legkisebbet!")
    elif smin == fmin:
        print("A legkisebb értékük egyenlő!")
    else:
        print("Fina dobta a legkisebbet!")
    nyertes = kinyert(sossz, fossz)
    print(nyertes)
main()