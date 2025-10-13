# változók deklarálása és inicializálása
# változók létherozása és kezdőérték adása
# változók = "kezdőérték"
nev = "Baksa Bence"
osztály = "10.B"
datum = "2025.09.08"

# "'"
# '"'
print(datum, datum)
print(osztály, nev, sep="\n")

# operátorok

# + konkatenálás, concat, összefűzés - két szöveget!!!!
összefűzés = nev+" bármit, akármit "+osztály
print(összefűzés)

# * többszörözés
soknev = nev * 5
print(soknev)

"""
Elemi típusok
-szöveg - string -str
(-karakter)
-szám -egész (integer - int), lebegőpontos (tört) (float)
-logikai
"""

aEgesz = 123
bTort = 34.23
szSzam = "12"
logikai = True

print("a Egész:", aEgesz)
print("b Tört:", bTort)
print("sz Szám:", szSzam)
print("logikai:", logikai)

# Egész operátorok
print("a * 2 =",aEgesz * 2)
print("a + 2 =",aEgesz + 2)
print("a - 2 =",aEgesz - 2)
print("a / 2 =",aEgesz / 2)

# Div - egészrész, Mod - modulus(maradék)
# div - //
# mod - %

print("a div 8=", aEgesz // 8)
print("a mod 8=", aEgesz % 8)
print(int(szSzam)+aEgesz)
print(aEgesz+str(+szSzam))

print(str(aEgesz)+szSzam)
print(szSzam+int(aEgesz))