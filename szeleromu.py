def adatokBeolvasasa():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(";")
        lista.append((st[0],st[1],st[2],int(st[3]),int(st[4]),int(st[5])))
    return lista

def szeleromuvekDarab(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i][3]
    return osszeg

def maximumIndexDb(lista):
    maxi = 0
    for i in range(1,len(lista),1):
        if lista[i][3] > lista[maxi][3]:
            maxi = i
    return maxi

def vaneSszeleromuVarosban(lista,varos):
    i = 0
    while i < len(lista) and lista[i][0] != varos:
        i += 1
    vane = i < len(lista)
    return vane

def main():
    txt = adatokBeolvasasa()

    db = szeleromuvekDarab(txt)
    print("Ennyi darab szélerőmű van Magyarországon:",db)

    maxindex = maximumIndexDb(txt)
    print(txt[maxindex][0], "városban",txt[maxindex][5],"évében csinálták a legtöbb szélerőművet.")

    varos = input("Adjon meg egy várost: ")
    vane = vaneSszeleromuVarosban(txt,varos)
    if vane:
        print("Ebben a városban van szélerőmű.")
    else:
        print("Ebben a városban nincs szélerőmű.")
main()

# hf.: Szavazatok.txt 2013 május (41 adat kb)
# http://informatika.fazekas.hu/erettsegi/emelt-szintu-feladatok/
# !6-os feladatig!