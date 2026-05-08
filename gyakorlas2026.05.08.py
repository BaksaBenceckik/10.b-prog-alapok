# Írjon függvényt, ami egy dátum-időt szé szed elemeire.
# pl. 2026.05.08 10:02 -> [2026,5,8,10,2]
# Írjon egy függvényt ami két szám hányadosának tizedestört tört részét adja vissza. 

def datumszetszed(datumIdo):
    szetszed = datumIdo.split(" ")
    datum = szetszed[0].split(".")
    ido = szetszed[1].split(":")
    szamok = [int(datum[0]),int(datum[1]),int(datum[2]),int(ido[0]),int(ido[1])]
    return szamok

def tortesfeladat(a,b):
    c = a/b
    d = str(c).split(".")
    return d

def main():
    t = datumszetszed("2026.05.08 10:02")
    print(t)
    c = tortesfeladat(1,3)
    print(c[1])
main()