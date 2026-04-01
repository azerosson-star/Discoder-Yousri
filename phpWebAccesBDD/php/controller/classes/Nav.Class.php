<?php

class Nav
{

    /*****************Attributs***************** */
    private $_libelle;
    private $_icone;
    private $_reference;
    private $_couleur;


#region
    /*****************Accesseurs***************** */

    public function getCouleur()
    {
        return $this->_couleur;
    }

    public function setCouleur($_couleur)
    {
        $this->_couleur = $_couleur;
    }

    public function getReference()
    {
        return $this->_reference;
    }

    public function setReference($_reference)
    {
        $this->_reference = $_reference;
    }

    public function getIcone()
    {
        return $this->_icone;
    }

    public function setIcone($_icone)
    {
        $this->_icone = $_icone;
    }

    public function getLibelle()
    {
        return $this->_libelle;
    }

    public function setLibelle($_libelle)
    {
        $this->_libelle = $_libelle;
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