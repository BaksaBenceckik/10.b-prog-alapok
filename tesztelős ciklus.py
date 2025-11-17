import random as r

"""
Elől tesztelős ciklus
While ciklus
 - Nem tudjuk hogy hányszor fog lefutni (hányszor ismétel)
 - Feltételhez kötött
 - Akkor ismétel, ha feltétel igaz

while(feltétel):
    utasítások(szekvencia) 
"""

# Generáljon véletlen számokat [0,10] között, amíg nullát nem kapunk!

velszam = r.randint(0,10)
print(velszam, end=" ")
while(velszam != 0):
    velszam = r.randint(0,10)
    print(velszam, end=" ")

# Kérjen be számokat addig amíg nullát nem adnak meg!

szam = int(input("Írj be egy számot (0-nál kilép!): "))
while(szam != 0):
    szam = int(input("Írj be egy számot (0-nál kilép!): "))
print()

# Adja meg a beírt számok átlagát!

while(szam != 0):
    osszeg += szam
    db += 1
    szam = int(input("Írj be egy számot (0-nál kilép!): "))
print(round(osszeg/db,2))

# Adott egy szöveg. Adja meg hogy van-e benne x betű!

