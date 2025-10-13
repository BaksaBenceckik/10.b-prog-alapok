import math
import random

a = 2
gyoka = math.sqrt(a)
print("gyök(" + str(a) +") = ",gyoka)

felkerekít = math.ceil(gyoka)
print("felsőegészrész:", felkerekít)
lekerekít = math.floor(gyoka)
print("alsóegészrész:", lekerekít)
kerekítés = round(gyoka,2)
print("kerekítés 2 tizedes jegyre:", kerekítés)
hatványozás = math.pow(gyoka, 2)
print("gyoka négyzeten:",hatványozás)

alap = 2
kitevo = 5
#hatványozás2 = math.pow(alap,kitevo)
hatványozás2 = alap ** kitevo
print(alap,"^",kitevo,"=",hatványozás2)

vszam1 = random.randint(2,10)
print(vszam1)