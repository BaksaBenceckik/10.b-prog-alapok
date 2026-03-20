def fajlBeolvasas():
    lista = []
    f = open("./pdf txt/forgalom.txt","r",encoding = "utf=8")
    elsoSor = f.readline()
    sorok = f.readlines()
    for sor in sorok:
        st = sor.strip().split(" ")
        lista.append((int(st[0]),int(st[1]),int(st[2]),int(st[3]),st[4]))
    f.close
    return lista, elsoSor

def main():
    txt = fajlBeolvasas()
    t = txt[0]
    elsoSor = txt[1]
    print(t)
    print()
    print(elsoSor)
main()