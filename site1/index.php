<?php

// 1. Autoload des classes
function ChargerClasse($classe)
{
    require "site1/php/controller/classes/" . $classe . ".Class.php";
}
spl_autoload_register("ChargerClasse");

// 2. Chargement du layout haut (General)
require "site1/php/view/general/head.php";
require "site1/php/view/general/header.php";

// 3. Récupération de la page demandée (par défaut: accueil)
$page = isset($_GET["page"]) ? $_GET["page"] : "accueil";

// 4. Routage (Le Switch)
switch ($page) {
    case 'contact':
        require "site1/php/view/form/contact.php";
        break;
    case 'produits':
        require "site1/php/view/list/produits.php";
        break;
    case 'accueil':
    default:
        require "site1/php/view/general/accueil.php";
        break;
}

// 5. Chargement du layout bas (General)
require "site1/php/view/general/footer.php";

?>