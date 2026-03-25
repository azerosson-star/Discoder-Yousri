<?php

function demandeLettre (){
do{$reponse= strtoupper(readline("entrer une seule lettre"));}
while(!ctype_alpha($reponse)||strlen($reponse)!=1);



};