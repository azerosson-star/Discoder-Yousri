<?php

class NavElement
{

    /*****************Attributs***************** */
    private $_reference;
    private $_icon;
    private $_nom;
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

    public function getNom()
    {
        return $this->_nom;
    }

    public function setNom($_nom)
    {
        $this->_nom = $_nom;
    }

    public function getIcon()
    {
        return $this->_icon;
    }

    public function setIcon($_icon)
    {
        $this->_icon = $_icon;
    }

    public function getReference()
    {
        return $this->_reference;
    }

    public function setReference($_reference)
    {
        $this->_reference = $_reference;
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