<?php
$nb = (int)readline("Entrez le nombre de notes a saisir : ");
$t = [];


if ($nb > 0) {
    for ($i = 0; $i < $nb; $i++) {
        $numero = $i + 1;
        $t[$i] = readline("Entrez le nombre n° " . $numero . " : ");
    }

    $moyenne = array_sum($t) / count($t);

    $nbsup = 0;
    for ($i = 0; $i < $nb; $i++) {
        if ($t[$i] > $moyenne) {
            $nbsup += 1;
        }
    }

    echo $nbsup . " élèves dépassent la moyenne de la classe";
    
} else {
    echo "Aucune note à calculer.";
}

