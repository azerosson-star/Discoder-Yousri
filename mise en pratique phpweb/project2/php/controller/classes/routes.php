<?php

function chargerPage()
{

    $routes[""]= new Routes(["chemin"=>"./php/view/general/","nomFichier"=>"accueil"]);
    $routes["contact"]= new Routes(["chemin"=>"./php/view/form/","nomFichier"=>"contact"]);
    $routes["accueil"]= new Routes(["chemin"=>"./php/view/general/","nomFichier"=>"accueil"]);
    $routes["produits"]= new Routes(["chemin"=>"./php/view/list/","nomFichier"=>"produits"]);
    $routes["inscription"]= new Routes (["chemin"=>"./php/view/form/","nomFichier"=>"inscriptionForm"]);
    $routes["actionConnexion"]= new Routes(["chemin"=>"./php/controller/action/","nomFichier"=>"actionInscription"]);
    $routes["connexionForm"]= new Routes(["chemin"=>"./php/view/form/","nomFichier"=>"connexionForm"]);
    $routes["actionConnexion"]= new Routes(["chemin"=>"./php/controller/action/","nomFichier"=>"actionConnexion"]);
    $routes["actionUtilisateur"]= new Routes(["chemin"=>"./php/controller/action/","nomFichier"=>"actionUtilisateur"]);
    $routes["utilisateurForm"]= new Routes(["chemin"=>"./php/view/form/","nomFichier"=>"utilisateurForm"]);


    require "./php/view/general/head.php";
    require "./php/view/general/header.php";
    $page = isset($_GET["page"]) ? $_GET["page"] : "";

    if (isset($routes[$page]))
        require $routes[$page]->getChemin(). $routes[$page]->getNomFichier() . ".php";
    else
        require "./php/view/general/accueil.php";
    
    require "./php/view/general/footer.php";
}
