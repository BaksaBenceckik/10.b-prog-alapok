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

# szöveg betűi közé vessző
szoveg = "kalapács"
print(szoveg)
for karakter in szoveg():
    print(karakter, end=",")