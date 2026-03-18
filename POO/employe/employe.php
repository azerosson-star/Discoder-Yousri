<?php

class employe 
{private $_nom;
 private $_prenom;
 private $_embauche;
 private $_poste;

 private $_salaire;
 private $_service;

public function __construct($nom = "",$prenom = "",$embauche = "",$poste = "",$salaire = 0,$service = "")
{
    $this->setNom($nom );
    $this->setPrenom($prenom);
    $this->setEmbauche($embauche);
    $this->setPoste($poste);
    $this->setSalaire($salaire);
    $this->setService($service);
}
public function getNom()
{
    return $this->_nom;
}

public function setNom($nom)
{
    $this->_nom = $nom;
}
public function getPrenom()
{
    return $this->_prenom;
}
public function setPrenom($prenom)
{
    $this->_prenom = $prenom;
}
public function getEmbauche()
{
    return $this->_embauche;
}
public function setEmbauche($embauche)
{
    $this->_embauche = $embauche;
}
public function getPoste()
{
    return $this->_poste;
}
public function setPoste($poste)
{
    $this->_poste = $poste;
}
public function getSalaire()
{
    return $this->_salaire;
}
public function setSalaire($salaire)
{
    $this->_salaire = $salaire;
}
public function getService()
{
    return $this->_service;
}
public function setService($service)
{
    $this->_service = $service;
}
public function calculdate()

{
$date_act=0;
date_default_timezone_set('Europe,Paris');
$date_act= intval(date("Y"));
$annee_embauche = intval($this->getEmbauche());
$anciennete = $date_act - $annee_embauche;
return $anciennete;
}

public function calculsalaire(){
$date_act=+1;
$salaire_act=intval($this->getSalaire());

}


 










}