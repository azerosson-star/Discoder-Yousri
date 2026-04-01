<?php

// 1. Autoload des classes
function ChargerClasse($classe)
{
    require __DIR__ . "/site1/php/controller/classes/" . $classe . ".Class.php";
}
spl_autoload_register("ChargerClasse");

// 2. Chargement du layout haut (General)
require __DIR__ . "/site1/php/view/general/head.php";
require __DIR__ . "/site1/php/view/general/header.php";


$page = isset($_GET["page"]) ? $_GET["page"] : "accueil";

switch ($page) {
    case 'contact':
        require __DIR__ . "/site1/php/view/form/contact.php";
        break;
    case 'produits':
        require __DIR__ . "/site1/php/view/list/produits.php";
        break;
    case 'accueil':
    default:
        require __DIR__ . "/site1/php/view/general/accueil.php";
        break;
}


require __DIR__ . "/site1/php/view/general/footer.php";

?>