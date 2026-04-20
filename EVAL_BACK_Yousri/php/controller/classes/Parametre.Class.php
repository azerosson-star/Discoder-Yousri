<?php

class Parametre
{

    /*****************Attributs***************** */
    private static $_host;
    private static $_login;
    private static $_password;
    private static $_nomBase;
    private static $_port;
    private static $_typeIcon;
    private static $_nav;

#region
    /*****************Accesseurs***************** */

    public static function getNav()
    {
        return self::$_nav;
    }

    public static function getTypeIcon()
    {
        return self::$_typeIcon;
    }

    public static function getPort()
    {
        return self::$_port;
    }

    public static function getNomBase()
    {
        return self::$_nomBase;
    }

    public static function getPassword()
    {
        return self::$_password;
    }

    public static function getLogin()
    {
        return self::$_login;
    }

    public static function getHost()
    {
        return self::$_host;
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
    public static function init()
    {
        if (file_exists("config.json")) {
            //json_decode => decode en objet
            // json_decode(...,true) =>decode en tableau associatif
            $contenu = json_decode(file_get_contents("config.json"));
            self::$_host = $contenu->host;
            self::$_login = $contenu->login;
            self::$_password = $contenu->password;
            self::$_nomBase = $contenu->nomBase;
            self::$_port = $contenu->port;
            self::$_typeIcon = $contenu->typeIcon;
            $tabNav = json_decode(json_encode($contenu->nav), true);
            // tabNav est un tableau associatif
            foreach ($tabNav as $key => $value) {
                $tabObj[] = new NavElement($value);
            }
            self::$_nav = $tabObj;
        }
    }
}
