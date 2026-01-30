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

# HF.: 
# 1. Készíts egy listát, ami feltölti a francia kártya lapjaival! T - treff, K - káró, S - szív, P - pikk, T1, T2, ... T13, K1, K2, K3, ... K13, P1, P2, P3, ... P13, S1, S2, S3, ... S13.
# Töltse fel a listát a kártáykkal! 
# 2. Írjon egy függvényt ami megkeveri a paklit! 
# index 1, index2, index3 cseréje
# seged = index1
# index1 = index2
# index2 = seged
# 3. Írjon egy paraméteres fv-t, ami megadja hogy hanyadik helyen szerepel a megadott paraméterben megadott lap!
# 4. Írjon be egy lapértéket ami megadja hanyadik helyen van a lap! 