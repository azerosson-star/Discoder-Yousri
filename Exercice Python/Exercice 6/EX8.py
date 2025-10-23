nb=map(int,input("entrez vos nombres séprarées par des virgules : ").split(","))
nb=list(nb)
print(f"les nombres positifs sont : {[i for i in nb if i>0]}")
print(f"les nombres négatifs sont : {[i for i in nb if i<0]}")