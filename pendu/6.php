<?php



function afficherMauvaisesLettres($liste) {
    echo "Les lettres non présentes sont : " . implode(", ", $liste) . "\n";
}
$liste = array('A','B','C') ;
echo "Cette méthode doit donner :\n Les lettres non présentes sont A,B,C \n et ca donne \n" ;
afficherMauvaisesLettres($liste);
