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



}

