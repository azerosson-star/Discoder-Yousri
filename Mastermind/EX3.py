combijou=   [9,5,4,8]
combisecret=[5,4,5,8]
secretclone=combisecret
jouclone=combijou
compteur=0
compteur2=0
for i in range(0,4):
    if jouclone[i] == secretclone[i]:
        secretclone[i]=0
        jouclone[i]=0
        compteur+=1

for i in range (0,4):
    for j in range (0,4):
        if secretclone[j]!=0 and jouclone[i]!=0:
        
            if jouclone[i]==secretclone[j] :
                secretclone[j]=0
                jouclone[i]=0
                compteur2+=1
            
print(f"il y a {compteur} bon chiffre bien placé et {compteur2} de bon chiffre mal placé")



        