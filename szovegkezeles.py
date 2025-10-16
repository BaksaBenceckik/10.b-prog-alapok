import random
# lebegőpontos - float - tört
a = 1.25
b = 1.25 #float(input("Adjon meg egy tízedes törtet: "))
print(b*4)

# generáljon [ki 1,10[ közötti tört számot 2 tizedes jegyre
# pl. 1.36, 2.30

#c = random.randint(100,999)/100
#c = random.random(1,10) # [0,1[
#print(round(c,2))

#HF: Ezt megoldani!

#Szövegkezelés
szoveg = input("Adjon meg egy szöveget: ")
print(szoveg)
print("Szöveg hossza:",len(szoveg))
print("Első karakter",szoveg[0])
# szöveg = karakter lánc 
karakter = szoveg[0]
kod = ord(szoveg[0])
print(kod)
ujkod = kod + 1 
ujkarakter = chr(ujkod)
print(ujkarakter)

d = chr(random.randint(97,122))
e = chr(random.randint(97,122))
f = chr(random.randint(97,122))
print(d,e,f)

#Kérje be a felhasználó keresztnevét! Generáljon neki egy jelszót, 
#az első három karakterének ascii kódjának szorzatát! Ha nincs a név háromjegyű,
#akkor kettő esetén a hossz érték legyen a szorzat harmadik tagja, egy esetén pedig a szám töve legyen. 
#Alma - 65 * 108 * 109
#Co - 67 * 111 * 2
#G - 71 * 71 * 71
input(Adja meg a keresztnevét: )