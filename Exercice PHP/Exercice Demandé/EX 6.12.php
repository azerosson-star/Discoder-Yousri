<?php

$nb = (int)readline("Entrez le nombre de valeurs : ");

$t = [];

for ($i = 0; $i < $nb; $i++) {
   
    $numero = $i + 1; 
    $t[$i] = readline("Entrez le nombre n° " . $numero . " : ");
}

echo "nouveau tableau : ";
for ($i = 0; $i < $nb; $i++) {
    $t[$i] += 1;
    echo $t[$i] ;
}
