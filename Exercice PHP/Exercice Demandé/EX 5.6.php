<?php
$n = 
readline("Entrez un nombre : ");

function factorielle($n) {
   if ($n <= 1) {
        echo "1 = ";
        return 1;
    }
     echo $n . " * ";
    return $n * factorielle($n - 1);
}


$resultat = factorielle($n);
echo $resultat;
