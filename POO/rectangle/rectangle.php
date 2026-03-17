<?php

class rectangle
{private $_longueur;
private $_largeur;



public function __construct( $longueur,$largeur)
{   $this->setLongueur($longueur != null ? $longueur: "");
    $this->setLargeur($largeur != null ? $largeur: "");
}
public function getLongueur()
    {
        return $this->_longueur;}
public function setLongueur($longueur)
{
    $this->_longueur = $longueur;
}
public function getLargeur()
    {
        return $this->_largeur;
    }
public function setLargeur($largeur)
{
    $this->_largeur = $largeur;
}
public function perimetre()
{
    return 2*($this->getLongueur()+$this->getLargeur());
}
public function aire()
{
    return $this->getLongueur()*$this->getLargeur();
}
public function estCarre(){
    if($this->getLongueur() == $this->getLargeur()){
        return "oui";
    } else {
        return "non";
    }

}
public function AfficherRectangle(){}
}
