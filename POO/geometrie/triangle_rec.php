<?php

class Triangle_rec
{private $_base;
private $_hauteur;

public function __construct($base,$hauteur)
    { $this->setBase($base != null ? $base: "");
    $this->setHauteur($hauteur != null ? $hauteur: "");
    }

public function getBase()
    {
        return $this->_base;}
public function setBase($base)
{
    $this->_base = $base;
}
public function getHauteur()
    {
        return $this->_hauteur;
    }
public function setHauteur($hauteur)
{
    $this->_hauteur = $hauteur;
}

public function Hypotenuse(){
$hypotenuse = sqrt(($this->getBase()*$this->getHauteur()))+sqrt(($this->getHauteur()*$this->getBase()));
return $hypotenuse;
}

public function Perimetre(){
$peri = $this->getBase()+$this->getHauteur()+$this->hypotenuse();
return $peri;
}

public function Aire(){
$aire = ($this->getBase()*$this->getHauteur())/2;
return $aire;

}

public function AfficherTriRec(){

$hauteur = $this->getHauteur();
$base = $this->getBase();
$perimetre= $this->Perimetre();
$aire= $this->Aire();
$hypotenuse=$this->Hypotenuse();
$aff= "Hauteur : $hauteur  Base: $base Perimetre: $perimetre  aire  : $aire hypotenuse : $hypotenuse" ;
return $aff;

}
}

