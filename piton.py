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
    rand = 1
    while rand % 7 != 0:
        rand = r.randint(10,99)
        lista.append(rand)
    return lista

def main():
    szam = 0
    t = elsoFeladat(szam)
    print(t)
    wasd = feladat()
    print(wasd)
main()