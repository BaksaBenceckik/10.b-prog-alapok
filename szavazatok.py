def listaFeltoltes():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(" ")
        lista.append((int(st[0]),int(st[1]),st[2],st[3],st[4]))
    return lista
"""
def jeloltekSzama(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg = i+1
    return osszeg

def hanySzavazat(lista,vn,kn):
    i = 0
    while i < len(lista) and not (lista[i][2] != vn and lista[i][3] != kn):
        i += 1
    vane = i < len(lista)
    if vane:
        return i
    else:
        return -1

def feladat(lista):
    knev = input("Keresztnév: ")
    vnev = input("Vezetéknév: ")
    if i >= 0:
        return(vnev,knev,"-nak/-nek",lista[i][1],"szavazata van.")
    else:
        return("Ő nem létezik!")
"""
def osszegZes(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i][1]
    return osszeg

def osszesszavazat(lista):
    osszeg = 0
    osszesen = 12345
    for i in range(0,len(lista),1):
        osszeg += lista[i][1]
    szazalek = osszeg/osszesen*100
    return (f"A választáson",(osszeg),"állampolgár, a jogosultak",round(szazalek,2),"%-a vett részt.")

def partDarab(lista,part):
    db = 0
    for i in range(len(lista)):
        if lista[i][4] == part:
            db += 1
    return db

def feladatS(lista):
    GYEP = partDarab(lista,"GYEP")
    HEP = partDarab(lista,"HEP")
    ZEP = partDarab(lista,"ZEP")
    TISZ = partDarab(lista,"TISZ")
    FUGG = partDarab(lista,"FUGG")
    print("Gyümölcs Evők Pártja: ",GYEP)
    print("Hús Evők Pártja: ",HEP)
    print("Zöldség Evők Pártja: ",ZEP)
    print("Tejivók Szövetsége: ",TISZ)
    print("Függetlenek: ",FUGG)

def feladat6(lista):
    maxe = lista[0]
    for i in range(1,len(lista),1):
        if lista[i] > maxe:
            maxe = lista[i]
    return maxe

def main():
    txt = listaFeltoltes()

    print("Képviselő jelöltek száma:",len(txt))

    osszeg = osszegZes(txt)
    print(osszeg)
    szazalek = osszesszavazat(txt)
    print(szazalek)

    fel5 = feladatS(txt)
    print(fel5)
main()