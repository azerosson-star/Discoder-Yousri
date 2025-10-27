nb = map(int, input("entrez vos nombres séparées par des virgules : ").split(","))
nb = list(nb)
n1 = len(nb)

nbcopy = [] # La liste commence vide

print(f"les nombres positifs sont : {[i for i in nb if i > 0]}")
print(f"les nombres négatifs sont : {[i for i in nb if i < 0]}")

# On parcourt les éléments de nb et on les ajoute (append) à nbcopy après modification
for nombre in nb:
    nbcopy.append(nombre + 1)
    
print(f"La liste modifiée est : {nbcopy}")