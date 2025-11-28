import random as r

# 1. Kérjen be egy szöveget és egy betűt! Adja meg hány db betű van a szövegben!
szoveg = input("szoveg: ")
betu = input("betu: ")
mennyiseg = 0
for i in range(len(szoveg)):
    mennyiseg += 1
print(mennyiseg)
mennyiseg2 = 0
for i in range(len(betu)):
    mennyiseg2 += 1
print(mennyiseg2)
#for i in range(0, len(szoveg), 1):
#    print(i, end=" ")
#print()
#for index in range(0, len(betu), 1):
#    print(index, end=" ")
#print()

"""
db = 0
for karakter in szoveg:
    if(karakter == betu):
        db += 0
        print(db)
"""

index = 1
while(index > len(szoveg) and szoveg[index] != betu):
    #index = index + 1
    index += 1
print(index)