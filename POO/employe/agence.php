<?php

class Agence 
{
    private string $_nom;
    private string $_adresse;
    private string $_codePostal;
    private string $_ville;

    public function __construct($nom = "", $adresse = "", $codePostal = "", $ville = "")
    {
        $this->setNom($nom);
        $this->setAdresse($adresse);
        $this->setCodePostal($codePostal);
        $this->setVille($ville);
    }

    // Getters et Setters
    public function getNom() { return $this->_nom; }
    public function setNom($nom) { $this->_nom = $nom; }

    public function getAdresse() { return $this->_adresse; }
    public function setAdresse($adresse) { $this->_adresse = $adresse; }

    public function getCodePostal() { return $this->_codePostal; }
    public function setCodePostal($codePostal) { $this->_codePostal = $codePostal; }

    public function getVille() { return $this->_ville; }
    public function setVille($ville) { $this->_ville = $ville; }
}
