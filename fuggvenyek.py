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