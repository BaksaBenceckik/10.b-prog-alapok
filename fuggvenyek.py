import random

"""
Függvények
(Scratch blokkok)

Előre megírt, definiált folyamatok amely külső mértéktől függően
végrehajtják a felső utasításokat.

def fuggvenynev():
    fuggveny tartalma

fuggvenynev() # Fuggveny meghívása
"""
# visszatérési érték nelküli függvények - eljárás
# álltalában kiíratás során használjuk
# osszeadás függvény definiálása

def osszeadas():
    a = 12
    b = 17
    print(a + b)

# összeadás külső értéktől függően, paraméteren keresztül
def osszpara(a,b):
    c = a + b
    print(c)

# összeadás függvény meghívása
osszeadas()
osszpara(32,23)

# visszatéréssel rendelkező függvények
def kettoatizediken():
    # a = math.pow(2,10)
    a = 2 ** 10
    return a

val = kettoatizediken()
print(val)

def osszre(a,b):
    c = a + b
    return c
print(osszre(11,10))

# házi feladat
# definiálj egy olyan eljárást, aminek a paraméterébe bekerül egy
# darabszám, és a függvény pedig kiír ennyi véletlen számot egymás mellé!

def veletlenszamkiiratas(db):
    for i in range(0,db,1):
        print(random.randint(100,999), end=" ")

veletlenszamkiiratas(10)
print()

# készítsen egy eljárást, ami függ egy szövegtől, és kiírja a szót visszafele

def visszafele(szoveg):
    n = len(szoveg)
    for i in range(n-1,-1,-1):
        print(szoveg[i], end="")

visszafele("kip kop kalapács")
print()
# készítsen egy függvényt, ami függ egy szövegtől, és visszaadja a szót visszafele

def szovegvisszafele(szoveg):
    visszaszoveg = ""
    n = len(szoveg)
    for i in range(n-1,-1,-1):
        visszaszoveg += szoveg[i]
    return visszaszoveg

print(szovegvisszafele("kalapács"))

# Írjon egy fv-t, ami egy szórol eldönti hogy palidrom-e és visszaadja válaszul. (visszafele ugyan az)

def palindrom(szo):
    if (szo == szovegvisszafele(szo)):
        return True
    else:
        return False
#     i = 0
#     while(i<=len(szo)//2 and szo[i] == szo[len(szo)-1-i]):
#         i +=1
#     if i>len(szo)//2:
#         return "palindrom"
#     else:
#         return "nem palindrom"

print("palindrom-e a szó: ", palindrom("görög"))