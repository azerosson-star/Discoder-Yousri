<?php

function chargerPage()
{
    $listeRoutes[""] = new Routes(["chemin" => "php/view/general/", "nomFichier" => "Accueil", "roleRequis" => 0]);
    $listeRoutes["Accueil"] = new Routes(["chemin" => "php/view/general/", "nomFichier" => "Accueil", "roleRequis" => 0]);
    $listeRoutes["VoitureList"] = new Routes(["chemin"=> "php/view/list/", "nomFichier" => "VoitureList","roleRequis"=> 0]);
     $listeRoutes["VoitureForm"] = new Routes(["chemin"=> "php/view/form/", "nomFichier" => "VoitureForm","roleRequis"=> 0]);
     $listeRoutes["VoitureAction"] = new Routes(["chemin"=> "php/controller/action/", "nomFichier" => "VoitureAction","roleRequis"=> 0]);
        require "./php/view/general/head.php";
    require "./php/view/general/header.php";
    $page = isset($_GET["page"]) ? $_GET["page"] : "";

    if (isset($routes[$page]))
        require $routes[$page]->getChemin(). $routes[$page]->getNomFichier() . ".php";
    else
        require "./php/view/general/accueil.php";
    
    require "./php/view/general/footer.php";
}