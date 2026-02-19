#a = 23
#b = "alma"
#c = True
#
#t = [a,b,c,["K1","K2"]]
#t[0]

# Írj egy fgv-t ami megadja, melyik hónapban volt a legjobb az eredménye.

def maxIndex(lista):
    maxi = 0
    for i in range(0,len(lista),1):
        if lista[i] > lista[maxi]:
            maxi = i
    return maxi

def legjobbErdmny(lista,lista2):
    maxi = 0
    honap = lista2[0]
    for i in range(1,len(lista),1):
        if lista[i] > lista[maxi]:
            maxi = i
            honap = lista2[i]
    return (honap, maxi, lista2[maxi])

def main():
    honapok = ["Január","Február","Március","Április","Május","Június","Július","Augusztus","Szeptember","Október","November","December"]
    Jani = [4.0, 3.8, 4.2, 4.1, 3.8, 4.2, 3.0, 3.6, 4.2, 4.1, 4.7, 4.2]
    eredmeny = legjobbErdmny(Jani,honapok)
    print(eredmeny)
    maxindex = maxIndex(Jani)
    print(honapok[maxindex])
    valasz = legjobbErdmny(Jani,honapok)
    #valasz[2] = 5.0
    print(valasz)

    # tördelés - split
    szoveg = "Jani 2000 10 03"
    print(szoveg)
    tordelt = szoveg.split(" ")
    print(tordelt)
    print(2026-int(tordelt[1]))

    adat = (tordelt[0], int(tordelt[1]), int(tordelt[2]), int(tordelt[3]))
    print(adat)

    szoveg2 = "2026.02.19 3 Programozás"
    tordelt2 = szoveg2.split(" ")
    print(tordelt2[0])

    adat2 = tordelt2[0].split(".")
    print(adat2[1])

    szoveg3 = "ABC-123,Kis Pista,KJ358638351,1992.03.10"
    tord = szoveg3.split(",")
    print(tord)
    ev = tord[3].split(".")
    print(ev[0])
    vnev = tord[1].split(" ")
    print(vnev[0])
main()

# HF.: 
# "ABC123 Kis Pista KJ-358638351 1992_03_10"
# rendszám utolsó 3 száma
# keresztnév
# hónap

# "Nagy Béla:2026_02_19 - 12:13:20"
# Nagy Béla az adott napon és időben csekkolt be!
# nap
# óra
# keresztnév