heure,min=map(int,input("entrer l'heure et les minutes separées par un espace : ").split())
# map permet d'intégrer les variables dans une liste et split de separer cette dites liste ce qui permet
# de rentrer plusieurs variables en une seule ligne
min+=1
if min==60:
    heure+=1
    min=0
    if heure==24:
        heure=0
print(f"dans une minute, il sera {heure},{min}")