<?php
// 1. Récupérer et convertir les nombres
$nombres_str = readline("Entrez vos nombres séparées par des virgules : ");


$morceaux = explode(",", $nombres_str);
$nb = [];


foreach ($morceaux as $valeur) {

    $valeur_propre = trim($valeur); 
    
    if (!is_numeric($valeur_propre)) {
        echo "Erreur : Veuillez n'entrer que des nombres entiers.";
        exit(); 
    }
    
    $nb[] = $valeur_propre; 
}
echo "Votre liste : [" . implode(", ", $nb) . "]";

if (count($nb) < 2) {
    echo "Il faut au moins deux nombres pour vérifier la consécutivité.";
    exit(); 
}

$ecart_attendu = $nb[1] - $nb[0];


if (abs($ecart_attendu) != 1) {
    echo "Le tableau n'est pas consécutif (l'écart initial n'est ni 1 ni -1).";
    exit();
}

$est_consecutif = true;  

$taille = count($nb);
for ($i = 1; $i < $taille - 1; $i++) {
    $ecart_actuel = $nb[$i+1] - $nb[$i];
    
    // Si l'écart actuel est différent de celui attendu
    if ($ecart_actuel != $ecart_attendu) {
        $est_consecutif = false;  
        break;  
    }
}

if ($est_consecutif) {
    if ($ecart_attendu == 1) {
        echo "Le tableau est consécutif (montant).";
    } else {
        echo "Le tableau est consécutif (descendant).";
    }
} else {
    echo "Le tableau n'est pas consécutif.";
}
