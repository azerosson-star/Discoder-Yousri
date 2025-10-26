import random

nom=input("Entrez votre nom : ")
print("Bienvenue",nom)
#On demande la proposition du joueur
def propJoueur():
    nombres=map(int,input("entrez 4 chiffres entre 1 et 6 : ").split(" ")) #map permet de mettre les réponses en liste et split de les séparer avec une virgule
    return list(nombres)

#On génere une combinaison aléatoire
def genRand():
    nb= random.randint(1,6) #random.randint pour générer une variable entière aléatoire
    return nb

#À l'aide de la fonction ci-dessus on génere une liste entiere aléatoire
def listRand():
    liste=[]
    for i in range(4):
        liste.append(genRand())
    return liste



def bienPlace(jouclone, secretclone):
    nbBienPlac=0
    for i in range(0,4):
        if jouclone[i] == secretclone[i]:
            jouclone[i]=0
            secretclone[i]=0
            nbBienPlac+=1
    return nbBienPlac



def malPlac(jouclone,secretclone):
    nbMalPlac=0
    for i in range (0,4):
        for j in range (0,4):
            if secretclone[j]!=0 and jouclone[i]!=0:
                if jouclone[i]==secretclone[j] and i!=j :
                    secretclone[j]=0
                    jouclone[i]=0
                    nbMalPlac+=1
    return nbMalPlac


def jouer():
    tour=0
    gagner=False
    secret= listRand()
    while tour<10 and gagner== False:
        tour+=1
        combijou= propJoueur()
        secretclone=secret
        jouclone=combijou
        bienPla=bienPlace(jouclone, secretclone)
        malPla=malPlac(jouclone, secretclone)
        print(f"il y a {bienPla} bon chiffre bien placé et {malPla} de bon chiffre mal placé")
        print(secretclone)
        print(jouclone)
        if bienPla==4:
            gagner=True
    if gagner==True:
        print("Bien joué tu as gagné")
    else:
        print("GAME OVER")
        print("La réponse était", secret)


jouer()