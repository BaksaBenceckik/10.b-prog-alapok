import random as r

# 1. feladat
szoveg = input("Adjon meg egy szöveget: ")
print(szoveg)
adjam = input("Adja meg hanyadik karakterig írjam: A szám értéke: 1 - " + len(szoveg) + "között legyen!")
# 2. feladat

ptdb = 0
egyben = 0
for i in range(13):
    veletlen = r.randint(10,99)
    if veletlen % 3 == 0:
        veletlen = r.randint(10,99)
    if veletlen % 2 == 1:
        veletlen += egyben
    if veletlen % 2 == 1:
        ptdb += 1
    print(veletlen, end= " ")
átlag = egyben / ptdb
print()
print("páratlanok összege: ",egyben)
print("páratlanok darabszáma: ",ptdb)
print("páratlan számok átlaga: ",round(átlag, 2))