<?php

class BDD {

private $_host;
private $_dbname;

private $_username;

private $_email;

private $_password;

private $_connexion;




 public function getConnexion()
    {
        return $this->_connexion;
    }

    public function setConnexion($_connexion)
    {
        $this->_connexion = $_connexion;
    }
   


 public function getDbname()
    {
        return $this->_dbname;
    }

    public function setDbname($_dbname)
    {
        $this->_dbname = $_dbname;
    }

    public function getUsername()
    {
        return $this->_username;
    }

    public function setUsername($_username)
    {
        $this->_username = $_username;
    }
       
    
public function getHost() {
    return $this->_host;
    
}

public function setHost($_host)
    {
        $this->_host = $_host;
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
            if (is_callable(([$this, $methode]))) //
                $this->$methode($value==""?null:$value);
        }
    }


public function Connexion(){
$this->_connexion = null;

try{

$this->_connexion = new PDO ("mysql:host=" . $this->_host . ";dbname=" . $this->_dbname . ";charset=utf8mb4", $this->_username, $this->_password);
$this->_connexion->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);


}catch(PDOException $e){
    echo "Erreur de connexion : " . $e->getMessage();

}

return $this->_connexion;




}}





    



    
    
    
    
    
    
    
    
    
    
























