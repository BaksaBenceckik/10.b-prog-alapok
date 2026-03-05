def adatokFeltoltese():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(";")
        lista.append((st[0],st[1],st[2],int(st[3]),st[4]))
    return lista

def kereses(lista,datum):
    i = 0
    while i < len(lista) and not (lista[i][0] == datum):
        i += 1
    vane = i < len(lista)
    if vane:
        return i
    else:
        return -1

def main():
    txt = adatokFeltoltese()
    print(txt)

    datum = input("Adjon meg egy dátumot: ")
    index = kereses(txt,datum)
    if index > -1:
        print(txt[index][1],txt[index][2],"született ekkor")
    else:
        print("Nem született senki ilyen dátummal")
main()