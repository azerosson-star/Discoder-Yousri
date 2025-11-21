class Personnage :
    def __init__(self,nom):
        self.__nom= nom
        self.__pv= 50
        self.__pa= 5

    def get_nom(self):
        return self.__nom
    
    def se_soigner(self):
        self.__pv = self.__pv + 10

    
perso = Personnage('Link')



print(perso.get_nom(), perso.get_se_soigner())