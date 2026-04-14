<?php

require_once "BDD.Class.php";

class Inscription{

private $_username;
private $_email;
private $_password;


   public function getUsername()
    {
        return $this->_username;
    }

    public function setUsername($_username)
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

 public function Lecture(){
 $chemin_config = dirname(__DIR__, 3) . '/config.json';
    $config = json_decode(file_get_contents($chemin_config), true);
    $username = null;
    $password = null;
    $email = null;
 if($_SERVER["REQUEST_METHOD"]=="POST"){

 
 $this->_username = $username= htmlspecialchars(trim($_POST['username']));
 $this->_password = $password = htmlspecialchars(trim($_POST['password']));
 $this->_email= $email = htmlspecialchars(trim($_POST['email']));}
 return [$username ,$password , $email , $config];
 }
 


public function Ajouter(){
$donneesLecture = $this->Lecture();
    
    $username = $donneesLecture[0];
    $password = $donneesLecture[1];
    $email = $donneesLecture[2];
    $config = $donneesLecture[3];
 if(!empty($username) && !empty($password) && !empty($email)) {
 try {
  $newUser = new BDD($config);
  $pdo = $newUser->connexion();
  $sql = "INSERT INTO users (username, email, password) VALUES (:username, :email, :password)";
  $requete = $pdo->prepare($sql);

  $requete->execute([
    ':username' => $username,
    ':email' => $email,
    ':password' => password_hash($password, PASSWORD_DEFAULT)
  ]);
 } catch (Exception $e) {
  echo "Erreur : " . $e->getMessage();
 }
 }
}}
