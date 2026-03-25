<?php



function ajouterLesLettres($lettre, $tab, $listePosition) {
    foreach ($listePosition as $position) {
        $tab = ajouterUneLettre($lettre, $tab, $position);
    }
    return $tab;
}

$motATrouver="BONJOUR";
$t = array( 'B', '_', 'N', 'J', '_', 'U', '_' );
echo "Cette méthode doit donner B O N J O U _ et ca donne \n";
afficherTableau(ajouterLesLettres('O', $t, testerLettre('O', str_split($motATrouver),0)));

print_r(ajouterLesLettres('O', $t, [1, 4]));

