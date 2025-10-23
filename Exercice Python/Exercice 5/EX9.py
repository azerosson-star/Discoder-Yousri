total=0
i=0
prix=1

while prix!=0:
    i+=1
    prix=float(input("prix article "+str(i)+" : "))
    total += prix

total=round(total,2)
print(f"votre total est de {total:.2f} pour {i-1} articles.")
paiement=-1.0
while paiement<total:
    paiement=float(input("votre paiement est de : "))

aRendre=paiement-total
print(f"la somme a rendre est de {aRendre:.2f} euros.")

while aRendre>=10:
    aRendre-=10
    print("10 euros")

if aRendre>=5:
    aRendre-=5
    print("5 euros")    

while aRendre>=1:
    print("1 euro")
    aRendre-=1