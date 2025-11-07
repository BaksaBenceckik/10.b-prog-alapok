import random as r 

"""
# Ciklusok - simétlés - loops

# Számlálós - for ciklus
Végig megy a megadott elemeken vagy intervallumon!

for elem in range(mettol, meddig, hányasával):
    Ismétlendő folyamat

for karakter in szoveg:
    Ismétlendő folyamat

Tesztelős - while
"""

# [1-10]ig a számok
#for elem in range(0, 19, 2):
#    print(elem, end=" ")

# első 10 db páros szám
for elem in range(0, 19, 2):
    print(elem, end=" ")
print()

# szöveg betűi közé vessző
szoveg = "kalapács"
print(szoveg)

for index in range(0, len(szoveg), 1):
    print(szoveg[index]+",", end="")
#print(szoveg[len(szoveg)-1])
#print(szoveg[-9])
#print()

# [30-50]-ból a 4-el osztható számokkal.
for elem in range(32, 50, 4):
    print(elem, end=" ")
print()

for elem in range(10, 0, -1):
    print(elem, end=" ")
print()

for index in range(len(szoveg)-1, -1, -1):
    print(szoveg[index], end=" ")
print()

n = len(szoveg)
for index in range(0, n, 1):
    print(szoveg[n-index-1], end=" ")
print()

for index in range(-1, -n-1, -1):
    print(szoveg[index], end=" ")
print()

# írassa ki a szöveget az helyével társítva! (1k 2a 3l 4a 5p 6á 7c 8s)
# BE: kalapács
# KI: 1k 2a 3l 4a 5p 6á 7c 8s

for index in range(0, n, 1):
    print(str(index+1)+szoveg[index], end=" ")
print()

# Írasson ki 5 db véletlen karaktert a szövegből!

for db in range(0, 5, 1):
    szam = r.randint(0,n-1)
    print(szoveg[szam],end=" ")
print()

ujszoveg = ""
for index in range(-1, -n-1, -1):
    ujszoveg += szoveg[index]
print(ujszoveg)