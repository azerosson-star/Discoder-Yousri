print("Depuis combien d'années avez vous votre permis de conduire ?")
année=int(input("entrez le nombre d'années : "))
print("quel est votre age ?")
age=int(input("entrez votre age : "))
print("De combien d'accidents etiez vous responsable ?")
accidents=int(input("entrez le nombre d'accidents : "))
if année<2 and age<25 and accidents==0:
    print("Vous vous voyez attribuer le tarif rouge")
elif accidents>0 and année<=2 and age<25:
    print("La compagnie refuse de vous assurer")
    if 2>année or age>=25 and accidents==0:
        print("Vous vous voyez attribuer le tarif orange")
    elif année>=2 or age>=25 and accidents>0:
        print("Vous vous voyez attribuer le tarif rouge")
