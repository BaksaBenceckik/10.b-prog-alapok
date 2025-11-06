import random

# 1. feladat

szerencse = random.randint(0-9)
if(szerencse == 1 or szerencse == 6): # if(szerencse % 5 == 1)
    print("labda")
elif(szerencse == 2 or szerencse == 7): # if(szerencse % 5 == 2)
    print("ceruza")
elif(szerencse == 3 or szerencse == 8): # if(szerencse % 5 == 3)
    print("színes papír")
elif(szerencse == 4 or szerencse == 9): # if(szerencse % 5 == 4)
    print("bicikli")
else:
    print("nem nyert")

