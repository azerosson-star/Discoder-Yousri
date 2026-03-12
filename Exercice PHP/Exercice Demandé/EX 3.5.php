<?php


$nb1 = (float) readline("Entrez le premier nombre : ");
$nb2 = (float) readline("Entrez le deuxieme nombre : ");


if ($nb1 < 0) {
    print("Le premier nombre $nb1 est negatif\n"); 
} elseif ($nb1 == 0) {                        
    print("Le premier nombre $nb1 est nul\n");
} else {
    print("Le premier nombre $nb1 est positif\n");
}


if ($nb2 < 0) {
    print("Le deuxieme nombre $nb2 est negatif");
} elseif ($nb2 == 0) {
    print("Le deuxieme nombre $nb2 est nul");
} else {
    print("Le deuxieme nombre $nb2 est positif");
}
