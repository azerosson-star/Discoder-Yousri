# Demande à l'utilisateur combien de photocopies il veut imprimer.
# On convertit l'entrée en entier.
nbphotocopies = int(input("Entrer le nombre de photocopies : "))

# Tarifs par tranche :
# - premiers 10 exemplaires : 0,10 € chacun
# - suivants jusqu'à 20 : 0,09 € chacun
# - au-delà de 20 : 0,08 € chacun
cout1 = 0.10
cout2 = 0.09
cout3 = 0.08

# Calcul du coût total selon le nombre de photocopies
if nbphotocopies <= 10:
    # Si <= 10 : on multiplie par le tarif de base
    total = nbphotocopies * cout1
elif nbphotocopies <= 20:
    # Si entre 11 et 20 :
    # - les 10 premiers au tarif cout1
    # - le reste (nbphotocopies - 10) au tarif cout2
    total = (10 * cout1) + (nbphotocopies - 10) * cout2
else:
    # Si plus de 20 :
    # - 10 premiers au tarif cout1
    # - 10 suivants au tarif cout2
    # - le reste (nbphotocopies - 20) au tarif cout3
    total = (10 * cout1) + (10 * cout2) + (nbphotocopies - 20) * cout3

# Affichage du total formaté en euros
print(f"Total : {total} €")