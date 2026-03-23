def fajlBeolvas():
    lista = []
    f = open("./pdf txt/resztvevok.txt","r",encoding="utf=8")
    elsoSor = f.readline()
    sorok = f.readlines()
    for sor in sorok:
        st = sor.strip().split(";")
        lista.append((st[0],st[1],st[2],int(st[3]),st[4]))
    f.close()
    return lista, elsoSor

def main():
    t = fajlBeolvas()
    print(t)
main()