<?php

echo"Entrez le scores des quatres candidats sans % :";
$candidat1=readline("candidat 1 : ");
$candidat2=readline("candidat 2 : ");
$candidat3=readline("candidat 3 : ");
$candidat4=readline("candidat 4 : ");
if ($candidat1>=50){
    echo"Un candidat 1 a obtenu la majorité absolue et est élu au premier tour.";}
elseif ($candidat2>=50){
    echo "Un candidat 2 a obtenu la majorité absolue et est élu au premier tour.";}
elseif ($candidat3>=50){
    echo"Un candidat 3 a obtenu la majorité absolue et est élu au premier tour.";}
elseif ($candidat4>=50){
    echo"Un candidat 4 a obtenu la majorité absolue et est élu au premier tour.";}
else{
    echo"Aucun candidat n'a obtenu la majorité absolue. Un second tour est nécessaire.";}

if (($candidat1>$candidat2) && ($candidat1>$candidat3) && ($candidat1>$candidat4)){
    echo"le candidat 1 se trouve en ballotage favorable. ";}
else{
    echo"le candidat 1 ne se trouve pas en ballotage defavorable. ";}
