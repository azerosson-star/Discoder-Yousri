print("entrer l'heure, les minutes et les secondes separées par un espace : ")
heure=int(input("entrer l'heure : "))
min=int(input("entrer les minutes : "))
sec=int(input("entrer les secondes : "))

sec+=1
if sec==60:
    min+=1
    sec=0
    if min==60:
        heure+=1
        min=0
        if heure==24:
            heure=0
if min==60:
    min+=1
    if min==60:
        heure+=1
        min=0
        if heure==24:
            heure=0
print(f"dans une minute, il sera {heure},{min},{sec}")