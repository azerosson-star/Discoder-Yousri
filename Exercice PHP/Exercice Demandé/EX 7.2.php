<?php
$nombres_str = readline("entrez vos nb séprarées par des virgules : ");
$morceaux = explode(",", $nombres_str);
$nb = [];

foreach ($morceaux as $val) {
    $nb[] = (int)$val;
}


sort($nb);
echo "[" . implode(", ", $nb) . "]";

rsort($nb);
echo "[" . implode(", ", $nb) . "]";
