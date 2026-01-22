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

def main():
    lista1 = veletlenlista(2)
    print(lista1)
    lista2 = veletlenlista(21)
    print(lista2)

    print("00-ra végződőek: "negativ00ravegzodo(lista2))
    print("00-ra végződőek: "negativ00ravegzodo(lista1))
main()

# egy listából adjuk meg hány db negatív 00-ra végződő szám van

def negativ00ravegzodo(barmilyenlista):
    db = 0
    for i in range(0,len(barmilyenlista),1):
        if barmilyenlista[i] % 100 == 0:
            db += 1
    return(db)