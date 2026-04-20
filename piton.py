import random as r

# Írjon egy függvényt ami eldönti egy számról hogy mileyn az előjele.
# Poz: 1
# Neg: -1
# Nulla: 0
# Írjon eljárást ami ellenőrzi a zelőző feladat működését, egy [-5,5] intervallumos kigenerált számot írasson ki és írja ki az előjelét!
# pl.: Szám: -2 előjele: -1
# pl.: Szám: 3 előjele: 1
# pl.: Szám: 0 előjele: 0


def elsoFeladat(szam):
    if szam > 0:
        return 1
    elif szam < 0:
        return -1
    else:
        return 0

# def elojelEllenorzo():
#     velszam = r.randint(-5,5)
#     elojel = elso(velszam)
#     print(f"Szám: {vel} előjele: {elojel}")

def feladat():
    lista = []
    lista2 = []
    rand = 1
    while rand % 7 != 0:
        rand = r.randint(5,49)*2+1
        lista.append(rand)
    if rand % 7 == 0:
        lista2.append(rand)
        print("Ezzel állt meg a program: ",lista2)
    return lista

def harommalVegzodo(lista,szamjegy):
    db = 0
    for elem in lista:
        if elem % 10 == szamjegy:
            db += 1
    return db

def main():
    szam = -6
    t = elsoFeladat(szam)
    print(t)
    wasd = feladat()
    print(wasd)
    dsaw = harommalVegzodo(wasd,3)
    print(dsaw)
main()