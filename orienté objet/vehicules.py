class Voiture():
    def __init__(self,nom):
        self._nom = nom
        self._couleur = 'vert'
        self._vitesse = 0


    def get_nom(self):
        return self._nom
    def get_couleur(self):
        return self._couleur
    def accelerer(self):
        self._vitesse = self._vitesse +10
    def get_vitesse(self):
        return self._vitesse
        


a=Voiture('renault')
a.accelerer()



print(a.get_nom(), a.get_couleur(), a.get_vitesse() )
    

