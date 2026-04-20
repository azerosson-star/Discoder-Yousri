<?php

class DbConnect
{

    /*****************Attributs***************** */
    static private $_db;

#region
    /*****************Accesseurs***************** */

    static public function getDb()
    {
        return self::$_db;
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
        foreach ($data as $key => $value) {
            $methode = "set" . ucfirst($key); //ucfirst met la 1ere lettre en majuscule
            if (is_callable(([$this, $methode]))) // is_callable verifie que la methode existe
            {
                $this->$methode($value == "" ? null : $value);
            }
        }
    }

#finregion
    /*****************Autres Méthodes***************** */

    static function init()
    {
        try {
            $connectionString = "mysql:host=".Parametre::getHost().";dbname=".Parametre::getNomBase().";port=".Parametre::getPort()."";
            self::$_db = new PDO($connectionString, Parametre::getLogin(), Parametre::getPassword());
        } catch (Exception $e) {
            echo "Base non trouvée";
            echo $e->getMessage();
        }
    }
}
