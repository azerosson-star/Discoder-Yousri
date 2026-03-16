<?php
$dict = ["chat", "bonjour", "voiture", "immeuble"];
sort($dict);
echo "[" . implode(", ", $dict) . "]";

$bmin = 0;
$bmax = count($dict) - 1;
$mot = readline("quel mot voulez vous chercher ? ");

$mottrouve = false;

while ($bmin <= $bmax) {
    $milieu = (int)(($bmin + $bmax) / 2);
    $motmilieu = $dict[$milieu];

    if ($motmilieu < $mot) {
        $bmin = $milieu + 1;
    } elseif ($motmilieu > $mot) {
        $bmax = $milieu - 1;
    } else {
        $mottrouve = true;
        break;
    }
}
if ($mottrouve) {
    echo "le mot " . $mot . " existe";
} else {
    echo "le mot " . $mot . " n'existe pas";
}
