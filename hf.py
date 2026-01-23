import random as r

# Eljárás: Olyan függvény aminek nincs visszatérési értéke.
# [-951,950] közötti x50 és x00 típusú számok

def veletlenlista(n):  
    lista = []
    for i in range(n):
        negative = r.randint(0,1)
        velsz = r.randint(2,19)*50
        if negative == 0:
            lista.append(-1*velsz)
        else:
            lista.append(velsz)
    return(lista)
veletlenlista(13)
#    return(lista)
#print(veletlenlista())

# Írjon egy függvényt ami bármilyen list elemei közül megadja a legnagyobb szám indexét!

def listaatlaga(lista):
    osszeg = 0
#    for i in raneg(0,len(lista),1):
#        osszeg += lista[i]
    for elem in lista:
        osszeg += elem
    atlag = osszeg / len(lista)
    return(atlag)

# Hány db pozitív szám van? + pozitív számok átlaga (bármilyen lista)

def pozitivszamokatlaga(lista):
    osszeg = 0
    db = 0
    for elem in lista:
        if elem > 0:
            osszeg += elem
            db += 1
    atlag = osszeg / db
    return(round(atlag,2))

# legnagyobb szám indexe!

def legnagyobszamindexe(lista):
    maxi = 0
    for i in range(1,len(lista),1):
        if lista[i] > lista[maxi]:
            maxi = i
    return(maxi)

# Írjon egy függvényt a listának a terjedelmét. Terjedelem =  maximum - minimum.

def terjedelem(lista):
    maxe = lista[0]
    for i in range(1,len(lista),1):
        if lista[i] > maxe:
            maxe = lista[i]
    mine = lista[0]
    for i in range(1,len(lista),1):
        if lista[i] < mine:
            mine = lista[i]
    terjedelem = maxe - mine
    return(terjedelem)
            
# egy listából adjuk meg hány db negatív 00-ra végződő szám van

def negativ00ravegzodo(barmilyenlista):
    db = 0
    for i in range(0,len(barmilyenlista),1):
        if barmilyenlista[i] % 100 == 0:
            db += 1
    return(db)

def main():
    lista1 = veletlenlista(2)
    print(lista1)
    lista2 = veletlenlista(21)
    print(lista2)
    """
    print("00-ra végződőek: ",negativ00ravegzodo(lista2))
    print("00-ra végződőek: ",negativ00ravegzodo(lista1))
    print("lista1 átlaga: ",listaatlaga(lista1))
    print("lista2 pozitívak átlaga: ",pozitivszamokatlaga(lista2))
    """
    print("lista2 legnagyobb index: ",legnagyobszamindexe(lista2)+1)
    maxilista1 = legnagyobszamindexe(lista1)
    print("lista1 legnagyobb szám indexe: ",maxilista1+1)
    mintolmaxig = terjedelem(lista2)
    print("A lista terjedelme: ",mintolmaxig)
main()