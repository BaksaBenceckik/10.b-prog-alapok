import random as r

# Generáljon egy listába 13 db olyan négyjegyű véletlen számokat amik 3-ra, 5-re és 7-re végződnek.
# Hány darab 3-ra, 5-re, 7-re végződő szám van. 

lista = []
for i in range(13):
    a = r.randint(100,999)
    veletlen = r.randint(1,3)
    if veletlen == 1:
        lista.append(a*10+3)
    elif veletlen == 2:
        lista.append(a*10+5)
    else:
        lista.append(a*10+7)
print(lista)

ötre = 0
hetre = 0
haromra = 0
for i in range(0, len(lista), 1):
    if(lista[i] % 10 == 3):
        haromra += 1
    elif(lista[i] % 10 == 5):
        ötre += 1
    elif(lista[i] % 10 == 7):
        hetre += 1
print("három: ", haromra, "öt: ", ötre, "hét: ", hetre)

# számtani átlag
# hány db szám van átlag alatt
# mértani átlag
# a mértani átlag alatti számok összege
# 30db 13-ra, 17-re végződő számokkal, hány osztható 13-mal és 17-tel
# ekérsz egy hosszabb szöveget, hány darab felhasználó álltal megadott betű van benne.
# bekérsz két szót, mondd meg adott indexen hány darab eltérés van! (pl.: alma, alkat -> 2 db külömbség)