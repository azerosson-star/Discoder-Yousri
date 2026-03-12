<?php

$age = 0;
$age = readline("Entrez l'age de l'enfant : ");

$categorie= match($age) {
6,7 => "Poussin",
8,9 => "Pupille",
10,11 => "Minime",

default => ($age >= 12) ? "Cadet" : "Non classé",

};

echo"L'enfant est dans la catégorie $categorie.";

