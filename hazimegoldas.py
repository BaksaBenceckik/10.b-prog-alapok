import random as r

def listafeltolt(n):
    lista = []
    for i in range(0,n,1):
        lista.append(r.randint(200, 900)/100)
        #lista.append(round(r.random()*7+2,2)) [0,1]*(9-2)+2
    return(lista)

def vaneszamnalnagyobb(szam, lista):
    i = 0
    while i < len(lista) and lista[i] <= szam:
        i += 1
    vane = i < len(lista) # ha nem teljesül akkor false lesz amúgy meg true
    return(vane)

def szamtanikozep(lista):
    darab = len(lista)
    osszeg = 0
    for elem in lista:
        osszeg += elem
    atlag = osszeg / darab
    return(round(atlag,2))

def ketszamkozott(a, b, lista):
    i = 0
    while i < len(lista) and not(lista[i] >= a and lista[i] <= b):
        i += 1
    vane = i < len(lista) # ha nem teljesül akkor false lesz amúgy meg true
    return(vane)

def jancsimax(lista):
    maxe = lista[0]
    for i in range(1,len(lista),1):
        if lista[i] > maxe:
            lista[i] = maxe
    return(maxe)

def main():
    jancsi = []
    juliska = []
    #lista = int(input())
    #listafeltolt(lista)
    jancsi = listafeltolt(14)
    juliska = listafeltolt(14)
    print("Juliska: ", juliska)
    print("Jancsi: ", jancsi)
    vanejuliska = vaneszamnalnagyobb(8.5, juliska)
    if vanejuliska:
        print("Van Juliskánál 8.5-nél nagyobb!")
    else:
        print("Nincs Juliskánál 8.5-nél nagyobb!")
    vanejancsi = vaneszamnalnagyobb(8.5, jancsi)
    if vanejancsi:
        print("Van Jancsinál 8.5-nél nagyobb!")
    else:
        print("Nincs Jancsinál 8.5-nél nagyobb!")
    jancsiatlag = szamtanikozep(jancsi)
    print("Jancsi átlaga: ",jancsiatlag)
    juliskaatlag = szamtanikozep(juliska)
    print("juliska átlaga: ",juliskaatlag)
    vanejuliskakozott = ketszamkozott(4.9, 5.1, juliska)
    if vanejuliskakozott:
        print("Juliskának van!")
    else:
        print("Juliskának nincs!")
    vanejancsikozott = ketszamkozott(4.9, 5.1, jancsi)
    if vanejancsikozott:
        print("Jancsninak van!")
    else:
        print("Jancsinak nincs!")
    maxjancsi = jancsimax(jancsi)
    print("Legnagyobb értéke Jancsinak: ",maxjancsi)
main()