import random

# készítsen egy függvényt ami egy db számtól függ, és visszaad egy feltöltött listát [-10,50] közötti számokkal.
# készítsen egy függvényt, ami bármilyen lista elemeit megvizsgálva visszaadja hogy hány db pozitív szám van. 

def listafeltolt(db):
    lista = []
    for i in range(db):
        lista.append(random.randint(-10,50))
    return(lista)
print(lista)

def pozitívdb(szamoklista):
      darab = 0
      for i in range(0,len(szamoklista),1):
        if szamoklista[i]>0:
            datab += 1
    return darab
print(pozitívdb())

def main():
    lista = []
    lista = listafeltolt(13)
    print(lista)

main()