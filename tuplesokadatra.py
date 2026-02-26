
def listaFeltolt():
    db = int(input())
    t = []
    for i in range(db):
        sor = input() # alma 12 500
        st = sor.split(" ") # segéd lista : ["alma" , "12" , "500"]
        tuple = (st[0],int(st[1]),int(st[2]))
        t.append(tuple)
    return t

def hanyMazsa(adatok):
    szam = 5
    valtozo = 0
    for i in range(0,szam,1):
        val = adatok[0][1]
        db += 1
        valtozo += val
    return valtozo

def hanyDarab(ertek,lista):
    db = 0
    for i in range(0,len(lista),1):
        if lista[i][2] > ertek:
            db += 1
    return db

# hf.:

def maxindex(lista):
    maxi = 0
    for i in range(1,len(lista,1)):
        if lista[i][2] > lista[maxi][2]:
            maxi = i
    return maxi

def gyumolcskerese(adatok,gyumolcsok):
    i = 0
    while i < len(adatok) and adatok[i][1] != gyumolcsok:
        i += 1
        vane = i < len(adatok)
        if vane:
            return i
        else:
            return -1

def main():
    adatok = listaFeltolt()
    print(adatok)
    adat = adatok[2]
    print(adat[0])
    hanyvan = hanyMazsa(adatok)
    print(hanyvan)
    db = hanyDarab(1000,adatok)
    print(db)
    index = maxindex(adatok)
    print(index[2])
    gyumolcsok = input("Gyümölcs neve: ")
    keresesindex = gyumolcskerese(adatok,gyumolcsok)
    if keresesindex < 0:
        print("Nincs ilyen gyümölcs")
    else:
        print(adatok[keresesindex][2],"a",adatok[keresesindex][2],"Ft/db")
main()

# Ítrjon fv-t, ami visszaadja a szerkezetből högy összesen hány mázsa gyümölcs van!
# Írjon egy fv-t ami visszaadja a paraméterben megadott értékektől nagyobb összeggel rendelkező gyümölcsök darabszámát!
# HF.: Írjon fv-t ami megadja a legdrágább gyümölcs nevét!
# Írjon fv-t ami bekér a felhasználótól egy gyümölcsöt és ha van ilyen ki írja az adatait. pl.: stzilva, 13, 300 Ft/kg
# Ha nincs ilyen adat akkor írja ki hogy nincs ilyen gyümölcs!