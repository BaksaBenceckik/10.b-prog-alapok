import random as r

# HF.: 
# 1. Készíts egy listát, ami feltölti a francia kártya lapjaival! T - treff, K - káró, S - szív, P - pikk, T1, T2, ... T13, K1, K2, K3, ... K13, P1, P2, P3, ... P13, S1, S2, S3, ... S13.
# Töltse fel a listát a kártáykkal! 
# 2. Írjon egy függvényt ami megkeveri a paklit! 
# index 1, index2, index3 cseréje
# seged = index1
# index1 = index2
# index2 = seged
# 3. Írjon egy paraméteres fv-t, ami megadja hogy hanyadik helyen szerepel a megadott paraméterben megadott lap!
# 4. Írjon be egy lapértéket ami megadja hanyadik helyen van a lap!

def kartyageneralas():
    lista = []
    for i in range(1,14,1):
        lista.append("T"+str(i))
        lista.append("K"+str(i))
        lista.append("S"+str(i))
        lista.append("P"+str(i))
    return lista

def keveres(pakli):
    for i in range(500):
        a = r.randint(0,51)
        b = r.randint(0,len(pakli)-1)
        sv = pakli[a]
        pakli[a] = pakli[b]
        pakli[b] = sv

def lapindex(lap,pakli):
    i = 0
    while pakli[i] != lap:
        i += 1
    return i

def main():
    pakli = kartyageneralas()
    #print(pakli)
    keveres(pakli)
    print(pakli)
    lap = input("1 és 13 között hajrá: ")
    index = lapindex(lap,pakli)
    print(index)
main()