def listaFeltolt():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(" ")
        lista.append((int(st[0]),int(st[1]),int(st[2])))
    return lista 

def main():
    lista = listaFeltolt()
    print(lista)
main()