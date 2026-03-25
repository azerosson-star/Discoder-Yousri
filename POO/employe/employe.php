<?php
require_once "agence.php";

class Employe 
{
    private $_nom;
    private $_prenom;
    private int $_embauche;
    private $_poste;
    private int $_salaire;
    private $_service;
    private Agence $_agence; // Lien avec l'agence

    public function __construct($nom = "", $prenom = "", $embauche = 0, $poste = "", $salaire = 0, $service = "", ?Agence $agence = null)
    {
        $this->setNom($nom);
        $this->setPrenom($prenom);
        $this->setEmbauche($embauche);
        $this->setPoste($poste);
        $this->setSalaire($salaire);
        $this->setService($service);
        if ($agence !== null) {
            $this->setAgence($agence);
        }
    }

    public function getNom() { return $this->_nom; }
    public function setNom($nom) { $this->_nom = $nom; }
    
    public function getPrenom() { return $this->_prenom; }
    public function setPrenom($prenom) { $this->_prenom = $prenom; }
    
    public function getEmbauche() { return $this->_embauche; }
    public function setEmbauche($embauche) { $this->_embauche = $embauche; }
    
    public function getPoste() { return $this->_poste; }
    public function setPoste($poste) { $this->_poste = $poste; }
    
    public function getSalaire() { return $this->_salaire; }
    public function setSalaire($salaire) { $this->_salaire = $salaire; }
    
    public function getService() { return $this->_service; }
    public function setService($service) { $this->_service = $service; }

    public function getAgence() { return $this->_agence; }
    public function setAgence(Agence $agence) { $this->_agence = $agence; }

    // Calcul de l'ancienneté
    public function calculdate()
    {
        date_default_timezone_set('Europe/Paris');
        $date_act = intval(date("Y"));
        $annee_embauche = intval($this->getEmbauche());
        $anciennete = $date_act - $annee_embauche;
        return $anciennete;
    }

    // Calcul de la prime selon l'ancienneté
    public function prime()
    {
        $anciennete = $this->calculdate();   
        $prime = 0; // Initialisation pour éviter l'erreur si l'ancienneté est faible

        for ($i = 1; $i <= $anciennete; $i++) 
        {
            $salaire = $this->getSalaire();
            // 5% du salaire + 2% par année d'ancienneté
            $primajout = ($salaire * 0.05) + ($i * ($salaire * 0.02)) + $salaire;
            $prime = $primajout - $salaire;
        }
        return $prime;    
    }

    // Méthode utilitaire pour afficher les infos d'un employé facilement
    public function getInfos() {
        return sprintf(
            "[%s] %s %s | Embauche: %d | Salaire: %d€ | Agence: %s (%s)",
            $this->getService(),
            strtoupper($this->getNom()),
            ucfirst($this->getPrenom()),
            $this->getEmbauche(),
            $this->getSalaire(),
            $this->getAgence()->getNom(),
            $this->getAgence()->getVille()
        );
    }
}
?>