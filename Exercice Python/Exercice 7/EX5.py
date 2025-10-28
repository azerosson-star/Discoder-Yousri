dict=["chat","bonjour","voiture","immeuble"]
dict.sort()
print(dict)


bmin = 0
bmax = len(dict)-1
milieu= len(dict)//2
mot = input("quel mot voulez vous chercher ? ")


mottrouvé = False

while bmin <= bmax:

    milieu = (bmin+bmax)//2

    motmilieu = dict[milieu]

    if motmilieu < mot:

        bmin = milieu + 1

    elif motmilieu>mot:

        bmax= milieu - 1

    elif motmilieu == mot:

        mottrouvé = True
        break

if mottrouvé:
        
        print(f"le mot {mot} existe")
else:
        print(f"le mot {mot} n'existe pas")