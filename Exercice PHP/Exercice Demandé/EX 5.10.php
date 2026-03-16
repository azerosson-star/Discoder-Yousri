<?php

function factorielle($num) {
    $resultat = 1;
    for ($i = 1; $i <= $num; $i++) {
        $resultat *= $i;
    }
    return $resultat;
}

$n = readline("nb chevaux partants : ");
$a = readline("nb chevaux joués : ");

$dansLOrdre = factorielle($n) / factorielle($n - $a);
$horsOrdre = factorielle($n) / (factorielle($a) * factorielle($n - $a));

echo "Dans l'ordre : " . $dansLOrdre ;
echo "Hors ordre : " . $horsOrdre;
