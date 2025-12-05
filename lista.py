# a szövegben van-e "sz" betű?

szoveg = "aszály"
dube = "sz"
"""
print(szoveg)
if "sz" in szoveg:
    print("Van benne sz betű!")
else:
    print("Nincs benne sz betű!")
"""
index = 0
while(index < len(szoveg)-1 and not(szoveg[index] == dube[0] and szoveg[index+1] == dube[1])):
    index += 1
if index < len(szoveg)-1:
    print("Van benne", dube, "betű!")
else:
    print("Nincs benne", dube, "betű!")