<?php

function ChargerClasse($classe)
{
    if (file_exists("./php/controller/classes/" . $classe . ".Class.php"))
        require "./php/controller/classes/" . $classe . ".Class.php";
    else
        require "./php/model/services/" . $classe . ".Class.php";
}
spl_autoload_register("ChargerClasse");

require "./php/controller/routes.php";
require "./php/controller/helpers.php";
// on initialise les parametres * on recupere les infos pour se connecter à la base
Parametres::init();

//on initialise la connection
DbConnect::init();

chargerPage();

// on etablit la connection (on recupere un objet PDO)
$db=DbConnect::getDb();
// on met à jour le PDO avec une requete
 $requete = $db->prepare("select * from user");
//on execute la requete
$requete->execute();
// on recupere la 1ere reponse
// fetch est un curseur qui va aller d'une reponse à la suivante
 $donnees = $requete->fetch(PDO::FETCH_ASSOC);
//on ferme la connexion pour eviter de saturer la base
 $requete->closeCursor();

var_dump($donnees);
// $u = new User($donnees);
echo $u->getNom();
