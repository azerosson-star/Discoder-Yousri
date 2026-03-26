<?php

class navbar{
private $_navbar;

private $_liensNavbar;

  public function hydrate(array $donnees) {
        foreach ($donnees as $cle => $valeur) {
            
            
            $formatage = str_replace(' ', '', ucwords(str_replace('_', ' ', $cle)));
            
           
            $methode = 'set' . $formatage; 
            
            
            if (method_exists($this, $methode)) {
                $this->$methode($valeur);
            }
        }
        
}
 public function setId($id) { 
        $this->id = (int) $id; 
    }

            public function setNavBar($navbar) { 
        $this->_navbar = ucfirst(strtolower($navbar));
    }
    public function setLiensNavbar($liensNavbar) { 
        $this->_liensNavbar = ucfirst(strtolower($liensNavbar));
    }


     public function getNavbar() { return $this->_navbar;}
    public function getLiensNavbar() { return $this->_liensNavbar; }


public function NavBar(){
$navbar = " ";




}


}