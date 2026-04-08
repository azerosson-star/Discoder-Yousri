<?php
require dirname(dirname(__DIR__)) . "/controller/classes/Parametres.Class.php";
class DBConnect{

static  private $_db;

static public function getDb()
{

return self::$_db;
}
public function __construct(array $options = [])
{
    if (!empty($options)){
        $this->hydrate($options);
    }


}

public function hydrate($data){
    foreach ($data as $key => $value){
    $methode = "set" . ucfirst($key);
    if (is_callable([$this,$methode])){
    
        $this->$methode($value=="" ? null : $value);
    }
    
    
    }


}

static public function init()
{
    try {
        $connectingstring = "mysql:host=".Parametres::getHost().";dbname=".Parametres::getDbname().";port=".Parametres::getPort()."";
        self::$_db = new PDO($connectingstring, Parametres::getLogin(),Parametres::getPwd());
    } catch (Exception $e) {
        echo "Base non trouvée";
        echo $e->getMessage();
    }
}
}