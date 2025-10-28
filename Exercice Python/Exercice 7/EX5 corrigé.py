
dict_mots = ["bonjour", "chat", "immeuble", "voiture"] 
print(dict_mots)

bmin = 0                  
bmax = len(dict_mots) - 1  
milieu = len(dict_mots) // 2
mot = input("quel mot voulez vous chercher ? ")


mot_trouve = False

while bmin <= bmax:

    milieu = (bmin + bmax) // 2 
    
    mot_milieu = dict_mots[milieu]

    if mot_milieu < mot:

        bmin = milieu + 1
    
    elif mot_milieu > mot:
       
        bmax = milieu - 1
    
    elif mot_milieu == mot:
   
        mot_trouve = True
        break


if mot_trouve:
    print(f"Le mot '{mot}' a été trouvé à l'index {milieu}.")
else:
    print(f"Le mot '{mot}' n'existe pas dans le dictionnaire.")