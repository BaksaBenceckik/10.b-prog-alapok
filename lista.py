import random as r

# a szövegben van-e "sz" betű?

szoveg = "aszály"
dube = "sz"
"""
print(szoveg)
if "sz" in szoveg:
    print("Van benne sz betű!")
else:
    print("Nincs benne sz betű!")
"""
index = 0
while(index < len(szoveg)-1 and not(szoveg[index] == dube[0] and szoveg[index+1] == dube[1])):
    index += 1
if index < len(szoveg)-1:
    print("Van benne", dube, "betű!")
else:
    print("Nincs benne", dube, "betű!")

"""
lista -dinamikus
- tudunk bele új elemet ralkni, ezzel nő az elem száma
- tudunk belőle törölni, ezzel csökken az elemszáma
- lekérhető bármelyik eleme
- módosítható bármelyik eleme
deklarálás + inicializálás:
létrehozás + kezdőérték adás:
lista_neve = []
új elem hozzáadása:
lista_neve.append(ujelem)
elem törlése:
lista_neve.remove(elem)
beégetett lista:
lista_neve = [3,2,5,7,1]
lista hossza:
len(lista_neve)
"""
számok = [3,2,5,7,1]
számok.append(12)
print("Első elem: ", számok[0])
számok.remove(3)
print("Utlsó elem: ", számok[len(számok)-1]) # könnyebb: számok[-1]
print("Hossza: ", len(számok))

# HF.: Tölts fel egy 13 elemű listát [0, 20]
# Számok átlaga
# Hány db páros szám van a listában
# van-e benne nulla?

n = 13
lista = []
for index in range(0,n,1):
    a = r.randint(0,20)
    lista.append(a)
print(lista)

osszeg = 0
for index in range(0,len(lista), 1):
    osszeg += lista[index]
print(osszeg)