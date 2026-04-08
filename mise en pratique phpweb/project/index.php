<?php
// 1. On inclut le haut de la page (le head et le menu)
// On ajoute 'php/' devant chaque chemin
include 'php/view/general/head.php';
include 'php/view/general/header.php';

// 2. On regarde quelle page on veut afficher (rudimentaire !)
$page = isset($_GET['page']) ? $_GET['page'] : 'acceuil';

// 3. On inclut le contenu central selon la page demandée
if ($page === 'acceuil') {
    include 'php/view/general/acceuil.php';
} elseif ($page === 'produits') {
   
    include 'php/view/general/produits.php'; 
} elseif ($page === 'contact') {
    // Si tu crées un php/view/general/contact.php plus tard
    include 'php/view/general/contact.php';
} elseif ($page=== 'inscription'){
    include 'php/view/form/inscription.php';
}

else {
    echo "<h1>Page introuvable</h1>";
}

// 4. On inclut le bas de la page
include 'php/view/general/footer.php';
