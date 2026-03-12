<?php

$sexe=readline("Entrez votre sexe Homme ou Femme : ");
$age=readline("entrez votre age : ");

if ($sexe=="femme" && $age>=18 && $age<35 ){
    echo"Vous etes imposable";
        }

if ($sexe=="homme" && $age>=20){
echo"Vous etes imposable";
}
else{
echo"Vous n'etes pas imposable";}