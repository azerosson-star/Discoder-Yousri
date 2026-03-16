<?php 

Class Voiture 
{   private string $_couleur ;
    private string $_marque;
    private string $_modele;
    private int $_km;
    private string $_motor;

    public function choixcouleur(){
        return $this->_couleur;
    }
    public function choixmarque(){
        return $this->_marque ;
    }
    public function choixmodele(){
        return $this->_modele ;
    }
    public function choixkm(){
        return $this->_km ;
    }
    public function choixmotor(){
        return $this->_motor ;
    }
}

