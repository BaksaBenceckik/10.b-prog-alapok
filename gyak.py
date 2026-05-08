szoveg = "okostábla kijelző választás"
print(szoveg)
for karakter in szoveg:
    if karakter != " ":
        print(karakter,end="")
    else:
        print()
print()    

print(f"Adjon meg egy számot [1,{len(szoveg)}] között: ")
db = int(input())
while(not(db <= len(szoveg) and db >= 1)):
    print(f"Adjon meg egy számot [1,{len(szoveg)}] között: ")
    db = int(input())
ujszoveg = ""
for i in range(0,db,1):
    ujszoveg += szoveg[i]
print(ujszoveg)

print(f"Adja meg hanyadik karaktertől induljunk [1, {len(szoveg)-db}]")
mettol = int(input())
while(not(mettol <= len(szoveg)-db and mettol >= 1)):
    print("Hibás számot adott meg!")
    print(f"Adja meg hanyadik karaktertől induljunk [1, {len(szoveg)-db}]")
    mettol = int(input())

for i in range(mettol-1, mettol + db,1):
    print(szoveg[i],end="")