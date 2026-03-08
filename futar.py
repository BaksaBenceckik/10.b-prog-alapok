def listaBeolvasas():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(" ")
        lista.append((int(st[0]),int(st[1]),int(st[2])))
    return lista

def hetElsoUtja(lista):
    mine = lista[0]
    for i in range(1,len(lista),1):
        if lista[i] < mine:
            mine = lista[i]
    return mine

def hetUtolsoUtja(lista):
    maxe = lista[0]
    for i in range(1,len(lista),1):
        if lista[i] > maxe:
            maxe = lista[i]
    return maxe
"""
def lustaDog(lista):
    het = [1,2,3,4,5,6,7]
    i = 0
    while i > len(lista) and lista[i] != het:
        i += 1
    index = i
    return index
"""
def legtobbFuvar(lista):
    maxe = lista[0]
    for i in range(1,len(lista),1):
        if lista[i][1] > maxe[1]:
            maxe = lista[i]
    return maxe

def egyNapMennyi(lista,tul):
    ures = 0
    for i in range(0,len(lista),1):
        if lista[i][0] == tul:
            ures += lista[i][2]
    return ures

def main():
    txt = listaBeolvasas()

    fuvar = hetElsoUtja(txt)
    print("A hét legelső fuvarja",fuvar[2],"km volt.")
    fuvar2 = hetUtolsoUtja(txt)
    print("A hét utolsó fuvarja",fuvar2[2],"km volt.")

    #mikornem = lustaDog(txt)
    #print(mikornem)

    legtobb = legtobbFuvar(txt)
    print("A legtöbb fuvar",legtobb[1],"volt egy nap.")

    osszeg = egyNapMennyi(txt,1)
    print(osszeg)
    osszeg2 = egyNapMennyi(txt,7)
    print(osszeg2)
main()