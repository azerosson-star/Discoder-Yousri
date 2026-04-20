<?php


class Voiture
{

    /*****************Attributs***************** */
    private $_idVoiture;
    private $_marque;
    private $_modele;
    private $_nbKilometres;
    private static $_attributes=['idVoiture',"marque","modele","nbKilometres"];

#region
    /*****************Accesseurs***************** */

    public static function getAttributes()
    {
        return self::$_attributes;
    }

    public function getIdVoiture()
    {
        return $this->_idVoiture;
    }


    public function getMarque()
    {
        return $this->_marque;
    }

public function getModele()
    {
        return $this->_modele;
    }
public function getNbKilometres()
    {
        return $this->_nbKilometres;
    }
  public function setIdVoiture($_idVoiture)
    {
        $this->_idVoiture = $_idVoiture;
    }
  public function setMarque($_marque)
    {
        $this->_marque = $_marque;
    }
  public function setModele($_modele)
    {
        $this->_modele= $_modele;
    }
  public function setNbKilometres($_nbKilometres)
    {
        $this->_nbKilometres = $_nbKilometres;
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