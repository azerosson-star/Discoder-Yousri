<?php

class Routes
{

    /*****************Attributs***************** */
    private $_chemin;
    private $_nomFichier;
    private $_roleRequis;

#region
    /*****************Accesseurs***************** */

    public function getRoleRequis()
    {
        return $this->_roleRequis;
    }

    public function setRoleRequis($_roleRequis)
    {
        $this->_roleRequis = $_roleRequis;
    }

    public function getNomFichier()
    {
        return $this->_nomFichier;
    }

    public function setNomFichier($_nomFichier)
    {
        $this->_nomFichier = $_nomFichier;
    }

    public function getChemin()
    {
        return $this->_chemin;
    }

    public function setChemin($_chemin)
    {
        $this->_chemin = $_chemin;
    }

    
    /*****************Constructeur***************** */

    public function __construct(array $options = [])
    {
        if (!empty($options)) // empty : renvoi vrai si le tableau est vide
        {
            $this->hydrate($options);
        }
    }
    public function hydrate($data)
    {
        foreach ($data as $key => $value)
        {
            $methode = "set" . ucfirst($key); //ucfirst met la 1ere lettre en majuscule
            if (is_callable(([$this, $methode]))) // is_callable verifie que la methode existe
            {
                $this->$methode($value==""?null:$value);
            }
        }
    }

#finregion
    /*****************Autres Méthodes***************** */
    
}