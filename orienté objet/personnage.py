class Personnage :
    def __init__(self,nom):
        self._nom= nom
        self._pv= 50
        self._pa= 5

    def get_nom(self):
        return self._nom
    
    def get_pv(self):
        return self._pv
    
    def se_soigner(self):
        self._pv = self._pv + 10

    
perso = Personnage('Link')

perso.se_soigner()



print(perso.get_nom(), perso.get_pv())