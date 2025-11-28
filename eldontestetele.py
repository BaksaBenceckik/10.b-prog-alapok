# Egy szövegben hány darab szóköz van?

db = 0
dbszo = 0
szoveg = "Géza kék az ég!"

for karakter in szoveg:
    if(karakter == " "):
        db += 1
        dbszo += 1
dbszo += 1 
print("Ennyi darab szóköz van a szövegben: ", db)
print("Ennyi szó van benne: ", dbszo)

# Adja meg, hogy a szövegben van-e cs betű (két karakter egymás mellett)
# pl. alma, kacsa, filc

szov = input("Adj meg egy szót: ")
i = 0

while(i < len(szov)-1 and (szov[i] != "c" or szov[i + 1] != "s")):
    i += 1
if i < len(szov)-1:
    print("Van benne!")
else:
    print("Nincs benne!")
print(i)

# HF.: De Morgan azonosság