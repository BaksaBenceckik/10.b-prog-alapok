def listaBeolvas():
    lista = []
    db = int(input())
    for i in range(db):  
        st = input().split(";")
        lista.append((int(st[0]),int(st[1]),st[2],st[3]))
    return lista

def listaDarab(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i]
    return osszeg

def kepviseloVane(lista,nev):
    i = 0
    while i < len(lista) and lista[i][2] != nev:
        i += 1
    vane = i < len(lista)
    szam = lista[i][1]
    return vane,szam

def main():
    adatok = listaBeolvas()

    db = listaDarab(adatok)
    print("A helyhatósági választáson",db,"Képviselőjelölt indult.")
    
    nev = input("Adjon meg egy nevet: ")
    vane = kepviseloVane(adatok,nev)
    if vane:
        print(nev,"szavazatot kapott!")
    else:
        print("Ilyen nevű képviselő jelölt nem szerepel a nyilvántartásban!")
main()