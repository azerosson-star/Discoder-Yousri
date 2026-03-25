<?php

class Rectangle
{private $_longueur;
private $_largeur;
    public function __construct($longueur,$largeur)
    { $this->setLongueur($longueur != null ? $longueur: "");
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
public function Perimetre()
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

public function AfficherRectangle(){

$longueur = $this->getLongueur();
$largeur = $this->getLargeur();
$perimetre= $this->Perimetre();
$estcarre= $this->estCarre();
$aff= "Longueur: $longueur <br> Largeur: $largeur <br> Perimetre: $perimetre <br> Est ce un carre? : $estcarre";
return $aff;

}










}