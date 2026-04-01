<?php



function chargerPage()
{
    $routes = [
        "" => "general/accueil",
        "contact" => "form/contact",
        "accueil" => "general/accueil",
        "produits" => "list/produits",
    ];


    require "./php/view/general/head.php";
    require "./php/view/general/header.php";
    $page = isset($_GET["page"]) ? $_GET["page"] : "";

    if (isset($routes[$page]))
        require "./php/view/" . $routes[$page] . ".php";
    else
        require "./php/view/general/accueil.php";
    
    require "./php/view/general/footer.php";
}
