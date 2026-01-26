def vaneketjegyu(lista):
    i = 0
    while i<len(lista) and not lista[i]>=10 and lista[i]<=99:
        i += 1
    vane = i<len(lista)
    return(vane)
def main():
    szamok = [2,5,6,3,7,11,9,1,2]
    print(szamok)
    ketjegyeu = vaneketjegyu(szamok)
    print(ketjegyeu)
main()