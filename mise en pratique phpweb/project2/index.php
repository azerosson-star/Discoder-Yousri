<?php

include 'php/view/general/head.php';
include 'php/view/general/header.php';

$page = isset($_GET['page']) ? $_GET['page'] : 'acceuil';


if ($page === 'acceuil') {
    include 'php/view/general/acceuil.php';
} elseif ($page === 'produits') {
   
    include 'php/view/general/produits.php'; 
} elseif ($page === 'contact') {

    include 'php/view/general/contact.php';
} elseif ($page === 'inscription') {
    include 'php/view/form/inscription.php';
} elseif ($page === 'connexion') {
    include 'php/model/services/DBConnect.Class.php';
    include 'php/view/form/connexion.php';
} else {
    echo "<h1>Page introuvable</h1>";
}


include 'php/view/general/footer.php';
