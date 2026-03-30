<?php

class Inscription {
    private $nom;
    private $prenom;
    private $email;
    private $mdp;
    private $date;
    private $erreurs = [];


    public function __construct(array $donnees = []) {
        if (!empty($donnees)) {
            $this->hydrate($donnees);
        }
    }

    
    public function hydrate(array $donnees) {
        foreach ($donnees as $cle => $valeur) {
            
            $methode = 'set' . ucfirst($cle);
            
        
            if (method_exists($this, $methode)) {
                $this->$methode($valeur);
            }
        }
    }

    
    public function setNom($nom) {
        $this->nom = htmlspecialchars(trim($nom));
    }

    public function setPrenom($prenom) {
        $this->prenom = htmlspecialchars(trim($prenom));
    }

    public function setEmail($email) {
        $this->email = filter_var(trim($email), FILTER_SANITIZE_EMAIL);
    }

    public function setMdp($mdp) {
        $this->mdp = $mdp;
    }

    public function setDate($date) {
        $this->date = trim($date);
    }


    private function valider() {
        if (empty($this->nom) || empty($this->prenom) || empty($this->email) || empty($this->mdp) || empty($this->date)) {
            $this->erreurs[] = "Veuillez remplir tous les champs.";
        }
        
        if (!empty($this->email) && !filter_var($this->email, FILTER_VALIDATE_EMAIL)) {
            $this->erreurs[] = "Le format de l'e-mail est invalide.";
        }

        return empty($this->erreurs);
    }

    public function enregistrer() {
       
        return $this->valider(); 
    }

    public function getMessage() {
        if (!empty($this->erreurs)) {
            return "<p style='color: #dc3545; text-align: center; font-weight: bold; margin: 0;'>Erreur : " . implode("<br>", $this->erreurs) . "</p>";
        }
        return "<p style='color: #28a745; text-align: center; font-weight: bold; margin: 0;'>Félicitations 🎉 ! Le compte de {$this->prenom} a été créé.</p>";
    }
}