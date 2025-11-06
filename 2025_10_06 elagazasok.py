import random
# kérjen be egy egész számot és döntse el, hogy páros vagy páratlan?

szam = 56 #int(input("Adjon meg egy egész számot:"))
if(szam % 2 == 0): 
    print("páros")
else:
    print("páratlan")

# kérjen be a felhasználótól egy számot és mondja meg hogy tízzel osztható -e? Ha nem osztható tízzel írja ki az utolsó számjegyét!
# pl. be: 10 ki: tízzel osztható
# pl. be: 12 ki: tízzel nem osztható, utolsó számjegy 2

szam2 = 24 #int(input("Adjon meg egy tízzel osztható számot:"))
if(szam2 % 10 == 0):
    print("tízzel osztható")
else:
    print("nem osztható tízzel")
    print("az utolsó számjegy:" + str(szam2 % 10))

# Kérjen be egy másik számot és írassa ki a két szám reciprokának összegét!

szam3 = 13 #int(input("adjon meg egy másik számot:"))

if(szam != 0):
    if(szam2 != 0):
        rec = 1/szam2
        rec2 = 1/szam3
        print(rec+rec2)
    else:
        print("a második számnak nincs reciproka")
else:
    print("az első számnak nincs reciproka")
import math
if(szam2 + szam3 >= 0):
    print(math.sqrt(szam2 + szam3))
else:
    ("a két számn összege negatív")
#logikai operátorok
#and, or ,not, xor

if(szam2 != 0 and szam3 != 0):
    rec = 1/szam2
    rec2 = 1/szam3
    print(rec+rec2)
else:
    print("A két szám valamelyike nulla!")
#HF: bool algebra
#HF: Kérjen be a felhasználótól három db számot (lehet tört is) ez a három szám egy háromszög három oldala.
# 1. derékszögű e a háromszög?
# 2. egyenlőszárú e a háromszög?
# 3. szabályos e a háromszög?

#HF: Python - ciklusok, loops, literáció, ...


#Generáljon ki három véletlen háromjegyű számot, amelyek 13-al oszthatók!
#Állítsa ezeket sorrendbe! 
#Adja meg az átlaguk!
#Van-e közöttük 4-el végződő?

#páros kétjegyű szám [5,44]*2
#100/7 = 7,6
#999/13 = 76,8

a = random.randint(8,76)*13
b = random.randint(8,76)*13
c = random.randint(8,76)*13

szamjegy = int(input("Adjon meg egy számjegyet: "))

print(a,b,c)

if(a % 10 == szamjegy or b % 10 == szamjegy or c % 10 == szamjegy):
    print("Van közte "+str(szamjegy)+"-re végződő")
else:
    print("Nincs közte "+str(szamjegy)+"-re végződő")
