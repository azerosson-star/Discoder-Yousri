sexe=input("Entrez votre sexe Homme ou Femme : ")
age=int(input("entrez votre age :"))
if sexe=="femme" and age>=18 and age<35:
    print("vous etes imposable")
if sexe=="homme" and age>=20:
    print("vous etes imposable")
else:
    print("vous n'etes pas imposable")
