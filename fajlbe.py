def fajlbeolvas():
    lista = []
    fajl = open("./pdf txt/szeleromu.txt","r",encoding="utf=8")
    sorok = fajl.readlines()
    lista = []
    for sor in sorok:
        st = sor.strip().split(";")
        lista.append((st[0],st[1],st[2],int(st[3]),int(st[4]),int(st[5])))

    # db = int(fajl.readline())
    # print(db)

    # lista = []
    # for i in range(db):
    #     sor = fajl.readline()
    #     sor2 = sor.strip().split(";")
    #     lista.append((sor2[0],sor2[1],sor2[2],int(sor2[3]),int(sor2[4]),int(sor2[5])))

    fajl.close
    return lista

def osszegzesTetele(lista, datum):
    osszeg = 0
    for i in range(0,len(lista),1):
        if lista[i][5] == datum:
            osszeg += lista[i][3]
    return osszeg

def main():
    fajl = fajlbeolvas()

    datum = int(input("Adjon meg egy évszámot: "))
    osszeg = osszegzesTetele(fajl,datum)
    print(datum,"-ban/ben",osszeg,"db szélerőművet telepítettek.")
    if datum < 2000:
        print(datum,"nem szerepel a listában.")
    elif datum > 2011:
        print(datum,"nem szerepel a listában.")
main()