# 1. Récupérer et convertir les nombres
try:
    nombres_str = input("Entrez vos nombres séparées par des virgules : ")
    # map(int, ...) convertit chaque élément en entier
    # list(...) transforme le résultat en une vraie liste
    nb = list(map(int, nombres_str.split(",")))
except ValueError:
    print("Erreur : Veuillez n'entrer que des nombres entiers.")
    exit() # Arrête le script si l'entrée est invalide

print(f"Votre liste : {nb}")

# 2. Gérer les cas simples (listes trop courtes)
if len(nb) < 2:
    print("Il faut au moins deux nombres pour vérifier la consécutivité.")
    exit() # Arrête le script

# 3. Déterminer l'écart attendu (la direction)
# On se base sur les deux premiers nombres
ecart_attendu = nb[1] - nb[0]

# 4. Vérifier si l'écart initial est valide (1 ou -1)
if abs(ecart_attendu) != 1:
    print("Le tableau n'est pas consécutif (l'écart initial n'est ni 1 ni -1).")
    exit() # Arrête le script

# 5. Vérifier le reste de la liste
# On utilise un "drapeau" booléen (True/False)
est_consecutif = True  

# On boucle de l'index 1 jusqu'à l'avant-dernier (len(nb) - 1)
# car on compare nb[i] avec nb[i+1]
for i in range(1, len(nb) - 1):
    ecart_actuel = nb[i+1] - nb[i]
    
    # Si l'écart actuel est différent de celui attendu
    if ecart_actuel != ecart_attendu:
        est_consecutif = False  # La liste n'est pas consécutive
        break  # On arrête la boucle, inutile de continuer

# 6. Afficher le résultat final (APRES la boucle)
if est_consecutif:
    if ecart_attendu == 1:
        print("Le tableau est consécutif (montant).")
    else:
        print("Le tableau est consécutif (descendant).")
else:
    print("Le tableau n'est pas consécutif.")