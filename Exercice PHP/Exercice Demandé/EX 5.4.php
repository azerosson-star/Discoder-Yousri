<?php

$nombre = readline("Entrez un nombre : ");
for ($i = 1; $i <= 10; $i++) {
    $resultat = $nombre * $i;
    echo "$nombre x $i = $resultat";
}