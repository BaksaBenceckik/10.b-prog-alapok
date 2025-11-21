# 1. Kérjen be egy szöveget és egy betűt! Adja meg hány db betű van a szövegben!
szoveg = input("szoveg: ")
betu = input("betu: ")
for i in range(0, len(szoveg), 1):
    print(i, end=" ")
print()
for index in range(0, len(betu), 1):
    print(index, end=" ")
print()

# Van e benne betű és ha van, hány db? 