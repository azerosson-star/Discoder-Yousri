<?php

class Inscription{

private $_username;

private $_email;

private $_password;


   public function getUsername()
    {
        return $this->_username;
    }

    public function setHauteur($_username)
    {
        $this->_username = $_username;
    }

public function getEmail() {
    return $this->_email;
    
}

public function setEmail($_email)
    {
        $this->_email = $_email;
    }


public function getPassword() {
    return $this->_password;
    
}

public function setPassword($_password)
    {
        $this->_password = $_password;
    }

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


    public function recupPassword(){}















}