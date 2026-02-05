import random as r

# Kérjen be a felhasználótól egy számot [10,20] úgy ha rossz értéket adott meg ismételje meg a bekérést!
# Adja vissza a bekért helyes értéket!
# Írjon egy FV-t, ami isszaad egy listát! A korábban bekért szám legyen a db szám. A számok pedig 2 jegyű, de 4-el nem osztható számok! 
# Írjon egy FV-t, ami visszaadja a listából az első 7-re végződő számot, ha van ilyen! 

def bekerfv():
    beker = int(input("Adjon meg egy számot 10 és 20 között: "))
    while beker < 10 or beker > 20:
        print("Hibásan adta meg a számot!!!")
        beker = int(input("Adjon meg egy számot 10 és 20 között: "))
    if beker >= 10 or beker <= 20:
        return(beker)

def listafv(szam):
    lista = []
    while szam > len(lista):
        velszam = r.randint(10,99)
        if velszam % 4 != 0:
            lista.append(velszam)
    return(lista)

def hetrefv(lista):
    i = 0
    while i < len(lista) and not lista[i] % 10 != 7:
        i += 1
    vane = i < len(lista)
    if vane:
        return i
    else:
        return -1

def main():
    db = bekerfv()
    print("A bekért szám: ",db)
    lista = listafv(db)
    print(lista)
    index = hetrefv(lista)
    if index == -1:
        print("Nincs a listában 7-el osztható elem!")
    else:
        print("Van a listában 7-el osztható elem az",index+1,".","helyen!")
main()