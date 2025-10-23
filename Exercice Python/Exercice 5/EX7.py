nb = int(input("Entrez un nombre : "))
nbmax = nb
position_max = 1  

for i in range(2, 11): 
    nb_courant = int(input("Entrez un nombre : "))
    
    if nb_courant > nbmax:
        nbmax = nb_courant
        position_max = i 
        

print(f"\nLa valeur maximale est {nbmax} et sa position est {position_max}")