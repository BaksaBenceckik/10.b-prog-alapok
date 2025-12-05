# palidrom-e

szoveg = input("Adjon meg egy szöveget: ")
ujszoveg = ""
for index in range(len(szoveg)-1, -1, -1):
    ujszoveg += szoveg[index]
if ujszoveg == szoveg:
    print("A szöveg palidrom!")
else:
    print("A szöveg nem palidrom!")

j = 0
while(j<len(szoveg)/2 and szoveg[j] == szoveg[len(szoveg)-1-j]):
    j += 1
if(j<len(szoveg)/2):
    print("A szoveg nem palidrom!")
else:
    print("A szöveg palidrom!")