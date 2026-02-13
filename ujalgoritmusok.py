import random as r

# Írjon függvényt ami függ egy egész számtól ami megadja hogy prím vagy nem prím!
# Írjon egy fv-t ami megmondja két pozitív egész számról az LNKO-t!
"""
def primszamE(szam):
    oszto = 0
    for i in range(2,szam-1,1):
        if szam % i == 0:
            return("A szám NEM prím!")
        else:
            return("A szám prím!")    
"""
def primszamE(szam):
    i = 2
    while i < szam-1 and szam % i == 0:
        i += 1
    aze = i < szam-1
    return aze

#def legnagyobbkozosOszto(szam):

def main():
    a = 13
    b = 26
    aszam = primszamE(a)
    print(aszam)
    bszam = primszamE(b)
    print(bszam)
main()