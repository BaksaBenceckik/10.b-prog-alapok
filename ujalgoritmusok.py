import random as r
import math as m

# Írjon függvényt ami függ egy egész számtól ami megadja hogy prím vagy nem prím!
# Írjon egy fv-t ami megmondja két pozitív egész számról az LNKO-t!
"""
def primszamE(szam):
    oszto = 0
    for i in range(2,szam-1,1):
        if szam % i == 0:
            return("A szám NEM  prím!")
        else:
            return("A szám prím!")

def primszamE(szam):
    a = 2
    b = m.sqrt(szam)
    while a<b and szam % a != 0:
        a += 1
    print(a)
    return a >= b
"""
def LNKO(a,b):
    if a == b:
        return a 
    if b < a:
        c = a
        a = b
        b = c
    while 0 < a:
        a, b = b % a, a
    return b
    #kisebb = szam1
    #if szam1 > szam2:
    #    kisebb = szam2
    #while kisebb >= 1 and not szam1 % kisebb == 0 and szam2 % kisebb == 0:
    #    kisebb += 1
    #return kisebb

def main():
    a = 13453543235462573654673524653246745627453546263476625462354623754632546324623745235
    b = 26434325468865734657263547826576375687256473863746375445643773643657675673462764726
    #for i in range(1000000,12000000,1):
    #    if primszamE(i):
    #        print(i)
    #print(primszamE(a))
    print(LNKO(a,b))
main()