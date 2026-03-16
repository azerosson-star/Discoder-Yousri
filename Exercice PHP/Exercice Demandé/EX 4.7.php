<?php

$anciennete = readline("Depuis combien d'années avez-vous votre permis ? ");
$age = readline("Quel est votre âge ? ");
$accidents = readline("De combien d'accidents étiez-vous responsable ? ");


if ($anciennete < 0 || $age < 0 || $accidents < 0) {
    echo "Entrée invalide : les valeurs ne peuvent pas être négatives.";
} else {

    if ($accidents > 0 && ($anciennete < 2 || $age < 25)) {
        echo "La compagnie refuse de vous assurer";
    } elseif ($accidents == 0 && $anciennete >= 2 && $age >= 25) {
        echo "Vous vous voyez attribuer le tarif vert";
    } elseif ($accidents == 0 && ($anciennete >= 2 || $age >= 25)) {
        echo "Vous vous voyez attribuer le tarif orange";
    } else {
        echo "Vous vous voyez attribuer le tarif rouge";
    }
}
