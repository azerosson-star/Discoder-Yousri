class Livre:
    def __init__(self,titre,auteur):
        self.titre = titre
        self.auteur = auteur


    def afficher_info(self):
        print(f"{self.titre} {self.auteur}")


mes_livre = Livre("Les Misérables" , "Victor Hugo")
mes_livre.afficher_info()