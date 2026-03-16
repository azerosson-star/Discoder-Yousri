<?php
$nb = [10, 12, 15, 15];
echo "[" . implode(", ", $nb) . "]";

$rep = readline("Quelle valeur voulez vous supprimer ? ");

$index = array_search($rep, $nb);

if ($index !== false) {
    unset($nb[$index]);
    $nb = array_values($nb); 
}

echo "[" . implode(", ", $nb) . "]";
