def akarmi():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split()
        lista.append((int(st[0]),int(st[1]),int(st[2])))
    return lista

def gyak():
    szoveg = input("Adjon meg egy szoveget: ")
    for i in range(0,len(szoveg),1):
        print(str(i) + szoveg[i],end= " ")

def main():
    hello = akarmi()
    print(hello)
main()