import random as r

"""
probalkozasok = 0
gondolt_szam = r.randint(10,99)
a = gondolt_szam + 10
b = gondolt_szam - 10
print("A gondolt szám" + " " + str(b) + " " + "és" + " " + str(a) + " " + "között van!")
tipp = ""
while(gondolt_szam != tipp):
    tipp = int(input("Írj be egy számot: "))
    if tipp == gondolt_szam:
        print("Eltaláltad!")
    elif tipp > gondolt_szam:
        print("A tipped NAGYOBB mint a gondolt szám!")
        probalkozasok += 1
    elif tipp < gondolt_szam:
        print("A tipped KISEBB mint a gondolt szám!")
        probalkozasok += 1
print("próbálkozások: ", probalkozasok)
print()
"""

# hf: ha nem kétjegyűt adott meg az ne legyen új próbálkozás és figyelmeztesse a felhasználót!

szo = "kalapács"
i = 0
while(i < len(szo) and szo[i] != "x"):
    i += 1
print(i)