def listaBeolvasas():
    lista = []
    fajl = open("./pdf txt/forgalom.txt","r",encoding="utf=8")
    elsoSor = fajl.readline()
    sorok = fajl.readlines()
    for sor in sorok:
        st = sor.strip().split(" ")
        lista.append((int(st[0]),int(st[1]),int(st[2]),int(st[3]),st[4]))
    fajl.close
    return lista

def melyikFele(lista,n):
    i = 0
    while i < len(lista) and n != lista[i]:
        i += 1
    vane = i < len(lista)
    if vane:
        return i
    else:
        return -1

def main():
    t = listaBeolvasas()

    n = int(input("Adjon meg egy értéket: "))
    hova = melyikFele(t,n)
    if hova < 1:
        print("Nincs ilyen jármű!")
    else:
        print("A jármű",t[4],"felől érkezett!")
main()