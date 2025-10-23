nb = int(input("Entrez un nombre : "))
nbmax = nb
position_max = 1  
compteur = 1
while True:
    nb_courant = int(input("Entrez un nombre : "))
    
            
    if nb_courant==0:
             break
    elif nb_courant>0  :
             continue
    compteur += 1
    if nb_courant > nbmax:
        nbmax = nb_courant
        position_max = compteur

print(f"\nLa valeur maximale est {nbmax} et sa position est {position_max}")