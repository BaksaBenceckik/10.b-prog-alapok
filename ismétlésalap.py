"""
Utasítás (szekvencia)
- menj előre
- fordulj
- szívd be a levegőt
- fújd ki a levegőt
- ...
- írasd ki - print()
- tárold el - vaáltozónév = érték
- számold ki - változónév = <képlet>
- kérd be -input("add meg: ")

Elágazás - (szelekció)
- ha piros a lámpa akkor megállok
- ha zöld a lámpa akkor alindulok
- ha fal van előttem akkor elfordulok
- ha tudom, hogy nem megy akkor gyakorlom
- ...
- ha a bekért szám páros akkor kiírom, hogy páros
  különben kiíratom, hogy páratlan
- ha a dobókocka értéke 5 akkor előre lépek 5-öt

Ismétlés - ciklus - (literáció)
- addig menj, amíg a tábla van
- addig dobáld az aprót a gépbe, amíg el nem éred a megfelelő összeget
- üss bele 3 db tojást
- addig tegyél bele cukrot, amíg elég édes nem lett
- addig gyakorlok, amíg meg nem értem
- addig fog a tanár piszkálni, amíg nem látja, hogy értem
"""

db = 12
print("szám: ",db)

# a szám utolsó számjegye páros-e?
utolso_szamjegy = db % 10
print("utolsó számjegy: ",utolso_szamjegy)

if(utolso_szamjegy % 2 == 0):
    print("páros")
else:
    print("páratlan")

# db-nyi almát szeretnék látni
for kiskutya in range(0, db, 1):
  print(kiskutya+1, "alma", end=" ")

index = 0
print()
szoveg = "kalapács"
for karakter in szoveg:
  print(index+1, karakter, end=" ")
  index += 1 # növelem az index értékét 1-el

print()
for i in range(0, len(szoveg), 1):
  print(i, szoveg[i], end=" ")