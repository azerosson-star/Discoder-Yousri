<?php
$total = 0;
$i = 0;
$prix = 1;

while ($prix != 0) {
    $i += 1;
    $prix = readline("prix article " . $i . " : ");
    $total += $prix;
}

$total = round($total, 2);
$nbArticles = $i - 1;
echo "votre total est de " . $total . " pour " . $nbArticles . " articles.";

$paiement = -1;
while ($paiement < $total) {
    $paiement = readline("votre paiement est de : ");
}

$aRendre = $paiement - $total;
$aRendre = round($aRendre, 2);
echo "la somme a rendre est de " . $aRendre . " euros.";

while ($aRendre >= 10) {
    $aRendre -= 10;
    echo "10 euros";
}

if ($aRendre >= 5) {
    $aRendre -= 5;
    echo "5 euros";
}

while ($aRendre >= 1) {
    echo "1 euro";
    $aRendre -= 1;
}
