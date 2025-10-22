print("entrer l'heure et les minutes separées par un espace : ")
heure=int(input("entrer l'heure : "))
min=int(input("entrer les minutes : "))
min+=1
if min==60:
    heure+=1
    min=0
    if heure==24:
        heure=0
print(f"dans une minute, il sera {heure},{min}")