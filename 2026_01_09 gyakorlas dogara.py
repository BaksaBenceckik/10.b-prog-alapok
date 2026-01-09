import random

# Jancsi és Juliska autós kártyát gyűjtenek. Hogy ne legyen vita és gyorsan meg tudják különböztetni melyik autó kié, ezért a következőt találták ki. Mivel minden autó 
#végsebessége 3 jegyű, ezért megnézik a középső számot. Ha páros akkor Jancsié, ha páratlan akkor Juliskáé. 
# Van összesen 30 kártyájuk. Szeretik egymás mellé rakni a kártyákat. Szimuláld a feladatot!
# Írj egy programot, ami kigenerál [301, 453] között egy számot úgy, hogy minden páros helyen Jancsi kártyája van, minden páratlan helyen Juliskáé!
# Add meg Jancsi autóinak végsebességének átlagát!
# Add meg hány darab autója van Juliskának, ami 380-nál nagyobb a végsebessége!

kartya = []
for i in range(0,30,1):
    elso = random.randint(3,4)
    masodik = -1
    if i % 2 == 1:
        masodik = random.randint(0,4)*2
    else:
        masodik = random.randint(0,4)*2+1
    harmadik = random.randint(0,9)
#    szam = int(str(elso)+str(masodik)+str(harmadik))
    szam = elso * 100 + masodik * 10 + harmadik
    kartya.append(szam)
print(kartya)

osszeg = 0
for i in range(1,len(kartya),2):
    osszeg += kartya[i]
db = len(kartya)/2
átlag = osszeg / db
print(round(átlag, 2))

nagyobb = 0
for a in range(0,len(kartya),2):
    if kartya[a] > 380:
        nagyobb += 1
print("Juliskának",nagyobb,"db 380-nál gyorsabb autója van")

