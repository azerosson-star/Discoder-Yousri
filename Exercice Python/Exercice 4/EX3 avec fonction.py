Hour,min,sec=map(int,input("entrer l'heure, les minutes et les secondes separées par un espace : ").split())
# map permet d'intégrer les variables dans une liste et split de separer cette dites liste ce qui permet
# de rentrer plusieurs variables en une seule ligne
sec+=1
if sec==60:
    min+=1
    sec=0
    if min==60:
        Hour+=1
        min=0
        if Hour==24:
            Hour=0
if min==60:
    Hour+=1
    min=0
    if Hour==24:
        Hour=0
print(f"dans une minute, il sera {Hour},{min},{sec}")