import math
import random

# 1. Adottak a téglalap alapélei. Írassa ki az oldalakat és a kerületet, területet!

ela = 2
elb = 4
print("K = ", 2 * (ela + elb))
print("T = ", ela * elb)

# 2. Legyen megadva a kör sugara alapértéknek. Számolja ki a kör átmérőjét, kerületét, területet!

sugara = 5
print("K = ", 2 * sugara * 3.14)
print("T = ", 3.14 * pow(sugara, 2))

# 3. Legyen megadva egy szabályos háromszög oldala. Írassa ki a megadott háromszög magasságát.

hszogoldal = 3
magassag = 3 * math.sqrt(3) / 2
print("A háromszög magassága: " +str(round(magassag, 2)))

#4. Legyen megadva egy szabályos háromszög oldala. Írassa ki a megadott háromszög magasságát.

holdal = 5
eredmény = (holdal * math.sqrt(3)) / 2
print("Magassága = ", round(eredmény, 2))

# 5. Legyen megadva egy kockának az egyik éle. Írassa ki a lap átló és a test átló hosszát!

ele = 5
lapatlo = 5 * math.sqrt(2)
testatlo = 5 * math.sqrt(3)
print("A lap átló: " +str(round(lapatlo, 2)) + " A test átló: " +str(round(testatlo, 2)))

# 6. Kérd be külön a vezetéknevet és a keresztnevet, majd összefűzve írasd ki!

vezeteknev = input("Írd be a vezetékneved: ")
keresztnev = input("Írd be a keresztneved: ")
print("A teljes neved: " +str(vezeteknev +" "+ keresztnev))

# 7. Kérjen be egy egész számot! Páros-e a szám? (Oszthatóság vizsgálata: % százék, mint művelet)

szam = int(input("adjon meg egy számot: "))
if(szam % 2 == 0):
    print("A szám páros!")
else:
    print("A szám páratlan!")

# 8. Segítsd az osztályfőnök munkáját a bizonyítvány íráshoz! Ha az érdemjegy 1,2,3,4,5 - írassa ki szövegesen: 1-elégtelen, 2-elégséges, 3-közepes, 4-jó, 5-jeles. Felhasználó adja meg az érdemjegyet!

jegy = int(input("Adja meg az érdemjegyet: "))
if(jegy == 1):
    print("1-elégtelen")
elif(jegy == 2):
    print("2-elégséges")
elif(jegy == 3):
    print("3-közepes")
elif(jegy == 4):
    print("4-jó")
elif(jegy == 5):
    print("5-jeles")
else:
    print("1-5-ig vannak érdemjegyek")

# 9. Megvan adva a víz hőfoka. Írassa ki, a hőfok alapján hogy szilárd, folyékony, gáz halmazállapotú!

hfok = int(input("Adja meg a víz hőfokát: "))
if(hfok < 0):
   print("szilárd")
elif(hfok >= 0 and hfok < 100):
    print("folyékony")
elif(hfok > 100):
    print("gáz")

# 10. Háromszög egyenlőtlenség. Adva van három oldal hossza. Adja meg, hogy szerkeszthető-e a háromszög! HE - akkor szerkeszthető egy háromszög, ha bármely két oldal összege, nagyobb a harmadiknál.

elsold = 3
masold = 2
harmold = 5
if(elsold + masold > harmold):
    print("szerkeszthető")
elif(elsold + harmold > masold):
    print("szerkeszthető")
elif(masold + harmold > elsold):
    print("szerkeszthető")
else:
    print("nem szerkeszthető")

# 11. Adott a hőmérséklet farenheitben. Számolja át cfokba! 

fho = 50
eredmeny = (fho - 32) * 5/9
print(eredmeny)

# 12. Adott a hőmérséklet cfokban. Számolja át farenheitbe!

cho = 10
erdmny = cho * 9/5 + 32
print(erdmny)

# 13. Kérjen be a felhasználótól egy időtávot másodpercben. Számolja át órára, percre, másodpercre!

ido = int(input("Írjon be mp-ben időt: "))
ora = ido / 3600
sec = ido / 60
print("mp = ", round(ido, 2))
print("perc = ", round(sec, 2))
print("óra = ", round(ora, 2))

# 14. Írasd ki egy bekért szó utolsó karakterét

szo = input("Írj be egy szót: ")
print(len(szo))
print("Utolsó karakter: ", szo[-1])

# 15. Írassa ki, hogy az adott szó első és utolsó karaktere egyezik-e?

if(szo[0] == szo[-1]):
    print("Az első és utolsó karakter megegyezik!")
else:
    print("Az első és utolsó karakter nem egyezik!")

# 16. Írassuk ki egy bekért szöveg minden második betűjét!

print("Minden második karakter: ", szo[: : 2])

# 17. Írasd ki visszafele egy bekért szót!

print(szo[: : -1])

# HF.: 17-21