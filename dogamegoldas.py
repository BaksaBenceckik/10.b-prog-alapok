import random

def listafeltolt(db):
    lista = []
    for i in range(db):
        rand = random.randint(2,36)
        lista.append(rand)
    return lista

def osszegzes(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i]
    return osszeg

def kiíratás(lista, osszeg):
    for i in range(0,len(lista),1):
        print(lista[i], end=" + ")
    print(lista[len(lista)-1], end=" ")
    print("=", osszeg)

def volte(slista,flista):
    i = 0
    while i < len(slista) and slista[i] != flista[i]:
        i += 1
    vane = i < len(slista)
    return vane

def main():
    shrek = listafeltolt(7)
    print("Shrek dobásai: ",shrek)
    fiona = listafeltolt(7)
    print("Fiona dobásai: ",fiona)
    osszegs = osszegzes(shrek)
    print("Shrek összege: ",osszegs)
    osszegf = osszegzes(fiona)
    print("Fiona összege: ",osszegf)
    kiiratass = kiíratás(shrek, osszegs)
    kiiratasf = kiíratás(fiona, osszegf)
    print(kiiratass)
    print(kiiratasf)
    vanee = volte(shrek, fiona)
    print(vanee)
main()