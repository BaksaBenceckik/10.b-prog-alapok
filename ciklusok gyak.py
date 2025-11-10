import random

# Generáljon ki 10db egy jegyű véletlen számot!
# Írassa ki a számok összegét!

osszeg = 0
for a in range(0, 11, 1):
    velSzam = random.randint(1,9)
    osszeg += velSzam
    print(velSzam, end=" ")
print( )
print("Összeg: ",osszeg)

# Hány db páros véletlen számot generált ki?
# Melyik a legnagyobb véletlen szám?