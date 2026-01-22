import random as r

osszege = 0
lista = []
for i in range(30):
    a = r.randint(10,99)
    lista.append(a)
print(lista)
osszeg = 0
for szam in lista:
    if szam % 7 == 0:
        osszeg += szam
print("Héttel osztható számok összege: ",osszeg)
#for i in range(0,len(lista),1):
index = r.randint(0,len(lista)-1)
elem = lista[index]
print(elem)
print(osszege)