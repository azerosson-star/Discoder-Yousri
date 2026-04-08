<?php


class Routes
{

  
    private $_chemin;
    private $_nomFichier;


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

    
   

    public function __construct(array $options = [])
    {
        if (!empty($options)) 
        {
            $this->hydrate($options);
        }
    }
    public function hydrate($data)
    {
        foreach ($data as $key => $value)
        {
            $methode = "set" . ucfirst($key); 
            if (is_callable(([$this, $methode])))
            {
                $this->$methode($value==""?null:$value);
            }
        }
    }

}