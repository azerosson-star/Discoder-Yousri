<?php

function ajouterUneLettre($lettre, $tab, $position) {
    $tab[$position] = $lettre;
    return $tab;
}

echo "Cette méthode doit donner B O N K O U R et ca donne\n";
$t = array('B', 'O', 'N', 'J', 'O', 'U', 'R');
afficherTableau(ajouterUneLettre('K', $t, 3));
