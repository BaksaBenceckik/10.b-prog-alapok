import random as r
import math

# Generáljon egy listába 13 db olyan négyjegyű véletlen számokat amik 3-ra, 5-re és 7-re végződnek.
# Hány darab 3-ra, 5-re, 7-re végződő szám van. 

lista = []
for i in range(13):
    a = r.randint(100,999)
    veletlen = r.randint(1,3)
    if veletlen == 1:
        lista.append(a*10+3)
    elif veletlen == 2:
        lista.append(a*10+5)
    else:
        lista.append(a*10+7)
print(lista)

ötre = 0
hetre = 0
haromra = 0
for i in range(0, len(lista), 1):
    if(lista[i] % 10 == 3):
        haromra += 1
    elif(lista[i] % 10 == 5):
        ötre += 1
    elif(lista[i] % 10 == 7):
        hetre += 1
print("három: ", haromra, "öt: ", ötre, "hét: ", hetre)

# számtani átlag

darab = len(lista)
összeg = 0
#for index in range(0,n,1):
#    osszeg += lista[index]
for elem in lista:
    összeg += elem
átlag = összeg / darab
print("lista elemeinek összege: ", összeg)
print("átlaga: ", round(átlag, 2))

# hány db szám van átlag alatt

db = 1
for i in range(0,len(lista),1):
    if(átlag > lista[i]):
        db += 1
print("darab: ",db)

# mértani átlag

szorzat = 1
for elem in lista:
    szorzat *= elem
matlag = math.pow(szorzat,1/len(lista))
print("mértani átlag: ", round(matlag,2))

# a mértani átlag alatti számok összege

nossz = 0
for a in lista:
    if(matlag > a):
        nossz += a
print("m összeg: ", nossz)

# 30db 13-ra, 17-re végződő számokkal, hány osztható 13-mal és 17-tel

lista2 = []
for i in range(30):
    a = r.randint(10,99)
    veletlen2 = r.randint(1,2)
    if veletlen2 == 1:
        lista2.append(a*100+13)
    else:
        lista2.append(a*100+17)
print(lista2)
tizenharom = 0
tizenhet = 0
for i in range(0, len(lista2), 1):
    if(lista2[i] % 13 == 0):
        tizenharom += 1
    elif(lista2[i] % 17 == 0):
        tizenhet += 1
print("tizenhárom: ", tizenharom, "tizenhét: ", tizenhet)

n = 30
listaa = []

for i in range(0, n, 1):
    b = r.randint(10,99)
    veletlen3 = r.randint(1,2)
    if(veletlen3 == 1):
        listaa.append(b*100+13)
    else:
        listaa.append(b*100+17)
print(listaa)

# bekérsz egy hosszabb szöveget, hány darab felhasználó álltal megadott betű van benne.

szoveg = "bekérsz egy hosszabb szöveget, hány darab felhasználó álltal megadott betű van benne."
betu = input("Adjon meg egy betűt: ")
dbb = 0
for karakter in szoveg:
    if karakter == betu:
        dbb += 1
print(dbb)

# bekérsz két szót, mondd meg adott indexen hány darab eltérés van! (pl.: alma, alkat -> 2 db külömbség)

szo1 = "alma"
szo2 = "alkat"
kulombseg = 0
minimumhoz = 0
if len(szo1)>len(szo2):
    minimumhoz = len(szo2)
else:
    minimumhoz = len(szo1)
for i in range(0,minimumhoz,1):
    if(szo1[i] != szo2[i]):
        kulombseg += 1
print("külömbség: ",kulombseg+)