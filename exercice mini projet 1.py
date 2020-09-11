#exercice1

from math import *
    
rayon = float(input("veuillez saisir le rayon :"))
hauteur = float(input("veuillez saisir la hauteur :"))
volume = 1/3*(rayon**2)*(pi*hauteur)

print(volume)


from random import*       
N=randint(1,100) 

#exercice 2

M=randint(1,100)
N=int(input("Entrer un nombre:"))
for i in range(1,5):
    if N==M:
        print("Gagné !")
        print("nombre de coups:",i)
        quit()
    elif N>M:
        print("Trop grand")
    else:
        print("Trop petit")
    N=int(input("Entrer un nombre:"))
print("Perdu en 5 coups")

#exercice 3

def sapin_noel(n):
    for size in range(1, n + 1, 2):
        print((size * "*").center(n))

sapin_noel(7)

#exercice 4

cou=12
while cou !=0:
    ttc=cou*1.2
print("prix ht",ttc,"€")

#exercice 5

def chasseur(poule,chien,vache,ami):
    i=poule*1+chien*3+vache*5+ami*10
    print("vous venez de tuer",i,"victime")
    i=i/100
    pp=i*200
    print("vous devez payer",pp,"€")

chasseur(67,13,56,76)







