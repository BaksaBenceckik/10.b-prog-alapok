import random as r

# HF 
# Szimuláljon egy matematika versenyt és az eredményeire készített statisztikát! Mind a 17 diák nagyon ügyes, így kevés rossz verseny dolgozat született. A döntőbe jutásésrt 70%-ot el kell érni.
# 1. Készítsen egy függvényt, amit feltölt egy listát úgy, hogy 50%-os eseéllyel szülessenek 120-200 közötti pontok, a maradék pedig 50-120 közötti pont legyen! ✔
# 2. Írjon függvényt, ami visszaadja a versenydolgozatok átlagát! ✔
# 3. Írjon függvényt, ami visszaadja a versenydolgozatok terjedelmét! ✔
# 4. Írjon függvényt, ami visszaadja lett-e maximum pontos? ✔
# 5. Írjon függvényt, ami visszaadja hány versenyző jutott a döntőbe? ✔
# 6. Írjon függvényt, ami visszaadja, hogy volt-e 50 pontos, ha volt hányadik tanuló? ✔

def maximum(lista):
    maxe = lista[0]
    for index in range(1,len(lista),1):
        if lista[index] > maxe:
            maxe = lista[index]
    return maxe

def minimum(lista):
    mine = lista[0]
    for index in range(1,len(lista),1):
        if lista[index] < mine:
            mine = lista[index]
    return mine

def datlag(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i]
        atlag = osszeg / len(lista)
    return(round(atlag,2))

def lettemax(lista):
    i = 0
    while i < len(lista) and lista[i] != 200:
        i += 1
    vane = i < len(lista)
    return vane

def eredmenyek():
    lista = []
    for i in range(17):
        vel = r.randint(1,2)
        if vel == 1:
            lista.append(r.randint(120,200))
        else:
            lista.append(r.randint(50,120))
    return lista

def kijutottbe(lista):
    bejutott = 0
    for i in range(0,len(lista),1):
        if lista[i] / 200 *100 >= 70:
            bejutott += 1
    return bejutott

def volteotvenpt(lista):
    i = 0
    van = 0
    while i < len(lista) and lista[i] != 50:
        i += 1
    vane = i < len(lista)
    if vane:
        van = i+1
    return vane, van

def main():
    eredm = eredmenyek()
    print(eredm)
    max = maximum(eredm)
    print("A legnagyobb pontszám: ",max)
    min = minimum(eredm)
    print("A legkisebb pontszám: ",min)
    terjedelem = max - min
    print("A pontszámok terjedelme: ", terjedelem)
    maxp = lettemax(eredm)
    if maxp:
        print("Van max pontszám!")
    else:
        print("Nincs max pontszám!")
    atlagos = datlag(eredm)
    print("Az összes pontszám átlaga: ",atlagos)
    bejut = kijutottbe(eredm)
    print("Ennyien jutottak be: ",bejut)
    otven = volteotvenpt(eredm)
    print(otven)
main()